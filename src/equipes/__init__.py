"""Pacote de equipes multiagentes especializadas (CrewAI).

Exporta as classes responsáveis pelas simulações operacionais de cada empresa:
- EquipeAtlasGestao: BPO financeiro, fiscal e controladoria.
- EquipeAuroraSkin: E-commerce, marketing digital e produtos cosméticos.
- EquipeClinicaEssenza: Saúde estética, agendamentos e compliance CFM.
"""

from .atlas_gestao import AtlasGestao, Atlas_Gestao, EquipeAtlasGestao
from .aurora_skin import AuroraSkin, Aurora_Skin, EquipeAuroraSkin
from .clinica_essenza import ClinicaEssenza, Clinica_Essenza, EquipeClinicaEssenza

__all__ = [
    "EquipeAtlasGestao",
    "AtlasGestao",
    "Atlas_Gestao",
    "EquipeAuroraSkin",
    "AuroraSkin",
    "Aurora_Skin",
    "EquipeClinicaEssenza",
    "ClinicaEssenza",
    "Clinica_Essenza",
]
