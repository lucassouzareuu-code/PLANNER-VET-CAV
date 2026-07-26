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
        "08:00 - 08:50", "08:50 - 09:40", "09:50 - 10:40", "10:40 - 11:30", "11:30 - 12:20",
        "13:10 - 14:00", "14:00 - 14:50", "14:50 - 15:40", "16:00 - 16:50", "16:50 - 17:40",
        "17:40 - 18:30", "18:30 - 19:20", "19:20 - 20:10", "20:10 - 21:00", "21:00 - 21:50", "21:50 - 22:00"
    ]
    if slot_idx < len(times):
        return times[slot_idx]
    return f"Slot {slot_idx}"


class Course:
    def __init__(self, code: str, name: str, credits: int, schedule: Dict[str, List[int]], phase: str = ""):
        self.code = code
        self.name = name
        self.credits = credits
        self.schedule = schedule
        self.phase = phase
        self.group = code
        self.kind = "unica"
        self.theory: Optional["Course"] = None

    def __str__(self):
        credits = self.credits
        if self.theory:
            credits += self.theory.credits
        return f"[{self.code}] {self.name} ({credits}h)"


def build_initial_catalog() -> List[Course]:
    """Catálogo completo de Medicina Veterinária UDESC CAV - Horários conforme cronograma 2026/2."""
    catalog: List[Course] = []

    def add(phase, code, name, credits, schedule):
        catalog.append(Course(code, name, credits, schedule, phase=phase))

    # =====================================================================
    # 1ª FASE - Conforme PDF de Horários (Página 1)
    # =====================================================================
    # Teóricas
    add("1ª Fase", "ANA1-TEO", "Anatomia I",
        90, {"SEGUNDA": [0, 1], "TERÇA": [0, 1]})
    add("1ª Fase", "HISTG-TEO", "Histologia Geral",
        72, {"TERÇA": [2, 3]})
    add("1ª Fase", "BIOQB-TEO", "Bioquímica de Biomoléculas",
        72, {"TERÇA": [6, 7]})
    add("1ª Fase", "INTMED", "Introdução à Medicina Veterinária",
        36, {"TERÇA": [2, 3]})  # PDF: TERÇA 09:50-10:40 e 10:40-11:30
    add("1ª Fase", "SOAMV", "Sociologia Aplicada à Saúde",
        36, {"SEGUNDA": [2, 3]})
    add("1ª Fase", "ECOLO", "Ecologia e Desenvolvimento Sustentável",
        36, {"QUINTA": [2, 3]})
    add("1ª Fase", "ESTCA", "Estatística e Experimentação Animal",
        54, {"SEGUNDA": [6, 7, 8]})
    add("1ª Fase", "EXTEN", "Extensão, Comunicação e Cidadania",
        36, {"SEXTA": [7]})
    add("1ª Fase", "COMPOR", "Comportamento e Bem-Estar Animal",
        36, {"QUINTA": [8, 9]})
    
    # Práticas Anatomia I
    add("1ª Fase", "ANA1-A", "Anatomia I (Turma A)",
        0, {"TERÇA": [8], "QUARTA": [2, 3]})
    add("1ª Fase", "ANA1-B", "Anatomia I (Turma B)",
        0, {"SEXTA": [8, 9]})
    add("1ª Fase", "ANA1-C", "Anatomia I (Turma C)",
        0, {"TERÇA": [10], "SEXTA": [0, 1]})
    add("1ª Fase", "ANA1-D", "Anatomia I (Turma D)",
        0, {"QUARTA": [0, 1], "SEXTA": [2, 3]})
    
    # Práticas Histologia
    add("1ª Fase", "HISTG-A", "Histologia Geral (Turma A)",
        0, {"QUARTA": [0, 1]})
    add("1ª Fase", "HISTG-C", "Histologia Geral (Turma C)",
        0, {"QUARTA": [6, 7]})
    add("1ª Fase", "HISTG-D", "Histologia Geral (Turma D)",
        0, {"QUARTA": [8, 9]})
    
    # Práticas Bioquímica
    add("1ª Fase", "BIOQB-A", "Bioquímica de Biomoléculas (Turma A)",
        0, {"QUARTA": [6, 7]})
    add("1ª Fase", "BIOQB-C", "Bioquímica de Biomoléculas (Turma C)",
        0, {"TERÇA": [10]})

    # =====================================================================
    # 2ª FASE - Conforme PDF de Horários (Página 2)
    # =====================================================================
    # Teóricas
    add("2ª Fase", "ANA2-TEO", "Anatomia II",
        90, {"SEGUNDA": [0, 1]})
    add("2ª Fase", "HIST2-TEO", "Histologia e Embriologia",
        90, {"SEGUNDA": [2, 3], "SEXTA": [0]})
    add("2ª Fase", "GENET-TEO", "Genética",
        72, {"SÁBADO": [0, 1]})
    add("2ª Fase", "BIOQM-TEO", "Bioquímica Metabólica",
        72, {"SÁBADO": [2, 3]})
    add("2ª Fase", "PARA1-TEO", "Parasitologia I",
        72, {"TERÇA": [2, 3], "QUINTA": [2, 3]})
    add("2ª Fase", "FISI1-TEO", "Fisiologia I",
        90, {"SÁBADO": [0, 1, 6, 7]})
    
    # Práticas Anatomia II
    add("2ª Fase", "ANA2-A", "Anatomia II (Turma A)",
        0, {"QUINTA": [6, 7], "SÁBADO": [8]})
    add("2ª Fase", "ANA2-B", "Anatomia II (Turma B)",
        0, {"QUARTA": [8, 9], "SÁBADO": [9]})
    add("2ª Fase", "ANA2-C", "Anatomia II (Turma C)",
        0, {"TERÇA": [10, 11]})
    add("2ª Fase", "ANA2-D", "Anatomia II (Turma D)",
        0, {"QUARTA": [0, 1], "QUINTA": [10, 11]})
    
    # Práticas Histologia
    add("2ª Fase", "HIST2-A", "Histologia e Embriologia (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("2ª Fase", "HIST2-B", "Histologia e Embriologia (Turma B)",
        0, {"SEGUNDA": [8, 9]})
    add("2ª Fase", "HIST2-C", "Histologia e Embriologia (Turma C)",
        0, {"TERÇA": [6, 7]})
    add("2ª Fase", "HIST2-D", "Histologia e Embriologia (Turma D)",
        0, {"SÁBADO": [6, 7]})
    
    # Práticas Genética
    add("2ª Fase", "GENE-A", "Genética (Turma A)",
        0, {"SÁBADO": [2, 3]})
    add("2ª Fase", "GENE-B", "Genética (Turma B)",
        0, {"SÁBADO": [6, 7]})
    
    # Práticas Bioquímica Metabólica
    add("2ª Fase", "BIOQM-A", "Bioquímica Metabólica (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("2ª Fase", "BIOQM-B", "Bioquímica Metabólica (Turma B)",
        0, {"SEGUNDA": [8, 9]})
    
    # Práticas Parasitologia I
    add("2ª Fase", "PARA1-A", "Parasitologia I (Turma A)",
        0, {"TERÇA": [0, 1]})
    add("2ª Fase", "PARA1-B", "Parasitologia I (Turma B)",
        0, {"TERÇA": [10, 11]})
    add("2ª Fase", "PARA1-C", "Parasitologia I (Turma C)",
        0, {"QUINTA": [2, 3]})
    add("2ª Fase", "PARA1-D", "Parasitologia I (Turma D)",
        0, {"SÁBADO": [6, 7]})
    
    # Práticas Fisiologia I
    add("2ª Fase", "FISI1-A", "Fisiologia I (Turma A)",
        0, {"QUINTA": [0, 1]})
    add("2ª Fase", "FISI1-B", "Fisiologia I (Turma B)",
        0, {"QUARTA": [8, 9]})
    add("2ª Fase", "FISI1-C", "Fisiologia I (Turma C)",
        0, {"QUINTA": [2, 3]})
    add("2ª Fase", "FISI1-D", "Fisiologia I (Turma D)",
        0, {"SEXTA": [8, 9]})

    # =====================================================================
    # 3ª FASE - Conforme PDF de Horários (Página 3)
    # =====================================================================
    # Teóricas
    add("3ª Fase", "MICRO-TEO", "Microbiologia Geral",
        72, {"SEGUNDA": [2, 3], "QUARTA": [6, 7]})
    add("3ª Fase", "IMUNO-TEO", "Imunologia",
        54, {"TERÇA": [0, 1]})
    add("3ª Fase", "FISI2-TEO", "Fisiologia II",
        72, {"SEGUNDA": [0, 1]})
    add("3ª Fase", "PARA2-TEO", "Parasitologia II",
        72, {"SEGUNDA": [0, 1]})
    add("3ª Fase", "FARMA-TEO", "Farmacologia Geral",
        72, {"SEGUNDA": [6, 7]})
    add("3ª Fase", "NUTRI-TEO", "Nutrição Animal",
        54, {"QUARTA": [0, 1]})
    
    # Práticas Microbiologia
    add("3ª Fase", "MICRO-A", "Microbiologia (Turma A)",
        0, {"SEGUNDA": [0, 1]})
    add("3ª Fase", "MICRO-B", "Microbiologia (Turma B)",
        0, {"SEGUNDA": [2, 3]})
    add("3ª Fase", "MICRO-C", "Microbiologia (Turma C)",
        0, {"SEXTA": [0, 1]})
    add("3ª Fase", "MICRO-D", "Microbiologia (Turma D)",
        0, {"SEXTA": [2, 3]})
    
    # Práticas Imunologia
    add("3ª Fase", "IMUNO-A", "Imunologia (Turma A)",
        0, {"TERÇA": [0, 1]})
    add("3ª Fase", "IMUNO-B", "Imunologia (Turma B)",
        0, {"TERÇA": [2, 3]})
    add("3ª Fase", "IMUNO-C", "Imunologia (Turma C)",
        0, {"QUINTA": [9, 10]})
    
    # Práticas Fisiologia II
    add("3ª Fase", "FISI2-A", "Fisiologia II (Turma A)",
        0, {"SEGUNDA": [0, 1]})
    add("3ª Fase", "FISI2-B", "Fisiologia II (Turma B)",
        0, {"SEGUNDA": [2, 3]})
    add("3ª Fase", "FISI2-C", "Fisiologia II (Turma C)",
        0, {"TERÇA": [6, 7]})
    add("3ª Fase", "FISI2-D", "Fisiologia II (Turma D)",
        0, {"TERÇA": [8, 9]})
    
    # Práticas Parasitologia II
    add("3ª Fase", "PARA2-A", "Parasitologia II (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("3ª Fase", "PARA2-B", "Parasitologia II (Turma B)",
        0, {"SEGUNDA": [8, 9]})
    add("3ª Fase", "PARA2-C", "Parasitologia II (Turma C)",
        0, {"QUARTA": [8, 9]})
    
    # Práticas Farmacologia
    add("3ª Fase", "FARMA-A", "Farmacologia (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("3ª Fase", "FARMA-B", "Farmacologia (Turma B)",
        0, {"TERÇA": [0, 1]})
    add("3ª Fase", "FARMA-C", "Farmacologia (Turma C)",
        0, {"QUARTA": [6, 7]})
    add("3ª Fase", "FARMA-D", "Farmacologia (Turma D)",
        0, {"TERÇA": [2, 3]})
    add("3ª Fase", "FARMA-E", "Farmacologia (Turma E)",
        0, {"TERÇA": [8, 9]})
    add("3ª Fase", "FARMA-F", "Farmacologia (Turma F)",
        0, {"QUARTA": [2, 3]})
    
    # Práticas Nutrição
    add("3ª Fase", "NUTRI-A", "Nutrição Animal (Turma A)",
        0, {"QUARTA": [0, 1]})
    add("3ª Fase", "NUTRI-B", "Nutrição Animal (Turma B)",
        0, {"QUARTA": [2, 3]})

    # =====================================================================
    # 4ª FASE - Conforme PDF de Horários (Página 4)
    # =====================================================================
    # Teóricas
    add("4ª Fase", "ECOAD", "Economia e Administração",
        72, {"QUINTA": [6, 7]})
    add("4ª Fase", "EPIDE", "Epidemiologia",
        36, {"QUINTA": [0, 1]})
    add("4ª Fase", "MICROE-TEO", "Microbiologia Especial",
        90, {"QUINTA": [2, 3]})
    
    # Práticas Microbiologia Especial
    add("4ª Fase", "MICROE-A", "Microbiologia Especial (Turma A)",
        0, {"QUARTA": [2, 3]})
    add("4ª Fase", "MICROE-B", "Microbiologia Especial (Turma B)",
        0, {"QUARTA": [6, 7]})
    add("4ª Fase", "MICROE-C", "Microbiologia Especial (Turma C)",
        0, {"TERÇA": [8, 9]})

    # =====================================================================
    # 5ª FASE - Conforme PDF de Horários (Página 5)
    # =====================================================================
    # Teóricas - CORRIGIDAS conforme PDF
    add("5ª Fase", "FORRAG", "Forragicultura",
        54, {"SEXTA": [0, 1, 2]})
    add("5ª Fase", "FARMD-T", "Farmacodinâmica",
        72, {"TERÇA": [0, 1]})
    add("5ª Fase", "PATCLI-T", "Patologia Clínica",
        72, {"TERÇA": [7, 8]})
    # SEMIOLOGIA - CORRIGIDA: Segunda-feira, 3 slots (09:50-11:30)
    add("5ª Fase", "SEMIO-T", "Semiologia",
        90, {"SEGUNDA": [1,2,3]})
    add("5ª Fase", "PATG-T", "Patologia Geral",
        90, {"SEGUNDA": [7, 8, 9]})
    add("5ª Fase", "ALIMA", "Alimentos e Alimentação",
        90, {"QUINTA": [7, 8, 9, 10]})
    add("5ª Fase", "COMEXT", "Comunicação e Extensão",
        36, {"SEGUNDA": [11, 12]})
    
    # Práticas Patologia Clínica
    add("5ª Fase", "PATCLI-A", "Patologia Clínica (Turma A)",
        0, {"TERÇA": [9, 10]})
    add("5ª Fase", "PATCLI-B", "Patologia Clínica (Turma B)",
        0, {"QUARTA": [1, 2]})
    add("5ª Fase", "PATCLI-C", "Patologia Clínica (Turma C)",
        0, {"QUARTA": [7, 8]})
    add("5ª Fase", "PATCLI-D", "Patologia Clínica (Turma D)",
        0, {"QUINTA": [1, 2]})
    
    # Práticas Semiologia
    add("5ª Fase", "SEMIO-A", "Semiologia (Turma A)",
        0, {"TERÇA": [3, 4]})
    add("5ª Fase", "SEMIO-B", "Semiologia (Turma B)",
        0, {"QUARTA": [3, 4]})
    add("5ª Fase", "SEMIO-C", "Semiologia (Turma C)",
        0, {"QUINTA": [3, 4]})
    add("5ª Fase", "SEMIO-D", "Semiologia (Turma D)",
        0, {"SEXTA": [2, 3]})
    
    # Práticas Farmacodinâmica
    add("5ª Fase", "FARMD-A", "Farmacodinâmica (Turma A)",
        0, {"QUINTA": [2, 3]})
    add("5ª Fase", "FARMD-B", "Farmacodinâmica (Turma B)",
        0, {"QUINTA": [2, 3]})
    add("5ª Fase", "FARMD-C", "Farmacodinâmica (Turma C)",
        0, {"SEXTA": [7, 8]})
    
    # Práticas Patologia Geral
    add("5ª Fase", "PATG-A", "Patologia Geral (Turma A)",
        0, {"TERÇA": [3, 4]})
    add("5ª Fase", "PATG-B", "Patologia Geral (Turma B)",
        0, {"TERÇA": [9, 10]})
    add("5ª Fase", "PATG-C", "Patologia Geral (Turma C)",
        0, {"QUARTA": [7, 8]})

    # =====================================================================
    # 6ª FASE - Conforme PDF de Horários (Página 6)
    # =====================================================================
    # Teóricas
    add("6ª Fase", "SUINO-T", "Suinocultura",
        54, {"SEGUNDA": [0, 1]})
    add("6ª Fase", "DOENC-T", "Doenças Infecto-Contagiosas",
        90, {"TERÇA": [0, 1]})
    add("6ª Fase", "DOENPAR-T", "Doenças Parasitárias",
        72, {"QUARTA": [0, 1]})
    add("6ª Fase", "CLIRUM-T", "Clínica Médica de Ruminantes",
        90, {"QUINTA": [0, 1]})
    add("6ª Fase", "PATE-T", "Patologia Especial",
        90, {"SEXTA": [0, 1]})
    add("6ª Fase", "TERAP", "Terapêutica",
        36, {"SEGUNDA": [2, 3]})
    add("6ª Fase", "PISCIC-T", "Piscicultura",
        36, {"QUARTA": [2, 3]})
    
    # Práticas Suinocultura
    add("6ª Fase", "SUINO-A", "Suinocultura (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("6ª Fase", "SUINO-B", "Suinocultura (Turma B)",
        0, {"SEGUNDA": [0, 1]})
    add("6ª Fase", "SUINO-C", "Suinocultura (Turma C)",
        0, {"SEGUNDA": [2, 3]})
    
    # Práticas Doenças Infecto-Contagiosas
    add("6ª Fase", "DOENC-A", "Doenças Infecto-Contagiosas (Turma A)",
        0, {"QUINTA": [2, 3]})
    add("6ª Fase", "DOENC-B", "Doenças Infecto-Contagiosas (Turma B)",
        0, {"QUINTA": [6, 7]})
    add("6ª Fase", "DOENC-C", "Doenças Infecto-Contagiosas (Turma C)",
        0, {"QUINTA": [8, 9]})
    
    # Práticas Doenças Parasitárias
    add("6ª Fase", "DOENPAR-A", "Doenças Parasitárias (Turma A)",
        0, {"TERÇA": [6, 7]})
    add("6ª Fase", "DOENPAR-B", "Doenças Parasitárias (Turma B)",
        0, {"TERÇA": [8, 9]})
    add("6ª Fase", "DOENPAR-C", "Doenças Parasitárias (Turma C)",
        0, {"TERÇA": [10, 11]})
    add("6ª Fase", "DOENPAR-D", "Doenças Parasitárias (Turma D)",
        0, {"QUARTA": [6, 7]})
    
    # Práticas Clínica Médica de Ruminantes
    add("6ª Fase", "CLIRUM-A", "Clínica Médica de Ruminantes (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("6ª Fase", "CLIRUM-B", "Clínica Médica de Ruminantes (Turma B)",
        0, {"QUINTA": [8, 9]})
    add("6ª Fase", "CLIRUM-C", "Clínica Médica de Ruminantes (Turma C)",
        0, {"TERÇA": [8, 9]})
    add("6ª Fase", "CLIRUM-D", "Clínica Médica de Ruminantes (Turma D)",
        0, {"QUARTA": [6, 7]})
    
    # Práticas Patologia Especial
    add("6ª Fase", "PATE-A", "Patologia Especial (Turma A)",
        0, {"QUINTA": [8, 9]})
    add("6ª Fase", "PATE-B", "Patologia Especial (Turma B)",
        0, {"SEXTA": [6, 7]})
    add("6ª Fase", "PATE-C", "Patologia Especial (Turma C)",
        0, {"SEXTA": [8, 9]})
    
    # Práticas Piscicultura
    add("6ª Fase", "PISCIC-A", "Piscicultura (Turma A)",
        0, {"QUARTA": [2, 3]})
    add("6ª Fase", "PISCIC-B", "Piscicultura (Turma B)",
        0, {"QUARTA": [4]})
    add("6ª Fase", "PISCIC-C", "Piscicultura (Turma C)",
        0, {"QUARTA": [4]})

    # =====================================================================
    # 7ª FASE - Conforme PDF de Horários (Página 7)
    # =====================================================================
    # Teóricas
    add("7ª Fase", "ANEST-T", "Anestesiologia",
        54, {"SEGUNDA": [0, 1]})
    add("7ª Fase", "TECIR-T", "Técnica Cirúrgica",
        90, {"TERÇA": [0, 1]})
    add("7ª Fase", "DIAG-T", "Diagnóstico por Imagem",
        54, {"QUARTA": [0, 1]})
    add("7ª Fase", "CLIMED-T", "Clínica Médica de Cães e Gatos",
        90, {"QUINTA": [0, 1]})
    add("7ª Fase", "BOVIC", "Bovinocultura de Corte",
        54, {"SEXTA": [0, 1]})
    add("7ª Fase", "FRIA1-T", "Fisiopatologia da Reprodução",
        90, {"SEGUNDA": [2, 3], "QUARTA": [6, 7]})
    add("7ª Fase", "SAUD-T", "Saúde Pública Veterinária",
        54, {"SEXTA": [6, 7]})
    
    # Práticas Anestesiologia
    add("7ª Fase", "ANEST-A", "Anestesiologia (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("7ª Fase", "ANEST-B", "Anestesiologia (Turma B)",
        0, {"TERÇA": [0, 1]})
    add("7ª Fase", "ANEST-C", "Anestesiologia (Turma C)",
        0, {"QUARTA": [6, 7]})
    add("7ª Fase", "ANEST-D", "Anestesiologia (Turma D)",
        0, {"SEXTA": [8, 9]})
    
    # Práticas Técnica Cirúrgica
    add("7ª Fase", "TECIR-A", "Técnica Cirúrgica (Turma A)",
        0, {"TERÇA": [0, 1]})
    add("7ª Fase", "TECIR-B", "Técnica Cirúrgica (Turma B)",
        0, {"QUARTA": [2, 3]})
    add("7ª Fase", "TECIR-C", "Técnica Cirúrgica (Turma C)",
        0, {"TERÇA": [2, 3]})
    add("7ª Fase", "TECIR-D", "Técnica Cirúrgica (Turma D)",
        0, {"QUARTA": [2, 3]})
    
    # Práticas Diagnóstico por Imagem
    add("7ª Fase", "DIAG-A", "Diagnóstico por Imagem (Turma A)",
        0, {"TERÇA": [2, 3]})
    add("7ª Fase", "DIAG-B", "Diagnóstico por Imagem (Turma B)",
        0, {"QUARTA": [2, 3]})
    add("7ª Fase", "DIAG-C", "Diagnóstico por Imagem (Turma C)",
        0, {"QUINTA": [6, 7]})
    add("7ª Fase", "DIAG-D", "Diagnóstico por Imagem (Turma D)",
        0, {"SEXTA": [8, 9]})
    
    # Práticas Clínica Médica de Cães e Gatos
    add("7ª Fase", "CLIMED-A", "Clínica Médica de Cães e Gatos (Turma A)",
        0, {"SEGUNDA": [6, 7]})
    add("7ª Fase", "CLIMED-B", "Clínica Médica de Cães e Gatos (Turma B)",
        0, {"TERÇA": [6, 7]})
    add("7ª Fase", "CLIMED-C", "Clínica Médica de Cães e Gatos (Turma C)",
        0, {"QUINTA": [2, 3]})
    add("7ª Fase", "CLIMED-D", "Clínica Médica de Cães e Gatos (Turma D)",
        0, {"QUINTA": [6, 7]})
    
    # Práticas Fisiopatologia da Reprodução
    add("7ª Fase", "FRIA1-A", "Fisiopatologia da Reprodução (Turma A)",
        0, {"TERÇA": [6, 7]})
    add("7ª Fase", "FRIA1-B", "Fisiopatologia da Reprodução (Turma B)",
        0, {"QUARTA": [8, 9]})
    add("7ª Fase", "FRIA1-C", "Fisiopatologia da Reprodução (Turma C)",
        0, {"QUINTA": [6, 7]})
    add("7ª Fase", "FRIA1-D", "Fisiopatologia da Reprodução (Turma D)",
        0, {"QUARTA": [8, 9]})
    
    # Práticas Saúde Pública
    add("7ª Fase", "SAUD-A", "Saúde Pública (Turma A)",
        0, {"SEXTA": [8, 9]})
    add("7ª Fase", "SAUD-B", "Saúde Pública (Turma B)",
        0, {"SEXTA": [8, 9]})

    # =====================================================================
    # 8ª FASE - Conforme PDF de Horários (Página 8)
    # =====================================================================
    # Teóricas
    add("8ª Fase", "CLIEQ-T", "Clínica Médica de Equinos",
        90, {"TERÇA": [0, 1,2]})
    add("8ª Fase", "PACC-T", "Patologia e Clínica Cirúrgica",
        108, {"TERÇA": [0, 1]})
    add("8ª Fase", "SANI-T", "Sanidade Suína",
        54, {"TERÇA": [2, 3]})
    add("8ª Fase", "BOVILE", "Bovinocultura de Leite",
        54, {"QUARTA": [0, 1]})
    add("8ª Fase", "AVIC-T", "Avicultura",
        54, {"QUINTA": [0, 1]})
    add("8ª Fase", "OVINOC", "Ovinocultura",
        36, {"SEXTA": [0, 1]})
    add("8ª Fase", "INSPET-T", "Inspeção e Tecnologia",
        72, {"SEXTA": [8, 9, 10, 11]})
    
    # Práticas Clínica Médica de Equinos
    add("8ª Fase", "CLIEQ-A", "Clínica Médica de Equinos (Turma A)",
        0, {"SEGUNDA": [0, 1]})
    add("8ª Fase", "CLIEQ-B", "Clínica Médica de Equinos (Turma B)",
        0, {"SEGUNDA": [2, 3]})
    add("8ª Fase", "CLIEQ-C", "Clínica Médica de Equinos (Turma C)",
        0, {"SEXTA": [0, 1]})
    add("8ª Fase", "CLIEQ-D", "Clínica Médica de Equinos (Turma D)",
        0, {"SEXTA": [2, 3]})
    
    # Práticas Patologia e Clínica Cirúrgica
    add("8ª Fase", "PACC-A", "Patologia e Clínica Cirúrgica (Turma A)",
        0, {"SEGUNDA": [0, 1]})
    add("8ª Fase", "PACC-B", "Patologia e Clínica Cirúrgica (Turma B)",
        0, {"QUARTA": [6, 7,8 ,9]})
    add("8ª Fase", "PACC-C", "Patologia e Clínica Cirúrgica (Turma C)",
        0, {"QUINTA": [2, 3,4,5]})
    add("8ª Fase", "PACC-D", "Patologia e Clínica Cirúrgica (Turma D)",
        0, {"QUINTA": [0, 1,2,3]})
    
    # Práticas Sanidade Suína
    add("8ª Fase", "SANI-A", "Sanidade Suína (Turma A)",
        0, {"TERÇA": [6, 7]})
    add("8ª Fase", "SANI-B", "Sanidade Suína (Turma B)",
        0, {"QUARTA": [6, 7]})
    add("8ª Fase", "SANI-C", "Sanidade Suína (Turma C)",
        0, {"QUINTA": [6, 7]})
    add("8ª Fase", "SANI-D", "Sanidade Suína (Turma D)",
        0, {"QUARTA": [8, 9]})
    
    # Práticas Avicultura
    add("8ª Fase", "AVIC-A", "Avicultura (Turma A)",
        0, {"QUINTA": [6, 7]})
    add("8ª Fase", "AVIC-B", "Avicultura (Turma B)",
        0, {"QUINTA": [8, 9]})
    add("8ª Fase", "AVIC-C", "Avicultura (Turma C)",
        0, {"SEXTA": [8, 9]})
    
    # Práticas Ovinocultura
    add("8ª Fase", "OVINOC-A", "Ovinocultura (Turma A)",
        0, {"SEXTA": [6, 7]})
    add("8ª Fase", "OVINOC-B", "Ovinocultura (Turma B)",
        0, {"SEXTA": [8, 9]})
    
    # Práticas Inspeção
    add("8ª Fase", "INSPET-A", "Inspeção (Turma A)",
        0, {"SEXTA": [8, 9]})
    add("8ª Fase", "INSPET-B", "Inspeção (Turma B)",
        0, {"SEXTA": [10, 11]})

    # =====================================================================
    # 9ª FASE - Conforme PDF de Horários (Página 9)
    # =====================================================================
    # Teóricas
    add("9ª Fase", "OBSTE-T", "Obstetrícia",
        72, {"SEGUNDA": [0, 1]})
    add("9ª Fase", "CLIMED2-T", "Clínica Médica de Cães e Gatos II",
        90, {"TERÇA": [0, 1]})
    add("9ª Fase", "INSPE-T", "Inspeção II",
        90, {"QUARTA": [0, 1]})
    add("9ª Fase", "FRIA2-T", "Fisiopatologia da Reprodução II",
        72, {"QUARTA": [10,11]})
    add("9ª Fase", "DAVES-T", "Doenças das Aves",
        72, {"QUINTA": [2, 3]})
    add("9ª Fase", "TOXICO", "Toxicologia e Plantas Tóxicas",
        36, {"TERÇA": [8, 9]})
    
    # Práticas Obstetrícia
    add("9ª Fase", "OBSTE-A", "Obstetrícia (Turma A)",
        0, {"SEGUNDA": [0, 1]})
    add("9ª Fase", "OBSTE-B", "Obstetrícia (Turma B)",
        0, {"SEGUNDA": [2, 3]})
    add("9ª Fase", "OBSTE-C", "Obstetrícia (Turma C)",
        0, {"SEGUNDA": [6, 7]})
    add("9ª Fase", "OBSTE-D", "Obstetrícia (Turma D)",
        0, {"SEGUNDA": [8, 9]})
    
    # Práticas Clínica Médica de Cães e Gatos II
    add("9ª Fase", "CLIMED2-A", "Clínica Médica de Cães e Gatos II (Turma A)",
        0, {"SEGUNDA": [0, 1]})
    add("9ª Fase", "CLIMED2-B", "Clínica Médica de Cães e Gatos II (Turma B)",
        0, {"SEGUNDA": [2, 3]})
    add("9ª Fase", "CLIMED2-C", "Clínica Médica de Cães e Gatos II (Turma C)",
        0, {"SEGUNDA": [8, 9]})
    add("9ª Fase", "CLIMED2-D", "Clínica Médica de Cães e Gatos II (Turma D)",
        0, {"TERÇA": [2, 3]})
    
    # Práticas Inspeção II
    add("9ª Fase", "INSPE-A", "Inspeção II (Turma A)",
        0, {"QUARTA": [2, 3]})
    add("9ª Fase", "INSPE-B", "Inspeção II (Turma B)",
        0, {"QUARTA": [6, 7]})
    add("9ª Fase", "INSPE-C", "Inspeção II (Turma C)",
        0, {"QUARTA": [8, 9]})
    add("9ª Fase", "INSPE-D", "Inspeção II (Turma D)",
        0, {"SEXTA": [10, 11]})
    
    # Práticas Fisiopatologia da Reprodução II
    add("9ª Fase", "FRIA2-A", "Fisiopatologia da Reprodução II (Turma A)",
        0, {"QUINTA": [0, 1]})
    add("9ª Fase", "FRIA2-B", "Fisiopatologia da Reprodução II (Turma B)",
        0, {"QUINTA": [2, 3]})
    add("9ª Fase", "FRIA2-C", "Fisiopatologia da Reprodução II (Turma C)",
        0, {"SEXTA": [0, 1]})
    add("9ª Fase", "FRIA2-D", "Fisiopatologia da Reprodução II (Turma D)",
        0, {"SEXTA": [2, 3]})
    
    # Práticas Doenças das Aves
    add("9ª Fase", "DAVES-A", "Doenças das Aves (Turma A)",
        0, {"QUINTA": [6, 7]})
    add("9ª Fase", "DAVES-B", "Doenças das Aves (Turma B)",
        0, {"SEGUNDA": [0, 1]})
    add("9ª Fase", "DAVES-C", "Doenças das Aves (Turma C)",
        0, {"SEGUNDA": [2, 3]})

    # =====================================================================
    # ELETIVAS - Conforme PDF de Horários (Página 10)
    # =====================================================================
    add("Eletivas", "LACTI", "Laticínios",
        36, {"SEGUNDA": [2, 3]})
    add("Eletivas", "OFTAL", "Oftalmologia Veterinária",
        36, {"TERÇA": [2, 3]})
    add("Eletivas", "DERMA", "Dermatologia Veterinária",
        36, {"QUINTA": [2, 3]})
    add("Eletivas", "CITODIAG", "Citologia Diagnóstica",
        36, {"QUARTA": [2, 3, 4]})
    add("Eletivas", "FISIATRIA", "Fisiatria Veterinária",
        36, {"SEGUNDA": [6, 7]})
    add("Eletivas", "COMPBEM", "Comportamento e Bem-Estar Animal II",
        36, {"TERÇA": [6, 7]})
    add("Eletivas", "GEREN", "Gerenciamento e Produção",
        36, {"QUARTA": [6, 7]})
    add("Eletivas", "EQUINO", "Equinocultura",
        36, {"QUINTA": [6, 7]})
    add("Eletivas", "MICROPESQ", "Microbiologia dos Pescados",
        36, {"SEXTA": [6, 7]})
    add("Eletivas", "CARDIOLOGIA", "Cardiologia de Cães e Gatos",
        36, {"SÁBADO": [6, 7]})
    add("Eletivas", "MEDSILV", "Medicina de Animais Silvestres",
        36, {"SEGUNDA": [8, 9]})
    add("Eletivas", "AQUACULT", "Aquacultura",
        36, {"SEGUNDA": [10, 11]})
    add("Eletivas", "ANATAVES", "Anatomia das Aves",
        36, {"QUARTA": [6, 7]})
    add("Eletivas", "ESTAGIO", "Estágio Curricular",
        486, {"SEGUNDA": [14]})

    link_theory_to_practicals(catalog)
    return catalog


# Mapeamento de códigos teóricos para grupos de práticas
GROUP_ALIASES = {
    "ANA1-TEO": "ANA1",
    "HISTG-TEO": "HISTG",
    "BIOQB-TEO": "BIOQB",
    "ANA2-TEO": "ANA2",
    "HIST2-TEO": "HIST2",
    "GENET-TEO": "GENE",
    "BIOQM-TEO": "BIOQM",
    "PARA1-TEO": "PARA1",
    "FISI1-TEO": "FISI1",
    "MICRO-TEO": "MICRO",
    "IMUNO-TEO": "IMUNO",
    "FISI2-TEO": "FISI2",
    "PARA2-TEO": "PARA2",
    "FARMA-TEO": "FARMA",
    "NUTRI-TEO": "NUTRI",
    "MICROE-TEO": "MICROE",
    "FARMD-TEO": "FARMD",
    "PATCLI-TEO": "PATCLI",
    "SEMIO-TEO": "SEMIO",
    "PATGER-TEO": "PATGER",
    "SUINO-TEO": "SUINO",
    "DOENC-TEO": "DOENC",
    "DOENPAR-TEO": "DOENPAR",
    "CLIRUM-TEO": "CLIRUM",
    "PATESP-TEO": "PATESP",
    "PISCIC-TEO": "PISCIC",
    "ANEST-TEO": "ANEST",
    "TECIR-TEO": "TECIR",
    "DIAGIM-TEO": "DIAGIM",
    "CLIMED-TEO": "CLIMED",
    "FISREP-TEO": "FISREP",
    "SAUDPUB-TEO": "SAUDPUB",
    "CLIEQ-TEO": "CLIEQ",
    "PACC-TEO": "PACC",
    "SANISUI-TEO": "SANISUI",
    "AVICUL-TEO": "AVICUL",
    "INSPET-TEO": "INSPET",
    "OBSTE-TEO": "OBSTE",
    "CLIMED2-TEO": "CLIMED2",
    "INSPE-TEO": "INSPE",
    "FISREP3-TEO": "FISREP3",
    "DAVES-TEO": "DAVES",
}


def infer_group_and_kind(code: str):
    """Deduz o 'grupo' e o 'tipo' a partir do código da matéria."""
    if code in GROUP_ALIASES:
        return GROUP_ALIASES[code], "teorica"
    if code.endswith("-TEO"):
        return code[:-4], "teorica"
    if code.endswith("-T"):
        return code[:-2], "teorica"
    if len(code) >= 2 and code[-2] == "-" and code[-1] in "ABCDEFGH":
        return code[:-2], "pratica"
    return code, "unica"


def link_theory_to_practicals(catalog: List[Course]) -> None:
    """Atribui group/kind a cada disciplina e vincula cada turma prática à sua teórica."""
    for c in catalog:
        c.group, c.kind = infer_group_and_kind(c.code)

    theory_by_group = {c.group: c for c in catalog if c.kind == "teorica"}
    for c in catalog:
        if c.kind == "pratica":
            c.theory = theory_by_group.get(c.group)


def combined_schedule(course: Course) -> Dict[str, List[int]]:
    """Horário da turma prática somado ao horário da teórica vinculada."""
    sched: Dict[str, List[int]] = {day: list(slots)
                                    for day, slots in course.schedule.items()}
    if course.theory:
        for day, slots in course.theory.schedule.items():
            sched[day] = sorted(set(sched.get(day, [])) | set(slots))
    return sched


def check_conflict(course_to_add: Course, registered_courses: List[Course]) -> Optional[str]:
    schedule_to_add = combined_schedule(course_to_add)
    for reg in registered_courses:
        for day, slots in schedule_to_add.items():
            if day in reg.schedule:
                overlap = set(slots).intersection(set(reg.schedule[day]))
                if overlap:
                    conflicting_slot = sorted(list(overlap))[0]
                    return f"Conflito com '{reg.name}' na {day} no horário {get_slot_time_str(conflicting_slot)}."
    return None


# =========================================================================
# TOKENS DE DESIGN
# =========================================================================

PAGE_BG = "#448D6FC8"
PANEL_BG = "#DBFAD7"
HEADER_GRADIENT = "linear-gradient(135deg, #1B1F3B 0%, #2E3566 100%)"
TIME_COL_GRADIENT = "linear-gradient(135deg, #EDEFF7 0%, #E3E6F3 100%)"
EMPTY_CELL_BG = "#B9F8DE"
GRID_LINE = "#000000"

PHASE_COLORS = {
    "1ª Fase":  ("#7C4DFF", "#9C7BFF"),
    "2ª Fase":  ("#2FB4C7", "#5FD3E3"),
    "3ª Fase":  ("#1FA37A", "#3FCB9C"),
    "4ª Fase":  ("#3D8BE0", "#63ABF2"),
    "5ª Fase":  ("#E0A62F", "#F2C55E"),
    "6ª Fase":  ("#E0632F", "#F28A5E"),
    "7ª Fase":  ("#D6396B", "#EE6D97"),
    "8ª Fase":  ("#8B3DE0", "#B06BF2"),
    "9ª Fase":  ("#2F5DE0", "#6086F2"),
    "Eletivas": ("#F00673", "#8C99A6"),
}


def phase_gradient(phase: str) -> str:
    c1, c2 = PHASE_COLORS.get(phase, ("#3D8BE0", "#63ABF2"))
    return f"linear-gradient(135deg, {c1} 0%, {c2} 100%)"


# =========================================================================
# INTERFACE — Streamlit
# =========================================================================

st.set_page_config(
    page_title="Simulador de Matrícula-CAV", layout="wide")

st.markdown(f"""
<style>
.stApp {{ background-color: {PAGE_BG}; }}
</style>
""", unsafe_allow_html=True)

if "available_courses" not in st.session_state:
    st.session_state.available_courses = build_initial_catalog()
if "registered_courses" not in st.session_state:
    st.session_state.registered_courses = []

st.title("Simulador de Matrícula - UDESC-CAV")

col_left, col_right = st.columns([1, 2], gap="large")

# ---------------- Painel esquerdo ----------------
with col_left:
    st.subheader("Buscar disciplinas")

    phase_choice = st.selectbox("Fase", ["Todas as Fases"] + PHASES)
    query = st.text_input(
        "Buscar por código, nome ou carga horária").lower().strip()

    filtered_courses = [
        c for c in st.session_state.available_courses
        if c.kind != "teorica"
        and (phase_choice == "Todas as Fases" or c.phase == phase_choice)
        and (query in c.code.lower() or query in c.name.lower() or query in str(c.credits))
    ]

    st.subheader(f"Todas Disciplinas")
    options = [str(c) for c in filtered_courses]
    selected_label = st.selectbox(
        "Catálogo", options, label_visibility="collapsed") if options else None

    selected_course = None
    if selected_label:
        idx = options.index(selected_label)
        selected_course = filtered_courses[idx]

        c1, c2 = PHASE_COLORS.get(
            selected_course.phase, ("#3D8BE0", "#63ABF2"))
        st.markdown(
            f"<span style='background:{phase_gradient(selected_course.phase)};color:white;"
            f"padding:2px 10px;border-radius:12px;font-size:14px;font-weight:600'>{selected_course.phase}</span>",
            unsafe_allow_html=True,
        )


    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        add_clicked = st.button(
            "➕ Adicionar Disciplina", use_container_width=True, disabled=selected_course is None)
    with btn_col2:
        custom_clicked = st.button("+ Personalizada", use_container_width=True)

    if add_clicked and selected_course:
        already_added = any(
            c.group == selected_course.group for c in st.session_state.registered_courses)
        if already_added:
            st.warning(
                f"Você já tem uma turma de '{selected_course.name}' adicionada. "
                "Remova-a antes de escolher outra."
            )
        else:
            conflict_msg = check_conflict(
                selected_course, st.session_state.registered_courses)
            if conflict_msg:
                st.error(f"Choque de Horário: {conflict_msg}")
            else:
                st.session_state.registered_courses.append(selected_course)
                if selected_course.theory:
                    st.session_state.registered_courses.append(
                        selected_course.theory)
                    st.success(
                        f"'{selected_course.name}' + Teórica adicionadas com sucesso!")
                else:
                    st.success(
                        f"'{selected_course.name}' adicionada com sucesso!")
                st.rerun()

    if custom_clicked:
        st.session_state["show_custom_form"] = True

    if st.session_state.get("show_custom_form"):
        with st.expander("Adicionar Matéria Personalizada", expanded=True):
            with st.form("custom_course_form", clear_on_submit=True):
                code = st.text_input("Código")
                name = st.text_input("Nome da Matéria")
                credits = st.number_input("Carga Horária", min_value=1, step=1)
                phase = st.selectbox("Fase", PHASES)
                day = st.selectbox("Dia da Semana", DAYS)
                slot_labels = [
                    f"Slot {s}: {get_slot_time_str(s)}" for s in range(TOTAL_SLOTS)]
                selected_slots_labels = st.multiselect(
                    "Selecione os Slots", slot_labels)

                submitted = st.form_submit_button("Salvar Matéria")
                if submitted:
                    if not code or not name or not selected_slots_labels:
                        st.error("Preencha todos os campos.")
                    else:
                        selected_slots = [slot_labels.index(
                            s) for s in selected_slots_labels]
                        new_course = Course(code, name, int(credits), {
                                            day: selected_slots}, phase=phase)
                        new_course.group = code
                        new_course.kind = "unica"
                        st.session_state.available_courses.append(new_course)
                        st.session_state["show_custom_form"] = False
                        st.success(
                            f"Matéria '{code}' criada e adicionada ao catálogo.")
                        st.rerun()

    grouped_groups = []
    for c in st.session_state.registered_courses:
        if c.group not in grouped_groups:
            grouped_groups.append(c.group)

    st.subheader(f"Matérias Selecionadas ({len(grouped_groups)})")
    for group in grouped_groups:
        group_courses = [
            c for c in st.session_state.registered_courses if c.group == group]
        practical = next(
            (c for c in group_courses if c.kind != "teorica"), group_courses[0])
        theory = next(
            (c for c in group_courses if c.kind == "teorica"), None)
        total_credits = sum(c.credits for c in group_courses)

        label = f"[{practical.code}] {practical.name} ({total_credits}h)"

        row_col1, row_col2 = st.columns([4, 1])
        row_col1.write(label)
        if row_col2.button("🗑️", key=f"remove_{group}"):
            st.session_state.registered_courses = [
                c for c in st.session_state.registered_courses if c.group != group]
            st.rerun()

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
                row += (
                    f"<td style='padding:6px;background:{bg};border:1px solid {GRID_LINE};"
                    "border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.15);"
                    "color:white;font-size:10px;font-weight:600;text-align:center'>"
                    f"{course.code}<br><span style='font-weight:400;opacity:0.9'>{course.name[:14]}...</span></td>"
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
