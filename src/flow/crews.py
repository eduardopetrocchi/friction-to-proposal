"""Módulo de compatibilidade: reexporta registro e criadores de equipes de src.fluxo.equipes."""

from src.fluxo.equipes import REGISTRO, REGISTRO_EQUIPES, criar_no_crew, criar_no_equipe

__all__ = ["REGISTRO", "REGISTRO_EQUIPES", "criar_no_crew", "criar_no_equipe"]
