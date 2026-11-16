"""Pacote do fluxo de orquestração com LangGraph (IdeiaFlui).

Exporta os principais elementos do fluxo:
- construir_grafo: Compila o grafo completo com roteador, equipes e vendedor.
- EstadoFluxo / Estado / State: Esquema de dados compartilhado.
- roteador: Nó de classificação e briefing.
- vendedor: Nó de elaboração da proposta comercial.
- criar_no_equipe: Gerador de nós para as equipes CrewAI.
"""

from .equipes import REGISTRO_EQUIPES, criar_no_crew, criar_no_equipe
from .estado import Estado, EstadoFluxo, State
from .grafo import build_graph, construir_grafo
from .roteador import roteador, router
from .vendedor import vendedor

__all__ = [
    "construir_grafo",
    "build_graph",
    "EstadoFluxo",
    "Estado",
    "State",
    "roteador",
    "router",
    "vendedor",
    "criar_no_equipe",
    "criar_no_crew",
    "REGISTRO_EQUIPES",
]
