"""Testes unitários para validação das estruturas e construção do grafo."""

import pytest
from src.fluxo.equipes import REGISTRO_EQUIPES
from src.fluxo.estado import EstadoFluxo
from src.fluxo.grafo import construir_grafo, rotear_empresa, sem_correspondencia
from src.fluxo.roteador import carregar_empresas


def test_carregar_empresas():
    """Valida se as empresas cadastradas no diretório de configuração são carregadas."""
    empresas = carregar_empresas()
    assert isinstance(empresas, dict)
    assert len(empresas) >= 3
    assert "atlas_gestao_financeira" in empresas
    assert "aurora_skin" in empresas
    assert "clinica_essenza" in empresas


def test_registro_equipes():
    """Valida se todas as empresas do registro possuem módulo e classe definidos."""
    assert len(REGISTRO_EQUIPES) == 3
    for id_empresa, (modulo, classe, relatorio) in REGISTRO_EQUIPES.items():
        assert isinstance(modulo, str) and modulo.startswith("src.equipes")
        assert isinstance(classe, str)
        assert relatorio.endswith(".md")


def test_rotear_empresa():
    """Testa a lógica de decisão condicional do roteador."""
    estado_valido: EstadoFluxo = {"empresa": "aurora_skin"}
    assert rotear_empresa(estado_valido) == "aurora_skin"

    estado_invalido: EstadoFluxo = {"empresa": "empresa_inexistente"}
    assert rotear_empresa(estado_invalido) == "sem_correspondencia"


def test_sem_correspondencia():
    """Testa a geração de mensagem para fluxo sem correspondência."""
    estado: EstadoFluxo = {"justificativa": "Tema fora do escopo."}
    resultado = sem_correspondencia(estado)
    assert "resultado" in resultado
    assert "Tema fora do escopo." in resultado["resultado"]


def test_construir_grafo():
    """Valida se o grafo compila com sucesso sem exceções."""
    grafo = construir_grafo(salvar_imagem=False)
    assert grafo is not None


def test_carregar_restricoes_empresa():
    """Valida se as restrições regulatórias, de conteúdo e de projeto são extraídas."""
    from src.fluxo.equipes import carregar_restricoes_empresa

    for id_empresa in ("atlas_gestao_financeira", "aurora_skin", "clinica_essenza"):
        texto = carregar_restricoes_empresa(id_empresa)
        assert "Restrições Regulatórias:" in texto
        assert "Restrições de Conteúdo:" in texto
        assert "Restrições de Projeto:" in texto
        assert "Não mencionar a IdeiaFlui" in texto


def test_consolidacao_no_gerente_geral_e_tabela_gargalos():
    """Valida se as tarefas de consolidação estão no gerente geral e exigem tabela de horas."""
    import yaml
    from pathlib import Path

    raiz = Path(__file__).resolve().parents[1]

    empresas_verificacao = {
        "atlas_gestao": ("relatorio_gerencial_atlas", "gerente_geral_atlas"),
        "aurora_skin": ("relatorio_gerencial_aurora", "gerente_geral_aurora"),
        "clinica_essenza": ("relatorio_gerencial_essenza", "gerente_geral_essenza"),
    }

    for pasta, (task_nome, agente_esperado) in empresas_verificacao.items():
        caminho_tasks = raiz / "config" / "empresas" / pasta / "tasks.yaml"
        tasks = yaml.safe_load(caminho_tasks.read_text(encoding="utf-8"))
        task_cfg = tasks[task_nome]

        assert task_cfg["agent"] == agente_esperado
        desc = task_cfg["description"].lower()
        exp = task_cfg["expected_output"].lower()
        assert "horas por semana" in desc or "horas por semana" in exp
        assert "gargalo" in desc or "gargalo" in exp


def test_placeholders_restricoes_nas_tasks_e_agents():
    """Valida se todas as tarefas e agentes possuem o placeholder {restricoes}."""
    import yaml
    from pathlib import Path

    raiz = Path(__file__).resolve().parents[1]
    pastas = ["atlas_gestao", "aurora_skin", "clinica_essenza"]

    for pasta in pastas:
        caminho_tasks = raiz / "config" / "empresas" / pasta / "tasks.yaml"
        tasks = yaml.safe_load(caminho_tasks.read_text(encoding="utf-8"))
        for t_nome, t_cfg in tasks.items():
            assert "{restricoes}" in t_cfg["description"], f"{pasta}/{t_nome} falta {{restricoes}}"

        caminho_agents = raiz / "config" / "empresas" / pasta / "agents.yaml"
        agents = yaml.safe_load(caminho_agents.read_text(encoding="utf-8"))
        for a_nome, a_cfg in agents.items():
            assert "{restricoes}" in a_cfg["backstory"], f"{pasta}/{a_nome} falta {{restricoes}}"


def test_estado_fluxo_sem_area():
    """Valida que area e area_justificativa foram removidas do estado."""
    assert "area" not in EstadoFluxo.__annotations__
    assert "area_justificativa" not in EstadoFluxo.__annotations__


def test_main_import_sem_compilar_grafo():
    """Valida que main.py não compila o grafo na simples importação."""
    import main

    assert main._grafo is None
    grafo = main.obter_grafo()
    assert grafo is not None
    assert main._grafo is not None
