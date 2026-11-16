"""Módulo de roteamento semântico do LangGraph.

Este módulo analisa a intenção e o assunto enviado pelo usuário, identifica
qual das empresas cadastradas possui maior aderência de segmento, público e pilares,
e redige um briefing operacional curto para direcionar a simulação da equipe.
"""

from pathlib import Path
from typing import Any, Literal

import yaml
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

from .equipes import REGISTRO_EQUIPES
from .estado import EstadoFluxo

# Garante o carregamento das variáveis de ambiente (.env)
load_dotenv()

# Diretórios de configurações
RAIZ_PROJETO = Path(__file__).resolve().parents[2]
DIRETORIO_EMPRESAS = RAIZ_PROJETO / "config" / "empresas"
if not DIRETORIO_EMPRESAS.exists():
    DIRETORIO_EMPRESAS = RAIZ_PROJETO / "config" / "companies"


def carregar_empresas() -> dict[str, dict[str, Any]]:
    """Carrega os arquivos de perfil de empresa (empresa.yaml) das empresas ativas.

    Returns:
        dict[str, dict[str, Any]]: Dicionário mapeando o id da empresa à sua configuração.
    """
    empresas: dict[str, dict[str, Any]] = {}
    for caminho in DIRETORIO_EMPRESAS.glob("*/empresa.yaml"):
        configuracao = yaml.safe_load(caminho.read_text(encoding="utf-8"))
        if configuracao and configuracao.get("id") in REGISTRO_EQUIPES:
            empresas[configuracao["id"]] = configuracao

    return empresas


EMPRESAS: dict[str, dict[str, Any]] = carregar_empresas()
IDS_EMPRESAS: tuple[str, ...] = tuple(EMPRESAS.keys())


class Roteamento(BaseModel):
    """Esquema de saída estruturada para a decisão de roteamento."""

    empresa: Literal[IDS_EMPRESAS + ("nenhuma",)] = Field(
        description="Id da empresa mais adequada ao assunto, ou 'nenhuma' se nenhuma combinar."
    )
    briefing: str = Field(
        description="Briefing em no máximo 2 frases para o planejamento da semana da empresa escolhida. Vazio se nenhuma."
    )
    justificativa: str = Field(description="Uma frase explicando a justificativa da escolha.")


def descrever_empresa(cfg: dict[str, Any]) -> str:
    """Formata o perfil e pilares da empresa para inclusão no prompt do roteador.

    Args:
        cfg (dict[str, Any]): Dicionário de configuração da empresa.

    Returns:
        str: Texto descritivo com segmento, público, pilares e setores da empresa.
    """
    setores = "; ".join(s["area"] for s in cfg.get("setores", []))
    pilares = "; ".join(cfg.get("marca", {}).get("pilares_conteudo", []))
    briefing_base = cfg.get("briefings", {}).get("base", "")

    return (
        f"- id: {cfg['id']}\n"
        f"  empresa: {cfg['nome_completo']}\n"
        f"  segmento: {cfg['segmento']}\n"
        f"  público: {cfg['publico_alvo']}\n"
        f"  pilares: {pilares}\n"
        f"  setores: {setores}\n"
        f"  exemplo de briefing: {briefing_base}"
    )


PROMPT_SISTEMA_ROTEADOR = (
    "Você é o roteador de uma simulação de empresas fictícias. Dado um assunto, escolha a empresa "
    "cujo segmento, público e pilares mais se aproximam dele e escreva um briefing curto para a "
    "semana de trabalho dela. O briefing deve ser concreto (produto, campanha ou situação), citar "
    "as frentes dos setores relevantes e seguir o estilo dos exemplos. Não mencione automação, "
    "IA nem serviços de terceiros. Se o assunto não combinar com nenhuma, use 'nenhuma'.\n\n"
    "EMPRESAS:\n" + "\n".join(descrever_empresa(c) for c in EMPRESAS.values())
)


def _obter_llm_roteador():
    """Inicializa o modelo de linguagem estruturado para roteamento."""
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.1)
    return llm.with_structured_output(Roteamento)


def roteador(estado: EstadoFluxo) -> dict[str, str]:
    """Nó do LangGraph responsável por rotear o assunto para a empresa adequada.

    Args:
        estado (EstadoFluxo): Estado do fluxo contendo o 'assunto'.

    Returns:
        dict[str, str]: Atualizações do estado com 'empresa', 'briefing' e 'justificativa'.
    """
    roteador_estruturado = _obter_llm_roteador()
    decisao: Roteamento | None = roteador_estruturado.invoke(
        [
            SystemMessage(PROMPT_SISTEMA_ROTEADOR),
            HumanMessage(estado["assunto"]),
        ]
    )

    if decisao is None:
        return {
            "empresa": "nenhuma",
            "briefing": "",
            "justificativa": "O roteador não gerou uma resposta válida para o assunto informado.",
        }

    return {
        "empresa": decisao.empresa,
        "briefing": decisao.briefing,
        "justificativa": decisao.justificativa,
    }


# Aliases para compatibilidade
router = roteador
descrever = descrever_empresa
SISTEMA = PROMPT_SISTEMA_ROTEADOR
IDS = IDS_EMPRESAS
CREW_DIR = DIRETORIO_EMPRESAS
