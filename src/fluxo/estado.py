"""Definição do esquema de estado compartilhado do LangGraph.

Este módulo define a estrutura de dados que trafega entre os nós do grafo,
mantendo o contexto acumulado desde a entrada do usuário, passando pelo
roteamento, execução da equipe especializada até a geração da proposta de venda.
"""

from typing import TypedDict


class EstadoFluxo(TypedDict, total=False):
    """Estado global do grafo de orquestração.

    Attributes:
        assunto (str): Tema ou demanda inicial submetida pelo usuário.
        empresa (str): Identificador da empresa selecionada pelo roteador
            ('atlas_gestao_financeira', 'aurora_skin', 'clinica_essenza' ou 'nenhuma').
        briefing (str): Contexto operacional e diretrizes resumidas para os agentes da empresa.
        justificativa (str): Explicação da IA para a escolha da empresa ou ausência de match.
        resultado (str): Conteúdo bruto ou relatório executivo gerado pela simulação da equipe.
        proposta (str): Texto completo em Markdown da proposta comercial elaborada pela IdeiaFlui.
        arquivo (str): Caminho no disco para o relatório gerencial Markdown gerado pela equipe.
        arquivo_proposta (str): Caminho no disco onde a proposta comercial Markdown foi salva.
    """

    assunto: str
    empresa: str
    briefing: str
    justificativa: str
    resultado: str
    proposta: str
    arquivo: str
    arquivo_proposta: str


# Aliases para compatibilidade e flexibilidade de nomenclatura
Estado = EstadoFluxo
State = EstadoFluxo
