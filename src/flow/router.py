"""Módulo de compatibilidade: reexporta roteador e utilitários de src.fluxo.roteador."""

from src.fluxo.roteador import (
    CREW_DIR,
    EMPRESAS,
    IDS,
    IDS_EMPRESAS,
    PROMPT_SISTEMA_ROTEADOR,
    Roteamento,
    SISTEMA,
    carregar_empresas,
    descrever,
    descrever_empresa,
    roteador,
    router,
)

__all__ = [
    "roteador",
    "router",
    "Roteamento",
    "carregar_empresas",
    "descrever",
    "descrever_empresa",
    "EMPRESAS",
    "IDS",
    "IDS_EMPRESAS",
    "SISTEMA",
    "PROMPT_SISTEMA_ROTEADOR",
    "CREW_DIR",
]
