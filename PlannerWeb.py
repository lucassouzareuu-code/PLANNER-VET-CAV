import streamlit as st
from typing import List, Dict, Optional

# =========================================================================
# LÓGICA E Mapeamentos de Horários
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
    def __init__(self, code: str, name: str, credits: int, schedule: Dict[str, List[int]], phase: str = "", creditos: Optional[int] = None):
        self.code = code
        self.name = name
        self.credits = credits  # representa a carga horária em horas (CH)
        self.schedule = schedule
        self.phase = phase
        self.group = code
        self.kind = "unica"
        self.theory: Optional["Course"] = None
        self.official_code: Optional[str] = None
        self.ch: Optional[int] = credits
        self.creditos: Optional[int] = creditos
        self.tipo: str = "Obrigatória"

    @property
    def display_code(self) -> str:
        return self.official_code or self.code

    @property
    def display_ch(self) -> int:
        return self.ch if self.ch is not None else self.credits

    def __str__(self):
        label = f"[{self.display_code}] {self.name} ({self.display_ch}h"
        if self.creditos is not None:
            label += f" | {self.creditos} créd."
        label += ")"
        return label

def build_initial_catalog() -> List[Course]:
    """Catálogo de Medicina Veterinária UDESC CAV - Horários e Matriz Curricular Atualizados"""
    catalog: List[Course] = []

    def add(phase, code, name, credits, schedule, creditos=None):
        catalog.append(Course(code, name, credits, schedule, phase=phase, creditos=creditos))

    # =========================================================================
    # 1ª FASE - VET122-01 (CH Total da Fase: 360h / 20 Créditos)
    # =========================================================================
    add("1ª Fase", "ANA1-T", "Anatomia I (Teórica)", 90, {"TERÇA": [1, 2], "QUARTA": [1, 2], "QUINTA": [1, 2], "SEXTA": [1, 2]}, creditos=5)
    add("1ª Fase", "ANA1-A", "Anatomia I (Turma A)", 90, {"SEGUNDA": [1, 2]}, creditos=5)
    add("1ª Fase", "ANA1-B", "Anatomia I (Turma B)", 90, {"SEGUNDA": [3, 4]}, creditos=5)
    add("1ª Fase", "ANA1-C", "Anatomia I (Turma C)", 90, {"TERÇA": [7, 8]}, creditos=5)
    add("1ª Fase", "ANA1-D", "Anatomia I (Turma D)", 90, {"QUARTA": [7, 8]}, creditos=5)

    add("1ª Fase", "HISTG-T", "Histologia Geral (Teórica)", 72, {"TERÇA": [3, 4], "SEXTA": [3, 4]}, creditos=4)
    add("1ª Fase", "HISTG-A", "Histologia Geral (Turma A)", 72, {"QUINTA": [7, 8]}, creditos=4)
    add("1ª Fase", "HISTG-B", "Histologia Geral (Turma B)", 72, {"QUARATA": [9, 10]} if "QUARATA" in [] else {"QUARTA": [9, 10]}, creditos=4)

    add("1ª Fase", "SOAMV", "Sociologia Aplicada", 36, {"SEGUNDA": [1, 2]}, creditos=2)
    add("1ª Fase", "INTRO", "Introdução à Medicina Veterinária", 36, {"TERÇA": [3]}, creditos=2)
    add("1ª Fase", "ECOLO", "Ecologia e Desenvolvimento", 36, {"QUINTA": [3, 4]}, creditos=2)
    add("1ª Fase", "ESTAT", "Estatística e Experimentação", 54, {"SEGUNDA": [6, 7, 8]}, creditos=3)
    add("1ª Fase", "BIOQB-T", "Bioquímica de Biomoléculas (Teórica)", 72, {"TERÇA": [6, 7], "QUARTA": [6, 7]}, creditos=4)
    add("1ª Fase", "COMPOR", "Comportamento e Bem-Estar Animal", 36, {"QUINTA": [9, 10]}, creditos=2)
    add("1ª Fase", "EXTEN", "Extensão, Comunicação e Sociedade", 36, {"SEXTA": [9, 10]}, creditos=2)

    # =========================================================================
    # 2ª FASE - VET122-02 (CH Total da Fase: 396h / 22 Créditos)
    # =========================================================================
    add("2ª Fase", "ANA2-T", "Anatomia II (Teórica)", 90, {"SEGUNDA": [1, 2], "TERÇA": [1, 2], "QUARTA": [1, 2], "QUINTA": [1, 2]}, creditos=5)
    add("2ª Fase", "ANA2-A", "Anatomia II (Turma A)", 90, {"SEGUNDA": [11, 12]}, creditos=5)
    add("2ª Fase", "ANA2-B", "Anatomia II (Turma B)", 90, {"QUARTA": [11, 12]}, creditos=5)

    add("2ª Fase", "HIST2-T", "Histologia e Embriologia (Teórica)", 90, {"SEGUNDA": [3, 4], "TERÇA": [3, 4], "QUARTA": [3, 4]}, creditos=5)
    add("2ª Fase", "HIST2-A", "Histologia e Embriologia (Turma A)", 90, {"SEXTA": [1, 2]}, creditos=5)

    add("2ª Fase", "GENET-T", "Genética (Teórica)", 72, {"SEXTA": [3, 4]}, creditos=4)
    add("2ª Fase", "BIOQM-T", "Bioquímica Metabólica (Teórica)", 72, {"SEGUNDA": [7, 8, 9, 10]}, creditos=4)

    add("2ª Fase", "PARA1-T", "Parasitologia I (Teórica)", 72, {"TERÇA": [7, 8], "QUINTA": [7, 8]}, creditos=4)
    add("2ª Fase", "PARA1-A", "Parasitologia I (Turma A)", 72, {"TERÇA": [11, 12]}, creditos=4)

    add("2ª Fase", "FISI1-T", "Fisiologia I (Teórica)", 90, {"SEGUNDA": [5], "QUARTA": [5, 6], "QUINTA": [5, 6]}, creditos=5)

    # =========================================================================
    # 3ª FASE - VET122-03 (CH Total da Fase: 396h / 22 Créditos)
    # =========================================================================
    add("3ª Fase", "IMUNO-T", "Imunologia Veterinária (Teórica)", 54, {"SEGUNDA": [1, 2, 11]}, creditos=3)
    add("3ª Fase", "FISI2-T", "Fisiologia II (Teórica)", 72, {"TERÇA": [1, 2], "SEGUNDA": [7, 8]}, creditos=4)
    add("3ª Fase", "PARA2-T", "Parasitologia II (Teórica)", 72, {"QUINTA": [1, 2], "SEGUNDA": [9, 10]}, creditos=4)
    add("3ª Fase", "MICRO-T", "Microbiologia Básica (Teórica)", 72, {"SEGUNDA": [3, 4], "TERÇA": [7, 8]}, creditos=4)
    add("3ª Fase", "NUTRI", "Nutrição Animal", 54, {"QUARTA": [3, 4, 6, 7, 8]}, creditos=3)
    add("3ª Fase", "FARM1-T", "Farmacologia Geral (Teórica)", 72, {"SEXTA": [1, 2, 3, 4, 7, 8, 9, 10]}, creditos=4)
    add("3ª Fase", "EPIST", "Epistemologia e Metodologia Científica", 36, {"QUARTA": [9, 10]}, creditos=2)
    add("3ª Fase", "MELHO", "Melhoramento Animal", 36, {"QUINTA": [10, 11]}, creditos=2)

    # =========================================================================
    # 4ª FASE - VET122-04 (CH Total da Fase: 504h / 28 Créditos)
    # =========================================================================
    add("4ª Fase", "ECONO", "Economia e Administração", 72, {"SEGUNDA": [1, 2], "QUARTA": [1, 2]}, creditos=4)
    add("4ª Fase", "EPIDE", "Epidemiologia", 36, {"QUINTA": [3, 4]}, creditos=2)
    add("4ª Fase", "FARMG", "Farmacologia Geral", 72, {"TERÇA": [3, 4], "QUARTA": [3, 4]}, creditos=4)
    add("4ª Fase", "FISI2", "Fisiologia II", 72, {"SEGUNDA": [3, 4], "TERÇA": [1, 2]}, creditos=4)
    add("4ª Fase", "NUTRI4", "Nutrição Animal", 54, {"QUARTA": [7, 8, 9]}, creditos=3)
    add("4ª Fase", "PARA2", "Parasitologia II", 72, {"SEGUNDA": [7, 8], "QUINTA": [1, 2]}, creditos=4)
    add("4ª Fase", "MICRE", "Microbiologia Especial", 90, {"QUARTA": [10, 11], "SEXTA": [1, 2, 3]}, creditos=5)

    # =========================================================================
    # 5ª FASE - VET122-05 (CH Total da Fase: 504h / 28 Créditos)
    # =========================================================================
    add("5ª Fase", "ALIMA", "Alimentos e Alimentação Animal", 90, {"SEGUNDA": [1, 2, 3], "QUARTA": [1, 2]}, creditos=5)
    add("5ª Fase", "COEXT", "Comunicação e Extensão Rural", 36, {"TERÇA": [1, 2]}, creditos=2)
    add("5ª Fase", "FARMD-T", "Farmacodinâmica (Teórica)", 72, {"QUINTA": [1, 2, 3, 4]}, creditos=4)
    add("5ª Fase", "FORRA", "Forragicultura", 54, {"SEXTA": [1, 2, 3]}, creditos=3)
    add("5ª Fase", "PACLI-T", "Patologia Clínica Vet. (Teórica)", 72, {"TERÇA": [7, 8, 9, 10]}, creditos=4)
    add("5ª Fase", "PATG-T", "Patologia Geral (Teórica)", 90, {"SEGUNDA": [7, 8, 9, 10, 11]}, creditos=5)
    add("5ª Fase", "SEMIO-T", "Semiologia (Teórica)", 90, {"QUARTA": [7, 8, 9, 10, 11]}, creditos=5)

    # =========================================================================
    # 6ª FASE - VET122-06 (CH Total da Fase: 468h / 26 Créditos)
    # =========================================================================
    add("6ª Fase", "SUINO-T", "Suinocultura (Teórica)", 54, {"SEGUNDA": [1, 2, 3]}, creditos=3)
    add("6ª Fase", "DOIC-T", "Doenças Infecto-Contagiosas (Teórica)", 90, {"TERÇA": [1, 2, 3, 4, 5]}, creditos=5)
    add("6ª Fase", "DOENP-T", "Doenças Parasitárias (Teórica)", 72, {"QUARTA": [1, 2, 3, 4]}, creditos=4)
    add("6ª Fase", "CLINR-T", "Clínica Médica de Ruminantes (Teórica)", 90, {"QUINTA": [1, 2, 3, 4, 5]}, creditos=5)
    add("6ª Fase", "PATE-T", "Patologia Especial (Teórica)", 90, {"SEXTA": [1, 2, 3, 4, 5]}, creditos=5)
    add("6ª Fase", "PISCI", "Piscicultura", 36, {"QUARTA": [7, 8]}, creditos=2)
    add("6ª Fase", "TERAP", "Terapêutica", 36, {"SEGUNDA": [7, 8]}, creditos=2)

    # =========================================================================
    # 7ª FASE - VET122-07 (CH Total da Fase: 486h / 27 Créditos)
    # =========================================================================
    add("7ª Fase", "TCIR-T", "Técnica Cirúrgica (Teórica)", 90, {"TERÇA": [0, 1], "QUARTA": [1, 2, 3, 4]}, creditos=5)
    add("7ª Fase", "ANEST-T", "Anestesiologia (Teórica)", 54, {"TERÇA": [1, 2], "QUARTA": [6, 7, 8, 9]}, creditos=3)
    add("7ª Fase", "DIAG-T", "Diagnóstico por Imagem (Teórica)", 54, {"QUINTA": [1, 2, 3, 4], "SEXTA": [9, 10, 11]}, creditos=3)
    add("7ª Fase", "CLINC-T", "Clínica Médica de Cães e Gatos I (Teórica)", 90, {"SEXTA": [0, 1, 2, 3, 4], "TERÇA": [7, 8]}, creditos=5)
    add("7ª Fase", "FISREPO-T", "Fisiopatologia da Reprodução I (Teórica)", 90, {"TERÇA": [3, 4, 5], "QUINTA": [6, 7, 8, 9, 10, 11]}, creditos=5)
    add("7ª Fase", "BOVIC-T", "Bovinocultura de Corte (Teórica)", 54, {"SÁBADO": [1, 2, 3]}, creditos=3)
    add("7ª Fase", "SAUP-T", "Saúde Pública Veterinária (Teórica)", 54, {"SÁBADO": [6, 7, 8]}, creditos=3)

    # =========================================================================
    # 8ª FASE - VET122-08 (CH Total da Fase: 468h / 26 Créditos)
    # =========================================================================
    add("8ª Fase", "CLINE-T", "Clínica Médica de Equinos (Teórica)", 90, {"TERÇA": [0, 1, 2, 3, 4]}, creditos=5)
    add("8ª Fase", "PATCL2-T", "Patologia e Clínica Cirúrgica (Teórica)", 108, {"QUARTA": [1, 2, 3, 4], "QUINTA": [0, 1, 2, 3, 4, 5], "SEXTA": [0, 1, 2, 3, 4, 5]}, creditos=6)
    add("8ª Fase", "SANSU-T", "Sanidade Suína (Teórica)", 54, {"TERÇA": [6, 7, 8]}, creditos=3)
    add("8ª Fase", "BOVIL", "Bovinocultura de Leite", 54, {"TERÇA": [7, 8, 9]}, creditos=3)
    add("8ª Fase", "INSPE-T", "Inspeção e Tec. Prod. Origem Animal I (Teórica)", 72, {"TERÇA": [9, 10, 11, 12]}, creditos=4)
    add("8ª Fase", "AVIC-T", "Avicultura (Teórica)", 54, {"SEXTA": [6, 7, 8, 9, 10]}, creditos=3)
    add("8ª Fase", "OVINO-T", "Ovinocultura (Teórica)", 36, {"SÁBADO": [1, 2]}, creditos=2)

    # =========================================================================
    # 9ª FASE - VET122-09 (CH Total da Fase: 828h / 46 Créditos)
    # =========================================================================
    add("9ª Fase", "CLCG2-T", "Clínica Médica de Cães e Gatos II (Teórica)", 90, {"TERÇA": [0, 1, 2, 3, 4]}, creditos=5)
    add("9ª Fase", "OBSTE-T", "Obstetrícia (Teórica)", 72, {"SEGUNDA": [1, 2, 3, 4], "TERÇA": [7, 8]}, creditos=4)
    add("9ª Fase", "FRIA2-T", "Fisiopatologia da Reprodução II (Teórica)", 72, {"QUINTA": [1, 2, 3, 4], "SEXTA": [1, 2, 3, 4], "TERÇA": [12]}, creditos=4)
    add("9ª Fase", "INSP2-T", "Inspeção e Tec. Prod. Origem Animal II (Teórica)", 90, {"QUARTA": [0, 1, 2, 3, 4, 7, 8, 9, 10, 12]}, creditos=5)
    add("9ª Fase", "TOXI", "Toxicologia e Plantas Tóxicas", 36, {"TERÇA": [9, 10]}, creditos=2)
    add("9ª Fase", "DAVES-T", "Doenças das Aves (Teórica)", 72, {"QUINTA": [7, 8, 9, 10]}, creditos=4)

    # =========================================================================
    # ELETIVAS (10ª FASE)
    # =========================================================================
    add("Eletivas", "LACTI", "Lacticínios", 36, {"TERÇA": [3, 4]}, creditos=2)
    add("Eletivas", "OFTAL", "Oftalmologia Veterinária", 36, {"QUARTA": [3, 4]}, creditos=2)
    add("Eletivas", "DERMA", "Dermatologia Veterinária", 36, {"QUINTA": [3], "SEXTA": [4]}, creditos=2)
    add("Eletivas", "CITO", "Citologia Diagnóstica", 36, {"QUINTA": [4], "SEXTA": [5]}, creditos=2)
    add("Eletivas", "FISIA", "Fisiatria Veterinária", 36, {"TERÇA": [7, 8]}, creditos=2)
    add("Eletivas", "COMPBEM", "Comportamento e Bem-Estar Animal", 36, {"QUARTA": [7, 8]}, creditos=2)
    add("Eletivas", "GEREN", "Gerenciamento e Produção Avícola", 36, {"QUINTA": [7, 8]}, creditos=2)
    add("Eletivas", "EQUIN", "Equinocultura", 36, {"SEXTA": [7, 8]}, creditos=2)
    add("Eletivas", "MICROAL", "Microbiologia dos Produtos de Origem Animal", 36, {"SEXTA": [7, 8]}, creditos=2)
    add("Eletivas", "CARDIO", "Cardiologia de Cães e Gatos", 36, {"SEXTA": [7, 8]}, creditos=2)
    add("Eletivas", "MEDSEL", "Medicina de Animais Silvestres", 36, {"SEGUNDA": [9, 10]}, creditos=2)
    add("Eletivas", "AQUAC", "Aquacultura", 36, {"SEGUNDA": [11, 12]}, creditos=2)
    add("Eletivas", "ESTAG", "Estágio Curricular Supervisionado", 486, {"SEGUNDA": [14]}, creditos=27)

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
    
    for day, slots in course.schedule.items():
        combined[day] = list(slots)
    
    if course.theory:
        for day, slots in course.theory.schedule.items():
            if day in combined:
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
        
        combined_schedule_data = get_combined_schedule(selected_course)
        
        details = (
            f"**Código:** {selected_course.display_code}  \n**Nome:** {selected_course.name}  \n"
            f"**Carga Horária:** {selected_course.display_ch}h{creditos_line}  \n**Horários (Teórica + Prática):**\n"
        )
        
        if combined_schedule_data:
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
                display_name = course.name
                if course.kind == "pratica":
                    display_name += f" ({course.code[-1]})"
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
