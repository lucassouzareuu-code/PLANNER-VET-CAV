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
        "17:40 - 18:30", "18:30 - 19:20", "19:20 - 20:10", "20:10 - 21:00", "21:00 - 21:50", "21:50 - 22:0"
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
        # "group" identifica a disciplina (ex.: "ANA1") independente da turma/teórica.
        # "kind" é "teorica", "pratica" ou "unica" (matéria sem divisão em turmas).
        # "theory" é preenchido automaticamente (ver link_theory_to_practicals) apontando
        # para o Course da parte teórica correspondente, quando existir.
        self.group = code
        self.kind = "unica"
        self.theory: Optional["Course"] = None
        self.official_code: Optional[str] = None
        self.ch: Optional[int] = None
        self.creditos: Optional[int] = None
        self.tipo: str = "Obrigatória"

    @property
    def display_code(self) -> str:
        """Código a ser exibido: o oficial da Grade Curricular quando existir."""
        return self.official_code or self.code

    @property
    def display_ch(self) -> int:
        """Carga horária a ser exibida: a oficial (da disciplina como um todo,
        já contemplando teórica + prática) quando existir."""
        return self.ch if self.ch is not None else self.credits

    def __str__(self):
        label = f"[{self.display_code}] {self.name} ({self.display_ch}h"
        if self.creditos is not None:
            label += f" | {self.creditos} créd."
        label += ")"
        return label


def build_initial_catalog() -> List[Course]:
    """Catálogo completo de Medicina Veterinária UDESC CAV """
    catalog: List[Course] = []

    def add(phase, code, name, credits, schedule):
        catalog.append(Course(code, name, credits, schedule, phase=phase))

    # 1ª FASE
    add("1ª Fase", "ANA1-TEO", "Anatomia I (Teórica)",
        72, {"SEGUNDA": [0, 1], "TERÇA": [0, 1]})
    add("1ª Fase", "ANA1-A", "Anatomia I (Turma A)", 36, {"QUINTA": [10]})
    add("1ª Fase", "ANA1-B", "Anatomia I (Turma B)", 36, {"QUARTA": [0, 1]})
    add("1ª Fase", "ANA1-C", "Anatomia I (Turma C)", 36, {"SEXTA": [0, 1]})
    add("1ª Fase", "ANA1-D", "Anatomia I (Turma D)", 36, {"SEXTA": [2, 10]})
    add("1ª Fase", "HISTG-T", "Histologia Geral (Teórica)",
        72, {"SEGUNDA": [2, 3]})
    add("1ª Fase", "HISTG-A", "Histologia Geral (Turma A)",
        36, {"QUARTA": [0, 1]})
    add("1ª Fase", "HISTG-B", "Histologia Geral (Turma B)",
        36, {"QUINTA": [6, 7]})
    add("1ª Fase", "HISTG-C", "Histologia Geral (Turma C)",
        36, {"QUARTA": [6, 7]})
    add("1ª Fase", "HISTG-D", "Histologia Geral (Turma D)",
        36, {"QUARTA": [8, 9]})
    add("1ª Fase", "SOAMV", "Sociologia Aplicada", 36, {"SEGUNDA": [2, 3]})
    add("1ª Fase", "ECOLO-1", "Ecologia e Desenvolvimento",
        36, {"TERÇA": [2, 3]})
    add("1ª Fase", "BIOQB-T", "Bioquímica de Biomoléculas (Teórica)",
        54, {"TERÇA": [6, 7], "QUARTA": [6, 7]})
    add("1ª Fase", "BIOQB-B", "Bioquímica de Biomoléculas (Turma A)",
        54, {"QUARTA": [8, 9]})
    add("1ª Fase", "BIOQB-C", "Bioquímica de Biomoléculas (Turma B)",
        54, {"QUINTA": [6, 7]})
    add("1ª Fase", "ESTCA", "Estatística e Experimentação",
        54, {"SEGUNDA": [6, 7, 8]})
    add("1ª Fase", "EXTEN", "Extensão, Comunicação e Sociedade",
        36, {"SEXTA": [6, 7]})
    add("1ª Fase", "COMPOR", "Comportamento e Bem-Estar Animal",
        36, {"QUINTA": [8, 9]})

    # 2ª FASE
    add("2ª Fase", "ANA2-TEO", "Anatomia II (Teórica)",
        72, {"SEGUNDA": [0, 1], "TERÇA": [2, 3]})
    add("2ª Fase", "ANA2-A", "Anatomia II (Turma A)",
        36, {"QUINTA": [6, 7], "SEXTA": [8]})
    add("2ª Fase", "ANA2-B", "Anatomia II (Turma B)",
        36, {"QUINTA": [8], "SÁBADO": [9, 10]})
    add("2ª Fase", "ANA2-C", "Anatomia II (Turma C)",
        36, {"QUINTA": [10, 11], "SEXTA": [11]})
    add("2ª Fase", "ANA2-D", "Anatomia II (Turma D)",
        36, {"SÁBADO": [0, 1], "SEXTA": [10, 11]})
    add("2ª Fase", "HIST2-TEO", "Histologia e Embriologia Vet. (Teórica)",
        72, {"SEGUNDA": [2, 3], "QUINTA": [0]})
    add("2ª Fase", "HIST2-A", "Histologia e Embriologia (Turma A)",
        36, {"SEGUNDA": [6, 7]})
    add("2ª Fase", "HIST2-B", "Histologia e Embriologia (Turma B)",
        36, {"SEGUNDA": [8, 9]})
    add("2ª Fase", "HIST2-C", "Histologia e Embriologia (Turma C)",
        36, {"TERÇA": [6, 7]})
    add("2ª Fase", "HIST2-D", "Histologia e Embriologia (Turma D)",
        36, {"SEXTA": [6, 7]})
    add("2ª Fase", "GENET", "Genética (Teórica)", 54, {"SEXTA": [0, 1]})
    add("2ª Fase", "GENE-A", "Genética (Turma A)", 36, {"SEXTA": [2, 3]})
    add("2ª Fase", "GENE-B", "Genética (Turma B)", 36, {"SEXTA": [6, 7]})
    add("2ª Fase", "BIOQM-T",
        "Bioquímica Metabólica (Teórica)", 54, {"SEXTA": [2, 3]})
    add("2ª Fase", "BIOQM-A", "Bioquímica Metabólica (Turma A)",
        36, {"SEGUNDA": [6, 7]})
    add("2ª Fase", "BIOQM-B", "Bioquímica Metabólica (Turma B)",
        36, {"TERÇA": [6, 7, 8]})
    
    # 3ª FASE
    add("3ª Fase", "IMUNO-T", "Imunologia (Teórica)",
        54, {"SEGUNDA": [0, 1]})
    add("3ª Fase", "IMUNO-A", "Imunologia (Turma A)", 36, {"SEGUNDA": [11]})
    add("3ª Fase", "IMUNO-B", "Imunologia (Turma B)", 36, {"SEGUNDA": [10]})
    add("3ª Fase", "PARA1-TEO",
            "Parasitologia I (Teórica)", 72, {"SEXTA": [3, 4]})
    add("3ª Fase", "PARA1-A", "Parasitologia I (Turma A)",
            36, {"SEGUNDA": [0, 1]})
    add("3ª Fase", "PARA1-B",
            "Parasitologia I (Turma B)", 36, {"QUINTA": [11]})
    add("3ª Fase", "PARA1-C", "Parasitologia I (Turma C)",
            36, {"QUINTA": [2, 3]})
    add("3ª Fase", "PARA1-D",
            "Parasitologia I (Turma D)", 36, {"SEXTA": [6, 7]})
    add("3ª Fase", "FISI1-T", "Fisiologia I (Teórica)",
            72, {"QUINTA": [5, 6, 7]})
    add("3ª Fase", "FISI1-A", "Fisiologia I (Turma A)",
            36, {"SEGUNDA": [8, 9]})
    add("3ª Fase", "FISI1-B", "Fisiologia I (Turma B)",
            36, {"SEGUNDA": [10, 11]})
    add("3ª Fase", "FISI1-C", "Fisiologia I (Turma C)",
            36, {"QUINTA": [10, 11]})
    add("3ª Fase", "FISI1-D", "Fisiologia I (Turma D)",
            36, {"TERÇA": [10, 11]})
    add("3ª Fase", "MICRO-T", "Microbiologia Geral (Teórica)",
        72, {"SEGUNDA": [2, 3]})
    add("3ª Fase", "MICRO-A", "Microbiologia Geral (Turma A)",
        36, {"SEGUNDA": [8, 9]})
    add("3ª Fase", "MICRO-B", "Microbiologia Geral (Turma B)",
        36, {"TERÇA": [6, 7]})
    add("3ª Fase", "MICRO-C", "Microbiologia Geral (Turma C)",
        36, {"TERÇA": [8, 9]})
    add("3ª Fase", "MICRO-D", "Microbiologia Geral (Turma D)",
        36, {"SEGUNDA": [6, 7]})
    add("3ª Fase", "ANATT-T",
        "Anatomia Topográfica (Teórica)", 54, {"QUARTA": [6, 7]})
    add("3ª Fase", "ANATT-A", "Anatomia Topográfica (Turma A)",
        36, {"QUINTA": [2, 3]})
    add("3ª Fase", "ANATT-B", "Anatomia Topográfica (Turma B)",
        36, {"QUINTA": [6, 7]})
    add("3ª Fase", "ANATT-C", "Anatomia Topográfica (Turma C)",
        36, {"SEXTA": [8, 9]})
    add("3ª Fase", "ANATT-D", "Anatomia Topográfica (Turma D)",
        36, {"SEXTA": [6, 7]})

    # 4ª FASE
    add("4ª Fase", "NUTRI-4", "Nutrição Animal",
        54, {"QUARTA": [0, 1], "QUINTA": [0]})
    add("4ª Fase", "EPIDE-4", "Epidemiologia", 36, {"QUINTA": [2, 3]})
    add("4ª Fase", "ECONO-4", "Economia e Administração",
        54, {"SEXTA": [0, 1], "QUINTA": [6, 7]})
    add("4ª Fase", "MELHO-4", "Melhoramento Animal", 36, {"QUINTA": [8, 9]})
    add("4ª Fase", "FISIO2-T",
        "Fisiologia II (Teórica)", 72, {"SEGUNDA": [0, 1]})
    add("4ª Fase", "FISIO2-A", "Fisiologia II (Turma A)",
        36, {"SEGUNDA": [2, 3]})
    add("4ª Fase", "FISIO2-B",
        "Fisiologia II (Turma B)", 36, {"TERÇA": [0, 1]})
    add("4ª Fase", "FISIO2-C",
        "Fisiologia II (Turma C)", 36, {"TERÇA": [6, 7]})
    add("4ª Fase", "FISIO2-D", "Fisiologia II (Turma D)",
        36, {"QUARTA": [8, 9]})
    add("4ª Fase", "FARM1-T", "Farmacologia Geral (Teórica)",
        72, {"SEGUNDA": [6, 7]})
    add("4ª Fase", "FARM1-A", "Farmacologia Geral (Turma A)",
        36, {"TERÇA": [8, 9]})
    add("4ª Fase", "FARM1-B", "Farmacologia Geral (Turma B)",
        36, {"QUARTA": [2, 3]})
    add("4ª Fase", "FARM1-C", "Farmacologia Geral (Turma C)",
        36, {"TERÇA": [2, 3]})
    add("4ª Fase", "MICRE-T", "Microbiologia Especial (Teórica)",
        72, {"QUARTA": [2, 3], "SEXTA": [2, 3, 4]})
    add("4ª Fase", "MICRE-B", "Microbiologia Especial (Turma B)",
        36, {"QUARTA": [6, 7]})
    add("4ª Fase", "MICRE-C", "Microbiologia Especial (Turma C)",
        36, {"QUARTA": [8, 9]})

    # 5ª FASE
    add("5ª Fase", "FORRA-5", "Forragicultura", 54, {"SEXTA": [0, 1, 2]})
    add("5ª Fase", "SEMIO-T", "Semiologia (Teórica)",
        90, {"SEGUNDA": [1, 2, 3]})
    add("5ª Fase", "SEMIO-A", "Semiologia (Turma A)", 36, {"TERÇA": [2, 3]})
    add("5ª Fase", "SEMIO-B", "Semiologia (Turma B)", 36, {"QUARTA": [2, 3]})
    add("5ª Fase", "SEMIO-C", "Semiologia (Turma C)", 36, {"QUINTA": [2, 3]})
    add("5ª Fase", "SEMIO-D", "Semiologia (Turma D)", 36, {"SEXTA": [2, 3]})
    add("5ª Fase", "FARMD-T",
        "Farmacodinâmica (Teórica)", 72, {"TERÇA": [0, 1]})
    add("5ª Fase", "FARMD-A", "Farmacodinâmica (Turma A)",
        36, {"QUINTA": [0, 1]})
    add("5ª Fase", "FARMD-B", "Farmacodinâmica (Turma B)",
        36, {"QUINTA": [2, 3]})
    add("5ª Fase", "FARMD-C", "Farmacodinâmica (Turma C)",
        36, {"SEXTA": [6, 7]})
    add("5ª Fase", "PATCL-T",
        "Patologia Clínica Vet. (Teórica)", 72, {"TERÇA": [6, 7]})
    add("5ª Fase", "PATCL-A", "Patologia Clínica Vet. (Turma A)",
        36, {"QUARTA": [0, 1]})
    add("5ª Fase", "PATCL-B", "Patologia Clínica Vet. (Turma B)",
        36, {"QUARTA": [2, 3]})
    add("5ª Fase", "PATCL-C", "Patologia Clínica Vet. (Turma C)",
        36, {"QUARTA": [6, 7]})
    add("5ª Fase", "PATCL-D", "Patologia Clínica Vet. (Turma D)",
        36, {"QUINTA": [0, 1]})
    add("5ª Fase", "PATG-T", "Patologia Geral (Teórica)",
        90, {"SEGUNDA": [6, 7, 8]})
    add("5ª Fase", "PATG-A", "Patologia Geral (Turma A)",
        36, {"TERÇA": [2, 3]})
    add("5ª Fase", "PATG-B", "Patologia Geral (Turma B)",
        36, {"TERÇA": [8, 9]})
    add("5ª Fase", "PATG-C", "Patologia Geral (Turma C)",
        36, {"QUARTA": [8, 9]})
    add("5ª Fase", "ALIMA-5", "Alimentos e Alimentação Animal",
        90, {"QUINTA": [6, 7, 8, 9, 10]})
    add("5ª Fase", "COEXT-5", "Comunicação e Extensão Rural",
        36, {"SEGUNDA": [9, 10]})

    # 6ª FASE
    add("6ª Fase", "SUINO-T", "Suinocultura (Teórica)",
        54, {"SEGUNDA": [0, 1]})
    add("6ª Fase", "SUINO-A", "Suinocultura (Turma A)", 36, {"SEGUNDA": [6]})
    add("6ª Fase", "SUINO-B", "Suinocultura (Turma B)", 36, {"SEGUNDA": [7]})
    add("6ª Fase", "SUINO-C", "Suinocultura (Turma C)", 36, {"SEGUNDA": [8]})
    add("6ª Fase", "INFEC-T", "Doenças Infectocontagiosas (Teórica)",
        72, {"TERÇA": [0, 1, 2]})
    add("6ª Fase", "INFEC-A", "Doenças Infectocontagiosas (Turma A)",
        36, {"QUINTA": [6, 7]})
    add("6ª Fase", "INFEC-B", "Doenças Infectocontagiosas (Turma B)",
        36, {"SEXTA": [8, 9]})
    add("6ª Fase", "INFEC-C", "Doenças Infectocontagiosas (Turma C)",
        36, {"QUARTA": [8, 9]})
    add("6ª Fase", "PARAS2-T",
        "Doenças Parasitárias (Teórica)", 72, {"QUARTA": [0, 1]})
    add("6ª Fase", "PARAS2-A",
        "Doenças Parasitárias (Turma A)", 36, {"TERÇA": [6, 7]})
    add("6ª Fase", "PARAS2-B", "Doenças Parasitárias (Turma B)",
        36, {"TERÇA": [9, 10, 11]})
    add("6ª Fase", "PARAS2-D", "Doenças Parasitárias (Turma D)",
        36, {"QUARTA": [6, 7]})
    add("6ª Fase", "PARAS2-E",
        "Doenças Parasitárias (Turma E)", 36, {"TERÇA": [8]})
    add("6ª Fase", "CLINR-T", "Clínica Médica de Ruminantes (Teórica)",
        72, {"QUINTA": [0, 1, 2]})
    add("6ª Fase", "CLINR-A", "Clínica Médica de Ruminantes (Turma A)",
        36, {"SEGUNDA": [6, 7]})
    add("6ª Fase", "CLINR-B", "Clínica Médica de Ruminantes (Turma B)",
        36, {"TERÇA": [8, 9]})
    add("6ª Fase", "CLINR-C", "Clínica Médica de Ruminantes (Turma C)",
        36, {"QUARTA": [8, 9]})
    add("6ª Fase", "CLINR-D", "Clínica Médica de Ruminantes (Turma D)",
        36, {"QUINTA": [6, 7]})
    add("6ª Fase", "PATESP-T", "Patologia Especial (Teórica)",
        72, {"SEXTA": [0, 1, 2]})
    add("6ª Fase", "PATESP-A",
        "Patologia Especial (Turma A)", 36, {"SEXTA": [6, 7]})
    add("6ª Fase", "PATESP-B",
        "Patologia Especial (Turma B)", 36, {"SEXTA": [8, 9]})
    add("6ª Fase", "PATESP-C",
        "Patologia Especial (Turma C)", 36, {"SEXTA": [8, 9]})
    add("6ª Fase", "PISCI-7", "Piscicultura", 36, {"QUARTA": [2, 3, 4]})
    add("6ª Fase", "TERAP-7", "Terapêutica Veterinária",
        36, {"SEGUNDA": [2, 3]})

    # 7ª FASE
    add("7ª Fase", "ANEST-T", "Anestesiologia (Teórica)",
        54, {"SEGUNDA": [1, 2]})
    add("7ª Fase", "ANEST-A", "Anestesiologia (Turma A)",
        36, {"SEGUNDA": [6, 7]})
    add("7ª Fase", "ANEST-B", "Anestesiologia (Turma B)",
        36, {"TERÇA": [6, 7]})
    add("7ª Fase", "ANEST-C", "Anestesiologia (Turma C)",
        36, {"TERÇA": [8, 9]})
    add("7ª Fase", "ANEST-D", "Anestesiologia (Turma D)",
        36, {"TERÇA": [1, 2]})
    add("7ª Fase", "TCIR-T", "Técnica Cirúrgica (Teórica)",
        72, {"SEGUNDA": [8, 9]})
    add("7ª Fase", "TCIR-A", "Técnica Cirúrgica (Turma A)",
        36, {"TERÇA": [0, 1, 2]})
    add("7ª Fase", "TCIR-B", "Técnica Cirúrgica (Turma B)",
        36, {"TERÇA": [6, 7, 8]})
    add("7ª Fase", "TCIR-C", "Técnica Cirúrgica (Turma C)",
        36, {"QUARTA": [0, 1, 2]})
    add("7ª Fase", "TCIR-D", "Técnica Cirúrgica (Turma D)",
        36, {"QUARTA": [6, 7, 8]})
    add("7ª Fase", "DIAG-T", "Diagnóstico por Imagem (Teórica)",
        54, {"SEGUNDA": [10]})
    add("7ª Fase", "DIAG-A", "Diagnóstico por Imagem (Turma A)",
        36, {"QUARTA": [1, 2]})
    add("7ª Fase", "DIAG-B", "Diagnóstico por Imagem (Turma B)",
        36, {"QUARTA": [6, 7]})
    add("7ª Fase", "DIAG-C", "Diagnóstico por Imagem (Turma C)",
        36, {"QUARTA": [8, 9]})
    add("7ª Fase", "DIAG-D", "Diagnóstico por Imagem (Turma D)",
        36, {"QUINTA": [8, 9]})
    add("7ª Fase", "CLINC-T", "Clínica Médica de Cães e Gatos (Teórica)",
        72, {"QUINTA": [0, 1, 2]})
    add("7ª Fase", "CLINC-A", "Clínica Médica de Cães e Gatos (Turma A)",
        36, {"SEGUNDA": [6, 7]})
    add("7ª Fase", "CLINC-B", "Clínica Médica de Cães e Gatos (Turma B)",
        36, {"TERÇA": [7, 8]})
    add("7ª Fase", "CLINC-C", "Clínica Médica de Cães e Gatos (Turma C)",
        36, {"QUARTA": [7, 8]})
    add("7ª Fase", "CLINC-D", "Clínica Médica de Cães e Gatos (Turma D)",
        36, {"QUARTA": [6, 7]})
    add("7ª Fase", "FISREPO-T", "Fisiopatologia da Reprodução (Teórica)",
        72, {"SEGUNDA": [6, 7, 8]})
    add("7ª Fase", "FISREPO-A",
        "Fisiopatologia da Reprodução (Turma A)", 36, {"TERÇA": [7, 8]})
    add("7ª Fase", "FISREPO-B",
        "Fisiopatologia da Reprodução (Turma B)", 36, {"TERÇA": [8, 9]})
    add("7ª Fase", "FISREPO-C",
        "Fisiopatologia da Reprodução (Turma C)", 36, {"QUARTA": [7, 8]})
    add("7ª Fase", "FISREPO-D",
        "Fisiopatologia da Reprodução (Turma D)", 36, {"QUINTA": [8, 9]})
    add("7ª Fase", "BOVIC-T",
        "Bovinocultura de Corte (Teórica)", 54, {"SEXTA": [1, 2]})
    add("7ª Fase", "BOVIC-A", "Bovinocultura de Corte (Turma A)",
        36, {"SEXTA": [6, 7, 8]})
    add("7ª Fase", "SAUP-T",
        "Saúde Pública Veterinária (Teórica)", 54, {"SEXTA": [6, 7]})
    add("7ª Fase", "SAUP-A",
        "Saúde Pública Veterinária (Turma A)", 36, {"SEXTA": [8]})
    add("7ª Fase", "SAUP-B",
        "Saúde Pública Veterinária (Turma B)", 36, {"SEXTA": [9]})

    # 8ª FASE
    add("8ª Fase", "CLINE-T", "Clínica Médica de Equinos (Teórica)",
        72, {"TERÇA": [0, 1, 2]})
    add("8ª Fase", "CLINE-A", "Clínica Médica de Equinos (Turma A)",
        36, {"SEGUNDA": [0, 1]})
    add("8ª Fase", "CLINE-B", "Clínica Médica de Equinos (Turma B)",
        36, {"QUARTA": [2, 3]})
    add("8ª Fase", "CLINE-C", "Clínica Médica de Equinos (Turma C)",
        36, {"QUARTA": [8, 9]})
    add("8ª Fase", "CLINE-D", "Clínica Médica de Equinos (Turma D)",
        36, {"SEXTA": [0, 1]})
    add("8ª Fase", "PATCL2-T",
        "Patologia e Clínica Cirúrgica (Teórica)", 72, {"QUARTA": [0, 1]})
    add("8ª Fase", "PATCL2-A", "Patologia e Clínica Cirúrgica (Turma A)",
        36, {"SEGUNDA": [0, 1, 2, 3]})
    add("8ª Fase", "PATCL2-B", "Patologia e Clínica Cirúrgica (Turma B)",
        36, {"TERÇA": [6, 7, 8]})
    add("8ª Fase", "PATCL2-C", "Patologia e Clínica Cirúrgica (Turma C)",
        36, {"QUARTA": [0, 1, 2, 3]})
    add("8ª Fase", "PATCL2-D", "Patologia e Clínica Cirúrgica (Turma D)",
        36, {"SEXTA": [0, 1, 2, 3]})
    add("8ª Fase", "BOVIL-8", "Bovinocultura de Leite",
        54, {"SEGUNDA": [6, 7, 8]})
    add("8ª Fase", "SANSU-T", "Sanidade Suína (Teórica)",
        54, {"TERÇA": [6, 7, 8]})
    add("8ª Fase", "SANSU-A", "Sanidade Suína (Turma A)", 36, {"QUARTA": [6]})
    add("8ª Fase", "SANSU-B", "Sanidade Suína (Turma B)", 36, {"QUARTA": [6]})
    add("8ª Fase", "SANSU-C", "Sanidade Suína (Turma C)", 36, {"QUARTA": [8]})
    add("8ª Fase", "INSPE-T", "Inspeção e Tech. Prod. Origem Anim. I",
        72, {"SEGUNDA": [9, 10]})
    add("8ª Fase", "INSPE-A", "Inspeção e Tech. Origem Anim. I (Turma A)",
        36, {"TERÇA": [9, 10]})
    add("8ª Fase", "INSPE-B", "Inspeção e Tech. Origem Anim. I (Turma B)",
        36, {"TERÇA": [11, 12]})
    add("8ª Fase", "AVIC-T", "Avicultura (Teórica)", 54, {"QUARTA": [6, 7]})
    add("8ª Fase", "AVIC-A", "Avicultura (Turma A)", 36, {"QUARTA": [8]})
    add("8ª Fase", "AVIC-B", "Avicultura (Turma B)", 36, {"QUARTA": [8]})
    add("8ª Fase", "AVIC-C", "Avicultura (Turma C)", 36, {"QUARTA": [9]})
    add("8ª Fase", "OVINO-T", "Ovinocultura (Teórica)", 54, {"SEXTA": [6]})
    add("8ª Fase", "OVINO-A", "Ovinocultura (Turma A)", 36, {"SEXTA": [8]})
    add("8ª Fase", "OVINO-B", "Ovinocultura (Turma B)", 36, {"SEXTA": [8]})

    # 9ª FASE
    add("9ª Fase", "OBSTE-T", "Obstetrícia Veterinária (Teórica)",
        54, {"SEGUNDA": [10, 11]})
    add("9ª Fase", "OBSTE-A", "Obstetrícia Veterinária (Turma A)",
        36, {"SEGUNDA": [0, 1]})
    add("9ª Fase", "OBSTE-B", "Obstetrícia Veterinária (Turma B)",
        36, {"SEGUNDA": [2, 3]})
    add("9ª Fase", "OBSTE-C", "Obstetrícia Veterinária (Turma C)",
        36, {"SEGUNDA": [6, 7]})
    add("9ª Fase", "OBSTE-D", "Obstetrícia Veterinária (Turma D)",
        36, {"SEGUNDA": [8, 9]})
    add("9ª Fase", "FRIA272-T", "Fisiopatologia da Reprodução II (Teórica)",
        72, {"QUINTA": [11, 12]})
    add("9ª Fase", "FRIA272-A", "Fisiopatologia da Reprodução II (Turma A)",
            72, {"SEXTA": [0, 1]})
    add("9ª Fase", "FRIA272-B", "Fisiopatologia da Reprodução II (Turma B)",
            72, {"SEXTA": [2, 3]})  
    add("9ª Fase", "INSP2-T",
        "Inspeção e Tech. Prod. Origem Anim. II", 72, {"QUARTA": [0, 1]})
    add("9ª Fase", "INSP2-A", "Inspeção e Tech. Origem Anim. II (Turma A)",
        36, {"QUARTA": [2, 3]})
    add("9ª Fase", "INSP2-B", "Inspeção e Tech. Origem Anim. II (Turma B)",
        36, {"QUARTA": [6, 7]})
    add("9ª Fase", "INSP2-C", "Inspeção e Tech. Origem Anim. II (Turma C)",
        36, {"QUARTA": [8, 9]})
    add("9ª Fase", "TOXI-9", "Toxicologia e Plantas Tóxicas",
        54, {"TERÇA": [8, 9]})
    add("9ª Fase", "DAVES-T",
        "Doenças das Aves (Teórica)", 54, {"QUARTA": [8, 9]})
    add("9ª Fase", "DAVES-A", "Doenças das Aves (Turma A)",
        36, {"SEXTA": [0, 1]})
    add("9ª Fase", "DAVES-B", "Doenças das Aves (Turma B)",
        36, {"SEXTA": [2, 3]})
    add("9ª Fase", "DAVES-C", "Doenças das Aves (Turma C)",
        36, {"QUARTA": [6, 7]})

    # ELETIVAS
    add("Eletivas", "LACTI-EL", "Tecnologia de Lacticínios",
        36, {"SEGUNDA": [2, 3]})
    add("Eletivas", "CITO-EL", "Citologia Diagnóstica", 36, {"QUARTA": [2, 3]})
    add("Eletivas", "DERMA-EL",
        "Dermatologia Veterinária", 36, {"SEXTA": [2, 3]})
    add("Eletivas", "FISIA-EL", "Fisiatra Veterinária",
        36, {"SEGUNDA": [6, 7]})
    add("Eletivas", "GEREN-EL",
        "Gerenciamento e Projetos Agropecuários", 36, {"QUARTA": [6, 7]})
    add("Eletivas", "MICRO-PESQ",
        "Microbiologia dos Pescados", 36, {"QUINTA": [6, 7]})
    add("Eletivas", "EQUIN-EL", "Equinocultura", 36, {"QUINTA": [6, 7]})
    add("Eletivas", "INSEM-EL",
        "Inseminação Artificial", 36, {"QUINTA": [6, 7]})
    add("Eletivas", "BIOMOL-EL", "Biologia Molecular", 36, {"SEGUNDA": [8, 9]})
    add("Eletivas", "CARDIO-EL",
        "Cardiologia de Cães e Gatos", 36, {"TERÇA": [8, 9]})
    add("Eletivas", "MEDSEL-EL",
        "Medicina de Animais Selvagens", 36, {"QUARTA": [8, 9]})
    add("Eletivas", "COMPBEM-EL",
        "Comportamento e Bem-Estar Animal II", 36, {"TERÇA": [10, 11]})
    add("Eletivas", "ANALAL-EL", "Análise de Alimentos",
        54, {"SEGUNDA": [11, 12, 13, 14]})
    add("Eletivas", "LIBRAS-EL", "Libras", 36, {"SEGUNDA": [6, 7]})
    add("Eletivas", "PECON-EL", "Animais Peçonhentos", 36, {"SEGUNDA": [8, 9]})

    link_theory_to_practicals(catalog)
    catalog = apply_official_data(catalog)
    return catalog


# Exceções em que o código da teórica não segue o padrão "<GRUPO>-T"/"<GRUPO>-TEO"
# (ex.: "GENET" é a teórica de "GENE-A"/"GENE-B").
GROUP_ALIASES = {
    "GENET": "GENE",
}


def infer_group_and_kind(code: str):
    """Deduz o 'grupo' (a disciplina em si, sem sufixo de turma/teórica) e o
    'tipo' (teorica / pratica / unica) a partir do código da matéria."""
    if code in GROUP_ALIASES:
        return GROUP_ALIASES[code], "teorica"
    if code.endswith("-TEO"):
        return code[:-4], "teorica"
    if code.endswith("-T"):
        return code[:-2], "teorica"
    if len(code) >= 2 and code[-2] == "-" and code[-1] in "ABCDE":
        return code[:-2], "pratica"
    return code, "unica"


def link_theory_to_practicals(catalog: List[Course]) -> None:
    """Atribui group/kind a cada disciplina do catálogo e vincula cada turma
    prática à sua teórica correspondente (mesmo grupo). Assim, ao escolher
    qualquer turma prática, a teórica (que tem sempre o mesmo horário,
    independente da turma) é carregada automaticamente junto."""
    for c in catalog:
        c.group, c.kind = infer_group_and_kind(c.code)

    theory_by_group = {c.group: c for c in catalog if c.kind == "teorica"}
    for c in catalog:
        if c.kind == "pratica":
            c.theory = theory_by_group.get(c.group)


def combined_schedule(course: Course) -> Dict[str, List[int]]:
    """Horário da turma prática somado ao horário da teórica vinculada (se houver)."""
    sched: Dict[str, List[int]] = {day: list(slots)
                                    for day, slots in course.schedule.items()}
    if course.theory:
        for day, slots in course.theory.schedule.items():
            sched[day] = sorted(set(sched.get(day, [])) | set(slots))
    return sched


# =========================================================================
# GRADE CURRICULAR VIGENTE — UDESC CAV (VET122 - Medicina Veterinária, 2012/2)
# Fonte: PDF oficial fornecido. Chave = código oficial da disciplina.
# Valor = (nome oficial, carga horária, créditos, tipo)
# =========================================================================

OFFICIAL: Dict[str, tuple] = {
    # 1ª Fase
    "ANA1-90": ("Anatomia I", 90, 5, "Obrigatória"),
    "BIOQB72": ("Bioquímica de Biomoléculas", 72, 4, "Obrigatória"),
    "DEONT36": ("Deontologia", 36, 2, "Obrigatória"),
    "EPIMC36": ("Epistemologia e Metodologia Científica", 36, 2, "Obrigatória"),
    "ESTCA54": ("Estatística", 54, 3, "Obrigatória"),
    "HISTG72": ("Histologia Geral", 72, 4, "Obrigatória"),
    # 2ª Fase
    "ANAII90": ("Anatomia II", 90, 5, "Obrigatória"),
    "BIOQM72": ("Bioquímica Metabólica", 72, 4, "Obrigatória"),
    "ECOLO36": ("Ecologia", 36, 2, "Obrigatória"),
    "EXPER36": ("Experimentação Animal", 36, 2, "Obrigatória"),
    "GENET72": ("Genética", 72, 4, "Obrigatória"),
    "HIST-90": ("Histologia e Embriologia", 90, 5, "Obrigatória"),
    # 3ª Fase
    "ANATT72": ("Anatomia Topográfica", 72, 4, "Obrigatória"),
    "FIS-I90": ("Fisiologia I", 90, 5, "Obrigatória"),
    "IMUNO54": ("Imunologia", 54, 3, "Obrigatória"),
    "MICR72": ("Microbiologia Geral", 72, 4, "Obrigatória"),
    "PARA172": ("Parasitologia I", 72, 4, "Obrigatória"),
    "SOAMV36": ("Sociologia Aplicada a Med Veterinária", 36, 2, "Obrigatória"),
    # 4ª Fase
    "ECOAD72": ("Economia e Administração", 72, 4, "Obrigatória"),
    "EPIDE36": ("Epidemiologia", 36, 2, "Obrigatória"),
    "FARMG72": ("Farmacologia Geral", 72, 4, "Obrigatória"),
    "FISI272": ("Fisiologia II", 72, 4, "Obrigatória"),
    "MELHO36": ("Melhoramento Animal", 36, 2, "Obrigatória"),
    "MICR-90": ("Microbiologia Especial", 90, 5, "Obrigatória"),
    "NUTRI54": ("Nutrição Animal", 54, 3, "Obrigatória"),
    "PARA272": ("Parasitologia II", 72, 4, "Obrigatória"),
    # 5ª Fase
    "ALIMA90": ("Alimentos e Alimentação Animal", 90, 5, "Obrigatória"),
    "COEXT36": ("Comunicação Extensão Rural", 36, 2, "Obrigatória"),
    "FARMD72": ("Farmacodinâmica", 72, 4, "Obrigatória"),
    "FORRA54": ("Forragicultura", 54, 3, "Obrigatória"),
    "PACLI72": ("Patologia Clínica Veterinária", 72, 4, "Obrigatória"),
    "PATG-90": ("Patologia Geral", 90, 5, "Obrigatória"),
    "SEMIO90": ("Semiologia", 90, 5, "Obrigatória"),
    # 6ª Fase
    "CLINR90": ("Clínica Médica de Ruminantes", 90, 5, "Obrigatória"),
    "DOENP72": ("Doenças Parasitárias", 72, 4, "Obrigatória"),
    "DOIC90": ("Doenças Infecto-Contagiosas", 90, 5, "Obrigatória"),
    "PATE-90": ("Patologia Especial", 90, 5, "Obrigatória"),
    "PISCI36": ("Piscicultura", 36, 2, "Obrigatória"),
    "SUINO54": ("Suinocultura", 54, 3, "Obrigatória"),
    "TERAP36": ("Terapêutica", 36, 2, "Obrigatória"),
    # 7ª Fase
    "ANES54": ("Anestesiologia", 54, 3, "Obrigatória"),
    "BOVCO54": ("Bovinocultura de Corte", 54, 3, "Obrigatória"),
    "CLCG90": ("Clínica Médica de Cães e Gatos I", 90, 5, "Obrigatória"),
    "DIAGI54": ("Diagnóstico por Imagem", 54, 3, "Obrigatória"),
    "FRIA190": ("Fisiopatologia da Reprodução I", 90, 5, "Obrigatória"),
    "SAUPU54": ("Saúde Pública Veterinária", 54, 3, "Obrigatória"),
    "TECIR90": ("Técnica Cirúrgica", 90, 5, "Obrigatória"),
    # 8ª Fase
    "AVICU54": ("Avicultura", 54, 3, "Obrigatória"),
    "BOVLE54": ("Bovinocultura de Leite", 54, 3, "Obrigatória"),
    "CLIEQ90": ("Clínica Médica de Equinos", 90, 5, "Obrigatória"),
    "INSP172": ("Inspeção e Tecn de Prod Origem Animal I", 72, 4, "Obrigatória"),
    "OVINO36": ("Ovinocultura", 36, 2, "Obrigatória"),
    "PACC108": ("Patologia e Clínica Cirúrgica", 108, 6, "Obrigatória"),
    "SANSU54": ("Sanidade Suína", 54, 3, "Obrigatória"),
    # 9ª Fase
    "ATCO396": ("Atividades Complementares", 396, 22, "Atividade"),
    "CLCG290": ("Clínica Médica de Cães e Gatos II", 90, 5, "Obrigatória"),
    "DAVES72": ("Doenças das Aves", 72, 4, "Obrigatória"),
    "FRIA272": ("Fisiopatologia da Reprodução II", 72, 4, "Obrigatória"),
    "INS-290": ("Inspeção e Tec Produtos Origem Animal II", 90, 5, "Obrigatória"),
    "OBSTE72": ("Obstetrícia", 72, 4, "Obrigatória"),
    "TOPTO36": ("Toxicologia e Plantas Tóxicas", 36, 2, "Obrigatória"),
    # 10ª Fase — Eletivas / Estágio
    "AALIM54": ("Análise de Alimentos para Animais", 54, 3, "Eletiva"),
    "AGVIR36": ("Agentes Virais de Caninos e Felinos", 36, 2, "Eletiva"),
    "ANIMP36": ("Animais Peçonhentos e Ven. Int. Med. Vet.", 36, 2, "Eletiva"),
    "AQUAC36": ("Aqüicultura", 36, 2, "Eletiva"),
    "BIOMO36": ("Biologia Molecular", 36, 2, "Eletiva"),
    "CARDI36": ("Cardiologia de Cães e Gatos", 36, 2, "Eletiva"),
    "CINOF36": ("Cinofilia e Felinotecnia", 36, 2, "Eletiva"),
    "CITOL36": ("Citologia Diagnóstica", 36, 2, "Eletiva"),
    "COMPO36": ("Comportamento e Bem Estar Animal", 36, 2, "Eletiva"),
    "CRIAA36": ("Criação de Aves de Interesse Zootécnico", 36, 2, "Eletiva"),
    "DERMA36": ("Dermatologia Veterinária", 36, 2, "Eletiva"),
    "EQUIN36": ("Eqüinocultura", 36, 2, "Eletiva"),
    "ESTC486": ("Estágio Curricular Supervisionado", 486, 27, "Estágio"),
    "FISIA36": ("Fisiatria Veterinária", 36, 2, "Eletiva"),
    "GENET36": ("Genética Médica Veterinária", 36, 2, "Eletiva"),
    "GERAV36": ("Gerenciamento e Produção Avícola", 36, 2, "Eletiva"),
    "GEREL54": ("Gerenciamento Prod. de Bovinos de Leite", 54, 3, "Eletiva"),
    "GERSU36": ("Gerenciamento e Produção de Suínos", 36, 2, "Eletiva"),
    "INSEM36": ("Inseminação Artificial e Andrologia", 36, 2, "Eletiva"),
    "LACTI36": ("Lacticínios", 36, 2, "Eletiva"),
    "MANFS72": ("Manejo de Fauna Silvestre", 72, 4, "Eletiva"),
    "MEDAS36": ("Medicina de Animais Silvestres", 36, 2, "Eletiva"),
    "MICRA36": ("Microbiologia dos Prod. de Origem Animal", 36, 2, "Eletiva"),
    "OFTAL36": ("Oftalmologia Veterinária", 36, 2, "Eletiva"),
    "TEMBR36": ("Tec. p/ a Produção de Embriões Bovinos", 36, 2, "Eletiva"),
}

# Mapeia o "group" interno (usado para juntar teórica+turmas) ao código oficial
# correspondente. Grupos que não aparecem aqui não têm equivalente na grade oficial.
GROUP_TO_OFFICIAL: Dict[str, str] = {
    "ANA1": "ANA1-90", "HISTG": "HISTG72", "BIOQB": "BIOQB72",
    "ESTCA": "ESTCA54", "SOAMV": "SOAMV36", "ECOLO-1": "ECOLO36",
    "ANA2": "ANAII90", "HIST2": "HIST-90", "GENE": "GENET72", "BIOQM": "BIOQM72",
    "IMUNO": "IMUNO54", "PARA1": "PARA172", "FISI1": "FIS-I90",
    "MICRO": "MICR72", "ANATT": "ANATT72",
    "NUTRI-4": "NUTRI54", "EPIDE-4": "EPIDE36", "ECONO-4": "ECOAD72",
    "MELHO-4": "MELHO36", "FISIO2": "FISI272", "FARM1": "FARMG72", "MICRE": "MICR-90",
    "FORRA-5": "FORRA54", "SEMIO": "SEMIO90", "FARMD": "FARMD72", "PATCL": "PACLI72",
    "PATG": "PATG-90", "ALIMA-5": "ALIMA90", "COEXT-5": "COEXT36",
    "SUINO": "SUINO54", "INFEC": "DOIC90", "PARAS2": "DOENP72", "CLINR": "CLINR90",
    "PATESP": "PATE-90", "PISCI-7": "PISCI36", "TERAP-7": "TERAP36",
    "ANEST": "ANES54", "TCIR": "TECIR90", "DIAG": "DIAGI54", "CLINC": "CLCG90",
    "FISREPO": "FRIA190", "BOVIC": "BOVCO54", "SAUP": "SAUPU54",
    "CLINE": "CLIEQ90", "PATCL2": "PACC108", "BOVIL-8": "BOVLE54", "SANSU": "SANSU54",
    "INSPE": "INSP172", "AVIC": "AVICU54", "OVINO": "OVINO36",
    "OBSTE": "OBSTE72", "FRIA272": "FRIA272", "INSP2": "INS-290",
    "TOXI-9": "TOPTO36", "DAVES": "DAVES72",
    # Eletivas já existentes no catálogo original, mapeadas para o código oficial
    "LACTI-EL": "LACTI36", "CITO-EL": "CITOL36", "DERMA-EL": "DERMA36",
    "FISIA-EL": "FISIA36", "EQUIN-EL": "EQUIN36", "INSEM-EL": "INSEM36",
    "BIOMOL-EL": "BIOMO36", "CARDIO-EL": "CARDI36", "MEDSEL-EL": "MEDAS36",
    "ANALAL-EL": "AALIM54", "PECON-EL": "ANIMP36",
    "COMPOR": "COMPO36",
}
GROUP_PHASE_OVERRIDE: Dict[str, str] = {
    "SOAMV": "3ª Fase",     # estava em "1ª Fase"
    "ECOLO-1": "2ª Fase",   # estava em "1ª Fase"
    "COMPOR": "Eletivas",   # estava obrigatória na "1ª Fase"; na grade é eletiva
}

GROUPS_TO_REMOVE = {"EXTEN", "GEREN-EL", "MICRO-PESQ", "COMPBEM-EL", "LIBRAS-EL"}

# Disciplinas presentes na Grade Curricular Vigente 
# "+ Personalizada" ou editando o código.
NEW_OFFICIAL_ITEMS = [
    ("DEONT36", "1ª Fase"), ("EPIMC36", "1ª Fase"),
    ("EXPER36", "2ª Fase"),
    ("PARA272", "4ª Fase"),
    ("CLCG290", "9ª Fase"),
    ("AGVIR36", "Eletivas"), ("AQUAC36", "Eletivas"), ("CINOF36", "Eletivas"),
    ("CRIAA36", "Eletivas"), ("GENET36", "Eletivas"), ("GERAV36", "Eletivas"),
    ("GEREL54", "Eletivas"), ("GERSU36", "Eletivas"), ("MANFS72", "Eletivas"),
    ("MICRA36", "Eletivas"), ("OFTAL36", "Eletivas"), ("TEMBR36", "Eletivas"),
    ("ATCO396", "9ª Fase"),   # Atividades Complementares é da 9ª fase na grade oficial
    ("ESTC486", "Eletivas"),  # Estágio aparece junto às eletivas (10ª fase) na grade
]


def apply_official_data(catalog: List[Course]) -> List[Course]:
    """Aplica à catalogação os códigos, CH e créditos da Grade Curricular
    Vigente: remove disciplinas fora da grade, corrige a fase de quem mudou,
    e acrescenta as disciplinas oficiais que ainda não existiam."""
    result: List[Course] = []
    for c in catalog:
        if c.group in GROUPS_TO_REMOVE:
            continue
        official_code = GROUP_TO_OFFICIAL.get(c.group)
        if official_code:
            _, ch, creditos, tipo = OFFICIAL[official_code]
            c.official_code = official_code
            c.ch = ch
            c.creditos = creditos
            c.tipo = tipo
            if c.group in GROUP_PHASE_OVERRIDE:
                c.phase = GROUP_PHASE_OVERRIDE[c.group]
        result.append(c)

    for official_code, item_phase in NEW_OFFICIAL_ITEMS:
        name, ch, creditos, tipo = OFFICIAL[official_code]
        new_c = Course(official_code, name, ch, {}, phase=item_phase)
        new_c.group = official_code
        new_c.kind = "unica"
        new_c.official_code = official_code
        new_c.ch = ch
        new_c.creditos = creditos
        new_c.tipo = tipo
        result.append(new_c)

    return result


def check_conflict(course_to_add: Course, registered_courses: List[Course]) -> Optional[str]:
    schedule_to_add = combined_schedule(course_to_add)
    for reg in registered_courses:
        for day, slots in schedule_to_add.items():
            if day in reg.schedule:
                overlap = set(slots).intersection(set(reg.schedule[day]))
                if overlap:
                    conflicting_slot = sorted(list(overlap))[0]
                    return f"Com '{reg.name}' na {day} no horário {get_slot_time_str(conflicting_slot)}."
    return None


# =========================================================================
# TOKENS DE DESIGN —, uma cor-assinatura por fase
# =========================================================================

PAGE_BG = "#25CC8CC1"
PANEL_BG = "#FEFFB0BA"
HEADER_GRADIENT = "linear-gradient(135deg, #1B1F3B 0%, #2E3566 100%)"
TIME_COL_GRADIENT = "linear-gradient(135deg, #EDEFF7 0%, #E3E6F3 100%)"
EMPTY_CELL_BG = "#B6F8DD"
GRID_LINE = "#000000"

# saturação/luminosidade para manter a paleta coesa mesmo com 10 cores.
PHASE_COLORS = {
    "1ª Fase":  ("#6836F3", "#9C7BFF"),  # violeta
    "2ª Fase":  ("#08C9E7", "#5FD3E3"),  # ciano
    "3ª Fase":  ("#086E4E", "#3FCB9C"),  # esmeralda
    "4ª Fase":  ("#3178C4", "#63ABF2"),  # azul
    "5ª Fase":  ("#E0A62F", "#F2C55E"),  # âmbar
    "6ª Fase":  ("#E0632F", "#F28A5E"),  # laranja
    "7ª Fase":  ("#D6396B", "#EE6D97"),  # magenta
    "8ª Fase":  ("#7B05FAD1", "#B06BF2"),  # roxo
    "9ª Fase":  ("#DB2A33", "#662D2D"),  # índigo
    "Eletivas": ("#BB3D4E", "#8C99A6"),  # grafite neutro
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
    query = st.text_input(
        "Buscar por código, nome ou carga horária").lower().strip()

    filtered_courses = [
        c for c in st.session_state.available_courses
        # Teóricas não aparecem como opção separada: elas são vinculadas
        # automaticamente à turma prática correspondente (ver .theory).
        if c.kind != "teorica"
        and (phase_choice == "Todas as Fases" or c.phase == phase_choice)
        and (query in c.display_code.lower() or query in c.name.lower() or query in str(c.display_ch))
    ]

    st.subheader(f"Todas Disciplinas ({len(filtered_courses)})")
    options = [str(c) for c in filtered_courses]
    selected_label = st.selectbox(
        "Catálogo", options, label_visibility="collapsed") if options else None

    selected_course = None
    if selected_label:
        idx = options.index(selected_label)
        selected_course = filtered_courses[idx]

        c1, c2 = PHASE_COLORS.get(
            selected_course.phase, ("#0A0B0C", "#0C0D0E"))
        st.markdown(
            f"<span style='background:{phase_gradient(selected_course.phase)};color:white;"
            f"padding:2px 10px;border-radius:12px;font-size:14px;font-weight:600'>{selected_course.phase}</span>",
            unsafe_allow_html=True,
        )

        creditos_line = f"  \n**Créditos:** {selected_course.creditos}" if selected_course.creditos is not None else ""
        details = (
            f"**Código:** {selected_course.display_code}  \n**Nome:** {selected_course.name}  \n"
            f"**Carga Horária:** {selected_course.display_ch}h{creditos_line}  \n**Horários:**\n"
        )
        if selected_course.schedule:
            for day, slots in selected_course.schedule.items():
                slot_str = ", ".join([get_slot_time_str(s) for s in slots])
                details += f"- {day}: {slot_str}\n"


        if selected_course.theory:
            t = selected_course.theory
            for day, slots in t.schedule.items():
                slot_str = ", ".join([get_slot_time_str(s) for s in slots])
                details += f"- {day}: {slot_str}\n"
        st.markdown(details)

    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        add_clicked = st.button(
            "➕ Adicionar Disciplina", use_container_width=True, disabled=selected_course is None)
    with btn_col2:
        custom_clicked = st.button("+ Personalizada", use_container_width=True)

    if add_clicked and selected_course:
        # Checagem por "grupo": impede ter duas turmas da mesma disciplina
        # ao mesmo tempo (ex.: Turma A e Turma B de Anatomia I juntas).
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
                        f"'{selected_course.name}' adicionada com sucesso!")
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
                        # Matéria personalizada é tratada como "única" (sem
                        # vínculo automático com teórica), usando o próprio
                        # código como grupo.
                        new_course.group = code
                        new_course.kind = "unica"
                        st.session_state.available_courses.append(new_course)
                        st.session_state["show_custom_form"] = False
                        st.success(
                            f"Matéria '{code}' criada e adicionada ao catálogo.")
                        st.rerun()

    # Agrupa por disciplina (group) para mostrar prática + teórica vinculada
    # como uma única linha, com um só botão de remover para o pacote todo.
    grouped_groups = []
    for c in st.session_state.registered_courses:
        if c.group not in grouped_groups:
            grouped_groups.append(c.group)

    st.subheader(f"Matérias Selecionadas ({len(grouped_groups)})")
    total_ch_geral = 0
    total_creditos_geral = 0
    for group in grouped_groups:
        group_courses = [
            c for c in st.session_state.registered_courses if c.group == group]
        practical = next(
            (c for c in group_courses if c.kind != "teorica"), group_courses[0])

        # CH/créditos oficiais já representam a disciplina inteira (teórica +
        # prática), então usamos os da própria representante do grupo — nunca
        # somamos com a teórica de novo, para não contar duas vezes.
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
            st.session_state.registered_courses = [
                c for c in st.session_state.registered_courses if c.group != group]
            st.rerun()

    if grouped_groups:
        st.markdown(
            f"**Total:** {total_ch_geral}h &nbsp;|&nbsp; {total_creditos_geral} créditos")


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
                    f"{course.display_code}<br><span style='font-weight:400;opacity:0.9'>{course.name[:14]}...</span></td>"
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
