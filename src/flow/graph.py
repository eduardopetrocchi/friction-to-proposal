"""Módulo de compatibilidade: reexporta montador de grafo de src.fluxo.grafo."""

from src.fluxo.grafo import build_graph, construir_grafo, escolher, rotear_empresa, sem_correspondencia

__all__ = [
    "construir_grafo",
    "build_graph",
    "rotear_empresa",
    "escolher",
    "sem_correspondencia",
]