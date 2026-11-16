"""Pacote de compatibilidade src.flow reexportando de src.fluxo."""

from src.fluxo import (
    REGISTRO_EQUIPES,
    Estado,
    EstadoFluxo,
    State,
    build_graph,
    construir_grafo,
    criar_no_crew,
    criar_no_equipe,
    roteador,
    router,
    vendedor,
)

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
