"""Construção e compilação do grafo de fluxo no LangGraph.

Este módulo define a máquina de estados completa do sistema IdeiaFlui:
1. Roteamento do assunto de entrada para a empresa ideal;
2. Disparo da equipe multiagente (CrewAI) correspondente;
3. Encaminhamento do relatório da equipe para o agente Vendedor (IdeiaFlui);
4. Geração e salvamento da proposta comercial consultiva.
"""

from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .equipes import REGISTRO_EQUIPES, criar_no_equipe
from .estado import EstadoFluxo
from .roteador import roteador
from .vendedor import vendedor

# Garante o carregamento prévio do ambiente
load_dotenv()


def sem_correspondencia(estado: EstadoFluxo) -> dict[str, str]:
    """Nó executado quando o assunto não é compatível com nenhuma das empresas cadastradas.

    Args:
        estado (EstadoFluxo): Estado atual do grafo contendo a justificativa do roteador.

    Returns:
        dict[str, str]: Mensagem explicativa no campo 'resultado'.
    """
    justificativa = estado.get("justificativa", "")
    return {
        "resultado": (
            "Nenhuma empresa cadastrada combina com o assunto informado. "
            f"Justificativa: {justificativa}"
        )
    }


def rotear_empresa(estado: EstadoFluxo) -> str:
    """Função condicional para determinar o próximo nó após a etapa de roteamento.

    Args:
        estado (EstadoFluxo): Estado com a chave 'empresa' preenchida pelo roteador.

    Returns:
        str: Nome do nó de destino (id da empresa ou 'sem_correspondencia').
    """
    id_empresa = estado.get("empresa", "")
    return id_empresa if id_empresa in REGISTRO_EQUIPES else "sem_correspondencia"


def construir_grafo(salvar_imagem: bool = False) -> CompiledStateGraph:
    """Monta, valida e compila o grafo de estados do LangGraph.

    Args:
        salvar_imagem (bool, opcional): Se True, tenta gerar e salvar o diagrama
            visual do grafo em 'outputs/grafo.png'. Padrão é False.

    Returns:
        CompiledStateGraph: Grafo compilado pronto para execução via .invoke().
    """
    builder = StateGraph(EstadoFluxo)

    # Adiciona nós principais do fluxo
    builder.add_node("roteador", roteador)
    builder.add_node("sem_correspondencia", sem_correspondencia)
    builder.add_node("vendedor", vendedor)

    # Adiciona nós dinâmicos para cada empresa registrada
    for id_empresa in REGISTRO_EQUIPES:
        builder.add_node(id_empresa, criar_no_equipe(id_empresa))

    # Conecta o ponto inicial ao roteador
    builder.add_edge(START, "roteador")

    # Aresta condicional a partir da decisão do roteador
    destinos_possiveis = [*REGISTRO_EQUIPES.keys(), "sem_correspondencia"]
    builder.add_conditional_edges("roteador", rotear_empresa, destinos_possiveis)

    # Cada empresa encaminha seu relatório para o agente vendedor
    for id_empresa in REGISTRO_EQUIPES:
        builder.add_edge(id_empresa, "vendedor")

    # Finalização do fluxo
    builder.add_edge("vendedor", END)
    builder.add_edge("sem_correspondencia", END)

    # Compilação
    grafo = builder.compile()

    # Opcionalmente gera o diagrama em imagem PNG
    if salvar_imagem:
        caminho_destino = Path("outputs/grafo.png")
        try:
            caminho_destino.parent.mkdir(parents=True, exist_ok=True)
            dados_imagem = grafo.get_graph().draw_mermaid_png()
            caminho_destino.write_bytes(dados_imagem)
            print(f"Diagrama do fluxo salvo em: {caminho_destino}")
        except Exception as erro:
            print(f"Aviso: Não foi possível gerar a imagem mermaid do grafo: {erro}")

    return grafo


# Aliases para compatibilidade
build_graph = construir_grafo
escolher = rotear_empresa
