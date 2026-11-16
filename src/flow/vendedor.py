"""Módulo de compatibilidade: reexporta agente vendedor de src.fluxo.vendedor."""

from src.fluxo.vendedor import (
    CAMINHO_SERVICOS,
    PROMPT_SISTEMA_VENDEDOR,
    SERVICOS,
    SERVICOS_PATH,
    SISTEMA,
    carregar_catalogo_servicos,
    carregar_servicos,
    vendedor,
)

__all__ = [
    "vendedor",
    "carregar_servicos",
    "carregar_catalogo_servicos",
    "SERVICOS",
    "SERVICOS_PATH",
    "CAMINHO_SERVICOS",
    "SISTEMA",
    "PROMPT_SISTEMA_VENDEDOR",
]
