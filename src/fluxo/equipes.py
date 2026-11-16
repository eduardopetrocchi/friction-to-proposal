"""Módulo de integração entre o fluxo LangGraph e as equipes CrewAI.

Este módulo gerencia o registro das equipes de cada empresa participante
e fornece geradores de nós executáveis para o grafo de orquestração.
"""

from importlib import import_module
from pathlib import Path
from typing import Any, Callable

import yaml

from .estado import EstadoFluxo

RAIZ_PROJETO = Path(__file__).resolve().parents[2]
DIRETORIO_EMPRESAS = RAIZ_PROJETO / "config" / "empresas"
if not DIRETORIO_EMPRESAS.exists():
    DIRETORIO_EMPRESAS = RAIZ_PROJETO / "config" / "companies"


def carregar_restricoes_empresa(id_empresa: str) -> str:
    """Lê do empresa.yaml as restrições regulatórias, de conteúdo e de projeto, unindo-as em texto.

    Args:
        id_empresa (str): Identificador único da empresa.

    Returns:
        str: Texto formatado com as restrições consolidadas.
    """
    for caminho in DIRETORIO_EMPRESAS.glob("*/empresa.yaml"):
        try:
            with caminho.open(encoding="utf-8") as f:
                cfg = yaml.safe_load(f)
            if cfg and cfg.get("id") == id_empresa:
                restricoes = cfg.get("restricoes", {})
                linhas: list[str] = []
                if restricoes.get("regulatorias"):
                    linhas.append("Restrições Regulatórias:")
                    linhas.extend(f"- {r}" for r in restricoes["regulatorias"])
                if restricoes.get("conteudo"):
                    linhas.append("Restrições de Conteúdo:")
                    linhas.extend(f"- {r}" for r in restricoes["conteudo"])
                if restricoes.get("projeto"):
                    linhas.append("Restrições de Projeto:")
                    linhas.extend(f"- {r}" for r in restricoes["projeto"])
                return "\n".join(linhas)
        except Exception:
            continue
    return ""


# Mapeamento oficial de cada empresa para seu módulo, classe e caminho de relatório
REGISTRO_EQUIPES: dict[str, tuple[str, str, str]] = {
    "atlas_gestao_financeira": (
        "src.equipes.atlas_gestao",
        "EquipeAtlasGestao",
        "relatorios/atlas_gestao_financeira/relatorio_gerencial.md",
    ),
    "aurora_skin": (
        "src.equipes.aurora_skin",
        "EquipeAuroraSkin",
        "relatorios/aurora_skin/relatorio_gerencial.md",
    ),
    "clinica_essenza": (
        "src.equipes.clinica_essenza",
        "EquipeClinicaEssenza",
        "relatorios/clinica_essenza/relatorio_gerencial.md",
    ),
}


def criar_no_equipe(id_empresa: str) -> Callable[[EstadoFluxo], dict[str, str]]:
    """Gera uma função de nó encapsulando a execução da equipe CrewAI correspondente.

    Args:
        id_empresa (str): Identificador único da empresa cadastrada no registro.

    Returns:
        Callable[[EstadoFluxo], dict[str, str]]: Função executável compatível com
            nós de execução do LangGraph.

    Raises:
        KeyError: Se o id_empresa não estiver presente no registro de equipes.
    """
    if id_empresa not in REGISTRO_EQUIPES:
        raise KeyError(
            f"Empresa '{id_empresa}' não encontrada no registro de equipes. "
            f"Opções disponíveis: {list(REGISTRO_EQUIPES.keys())}"
        )

    def executar_equipe(estado: EstadoFluxo) -> dict[str, str]:
        """Executa a equipe multiagente e salva a referência do relatório.

        Args:
            estado (EstadoFluxo): Estado atual do grafo contendo o briefing.

        Returns:
            dict[str, str]: Dicionário com 'resultado' e 'arquivo'.
        """
        modulo, nome_classe, caminho_relatorio = REGISTRO_EQUIPES[id_empresa]
        classe_equipe = getattr(import_module(modulo), nome_classe)
        arquivo = Path(caminho_relatorio)
        arquivo.parent.mkdir(parents=True, exist_ok=True)

        instancia = classe_equipe()
        # Suporta tanto o método em português (equipe) quanto o padrão (crew) sem avaliar fallback desnecessariamente
        metodo_crew = getattr(instancia, "equipe", None) or getattr(instancia, "crew")
        restricoes_texto = carregar_restricoes_empresa(id_empresa)
        saida = metodo_crew().kickoff(
            inputs={
                "briefing": estado["briefing"],
                "restricoes": restricoes_texto,
            }
        )

        return {"resultado": saida.raw, "arquivo": str(arquivo)}

    return executar_equipe


# Aliases para compatibilidade com versões prévias do código
REGISTRO = REGISTRO_EQUIPES
criar_no_crew = criar_no_equipe
