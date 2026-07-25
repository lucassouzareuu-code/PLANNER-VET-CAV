import streamlit as st
from typing import List, Dict, Optional

# =========================================================================
# LÓGICA 
# =========================================================================

DAYS = ["SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA", "SÁBADO"]
TOTAL_SLOTS = 16

PHASES = ["1ª Fase", "2ª Fase", "3ª Fase", "4ª Fase", "5ª Fase",
          "6ª Fase", "7ª Fase", "8ª Fase", "9ª Fase", "Eletivas"]

def get_slot_time_str(slot_idx: int) -> str:
    times = [
        "07:10 - 08:00", # Slot 0
        "08:00 - 08:50", # Slot 1
        "08:50 - 09:40", # Slot 2
        "09:50 - 10:40", # Slot 3
        "10:40 - 11:30", # Slot 4
        "11:30 - 12:20", # Slot 5
        "13:10 - 14:00", # Slot 6
        "14:00 - 14:50", # Slot 7
        "14:50 - 15:40", # Slot 8
        "16:00 - 16:50", # Slot 9
        "16:50 - 17:40", # Slot 10
        "17:40 - 18:30", # Slot 11
        "18:30 - 19:20", # Slot 12
        "19:20 - 20:10", # Slot 13
        "20:10 - 21:00", # Slot 14
        "21:00 - 21:50"  # Slot 15
    ]
    if slot_idx < len(times):
        return times[slot_idx]  
    return f"Slot {slot_idx}"

class Course:
    def __init__(self, code: str, name: str, total_hours: int, schedule: Dict[str, List[int]], phase: str = ""):
        self.code = code
        self.name = name
        self.total_hours = total_hours
        self.schedule = schedule
        self.phase = phase
        self.group = code
        self.kind = "unica"
        self.theory: Optional["Course"] = None
        self.official_code: Optional[str] = None
        self.creditos: Optional[int] = None
        self.tipo: str = "Obrigatória"

    @property
    def display_code(self) -> str:
        return self.official_code or self.code

    @property
    def display_ch(self) -> int:
        return self.total_hours

    def __str__(self):
        label = f"[{self.display_code}] {self.name} ({self.display_ch}h"
        if self.creditos is not None:
            label += f" | {self.creditos} créd."
        label += ")"
        return label

def build_initial_catalog() -> List[Course]:
    """Catálogo completo de Medicina Veterinária UDESC CAV - HORÁRIOS 2026/2 E CARGAS HORÁRIAS OFICIAIS"""
    catalog: List[Course] = []

    def add(phase, code, name, total_hours, schedule):
        catalog.append(Course(code, name, total_hours, schedule, phase=phase))

    # =========================================================================
    # 1ª FASE - 2026/2 (Cargas conforme grade: ANA1-90=90h, BIOQB72=72h, etc.)
    # =========================================================================
    add("1ª Fase", "ANA1-T", "Anatomia I (Teórica)", 90, {"SEGUNDA": [1, 2], "TERÇA": [1, 2]})
    add("1ª Fase", "ANA1-A", "Anatomia I (Turma A)", 90, {"QUARTA": [3, 4], "TERÇA": [9]})
    add("1ª Fase", "ANA1-B", "Anatomia I (Turma B)", 90, {"TERÇA": [10]})
    add("1ª Fase", "ANA1-C", "Anatomia I (Turma C)", 90, {"TERÇA": [11], "SEXTA": [1, 2]})
    add("1ª Fase", "ANA1-D", "Anatomia I (Turma D)", 90, {"QUARTA": [1, 2], "SEXTA": [3, 4]})
    
    add("1ª Fase", "HISTG-T", "Histologia Geral (Teórica)", 72, {"TERÇA": [3, 4], "QUINTA": [1, 2]})
    add("1ª Fase", "HISTG-A", "Histologia Geral (Turma A)", 72, {"QUINTA": [1, 2]})
    add("1ª Fase", "HISTG-B", "Histologia Geral (Turma B)", 72, {"QUARTA": [3, 4]})
    add("1ª Fase", "HISTG-C", "Histologia Geral (Turma C)", 72, {"QUINTA": [7, 8]})
    add("1ª Fase", "HISTG-D", "Histologia Geral (Turma D)", 72, {"QUARTA": [9, 10]})
    
    add("1ª Fase", "INTRO", "Introdução à Medicina Veterinária", 36, {"QUARTA": [2]}) # Deontologia (36h)
    add("1ª Fase", "SOAMV", "Sociologia Aplicada", 36, {"SEGUNDA": [3, 4]})
    add("1ª Fase", "ECOLO", "Ecologia e Desenvolvimento", 36, {"QUINTA": [3, 4]})
    add("1ª Fase", "ESTAT", "Estatística e Experimentação", 54, {"SEGUNDA": [7, 8, 9]})
    add("1ª Fase", "BIOQB-T", "Bioquímica de Biomoléculas (Teórica)", 72, {"TERÇA": [7, 8], "QUARTA": [7]})
    add("1ª Fase", "BIOQB-A", "Bioquímica de Biomoléculas (Turma A)", 72, {"QUARTA": [7]})
    add("1ª Fase", "BIOQB-B", "Bioquímica de Biomoléculas (Turma B)", 72, {"SEXTA": [8]})
    add("1ª Fase", "BIOQB-C", "Bioquímica de Biomoléculas (Turma C)", 72, {"QUARTA": [11]})
    add("1ª Fase", "EXTEN", "Extensão, Comunicação e Sociedade", 36, {"SEXTA": [7, 8]})
    add("1ª Fase", "COMPOR", "Comportamento e Bem-Estar Animal", 36, {"QUINTA": [9, 10]})

    # =========================================================================
    # 2ª FASE - 2026/2
    # =========================================================================
    add("2ª Fase", "ANA2-T", "Anatomia II (Teórica)", 90, {"SEGUNDA": [1, 2], "QUARTA": [3, 4]})
    add("2ª Fase", "ANA2-A", "Anatomia II (Turma A)", 90, {"QUINTA": [7, 8], "SEXTA": [9]})
    add("2ª Fase", "ANA2-B", "Anatomia II (Turma B)", 90, {"QUARTA": [9, 10], "SEXTA": [10]})
    add("2ª Fase", "ANA2-C", "Anatomia II (Turma C)", 90, {"SEGUNDA": [11, 12], "QUARTA": [12]})
    add("2ª Fase", "ANA2-D", "Anatomia II (Turma D)", 90, {"QUARTA": [1, 2], "QUARTA": [11]})
    
    add("2ª Fase", "HIST2-T", "Histologia e Embriologia (Teórica)", 90, {"SEGUNDA": [3, 4], "SEXTA": [1]})
    add("2ª Fase", "HIST2-A", "Histologia e Embriologia (Turma A)", 90, {"TERÇA": [7, 8]})
    add("2ª Fase", "HIST2-B", "Histologia e Embriologia (Turma B)", 90, {"TERÇA": [9, 10]})
    add("2ª Fase", "HIST2-C", "Histologia e Embriologia (Turma C)", 90, {"QUARTA": [7, 8]})
    add("2ª Fase", "HIST2-D", "Histologia e Embriologia (Turma D)", 90, {"SEXTA": [7, 8]})

    add("2ª Fase", "GENET-T", "Genética (Teórica)", 72, {"SEXTA": [2]})
    add("2ª Fase", "GENE-A", "Genética (Turma A)", 72, {"SEXTA": [3, 4]})
    add("2ª Fase", "GENE-B", "Genética (Turma B)", 72, {"SEXTA": [8]})
    
    add("2ª Fase", "BIOQM-T", "Bioquímica Metabólica (Teórica)", 72, {})
    add("2ª Fase", "BIOQM-A", "Bioquímica Metabólica (Turma A)", 72, {"SEGUNDA": [7, 8]})
    add("2ª Fase", "BIOQM-B", "Bioquímica Metabólica (Turma B)", 72, {"SEGUNDA": [9, 10]})
    
    add("2ª Fase", "PARA1-T", "Parasitologia I (Teórica)", 72, {"TERÇA": [3, 4]})
    add("2ª Fase", "PARA1-A", "Parasitologia I (Turma A)", 72, {"TERÇA": [1, 2]})
    add("2ª Fase", "PARA1-B", "Parasitologia I (Turma B)", 72, {"TERÇA": [11, 12]})
    add("2ª Fase", "PARA1-C", "Parasitologia I (Turma C)", 72, {"QUINTA": [3, 4]})
    add("2ª Fase", "PARA1-D", "Parasitologia I (Turma D)", 72, {"QUINTA": [7, 8]})
    
    add("2ª Fase", "FISI1-T", "Fisiologia I (Teórica)", 90, {"SEGUNDA": [6], "SEXTA": [7, 8]})
    add("2ª Fase", "FISI1-A", "Fisiologia I (Turma A)", 90, {"QUINTA": [1, 2]})
    add("2ª Fase", "FISI1-B", "Fisiologia I (Turma B)", 90, {"QUINTA": [9, 10]})
    add("2ª Fase", "FISI1-C", "Fisiologia I (Turma C)", 90, {"QUINTA": [3, 4]})
    add("2ª Fase", "FISI1-D", "Fisiologia I (Turma D)", 90, {"QUINTA": [9, 10]})

    # =========================================================================
    # 3ª FASE - 2026/2
    # =========================================================================
    add("3ª Fase", "IMUNO-T", "Imunologia Veterinária (Teórica)", 54, {"SEGUNDA": [1, 2]})
    add("3ª Fase", "IMUNO-A", "Imunologia Veterinária (Turma A)", 54, {"SEGUNDA": [11]})
    add("3ª Fase", "IMUNO-B", "Imunologia Veterinária (Turma B)", 54, {"SEGUNDA": [12]})
    
    add("3ª Fase", "FISI2-T", "Fisiologia II (Teórica)", 72, {"TERÇA": [1, 2]})
    add("3ª Fase", "FISI2-A", "Fisiologia II (Turma A)", 72, {"SEGUNDA": [7, 8]})
    add("3ª Fase", "FISI2-B", "Fisiologia II (Turma B)", 72, {"SEGUNDA": [9, 10]})
    add("3ª Fase", "FISI2-C", "Fisiologia II (Turma C)", 72, {"TERÇA": [3, 4]})
    add("3ª Fase", "FISI2-D", "Fisiologia II (Turma D)", 72, {"QUARTA": [3, 4]})
    
    add("3ª Fase", "PARA2-T", "Parasitologia II (Teórica)", 72, {"QUINTA": [1, 2]})
    add("3ª Fase", "PARA2-A", "Parasitologia II (Turma A)", 72, {"SEGUNDA": [7, 8]})
    add("3ª Fase", "PARA2-B", "Parasitologia II (Turma B)", 72, {"SEGUNDA": [9, 10]})
    add("3ª Fase", "PARA2-C", "Parasitologia II (Turma C)", 72, {"TERÇA": [3, 4]})
    add("3ª Fase", "PARA2-D", "Parasitologia II (Turma D)", 72, {"QUARTA": [1, 2]})
    
    add("3ª Fase", "MICRO-T", "Microbiologia Básica (Teórica)", 72, {"SEGUNDA": [3, 4]})
    add("3ª Fase", "MICRO-A", "Microbiologia Básica (Turma A)", 72, {"SEGUNDA": [7, 8]})
    add("3ª Fase", "MICRO-B", "Microbiologia Básica (Turma B)", 72, {"SEGUNDA": [9, 10]})
    add("3ª Fase", "MICRO-C", "Microbiologia Básica (Turma C)", 72, {"TERÇA": [7, 8]})
    add("3ª Fase", "MICRO-D", "Microbiologia Básica (Turma D)", 72, {"TERÇA": [9, 10]})
    
    add("3ª Fase", "NUTRI", "Nutrição Animal", 54, {"QUARTA": [7, 8, 9, 10, 11, 12]})
    add("3ª Fase", "FARM1-T", "Farmacologia Geral (Teórica)", 72, {"SEXTA": [1, 2, 3, 4, 7, 8]})
    add("3ª Fase", "FARM1-A", "Farmacologia Geral (Turma A)", 72, {"QUINTA": [9, 10]})
    add("3ª Fase", "FARM1-B", "Farmacologia Geral (Turma B)", 72, {"SEXTA": [1, 2]})
    add("3ª Fase", "FARM1-C", "Farmacologia Geral (Turma C)", 72, {"SEXTA": [3, 4]})
    
    add("3ª Fase", "EPIST", "Epistemologia e Metodologia Científica", 36, {"QUARTA": [9, 10]})
    add("3ª Fase", "MELHO", "Melhoramento Animal", 36, {"QUINTA": [11, 12]})

    # =========================================================================
    # 4ª FASE - 2026/2
    # =========================================================================
    add("4ª Fase", "NUTRI-4", "Nutrição Animal", 54, {"SEGUNDA": [1, 2], "QUARTA": [1, 2]})
    
    add("4ª Fase", "FISI2-A", "Fisiologia II (Turma A)", 72, {"SEGUNDA": [3, 4]})
    add("4ª Fase", "FISI2-B", "Fisiologia II (Turma B)", 72, {"TERÇA": [1, 2]})
    add("4ª Fase", "FISI2-C", "Fisiologia II (Turma C)", 72, {"TERÇA": [7, 8]})
    add("4ª Fase", "FISI2-D", "Fisiologia II (Turma D)", 72, {"TERÇA": [9]})
    
    add("4ª Fase", "FARM1-D", "Farmacologia Geral (Turma D)", 72, {"TERÇA": [3, 4]})
    add("4ª Fase", "FARM1-E", "Farmacologia Geral (Turma E)", 72, {"TERÇA": [9]})
    add("4ª Fase", "FARM1-F", "Farmacologia Geral (Turma F)", 72, {"QUARTA": [3, 4]})
    
    add("4ª Fase", "PARA2-E", "Parasitologia II (Turma E)", 72, {"SEGUNDA": [3, 4]})
    add("4ª Fase", "PARA2-F", "Parasitologia II (Turma F)", 72, {"QUARTA": [3, 4]})
    add("4ª Fase", "PARA2-G", "Parasitologia II (Turma G)", 72, {"QUARTA": [9]})
    add("4ª Fase", "PARA2-H", "Parasitologia II (Turma H)", 72, {"QUINTA": [1, 2]})
    
    add("4ª Fase", "MICRE-A", "Microbiologia Especial (Turma A)", 90, {"QUARTA": [3, 4]})
    add("4ª Fase", "MICRE-B", "Microbiologia Especial (Turma B)", 90, {"QUARTA": [7, 8]})
    add("4ª Fase", "MICRE-C", "Microbiologia Especial (Turma C)", 90, {"QUARTA": [9]})
    
    add("4ª Fase", "ECONO", "Economia e Administração", 72, {"SEXTA": [1, 2], "QUARTA": [7, 8]})
    add("4ª Fase", "EPIDE", "Epidemiologia", 36, {"QUINTA": [3, 4]})

    # =========================================================================
    # 5ª FASE - 2026/2
    # =========================================================================
    add("5ª Fase", "ALIMA", "Alimentos e Alimentação Animal", 90, {})
    add("5ª Fase", "COEXT", "Comunicação e Extensão Rural", 36, {})
    add("5ª Fase", "FARMD-T", "Farmacodinâmica (Teórica)", 72, {})
    add("5ª Fase", "FORRA", "Forragicultura", 54, {})
    add("5ª Fase", "PACLI-T", "Patologia Clínica Vet. (Teórica)", 72, {})
    add("5ª Fase", "PATG-T", "Patologia Geral (Teórica)", 90, {})
    add("5ª Fase", "SEMIO-T", "Semiologia (Teórica)", 90, {})

    # =========================================================================
    # 6ª FASE - 2026/2
    # =========================================================================
    add("6ª Fase", "SUINO-T", "Suinocultura (Teórica)", 54, {"SEGUNDA": [1, 2]})
    add("6ª Fase", "SUINO-A", "Suinocultura (Turma A)", 54, {"SEGUNDA": [7, 8]})
    add("6ª Fase", "SUINO-B", "Suinocultura (Turma B)", 54, {"SEGUNDA": [8]})
    add("6ª Fase", "SUINO-C", "Suinocultura (Turma C)", 54, {"SEGUNDA": [9]})
    
    add("6ª Fase", "DOIC-T", "Doenças Infecto-Contagiosas (Teórica)", 90, {"TERÇA": [1, 2, 3, 4]})
    add("6ª Fase", "DOIC-A", "Doenças Infecto-Contagiosas (Turma A)", 90, {"QUARTA": [5], "QUINTA": [10]})
    add("6ª Fase", "DOIC-B", "Doenças Infecto-Contagiosas (Turma B)", 90, {"QUINTA": [7, 8]})
    add("6ª Fase", "DOIC-C", "Doenças Infecto-Contagiosas (Turma C)", 90, {"SEXTA": [9]})
    
    add("6ª Fase", "DOENP-T", "Doenças Parasitárias (Teórica)", 72, {"QUARTA": [1, 2, 3, 4]})
    add("6ª Fase", "DOENP-A", "Doenças Parasitárias (Turma A)", 72, {"QUARTA": [7, 8]})
    add("6ª Fase", "DOENP-B", "Doenças Parasitárias (Turma B)", 72, {"SEXTA": [9, 10]})
    add("6ª Fase", "DOENP-C", "Doenças Parasitárias (Turma C)", 72, {"SEGUNDA": [11], "SÁBADO": [12]})
    add("6ª Fase", "DOENP-D", "Doenças Parasitárias (Turma D)", 72, {"QUINTA": [7, 8]})
    
    add("6ª Fase", "CLINR-T", "Clínica Médica de Ruminantes (Teórica)", 90, {"QUINTA": [1, 2, 3, 4]})
    add("6ª Fase", "CLINR-A", "Clínica Médica de Ruminantes (Turma A)", 90, {"QUARTA": [7, 8]})
    add("6ª Fase", "CLINR-B", "Clínica Médica de Ruminantes (Turma B)", 90, {"SEXTA": [9, 10]})
    add("6ª Fase", "CLINR-C", "Clínica Médica de Ruminantes (Turma C)", 90, {"SEXTA": [9]})
    add("6ª Fase", "CLINR-D", "Clínica Médica de Ruminantes (Turma D)", 90, {"QUINTA": [7, 8]})
    
    add("6ª Fase", "PATE-T", "Patologia Especial (Teórica)", 90, {"SEXTA": [1, 2, 3, 4]})
    add("6ª Fase", "PATE-A", "Patologia Especial (Turma A)", 90, {"SEXTA": [9, 10]})
    add("6ª Fase", "PATE-B", "Patologia Especial (Turma B)", 90, {"QUINTA": [7, 8]})
    add("6ª Fase", "PATE-C", "Patologia Especial (Turma C)", 90, {"SÁBADO": [10, 11]})
    
    add("6ª Fase", "PISCI", "Piscicultura", 36, {"QUARTA": [3, 4, 5]})
    add("6ª Fase", "TERAP", "Terapêutica", 36, {"SEGUNDA": [3, 4]})

    # =========================================================================
    # 7ª FASE - 2026/2 (CORRIGIDA)
    # =========================================================================
    # ANESTESIOLOGIA (54h)
    add("7ª Fase", "ANEST-T", "Anestesiologia (Teórica)", 54, {"SEGUNDA": [1, 2]})
    add("7ª Fase", "ANEST-A", "Anestesiologia (Turma A)", 54, {"SEGUNDA": [7]})
    add("7ª Fase", "ANEST-B", "Anestesiologia (Turma B)", 54, {"SEGUNDA": [7]})
    add("7ª Fase", "ANEST-C", "Anestesiologia (Turma C)", 54, {"TERÇA": [7, 8]})
    add("7ª Fase", "ANEST-D", "Anestesiologia (Turma D)", 54, {"TERÇA": [9, 10]})

    # TÉCNICA CIRÚRGICA (90h)
    add("7ª Fase", "TCIR-T", "Técnica Cirúrgica (Teórica)", 90, {"SEGUNDA": [9, 10], "QUINTA": [9, 10]})
    add("7ª Fase", "TCIR-A", "Técnica Cirúrgica (Turma A)", 90, {"TERÇA": [1, 2]})
    add("7ª Fase", "TCIR-B", "Técnica Cirúrgica (Turma B)", 90, {"TERÇA": [3, 4]})
    add("7ª Fase", "TCIR-C", "Técnica Cirúrgica (Turma C)", 90, {"QUARTA": [1, 2]})
    add("7ª Fase", "TCIR-D", "Técnica Cirúrgica (Turma D)", 90, {"QUARTA": [3, 4]})

    # DIAGNÓSTICO POR IMAGEM (54h)
    add("7ª Fase", "DIAG-T", "Diagnóstico por Imagem (Teórica)", 54, {"QUINTA": [9, 10]})
    add("7ª Fase", "DIAG-A", "Diagnóstico por Imagem (Turma A)", 54, {"TERÇA": [1, 2]})
    add("7ª Fase", "DIAG-B", "Diagnóstico por Imagem (Turma B)", 54, {"TERÇA": [3, 4]})
    add("7ª Fase", "DIAG-C", "Diagnóstico por Imagem (Turma C)", 54, {"QUARTA": [3, 4]})
    add("7ª Fase", "DIAG-D", "Diagnóstico por Imagem (Turma D)", 54, {"QUINTA": [7, 8]})

    # CLÍNICA MÉDICA DE CÃES E GATOS I (90h)
    add("7ª Fase", "CLINC-T", "Clínica Médica de Cães e Gatos I (Teórica)", 90, {"QUINTA": [1, 2], "SEXTA": [1, 2]})
    add("7ª Fase", "CLINC-A", "Clínica Médica de Cães e Gatos I (Turma A)", 90, {"SEGUNDA": [7, 8]})
    add("7ª Fase", "CLINC-B", "Clínica Médica de Cães e Gatos I (Turma B)", 90, {"SEGUNDA": [9, 10]})
    add("7ª Fase", "CLINC-C", "Clínica Médica de Cães e Gatos I (Turma C)", 90, {"QUARTA": [9]})
    add("7ª Fase", "CLINC-D", "Clínica Médica de Cães e Gatos I (Turma D)", 90, {"QUINTA": [7, 8]})

    # FISIOPATOLOGIA DA REPRODUÇÃO I (90h)
    add("7ª Fase", "FISREPO-T", "Fisiopatologia da Reprodução I (Teórica)", 90, {"SEGUNDA": [3, 4]})
    add("7ª Fase", "FISREPO-A", "Fisiopatologia da Reprodução I (Turma A)", 90, {"TERÇA": [7, 8]})
    add("7ª Fase", "FISREPO-B", "Fisiopatologia da Reprodução I (Turma B)", 90, {"TERÇA": [9, 10]})
    add("7ª Fase", "FISREPO-C", "Fisiopatologia da Reprodução I (Turma C)", 90, {"QUARTA": [7, 8]})
    add("7ª Fase", "FISREPO-D", "Fisiopatologia da Reprodução I (Turma D)", 90, {"QUINTA": [7, 8]})

    # BOVINOCULTURA DE CORTE (54h)
    add("7ª Fase", "BOVIC", "Bovinocultura de Corte", 54, {"SÁBADO": [2, 3, 4]})

    # SAÚDE PÚBLICA VETERINÁRIA (54h)
    add("7ª Fase", "SAUP-T", "Saúde Pública Veterinária (Teórica)", 54, {"SEXTA": [7, 8]})
    add("7ª Fase", "SAUP-A", "Saúde Pública Veterinária (Turma A)", 54, {"SÁBADO": [9]})
    add("7ª Fase", "SAUP-B", "Saúde Pública Veterinária (Turma B)", 54, {"SÁBADO": [10]})

    # =========================================================================
    # 8ª FASE - 2026/2
    # =========================================================================
    add("8ª Fase", "CLINE-T", "Clínica Médica de Equinos (Teórica)", 90, {"TERÇA": [1, 2, 3, 4]})
    add("8ª Fase", "CLINE-A", "Clínica Médica de Equinos (Turma A)", 90, {"SEGUNDA": [1, 2]})
    add("8ª Fase", "CLINE-B", "Clínica Médica de Equinos (Turma B)", 90, {"SEGUNDA": [3, 4]})
    add("8ª Fase", "CLINE-C", "Clínica Médica de Equinos (Turma C)", 90, {"QUINTA": [9, 10]})
    add("8ª Fase", "CLINE-D", "Clínica Médica de Equinos (Turma D)", 90, {"SEXTA": [1, 2]})

    add("8ª Fase", "PATCL2-T", "Patologia e Clínica Cirúrgica (Teórica)", 108, {"QUINTA": [3, 4, 11], "SEXTA": [3, 4, 9, 10], "SÁBADO": [3, 4]})
    add("8ª Fase", "PATCL2-A", "Patologia e Clínica Cirúrgica (Turma A)", 108, {"SEGUNDA": [2]})
    add("8ª Fase", "PATCL2-B", "Patologia e Clínica Cirúrgica (Turma B)", 108, {"QUARTA": [3, 4, 11]})
    add("8ª Fase", "PATCL2-C", "Patologia e Clínica Cirúrgica (Turma C)", 108, {"QUINTA": [1, 2]})
    add("8ª Fase", "PATCL2-D", "Patologia e Clínica Cirúrgica (Turma D)", 108, {"SEXTA": [1, 2]})

    add("8ª Fase", "BOVIL", "Bovinocultura de Leite", 54, {"SEGUNDA": [7, 8, 9, 10]})
    add("8ª Fase", "SANSU-T", "Sanidade Suína (Teórica)", 54, {"TERÇA": [7, 8]})
    add("8ª Fase", "SANSU-A", "Sanidade Suína (Turma A)", 54, {"TERÇA": [9]})
    add("8ª Fase", "SANSU-B", "Sanidade Suína (Turma B)", 54, {"QUARTA": [7, 8]})
    add("8ª Fase", "SANSU-C", "Sanidade Suína (Turma C)", 54, {"QUARTA": [8]})
    
    add("8ª Fase", "INSPE-T", "Inspeção e Tec. Prod. Origem Animal I (Teórica)", 72, {"SEGUNDA": [11, 12]})
    add("8ª Fase", "INSPE-A", "Inspeção e Tec. Prod. Origem Animal I (Turma A)", 72, {"TERÇA": [11]})
    add("8ª Fase", "INSPE-B", "Inspeção e Tec. Prod. Origem Animal I (Turma B)", 72, {"TERÇA": [12]})
    
    add("8ª Fase", "AVIC-T", "Avicultura (Teórica)", 54, {"QUINTA": [7, 8]})
    add("8ª Fase", "AVIC-A", "Avicultura (Turma A)", 54, {"QUINTA": [9]})
    add("8ª Fase", "AVIC-B", "Avicultura (Turma B)", 54, {"QUINTA": [10]})
    add("8ª Fase", "AVIC-C", "Avicultura (Turma C)", 54, {"QUINTA": [11]})
    
    add("8ª Fase", "OVINO-T", "Ovinocultura (Teórica)", 36, {"SÁBADO": [7, 8, 9]})
    add("8ª Fase", "OVINO-A", "Ovinocultura (Turma A)", 36, {"SÁBADO": [9]})
    add("8ª Fase", "OVINO-B", "Ovinocultura (Turma B)", 36, {"SÁBADO": [10]})

    # =========================================================================
    # 9ª FASE - 2026/2
    # =========================================================================
    add("9ª Fase", "OBSTE-T", "Obstetrícia (Teórica)", 72, {"TERÇA": [7, 8]})
    add("9ª Fase", "OBSTE-A", "Obstetrícia (Turma A)", 72, {"SEGUNDA": [1, 2]})
    add("9ª Fase", "OBSTE-B", "Obstetrícia (Turma B)", 72, {"SEGUNDA": [3, 4]})
    add("9ª Fase", "OBSTE-C", "Obstetrícia (Turma C)", 72, {"SEGUNDA": [7, 8]})
    add("9ª Fase", "OBSTE-D", "Obstetrícia (Turma D)", 72, {"SEGUNDA": [9, 10]})

    add("9ª Fase", "CLCG2-T", "Clínica Médica de Cães e Gatos II (Teórica)", 90, {"TERÇA": [1, 2]})
    add("9ª Fase", "CLCG2-A", "Clínica Médica de Cães e Gatos II (Turma A)", 90, {"SEGUNDA": [1, 2]})
    add("9ª Fase", "CLCG2-B", "Clínica Médica de Cães e Gatos II (Turma B)", 90, {"SEGUNDA": [3, 4]})
    add("9ª Fase", "CLCG2-C", "Clínica Médica de Cães e Gatos II (Turma C)", 90, {"SEGUNDA": [9, 10]})
    add("9ª Fase", "CLCG2-D", "Clínica Médica de Cães e Gatos II (Turma D)", 90, {"QUARTA": [3, 4]})

    add("9ª Fase", "FRIA2-T", "Fisiopatologia da Reprodução II (Teórica)", 72, {"SÁBADO": [12]})
    add("9ª Fase", "FRIA2-A", "Fisiopatologia da Reprodução II (Turma A)", 72, {"QUINTA": [1, 2]})
    add("9ª Fase", "FRIA2-B", "Fisiopatologia da Reprodução II (Turma B)", 72, {"QUINTA": [3, 4]})
    add("9ª Fase", "FRIA2-C", "Fisiopatologia da Reprodução II (Turma C)", 72, {"SEXTA": [1, 2]})
    add("9ª Fase", "FRIA2-D", "Fisiopatologia da Reprodução II (Turma D)", 72, {"SEXTA": [3, 4]})

    add("9ª Fase", "INSP2-T", "Inspeção e Tec. Prod. Origem Animal II (Teórica)", 90, {"QUARTA": [1, 2]})
    add("9ª Fase", "INSP2-A", "Inspeção e Tec. Prod. Origem Animal II (Turma A)", 90, {"QUARTA": [3, 4]})
    add("9ª Fase", "INSP2-B", "Inspeção e Tec. Prod. Origem Animal II (Turma B)", 90, {"QUARTA": [7, 8]})
    add("9ª Fase", "INSP2-C", "Inspeção e Tec. Prod. Origem Animal II (Turma C)", 90, {"QUARTA": [9, 10]})
    add("9ª Fase", "INSP2-D", "Inspeção e Tec. Prod. Origem Animal II (Turma D)", 90, {"QUARTA": [12]})

    add("9ª Fase", "TOXI", "Toxicologia e Plantas Tóxicas", 36, {"TERÇA": [9, 10]})
    add("9ª Fase", "DAVES-T", "Doenças das Aves (Teórica)", 72, {"SÁBADO": [7, 8, 9, 10]})
    add("9ª Fase", "DAVES-A", "Doenças das Aves (Turma A)", 72, {"QUINTA": [7, 8]})
    add("9ª Fase", "DAVES-B", "Doenças das Aves (Turma B)", 72, {"SEXTA": [1, 2]})
    add("9ª Fase", "DAVES-C", "Doenças das Aves (Turma C)", 72, {"SEXTA": [3, 4]})

    # =========================================================================
    # ELETIVAS (10ª FASE) - 2026/2 (Conforme grade, todas eletivas têm 36h)
    # =========================================================================
    add("Eletivas", "LACTI", "Lacticínios", 36, {"TERÇA": [3, 4]})
    add("Eletivas", "OFTAL", "Oftalmologia Veterinária", 36, {"QUARTA": [3, 4]})
    add("Eletivas", "DERMA", "Dermatologia Veterinária", 36, {"QUINTA": [3], "SEXTA": [4]})
    add("Eletivas", "CITO", "Citologia Diagnóstica", 36, {"QUINTA": [4], "SEXTA": [5]})
    add("Eletivas", "FISIA", "Fisiatria Veterinária", 36, {"TERÇA": [7, 8]})
    add("Eletivas", "COMPBEM", "Comportamento e Bem-Estar Animal", 36, {"QUARTA": [7, 8]})
    add("Eletivas", "GEREN", "Gerenciamento e Produção Avícola", 36, {"QUINTA": [7, 8]})
    add("Eletivas", "EQUIN", "Equinocultura", 36, {"SEXTA": [7, 8]})
    add("Eletivas", "MICROAL", "Microbiologia dos Produtos de Origem Animal", 36, {"SEXTA": [7, 8]})
    add("Eletivas", "CARDIO", "Cardiologia de Cães e Gatos", 36, {"SEXTA": [7, 8]})
    add("Eletivas", "MEDSEL", "Medicina de Animais Silvestres", 36, {"SEGUNDA": [9, 10]})
    add("Eletivas", "AQUAC", "Aquacultura", 36, {"SEGUNDA": [11, 12]})
    add("Eletivas", "ESTAG", "Estágio Curricular Supervisionado", 486, {"SEGUNDA": [15]})

    link_theory_to_practicals(catalog)
    return catalog

def infer_group_and_kind(code: str):
    if code.endswith("-T"):
        return code[:-2], "teorica"
    if code.endswith("-TEO"):
        return code[:-4], "teorica"
    if len(code) >= 2 and code[-2] == "-" and code[-1] in "ABCDE":
        return code[:-2], "pratica"
    return code, "unica"

def link_theory_to_practicals(catalog: List[Course]) -> None:
    for c in catalog:
        c.group, c.kind = infer_group_and_kind(c.code)

    theory_by_group = {c.group: c for c in catalog if c.kind == "teorica"}
    for c in catalog:
        if c.kind == "pratica":
            c.theory = theory_by_group.get(c.group)

def get_combined_schedule(course: Course) -> Dict[str, List[int]]:
    """Retorna um dicionário único com todos os horários (teórica + prática) mesclados e sem duplicatas."""
    combined: Dict[str, List[int]] = {}
    
    # Adiciona os horários da própria disciplina (prática)
    for day, slots in course.schedule.items():
        combined[day] = list(slots)
    
    # Adiciona os horários da teórica, se existir
    if course.theory:
        for day, slots in course.theory.schedule.items():
            if day in combined:
                # Mescla e ordena, removendo duplicatas
                combined[day] = sorted(set(combined[day] + slots))
            else:
                combined[day] = list(slots)
                
    return combined

def check_conflict(course_to_add: Course, registered_courses: List[Course]) -> Optional[str]:
    schedule_to_add = get_combined_schedule(course_to_add)
    for reg in registered_courses:
        reg_schedule = get_combined_schedule(reg)
        for day, slots in schedule_to_add.items():
            if day in reg_schedule:
                overlap = set(slots).intersection(set(reg_schedule[day]))
                if overlap:
                    conflicting_slot = sorted(list(overlap))[0]
                    return f"Com '{reg.name}' na {day} no horário {get_slot_time_str(conflicting_slot)}."
    return None

# =========================================================================
# TOKENS DE DESIGN E INTERFACE
# =========================================================================

PAGE_BG = "#25CC8CC1"
PANEL_BG = "#FEFFB0BA"
HEADER_GRADIENT = "linear-gradient(135deg, #1B1F3B 0%, #2E3566 100%)"
TIME_COL_GRADIENT = "linear-gradient(135deg, #EDEFF7 0%, #E3E6F3 100%)"
EMPTY_CELL_BG = "#B6F8DD"
GRID_LINE = "#000000"

PHASE_COLORS = {
    "1ª Fase":  ("#6836F3", "#9C7BFF"),
    "2ª Fase":  ("#08C9E7", "#5FD3E3"),
    "3ª Fase":  ("#086E4E", "#3FCB9C"),
    "4ª Fase":  ("#3178C4", "#63ABF2"),
    "5ª Fase":  ("#E0A62F", "#F2C55E"),
    "6ª Fase":  ("#E0632F", "#F28A5E"),
    "7ª Fase":  ("#D6396B", "#EE6D97"),
    "8ª Fase":  ("#7B05FAD1", "#B06BF2"),
    "9ª Fase":  ("#DB2A33", "#662D2D"),
    "Eletivas": ("#BB3D4E", "#8C99A6"),
}

def phase_gradient(phase: str) -> str:
    c1, c2 = PHASE_COLORS.get(phase, ("#04300A", "#5A7E21"))
    return f"linear-gradient(135deg, {c1} 0%, {c2} 100%)"

# =========================================================================
# INTERFACE — Streamlit
# =========================================================================

st.set_page_config(
    page_title="Simulador de Matrícula CAV", layout="wide")

st.markdown(f"""
<style>
.stApp {{ background-color: {PAGE_BG}; }}
</style>
""", unsafe_allow_html=True)

if "available_courses" not in st.session_state:
    st.session_state.available_courses = build_initial_catalog()
if "registered_courses" not in st.session_state:
    st.session_state.registered_courses = []

st.title("Simulador de Matrícula UDESC-CAV")

col_left, col_right = st.columns([1, 2], gap="large")

# ---------------- Painel esquerdo ----------------
with col_left:
    st.subheader("Buscar disciplinas")

    phase_choice = st.selectbox("Fase", ["Todas as Fases"] + PHASES)
    query = st.text_input("Buscar por código, nome ou carga horária").lower().strip()

    filtered_courses = [
        c for c in st.session_state.available_courses
        if c.kind != "teorica"
        and (phase_choice == "Todas as Fases" or c.phase == phase_choice)
        and (query in c.display_code.lower() or query in c.name.lower() or query in str(c.display_ch))
    ]

    st.subheader(f"Todas Disciplinas ({len(filtered_courses)})")
    options = [str(c) for c in filtered_courses]
    selected_label = st.selectbox("Catálogo", options, label_visibility="collapsed") if options else None

    selected_course = None
    if selected_label:
        idx = options.index(selected_label)
        selected_course = filtered_courses[idx]

        st.markdown(
            f"<span style='background:{phase_gradient(selected_course.phase)};color:white;"
            f"padding:2px 10px;border-radius:12px;font-size:14px;font-weight:600'>{selected_course.phase}</span>",
            unsafe_allow_html=True,
        )

        creditos_line = f"  \n**Créditos:** {selected_course.creditos}" if selected_course.creditos is not None else ""
        
        # CORREÇÃO DA EXIBIÇÃO DOS HORÁRIOS
        combined_schedule_data = get_combined_schedule(selected_course)
        
        details = (
            f"**Código:** {selected_course.display_code}  \n**Nome:** {selected_course.name}  \n"
            f"**Carga Horária:** {selected_course.display_ch}h{creditos_line}  \n**Horários (Teórica + Prática):**\n"
        )
        
        if combined_schedule_data:
            # Ordena os dias da semana conforme a ordem correta
            for day in DAYS:
                if day in combined_schedule_data:
                    slot_str = ", ".join([get_slot_time_str(s) for s in sorted(combined_schedule_data[day])])
                    details += f"- {day}: {slot_str}\n"
        else:
            details += "- Nenhum horário cadastrado.\n"

        st.markdown(details)

    if st.button("➕ Adicionar Disciplina", use_container_width=True, disabled=selected_course is None) and selected_course:
        already_added = any(c.group == selected_course.group for c in st.session_state.registered_courses)
        if already_added:
            st.warning(f"Você já tem uma turma de '{selected_course.name}' adicionada. Remova-a antes de escolher outra.")
        else:
            conflict_msg = check_conflict(selected_course, st.session_state.registered_courses)
            if conflict_msg:
                st.warning(f"Choque de Horário: {conflict_msg}")
            else:
                st.session_state.registered_courses.append(selected_course)
                if selected_course.theory:
                    st.session_state.registered_courses.append(selected_course.theory)
                st.success(f"'{selected_course.name}' adicionada com sucesso!")
                st.rerun()

    grouped_groups = []
    for c in st.session_state.registered_courses:
        if c.group not in grouped_groups:
            grouped_groups.append(c.group)

    st.subheader(f"Matérias Selecionadas ({len(grouped_groups)})")
    total_ch_geral = 0
    total_creditos_geral = 0
    for group in grouped_groups:
        group_courses = [c for c in st.session_state.registered_courses if c.group == group]
        practical = next((c for c in group_courses if c.kind != "teorica"), group_courses[0])
        ch = practical.display_ch
        creditos = practical.creditos
        total_ch_geral += ch
        if creditos is not None:
            total_creditos_geral += creditos
        creditos_str = f" | {creditos} créd." if creditos is not None else ""
        label = f"[{practical.display_code}] {practical.name} ({ch}h{creditos_str})"
        row_col1, row_col2 = st.columns([4, 1])
        row_col1.write(label)
        if row_col2.button("🗑️", key=f"remove_{group}"):
            st.session_state.registered_courses = [c for c in st.session_state.registered_courses if c.group != group]
            st.rerun()

    if grouped_groups:
        st.markdown(f"**Total:** {total_ch_geral}h &nbsp;|&nbsp; {total_creditos_geral} créditos")

# ---------------- Painel direito: agenda ----------------
with col_right:
    st.subheader("Organizador Semanal de Horários")

    grid: Dict[tuple, Course] = {}
    for c in st.session_state.registered_courses:
        for day, slots in c.schedule.items():
            if day not in DAYS:
                continue
            for slot in slots:
                if slot < TOTAL_SLOTS:
                    grid[(day, slot)] = c

    header_cells = "".join(
        f"<th style='padding:10px 6px;background:{HEADER_GRADIENT};color:white;"
        f"border:1px solid {GRID_LINE};font-size:12px;font-weight:600'>{d}</th>"
        for d in DAYS
    )

    rows_html = ""
    for slot in range(TOTAL_SLOTS):
        row = (
            f"<tr><td style='padding:8px 6px;background:{TIME_COL_GRADIENT};"
            f"border:1px solid {GRID_LINE};font-size:14px;color:#333;white-space:nowrap'>"
            f"{get_slot_time_str(slot)}</td>"
        )
        for day in DAYS:
            course = grid.get((day, slot))
            if course:
                bg = phase_gradient(course.phase)
                # Exibe o nome da disciplina e a turma de forma clara
                display_name = course.name
                if course.kind == "pratica":
                    display_name += f" ({course.code[-1]})"  # Exibe a letra da turma
                row += (
                    f"<td style='padding:6px;background:{bg};border:1px solid {GRID_LINE};"
                    "border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.15);"
                    "color:white;font-size:10px;font-weight:600;text-align:center'>"
                    f"{display_name[:20]}<br><span style='font-weight:400;opacity:0.9'>{course.display_code}</span></td>"
                )
            else:
                row += f"<td style='padding:6px;background:{EMPTY_CELL_BG};border:1px solid {GRID_LINE}'></td>"
        row += "</tr>"
        rows_html += row

    legend_html = "".join(
        f"<span style='display:inline-flex;align-items:center;margin:2px 8px 2px 0;font-size:11px;color:#333'>"
        f"<span style='width:10px;height:10px;border-radius:3px;background:{phase_gradient(p)};display:inline-block;margin-right:4px'></span>{p}</span>"
        for p in PHASES
    )

    table_html = f"""
    <div style="overflow-x:auto;background:{PANEL_BG};padding:10px;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,0.08)">
    <table style="border-collapse:collapse;width:100%;border-radius:8px;overflow:hidden">
      <tr><th style='padding:10px 6px;background:{HEADER_GRADIENT};color:white;border:1px solid {GRID_LINE};font-size:16px'>Horários</th>{header_cells}</tr>
      {rows_html}
    </table>
    <div style="margin-top:10px">{legend_html}</div>
    </div>
    """
    st.markdown(table_html, unsafe_allow_html=True)
    
