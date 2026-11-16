"""Módulo de compatibilidade: reexporta esquemas de estado de src.fluxo.estado."""

from src.fluxo.estado import Estado, EstadoFluxo, State

__all__ = ["EstadoFluxo", "Estado", "State"]
