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
    def __init__(self, code: str, name: str, total_ch: int, schedule: Dict[str, List[int]], 
                 phase: str = "", tipo: str = "Obrigatória", creditos: int = None):
        self.code = code
        self.name = name
        self.total_ch = total_ch  # Carga horária TOTAL (teórica + prática)
        self.schedule = schedule
        self.phase = phase
        self.tipo = tipo
        self.creditos = creditos
        self.group = code
        self.kind = "unica"
        self.theory: Optional["Course"] = None
        self.official_code: Optional[str] = None
        self.ch = total_ch  # Mantido para compatibilidade

    @property
    def display_code(self) -> str:
        return self.official_code or self.code

    @property
    def display_ch(self) -> int:
        return self.ch if self.ch is not None else self.total_ch

    def __str__(self):
        label = f"[{self.display_code}] {self.name} ({self.display_ch}h"
        if self.creditos is not None:
            label += f" | {self.creditos} créd."
        label += f" | {self.tipo})"
        return label

def infer_group_and_kind(code: str):
    """Infere grupo e tipo baseado no código da disciplina"""
    # Remove sufixo de turma se existir (-A, -B, -C, -D)
    if len(code) >= 2 and code[-2] == "-" and code[-1] in "ABCDE":
        return code[:-2], "pratica"
    
    # Remove sufixo -T se existir (teórica)
    if code.endswith("-T"):
        return code[:-2], "teorica"
    
    # Verifica se é uma disciplina com código composto (ex: MICR-90)
    if "-" in code and len(code.split("-")) == 2 and code.split("-")[1].isdigit():
        base_code = code.split("-")[0]
        return base_code, "unica"
    
    return code, "unica"

def link_theory_to_practicals(catalog: List[Course]) -> None:
    """Vincula disciplinas teóricas às suas respectivas práticas"""
    for c in catalog:
        c.group, c.kind = infer_group_and_kind(c.code)

    # Cria mapa de teóricas por grupo
    theory_by_group = {}
    for c in catalog:
        if c.kind == "teorica":
            # Tenta encontrar o código base sem o -T
            base_code = c.code[:-2] if c.code.endswith("-T") else c.code
            theory_by_group[base_code] = c

    # Vincula as práticas às teóricas
    for c in catalog:
        if c.kind == "pratica":
            # Tenta encontrar a teórica correspondente
            if c.group in theory_by_group:
                c.theory = theory_by_group[c.group]

def build_initial_catalog() -> List[Course]:
    """Catálogo completo baseado na Grade Curricular VET122 - 2012/2"""
    catalog: List[Course] = []

    def add(phase, code, name, total_ch, schedule, creditos=None, tipo="Obrigatória"):
        """Adiciona uma disciplina com sua carga horária TOTAL"""
        catalog.append(Course(code, name, total_ch, schedule, phase=phase, 
                            tipo=tipo, creditos=creditos))

    # =========================================================================
    # 1ª FASE
    # =========================================================================
    add("1ª Fase", "ANA1-90", "ANATOMIA I", 90, {
        "SEGUNDA": [1, 2],  # Teórica
        "TERÇA": [1, 2],    # Teórica
        "QUARTA": [3, 4],   # Prática A
        "TERÇA": [9]        # Prática A
    }, creditos=5)

    add("1ª Fase", "BIOQB", "BIOQUÍMICA DE BIOMOLÉCULAS", 72, {
        "TERÇA": [7, 8],    # Teórica
        "QUARTA": [7],      # Teórica
        "QUARTA": [7],      # Prática A
        "SEXTA": [8],       # Prática B
        "QUARTA": [11]      # Prática C
    }, creditos=4)

    add("1ª Fase", "DEONT", "DEONTOLOGIA", 36, {
        "QUARTA": [2]
    }, creditos=2)

    add("1ª Fase", "EPIMC", "EPISTEMOLOGIA E METODOLOGIA CIENTÍFICA", 36, {
        "QUARTA": [9, 10]
    }, creditos=2)

    add("1ª Fase", "ESTCA", "ESTATÍSTICA", 54, {
        "SEGUNDA": [7, 8, 9]
    }, creditos=3)

    add("1ª Fase", "HISTG", "HISTOLOGIA GERAL", 72, {
        "TERÇA": [3, 4],    # Teórica
        "QUINTA": [1, 2],   # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUARTA": [3, 4],   # Prática B
        "QUINTA": [7, 8],   # Prática C
        "QUARTA": [9, 10]   # Prática D
    }, creditos=4)

    # =========================================================================
    # 2ª FASE
    # =========================================================================
    add("2ª Fase", "ANAII", "ANATOMIA II", 90, {
        "SEGUNDA": [1, 2],  # Teórica
        "QUARTA": [3, 4],   # Teórica
        "QUINTA": [7, 8],   # Prática A
        "SEXTA": [9],       # Prática A
        "QUARTA": [9, 10],  # Prática B
        "SEXTA": [10],      # Prática B
        "SEGUNDA": [11, 12],# Prática C
        "QUARTA": [12],     # Prática C
        "QUARTA": [1, 2],   # Prática D
        "QUARTA": [11]      # Prática D
    }, creditos=5)

    add("2ª Fase", "BIOQM", "BIOQUÍMICA METABÓLICA", 72, {
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [9, 10]  # Prática B
    }, creditos=4)

    add("2ª Fase", "ECOLO", "ECOLOGIA", 36, {
        "QUINTA": [3, 4]
    }, creditos=2)

    add("2ª Fase", "EXPER", "EXPERIMENTAÇÃO ANIMAL", 36, {}, creditos=2)

    add("2ª Fase", "GENET", "GENÉTICA", 72, {
        "SEXTA": [2],       # Teórica
        "SEXTA": [3, 4],    # Prática A
        "SEXTA": [8]        # Prática B
    }, creditos=4)

    add("2ª Fase", "HIST-90", "HISTOLOGIA E EMBRIOLOGIA", 90, {
        "SEGUNDA": [3, 4],  # Teórica
        "SEXTA": [1],       # Teórica
        "TERÇA": [7, 8],    # Prática A
        "TERÇA": [9, 10],   # Prática B
        "QUARTA": [7, 8],   # Prática C
        "SEXTA": [7, 8]     # Prática D
    }, creditos=5)

    # =========================================================================
    # 3ª FASE
    # =========================================================================
    add("3ª Fase", "ANATT", "ANATOMIA TOPOGRÁFICA", 72, {
        # Horários a serem preenchidos
    }, creditos=4)

    add("3ª Fase", "FIS-I", "FISIOLOGIA I", 90, {
        "SEGUNDA": [6],     # Teórica
        "SEXTA": [7, 8],    # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUINTA": [9, 10],  # Prática B
        "QUINTA": [3, 4],   # Prática C
        "QUINTA": [9, 10]   # Prática D (mesmo horário da B - verificar)
    }, creditos=5)

    add("3ª Fase", "IMUNO", "IMUNOLOGIA", 54, {
        "SEGUNDA": [1, 2],  # Teórica
        "SEGUNDA": [11],    # Prática A
        "SEGUNDA": [12]     # Prática B
    }, creditos=3)

    add("3ª Fase", "MICR", "MICROBIOLOGIA GERAL", 72, {
        "SEGUNDA": [3, 4],  # Teórica
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [9, 10], # Prática B
        "TERÇA": [7, 8],    # Prática C
        "TERÇA": [9, 10]    # Prática D
    }, creditos=4)

    add("3ª Fase", "PARA1", "PARASITOLOGIA I", 72, {
        "TERÇA": [3, 4],    # Teórica
        "TERÇA": [1, 2],    # Prática A
        "TERÇA": [11, 12],  # Prática B
        "QUINTA": [3, 4],   # Prática C
        "QUINTA": [7, 8]    # Prática D
    }, creditos=4)

    add("3ª Fase", "SOAMV", "SOCIOLOGIA APLICADA A MED VETERINÁRIA", 36, {
        "SEGUNDA": [3, 4]
    }, creditos=2)

    # =========================================================================
    # 4ª FASE
    # =========================================================================
    add("4ª Fase", "ECOAD", "ECONOMIA E ADMINISTRAÇÃO", 72, {
        "SEXTA": [1, 2],
        "QUARTA": [7, 8]
    }, creditos=4)

    add("4ª Fase", "EPIDE", "EPIDEMIOLOGIA", 36, {
        "QUINTA": [3, 4]
    }, creditos=2)

    add("4ª Fase", "FARMG", "FARMACOLOGIA GERAL", 72, {
        "SEXTA": [1, 2, 3, 4, 7, 8],  # Teórica (verificar horários)
        "QUINTA": [9, 10],             # Prática A
        "SEXTA": [1, 2],               # Prática B
        "SEXTA": [3, 4],               # Prática C
        "TERÇA": [3, 4],               # Prática D
        "TERÇA": [9],                  # Prática E
        "QUARTA": [3, 4]               # Prática F
    }, creditos=4)

    add("4ª Fase", "FISI2", "FISIOLOGIA II", 72, {
        "TERÇA": [1, 2],    # Teórica
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [9, 10], # Prática B
        "TERÇA": [3, 4],    # Prática C
        "QUARTA": [3, 4]    # Prática D
    }, creditos=4)

    add("4ª Fase", "MELHO", "MELHORAMENTO ANIMAL", 36, {
        "QUINTA": [11, 12]
    }, creditos=2)

    add("4ª Fase", "MICR-90", "MICROBIOLOGIA ESPECIAL", 90, {
        "QUARTA": [3, 4],   # Prática A
        "QUARTA": [7, 8],   # Prática B
        "QUARTA": [9]       # Prática C
    }, creditos=5)

    add("4ª Fase", "NUTRI", "NUTRIÇÃO ANIMAL", 54, {
        "QUARTA": [7, 8, 9, 10, 11, 12],
        "SEGUNDA": [1, 2],
        "QUARTA": [1, 2]
    }, creditos=3)

    add("4ª Fase", "PARA2", "PARASITOLOGIA II", 72, {
        "QUINTA": [1, 2],   # Teórica
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [9, 10], # Prática B
        "TERÇA": [3, 4],    # Prática C
        "QUARTA": [1, 2],   # Prática D
        "SEGUNDA": [3, 4],  # Prática E
        "QUARTA": [3, 4],   # Prática F
        "QUARTA": [9],      # Prática G
        "QUINTA": [1, 2]    # Prática H
    }, creditos=4)

    # =========================================================================
    # 5ª FASE
    # =========================================================================
    add("5ª Fase", "ALIMA", "ALIMENTOS E ALIMENTAÇÃO ANIMAL", 90, {}, creditos=5)
    add("5ª Fase", "COEXT", "COMUNICAÇÃO EXTENSÃO RURAL", 36, {}, creditos=2)
    add("5ª Fase", "FARMD", "FARMACODINÂMICA", 72, {}, creditos=4)
    add("5ª Fase", "FORRA", "FORRAGICULTURA", 54, {}, creditos=3)
    add("5ª Fase", "PACLI", "PATOLOGIA CLÍNICA VETERINÁRIA", 72, {}, creditos=4)
    add("5ª Fase", "PATG-90", "PATOLOGIA GERAL", 90, {}, creditos=5)
    add("5ª Fase", "SEMIO", "SEMIOLOGIA", 90, {}, creditos=5)

    # =========================================================================
    # 6ª FASE
    # =========================================================================
    add("6ª Fase", "CLINR", "CLÍNICA MÉDICA DE RUMINANTES", 90, {
        "QUINTA": [1, 2, 3, 4],  # Teórica
        "QUARTA": [7, 8],        # Prática A
        "SEXTA": [9, 10],        # Prática B
        "SEXTA": [9],            # Prática C
        "QUINTA": [7, 8]         # Prática D
    }, creditos=5)

    add("6ª Fase", "DOENP", "DOENÇAS PARASITÁRIAS", 72, {
        "QUARTA": [1, 2, 3, 4],  # Teórica
        "QUARTA": [7, 8],        # Prática A
        "SEXTA": [9, 10],        # Prática B
        "SEGUNDA": [11],         # Prática C
        "SÁBADO": [12],          # Prática C
        "QUINTA": [7, 8]         # Prática D
    }, creditos=4)

    add("6ª Fase", "DOIC", "DOENÇAS INFECTO-CONTAGIOSAS", 90, {
        "TERÇA": [1, 2, 3, 4],   # Teórica
        "QUARTA": [5],           # Prática A
        "QUINTA": [10],          # Prática A
        "QUINTA": [7, 8],        # Prática B
        "SEXTA": [9]             # Prática C
    }, creditos=5)

    add("6ª Fase", "PATE-90", "PATOLOGIA ESPECIAL", 90, {
        "SEXTA": [1, 2, 3, 4],   # Teórica
        "SEXTA": [9, 10],        # Prática A
        "QUINTA": [7, 8],        # Prática B
        "SÁBADO": [10, 11]       # Prática C
    }, creditos=5)

    add("6ª Fase", "PISC", "PISCICULTURA", 36, {
        "QUARTA": [3, 4, 5]
    }, creditos=2)

    add("6ª Fase", "SUINO", "SUINOCULTURA", 54, {
        "SEGUNDA": [1, 2],  # Teórica
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [8],     # Prática B
        "SEGUNDA": [9]      # Prática C
    }, creditos=3)

    add("6ª Fase", "TERAP", "TERAPÊUTICA", 36, {
        "SEGUNDA": [3, 4]
    }, creditos=2)

    # =========================================================================
    # 7ª FASE
    # =========================================================================
    add("7ª Fase", "ANES", "ANESTESIOLOGIA", 54, {
        "TERÇA": [1, 2],    # Teórica
        "QUARTA": [7],      # Prática A
        "QUARTA": [8],      # Prática B
        "QUARTA": [7],      # Prática C
        "QUARTA": [9]       # Prática D
    }, creditos=3)

    add("7ª Fase", "BOVCO", "BOVINOCULTURA DE CORTE", 54, {
        "SÁBADO": [2, 3, 4]
    }, creditos=3)

    add("7ª Fase", "CLCG", "CLÍNICA MÉDICA DE CÃES E GATOS I", 90, {
        "SEXTA": [1, 2],    # Teórica
        "QUINTA": [7, 8],   # Teórica
        "TERÇA": [7],       # Prática A
        "QUINTA": [9, 10],  # Prática C
        "QUINTA": [7, 8]    # Prática D
    }, creditos=5)

    add("7ª Fase", "DIAGI", "DIAGNÓSTICO POR IMAGEM", 54, {
        "QUINTA": [5, 10],  # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUINTA": [3, 4],   # Prática B
        "QUINTA": [9, 10]   # Prática D
    }, creditos=3)

    add("7ª Fase", "FRIA1", "FISIOPATOLOGIA DA REPRODUÇÃO I", 90, {
        "TERÇA": [3, 4],    # Teórica
        "QUARTA": [7],      # Prática A
        "QUARTA": [11],     # Prática B
        "QUINTA": [7, 8],   # Prática C
        "QUINTA": [9, 10]   # Prática D
    }, creditos=5)

    add("7ª Fase", "SAUPU", "SAÚDE PÚBLICA VETERINÁRIA", 54, {
        "SÁBADO": [7, 8],   # Teórica
        "SÁBADO": [9],      # Prática A
        "SÁBADO": [10]      # Prática B
    }, creditos=3)

    add("7ª Fase", "TECIR", "TÉCNICA CIRÚRGICA", 90, {
        "TERÇA": [9, 10],   # Teórica
        "QUARTA": [1, 2],   # Prática A
        "QUARTA": [3, 4],   # Prática B
        "QUINTA": [1, 2],   # Prática C
        "QUINTA": [3, 4]    # Prática D
    }, creditos=5)

    # =========================================================================
    # 8ª FASE
    # =========================================================================
    add("8ª Fase", "AVICU", "AVICULTURA", 54, {
        "QUINTA": [7, 8],   # Teórica
        "QUINTA": [9],      # Prática A
        "QUINTA": [10],     # Prática B
        "QUINTA": [11]      # Prática C
    }, creditos=3)

    add("8ª Fase", "BOVLE", "BOVINOCULTURA DE LEITE", 54, {
        "SEGUNDA": [7, 8, 9, 10]
    }, creditos=3)

    add("8ª Fase", "CLIEQ", "CLÍNICA MÉDICA DE EQUÍNOS", 90, {
        "TERÇA": [1, 2, 3, 4],  # Teórica
        "SEGUNDA": [1, 2],      # Prática A
        "SEGUNDA": [3, 4],      # Prática B
        "QUINTA": [9, 10],      # Prática C
        "SEXTA": [1, 2]         # Prática D
    }, creditos=5)

    add("8ª Fase", "INSP1", "INSPEÇÃO E TECN DE PROD ORIGEM ANIMAL I", 72, {
        "SEGUNDA": [11, 12],    # Teórica
        "TERÇA": [11],          # Prática A
        "TERÇA": [12]           # Prática B
    }, creditos=4)

    add("8ª Fase", "OVINO", "OVINOCULTURA", 36, {
        "SÁBADO": [7, 8, 9],    # Teórica
        "SÁBADO": [9],          # Prática A
        "SÁBADO": [10]          # Prática B
    }, creditos=2)

    add("8ª Fase", "PACC", "PATOLOGIA E CLÍNICA CIRÚRGICA", 108, {
        "QUINTA": [3, 4, 11],   # Teórica
        "SEXTA": [3, 4, 9, 10], # Teórica
        "SÁBADO": [3, 4],       # Teórica
        "SEGUNDA": [2],         # Prática A
        "QUARTA": [3, 4, 11],   # Prática B
        "QUINTA": [1, 2],       # Prática C
        "SEXTA": [1, 2]         # Prática D
    }, creditos=6)

    add("8ª Fase", "SANSU", "SANIDADE SUÍNA", 54, {
        "TERÇA": [7, 8],    # Teórica
        "TERÇA": [9],       # Prática A
        "QUARTA": [7, 8],   # Prática B
        "QUARTA": [8]       # Prática C
    }, creditos=3)

    # =========================================================================
    # 9ª FASE
    # =========================================================================
    add("9ª Fase", "CLCG2", "CLÍNICA MÉDICA DE CÃES E GATOS II", 90, {
        "TERÇA": [1, 2],    # Teórica
        "SEGUNDA": [1, 2],  # Prática A
        "SEGUNDA": [3, 4],  # Prática B
        "SEGUNDA": [9, 10], # Prática C
        "QUARTA": [3, 4]    # Prática D
    }, creditos=5)

    add("9ª Fase", "DAVES", "DOENÇAS DAS AVES", 72, {
        "SÁBADO": [7, 8, 9, 10],  # Teórica
        "QUINTA": [7, 8],         # Prática A
        "SEXTA": [1, 2],          # Prática B
        "SEXTA": [3, 4]           # Prática C
    }, creditos=4)

    add("9ª Fase", "FRIA2", "FISIOPATOLOGIA DA REPRODUÇÃO II", 72, {
        "SÁBADO": [12],     # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUINTA": [3, 4],   # Prática B
        "SEXTA": [1, 2],    # Prática C
        "SEXTA": [3, 4]     # Prática D
    }, creditos=4)

    add("9ª Fase", "INS-2", "INSPEÇÃO E TEC PRODUTOS ORIGEM ANIMAL II", 90, {
        "QUARTA": [1, 2],   # Teórica
        "QUARTA": [3, 4],   # Prática A
        "QUARTA": [7, 8],   # Prática B
        "QUARTA": [9, 10],  # Prática C
        "QUARTA": [12]      # Prática D
    }, creditos=5)

    add("9ª Fase", "OBSTE", "OBSTETRÍCIA", 72, {
        "TERÇA": [7, 8],    # Teórica
        "SEGUNDA": [1, 2],  # Prática A
        "SEGUNDA": [3, 4],  # Prática B
        "SEGUNDA": [7, 8],  # Prática C
        "SEGUNDA": [9, 10]  # Prática D
    }, creditos=4)

    add("9ª Fase", "TOPTO", "TOXICOLOGIA E PLANTAS TÓXICAS", 36, {
        "TERÇA": [9, 10]
    }, creditos=2)

    # ATIVIDADES COMPLEMENTARES (não tem horário)
    add("9ª Fase", "ATCO", "ATIVIDADES COMPLEMENTARES", 396, {}, 
        creditos=22, tipo="Atividade")

    # =========================================================================
    # 10ª FASE - ELETIVAS
    # =========================================================================
    add("Eletivas", "AALIM", "ANÁLISE DE ALIMENTOS PARA ANIMAIS", 54, {
        # Horários a definir
    }, creditos=3, tipo="Eletiva")

    add("Eletivas", "AGVIR", "AGENTES VIRAIS DE CANINOS E FELINOS", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "ANIMP", "ANIM. PEÇONHENTOS E VEN. INT. MED. VET.", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "AQUAC", "AQUACULTURA", 36, {"SEGUNDA": [11, 12]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "BIOMO", "BIOLOGIA MOLECULAR", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "CARDI", "CARDIOLOGIA DE CÃES E GATOS", 36, {"SEXTA": [7, 8]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "CINOF", "CINOFILIA E FELINOTECNIA", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "CITOL", "CITOLOGIA DIAGNÓSTICA", 36, {"QUINTA": [4], "SEXTA": [5]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "COMPO", "COMPORTAMENTO E BEM ESTAR ANIMAL", 36, {"QUARTA": [7, 8]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "CRIA", "CRIAÇÃO DE AVES DE INTERESSE ZOOTÉCNICO", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "DERMA", "DERMATOLOGIA VETERINÁRIA", 36, {"QUINTA": [3], "SEXTA": [4]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "EQUIN", "EQUINOCULTURA", 36, {"SEXTA": [7, 8]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "ESTC", "ESTÁGIO CURRICULAR SUPERVISIONADO", 486, {"SEGUNDA": [15]}, 
        creditos=27, tipo="Estágio(Registro)")
    add("Eletivas", "FISIA", "FISIATRIA VETERINÁRIA", 36, {"TERÇA": [7, 8]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "GENET", "GENÉTICA MÉDICA VETERINÁRIA", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "GERAV", "GERENCIAMENTO E PRODUÇÃO AVÍCOLA", 36, {"QUINTA": [7, 8]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "GEREL", "GERENCIAMENTO PROD. DE BOVINOS DE LEITE", 54, {}, 
        creditos=3, tipo="Eletiva")
    add("Eletivas", "GERSU", "GERENCIAMENTO E PRODUÇÃO DE SUÍNOS", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "INSEM", "INSEMINAÇÃO ARTIFICIAL E ANDROLOGIA", 36, {}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "LACTI", "LACTICÍNIOS", 36, {"TERÇA": [3, 4]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "MANFS", "MANEJO DE FAUNA SILVESTRE", 72, {}, 
        creditos=4, tipo="Eletiva")
    add("Eletivas", "MEDAS", "MEDICINA DE ANIMAIS SILVESTRES", 36, {"SEGUNDA": [9, 10]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "MICRA", "MICROBIOLOGIA DOS PROD. DE ORIGEM ANIMAL", 36, {"SEXTA": [7, 8]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "OFTAL", "OFTALMOLOGIA VETERINARIA", 36, {"QUARTA": [3, 4]}, 
        creditos=2, tipo="Eletiva")
    add("Eletivas", "TEMBR", "TEC. P/A PRODUÇÃO DE EMBRIÕES BOVINOS", 36, {}, 
        creditos=2, tipo="Eletiva")

    link_theory_to_practicals(catalog)
    return catalog

def get_combined_schedule(course: Course) -> Dict[str, List[int]]:
    """Retorna um dicionário único com todos os horários (teórica + prática) mesclados e sem duplicatas."""
    combined: Dict[str, List[int]] = {}
    
    # Adiciona os horários da própria disciplina
    for day, slots in course.schedule.items():
        combined[day] = list(slots)
    
    # Adiciona os horários da teórica, se existir
    if course.theory:
        for day, slots in course.theory.schedule.items():
            if day in combined:
                combined[day] = sorted(set(combined[day] + slots))
            else:
                combined[day] = list(slots)
                
    return combined

def check_conflict(course_to_add: Course, registered_courses: List[Course]) -> Optional[str]:
    """Verifica conflitos de horário entre uma disciplina e as já registradas"""
    schedule_to_add = get_combined_schedule(course_to_add)
    for reg in registered_courses:
        reg_schedule = get_combined_schedule(reg)
        for day, slots in schedule_to_add.items():
            if day in reg_schedule:
                overlap = set(slots).intersection(set(reg_schedule[day]))
                if overlap:
                    conflicting_slot = sorted(list(overlap))[0]
                    reg_type = "Prática" if reg.kind == "pratica" else "Teórica"
                    return f"Conflito com '{reg.name}' ({reg_type}) na {day} às {get_slot_time_str(conflicting_slot)}."
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
    page_title="Simulador de Matrícula CAV - UDESC",
    layout="wide"
)

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
st.caption("Baseado na Grade Curricular VET122 - 2012/2")

col_left, col_right = st.columns([1, 2], gap="large")

# ---------------- Painel esquerdo ----------------
with col_left:
    st.subheader("Buscar disciplinas")

    phase_choice = st.selectbox("Fase", ["Todas as Fases"] + PHASES)
    
    col_filtro1, col_filtro2 = st.columns(2)
    with col_filtro1:
        tipo_filter = st.selectbox("Tipo", ["Todos", "Obrigatória", "Eletiva", "Atividade", "Estágio(Registro)"])
    with col_filtro2:
        show_only_available = st.checkbox("Apenas disponíveis", value=False)
    
    query = st.text_input("Buscar por código ou nome", placeholder="Ex: ANATOMIA ou ANA1").lower().strip()

    filtered_courses = [
        c for c in st.session_state.available_courses
        if c.kind != "teorica"
        and (phase_choice == "Todas as Fases" or c.phase == phase_choice)
        and (tipo_filter == "Todos" or c.tipo == tipo_filter)
        and (query in c.display_code.lower() or query in c.name.lower())
    ]

    if show_only_available:
        available = []
        for c in filtered_courses:
            # Verifica se já não está registrada
            already_added = any(reg.group == c.group for reg in st.session_state.registered_courses)
            if not already_added and not check_conflict(c, st.session_state.registered_courses):
                available.append(c)
        filtered_courses = available

    st.subheader(f"Disciplinas ({len(filtered_courses)})")
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
        
        combined_schedule_data = get_combined_schedule(selected_course)
        
        details = (
            f"**Código:** {selected_course.display_code}  \n**Nome:** {selected_course.name}  \n"
            f"**Carga Horária:** {selected_course.display_ch}h{creditos_line}  \n"
            f"**Tipo:** {selected_course.tipo}  \n**Horários (Teórica + Prática):**\n"
        )
        
        if combined_schedule_data:
            for day in DAYS:
                if day in combined_schedule_data:
                    slot_str = ", ".join([get_slot_time_str(s) for s in sorted(combined_schedule_data[day])])
                    details += f"- {day}: {slot_str}\n"
        else:
            details += "- Nenhum horário cadastrado.\n"

        st.markdown(details)

    # Botão de adicionar com verificação de pré-requisitos
    if st.button("➕ Adicionar Disciplina", use_container_width=True, disabled=selected_course is None) and selected_course:
        already_added = any(c.group == selected_course.group for c in st.session_state.registered_courses)
        if already_added:
            st.warning(f"Você já tem uma turma de '{selected_course.name}' adicionada.")
        else:
            conflict_msg = check_conflict(selected_course, st.session_state.registered_courses)
            if conflict_msg:
                st.warning(f"{conflict_msg}")
            else:
                st.session_state.registered_courses.append(selected_course)
                if selected_course.theory:
                    st.session_state.registered_courses.append(selected_course.theory)
                st.success(f"'{selected_course.name}' adicionada com sucesso!")
                st.rerun()

    # Lista de disciplinas selecionadas
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
        
        # Botão para limpar tudo
        if st.button("🗑️ Limpar todas", use_container_width=True):
            st.session_state.registered_courses = []
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
                display_name = course.name
                if course.kind == "pratica":
                    display_name += f" ({course.code[-1]})"
                
                # Tooltip com informações
                tooltip = f"{course.name}\nCódigo: {course.display_code}\nCH: {course.display_ch}h"
                if course.creditos:
                    tooltip += f"\nCréditos: {course.creditos}"
                if course.phase:
                    tooltip += f"\nFase: {course.phase}"
                
                row += (
                    f"<td style='padding:6px;background:{bg};border:1px solid {GRID_LINE};"
                    "border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.15);"
                    "color:white;font-size:10px;font-weight:600;text-align:center;"
                    f"title='{tooltip}'>"
                    f"{display_name[:20]}<br><span style='font-weight:400;opacity:0.9'>{course.display_code}</span></td>"
                )
            else:
                row += f"<td style='padding:6px;background:{EMPTY_CELL_BG};border:1px solid {GRID_LINE}'></td>"
        row += "</tr>"
        rows_html += row

    # Legenda
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
    <div style="margin-top:10px;display:flex;flex-wrap:wrap">{legend_html}</div>
    </div>
    """
    st.markdown(table_html, unsafe_allow_html=True)
    
    # Estatísticas rápidas
    if grouped_groups:
        st.caption(f"📊 {len(grouped_groups)} disciplinas | {total_ch_geral}h | {total_creditos_geral} créditos")
