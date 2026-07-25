import streamlit as st
from typing import List, Dict, Optional

# =========================================================================
# LÓGICA E ESTRUTURAS DE DADOS
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
    def __init__(self, code: str, name: str, credits: int, schedule: Dict[str, List[int]], phase: str = ""):
        self.code = code
        self.name = name
        self.credits = credits  # Trated as carga horária (CH) default
        self.schedule = schedule
        self.phase = phase
        self.group = code
        self.kind = "unica"
        self.theory: Optional["Course"] = None
        self.official_code: Optional[str] = None
        self.ch: Optional[int] = credits
        # Cálculo estimado de créditos acadêmicos (ex: 18h = 1 crédito)
        self.creditos: Optional[int] = max(1, credits // 18) if credits else 0
        self.tipo: str = "Obrigatória"

    @property
    def display_code(self) -> str:
        return self.official_code or self.code

    @property
    def display_ch(self) -> int:
        return self.ch if self.ch is not None else self.credits

    def __str__(self):
        label = f"[{self.display_code}] {self.name} ({self.display_ch}h"
        if self.creditos:
            label += f" | {self.creditos} cr."
        label += ")"
        return label

def build_initial_catalog() -> List[Course]:
    """Catálogo completo de Medicina Veterinária UDESC CAV - HORÁRIOS 2026/2"""
    catalog: List[Course] = []

    def add(phase, code, name, credits, schedule):
        catalog.append(Course(code, name, credits, schedule, phase=phase))

    # 1ª FASE
    add("1ª Fase", "ANA1-T", "Anatomia I (Teórica)", 72, {"SEGUNDA": [1, 2], "TERÇA": [1, 2]})
    add("1ª Fase", "ANA1-A", "Anatomia I (Turma A)", 36, {"QUARTA": [3, 4], "TERÇA": [9]})
    add("1ª Fase", "ANA1-B", "Anatomia I (Turma B)", 36, {"TERÇA": [10]})
    add("1ª Fase", "ANA1-C", "Anatomia I (Turma C)", 36, {"TERÇA": [11], "SEXTA": [1, 2]})
    add("1ª Fase", "ANA1-D", "Anatomia I (Turma D)", 36, {"QUARTA": [1, 2], "SEXTA": [3, 4]})
    add("1ª Fase", "HISTG-T", "Histologia Geral (Teórica)", 72, {"TERÇA": [3, 4], "QUINTA": [1, 2]})
    add("1ª Fase", "HISTG-A", "Histologia Geral (Turma A)", 36, {"QUINTA": [1, 2]})
    add("1ª Fase", "HISTG-B", "Histologia Geral (Turma B)", 36, {"QUARTA": [3, 4]})
    add("1ª Fase", "HISTG-C", "Histologia Geral (Turma C)", 36, {"QUINTA": [7, 8]})
    add("1ª Fase", "HISTG-D", "Histologia Geral (Turma D)", 36, {"QUARTA": [9, 10]})
    add("1ª Fase", "INTRO", "Introdução à Medicina Veterinária", 36, {"QUARTA": [2]})
    add("1ª Fase", "SOAMV", "Sociologia Aplicada", 36, {"SEGUNDA": [3, 4]})
    add("1ª Fase", "ECOLO", "Ecologia e Desenvolvimento", 36, {"QUINTA": [3, 4]})
    add("1ª Fase", "ESTAT", "Estatística e Experimentação", 54, {"SEGUNDA": [7, 8, 9]})
    add("1ª Fase", "BIOQB-T", "Bioquímica de Biomoléculas (Teórica)", 54, {"TERÇA": [7, 8], "QUARTA": [7]})
    add("1ª Fase", "BIOQB-A", "Bioquímica de Biomoléculas (Turma A)", 54, {"QUARTA": [7]})
    add("1ª Fase", "BIOQB-B", "Bioquímica de Biomoléculas (Turma B)", 54, {"SEXTA": [8]})
    add("1ª Fase", "BIOQB-C", "Bioquímica de Biomoléculas (Turma C)", 54, {"QUARTA": [11]})
    add("1ª Fase", "EXTEN", "Extensão, Comunicação e Sociedade", 36, {"SEXTA": [7, 8]})
    add("1ª Fase", "COMPOR", "Comportamento e Bem-Estar Animal", 36, {"QUINTA": [9, 10]})

    # 2ª FASE
    add("2ª Fase", "ANA2-T", "Anatomia II (Teórica)", 72, {"SEGUNDA": [1, 2], "QUARTA": [3, 4]})
    add("2ª Fase", "ANA2-A", "Anatomia II (Turma A)", 36, {"QUINTA": [7, 8], "SEXTA": [9]})
    add("2ª Fase", "ANA2-B", "Anatomia II (Turma B)", 36, {"QUARTA": [9, 10], "SEXTA": [10]})
    add("2ª Fase", "ANA2-C", "Anatomia II (Turma C)", 36, {"SEGUNDA": [11, 12], "QUARTA": [12]})
    add("2ª Fase", "ANA2-D", "Anatomia II (Turma D)", 36, {"QUARTA": [1, 2], "QUARTA": [11]})
    add("2ª Fase", "HIST2-T", "Histologia e Embriologia (Teórica)", 72, {"SEGUNDA": [3, 4], "SEXTA": [1]})
    add("2ª Fase", "HIST2-A", "Histologia e Embriologia (Turma A)", 36, {"TERÇA": [7, 8]})
    add("2ª Fase", "HIST2-B", "Histologia e Embriologia (Turma B)", 36, {"TERÇA": [9, 10]})
    add("2ª Fase", "HIST2-C", "Histologia e Embriologia (Turma C)", 36, {"QUARTA": [7, 8]})
    add("2ª Fase", "HIST2-D", "Histologia e Embriologia (Turma D)", 36, {"SEXTA": [7, 8]})
    add("2ª Fase", "GENET-T", "Genética (Teórica)", 54, {"SEXTA": [2]})
    add("2ª Fase", "GENE-A", "Genética (Turma A)", 36, {"SEXTA": [3, 4]})
    add("2ª Fase", "GENE-B", "Genética (Turma B)", 36, {"SEXTA": [8]})
    add("2ª Fase", "BIOQM-T", "Bioquímica Metabólica (Teórica)", 72, {})
    add("2ª Fase", "BIOQM-A", "Bioquímica Metabólica (Turma A)", 36, {"SEGUNDA": [7, 8]})
    add("2ª Fase", "BIOQM-B", "Bioquímica Metabólica (Turma B)", 36, {"SEGUNDA": [9, 10]})
    add("2ª Fase", "PARA1-T", "Parasitologia I (Teórica)", 72, {"TERÇA": [3, 4]})
    add("2ª Fase", "PARA1-A", "Parasitologia I (Turma A)", 36, {"TERÇA": [1, 2]})
    add("2ª Fase", "PARA1-B", "Parasitologia I (Turma B)", 36, {"TERÇA": [11, 12]})
    add("2ª Fase", "PARA1-C", "Parasitologia I (Turma C)", 36, {"QUINTA": [3, 4]})
    add("2ª Fase", "PARA1-D", "Parasitologia I (Turma D)", 36, {"QUINTA": [7, 8]})
    add("2ª Fase", "FISI1-T", "Fisiologia I (Teórica)", 72, {"SEGUNDA": [6], "SEXTA": [7, 8]})
    add("2ª Fase", "FISI1-A", "Fisiologia I (Turma A)", 36, {"QUINTA": [1, 2]})
    add("2ª Fase", "FISI1-B", "Fisiologia I (Turma B)", 36, {"QUINTA": [9, 10]})
    add("2ª Fase", "FISI1-C", "Fisiologia I (Turma C)", 36, {"QUINTA": [3, 4]})
    add("2ª Fase", "FISI1-D", "Fisiologia I (Turma D)", 36, {"QUINTA": [9, 10]})

    # 3ª FASE
    add("3ª Fase", "IMUNO-T", "Imunologia Veterinária (Teórica)", 54, {"SEGUNDA": [1, 2]})
    add("3ª Fase", "IMUNO-A", "Imunologia Veterinária (Turma A)", 36, {"SEGUNDA": [11]})
    add("3ª Fase", "IMUNO-B", "Imunologia Veterinária (Turma B)", 36, {"SEGUNDA": [12]})
    add("3ª Fase", "FISI2-T", "Fisiologia II (Teórica)", 72, {"TERÇA": [1, 2]})
    add("3ª Fase", "FISI2-A", "Fisiologia II (Turma A)", 36, {"SEGUNDA": [7, 8]})
    add("3ª Fase", "FISI2-B", "Fisiologia II (Turma B)", 36, {"SEGUNDA": [9, 10]})
    add("3ª Fase", "FISI2-C", "Fisiologia II (Turma C)", 36, {"TERÇA": [3, 4]})
    add("3ª Fase", "FISI2-D", "Fisiologia II (Turma D)", 36, {"QUARTA": [3, 4]})
    add("3ª Fase", "PARA2-T", "Parasitologia II (Teórica)", 72, {"QUINTA": [1, 2]})
    add("3ª Fase", "PARA2-A", "Parasitologia II (Turma A)", 36, {"SEGUNDA": [7, 8]})
    add("3ª Fase", "PARA2-B", "Parasitologia II (Turma B)", 36, {"SEGUNDA": [9, 10]})
    add("3ª Fase", "PARA2-C", "Parasitologia II (Turma C)", 36, {"TERÇA": [3, 4]})
    add("3ª Fase", "PARA2-D", "Parasitologia II (Turma D)", 36, {"QUARTA": [1, 2]})
    add("3ª Fase", "MICRO-T", "Microbiologia Básica (Teórica)", 72, {"SEGUNDA": [3, 4]})
    add("3ª Fase", "MICRO-A", "Microbiologia Básica (Turma A)", 36, {"SEGUNDA": [7, 8]})
    add("3ª Fase", "MICRO-B", "Microbiologia Básica (Turma B)", 36, {"SEGUNDA": [9, 10]})
    add("3ª Fase", "MICRO-C", "Microbiologia Básica (Turma C)", 36, {"TERÇA": [7, 8]})
    add("3ª Fase", "MICRO-D", "Microbiologia Básica (Turma D)", 36, {"TERÇA": [9, 10]})
    add("3ª Fase", "NUTRI", "Nutrição Animal", 54, {"QUARTA": [7, 8, 9, 10, 11, 12]})
    add("3ª Fase", "FARM1-T", "Farmacologia Geral (Teórica)", 72, {"SEXTA": [1, 2, 3, 4, 7, 8]})
    add("3ª Fase", "FARM1-A", "Farmacologia Geral (Turma A)", 36, {"QUINTA": [9, 10]})
    add("3ª Fase", "FARM1-B", "Farmacologia Geral (Turma B)", 36, {"SEXTA": [1, 2]})
    add("3ª Fase", "FARM1-C", "Farmacologia Geral (Turma C)", 36, {"SEXTA": [3, 4]})
    add("3ª Fase", "EPIST", "Epistemologia e Metodologia Científica", 36, {"QUARTA": [9, 10]})
    add("3ª Fase", "MELHO", "Melhoramento Animal", 36, {"QUINTA": [11, 12]})

    # ELETIVAS
    add("Eletivas", "LACTI", "Lacticínios", 36, {"TERÇA": [3, 4]})
    add("Eletivas", "OFTAL", "Oftalmologia Veterinária", 36, {"QUARTA": [3, 4]})
    add("Eletivas", "DERMA", "Dermatologia Veterinária", 36, {"QUINTA": [3], "SEXTA": [4]})
    add("Eletivas", "CITO", "Citologia Diagnóstica", 36, {"QUINTA": [4], "SEXTA": [5]})
    add("Eletivas", "FISIA", "Fisiatria Veterinária", 36, {"TERÇA": [7, 8]})
    add("Eletivas", "COMPBEM", "Comportamento e Bem-Estar Animal", 36, {"QUARTA": [7, 8]})
    add("Eletivas", "GEREN", "Gerenciamento e Produção Avícola", 36, {"QUINTA": [7, 8]})
    add("Eletivas", "EQUIN", "Equinocultura", 36, {"SEXTA": [7, 8]})
    add("Eletivas", "MEDSEL", "Medicina de Animais Silvestres", 36, {"SEGUNDA": [9, 10]})

    link_theory_to_practicals(catalog)
    return catalog

def infer_group_and_kind(code: str):
    if code.endswith("-T"):
        return code[:-2], "teorica"
    if code.endswith("-TEO"):
        return code[:-4], "teorica"
    if len(code) >= 2 and code[-2] == "-" and code[-1] in "ABCDEFGH":
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
# CORES E TEMAS
# =========================================================================

PAGE_BG = "#F4F6F9"
PHASE_COLORS = {
    "1ª Fase":  ("#6836F3", "#9C7BFF"),
    "2ª Fase":  ("#08C9E7", "#5FD3E3"),
    "3ª Fase":  ("#086E4E", "#3FCB9C"),
    "4ª Fase":  ("#3178C4", "#63ABF2"),
    "5ª Fase":  ("#E0A62F", "#F2C55E"),
    "6ª Fase":  ("#E0632F", "#F28A5E"),
    "7ª Fase":  ("#D6396B", "#EE6D97"),
    "8ª Fase":  ("#7B05FA", "#B06BF2"),
    "9ª Fase":  ("#DB2A33", "#E66666"),
    "Eletivas": ("#4A5568", "#A0AEC0"),
}

def phase_gradient(phase: str) -> str:
    c1, c2 = PHASE_COLORS.get(phase, ("#2D3748", "#718096"))
    return f"linear-gradient(135deg, {c1} 0%, {c2} 100%)"

# =========================================================================
# INTERFACE STREAMLIT
# =========================================================================

st.set_page_config(page_title="Simulador CAV", layout="wide")

if "available_courses" not in st.session_state:
    st.session_state.available_courses = build_initial_catalog()
if "registered_courses" not in st.session_state:
    st.session_state.registered_courses = []

st.title("🎓 Simulador de Matrícula UDESC-CAV")

col_left, col_right = st.columns([1, 2], gap="large")

# ---------------- Painel Esquerdo (Seleção) ----------------
with col_left:
    st.subheader("🔍 Buscar Disciplinas")

    phase_choice = st.selectbox("Filtrar por Fase", ["Todas as Fases"] + PHASES)
    query = st.text_input("Nome ou Código").lower().strip()

    filtered_courses = [
        c for c in st.session_state.available_courses
        if c.kind != "teorica"
        and (phase_choice == "Todas as Fases" or c.phase == phase_choice)
        and (query in c.display_code.lower() or query in c.name.lower())
    ]

    options = [str(c) for c in filtered_courses]
    selected_label = st.selectbox("Catálogo Disponível", options) if options else None

    selected_course = None
    if selected_label:
        idx = options.index(selected_label)
        selected_course = filtered_courses[idx]

        st.markdown(
            f"<span style='background:{phase_gradient(selected_course.phase)};color:white;"
            f"padding:4px 12px;border-radius:12px;font-size:12px;font-weight:600'>{selected_course.phase}</span>",
            unsafe_allow_html=True,
        )

        combined_schedule_data = get_combined_schedule(selected_course)
        
        details = (
            f"\n\n**Código:** {selected_course.display_code}  \n**Carga Horária:** {selected_course.display_ch}h  \n"
            f"**Créditos:** {selected_course.creditos} cr.  \n\n**Horários Combinados:**\n"
        )
        
        if combined_schedule_data:
            for day in DAYS:
                if day in combined_schedule_data:
                    slot_str = ", ".join([get_slot_time_str(s) for s in sorted(combined_schedule_data[day])])
                    details += f"* **{day}:** {slot_str}\n"
        else:
            details += "* Nenhum horário cadastrado.\n"

        st.markdown(details)

    if st.button("➕ Adicionar Disciplina", use_container_width=True, disabled=selected_course is None) and selected_course:
        already_added = any(c.group == selected_course.group for c in st.session_state.registered_courses)
        if already_added:
            st.warning(f"Você já adicionou uma turma de '{selected_course.name}'.")
        else:
            conflict_msg = check_conflict(selected_course, st.session_state.registered_courses)
            if conflict_msg:
                st.error(f"⚠️ Choque de Horário: {conflict_msg}")
            else:
                st.session_state.registered_courses.append(selected_course)
                if selected_course.theory:
                    st.session_state.registered_courses.append(selected_course.theory)
                st.success(f"'{selected_course.name}' adicionada com sucesso!")
                st.rerun()

    st.markdown("---")
    st.subheader("📌 Disciplinas Selecionadas")
    
    grouped_groups = []
    for c in st.session_state.registered_courses:
        if c.group not in grouped_groups:
            grouped_groups.append(c.group)

    total_ch_geral = 0
    total_creditos_geral = 0
    
    for group in grouped_groups:
        group_courses = [c for c in st.session_state.registered_courses if c.group == group]
        practical = next((c for c in group_courses if c.kind != "teorica"), group_courses[0])
        
        ch = practical.display_ch
        creditos = practical.creditos or 0
        total_ch_geral += ch
        total_creditos_geral += creditos
        
        row_col1, row_col2 = st.columns([4, 1])
        row_col1.write(f"**[{practical.display_code}]** {practical.name} ({ch}h)")
        if row_col2.button("🗑️", key=f"remove_{group}"):
            st.session_state.registered_courses = [c for c in st.session_state.registered_courses if c.group != group]
            st.rerun()

    if grouped_groups:
        st.info(f"**Total acumulado:** {total_ch_geral}h | {total_creditos_geral} Créditos")

# ---------------- Painel Direito (Grade Semanal) ----------------
with col_right:
    st.subheader("📅 Grade Semanal")

    # Mapeamento do Grid
    grid = {}
    for c in st.session_state.registered_courses:
        for day, slots in c.schedule.items():
            if day in DAYS:
                for slot in slots:
                    grid[(day, slot)] = c

    # Construção da Tabela HTML Personalizada para Streamlit
    html_table = """
    <style>
        .grid-table { width: 100%; border-collapse: collapse; font-family: sans-serif; font-size: 11px; }
        .grid-table th { background-color: #1A202C; color: white; padding: 6px; text-align: center; }
        .grid-table td { border: 1px solid #CBD5E0; padding: 4px; text-align: center; height: 38px; }
        .time-col { background-color: #EDF2F7; font-weight: bold; width: 110px; }
        .cell-occupied { color: white; font-weight: bold; border-radius: 4px; padding: 2px; }
    </style>
    <table class="grid-table">
        <thead>
            <tr>
                <th>Horário</th>
    """
    for day in DAYS:
        html_table += f"<th>{day}</th>"
    html_table += "</tr></thead><tbody>"

    for slot in range(TOTAL_SLOTS):
        time_label = get_slot_time_str(slot)
        html_table += f"<tr><td class='time-col'>{time_label}</td>"
        
        for day in DAYS:
            course = grid.get((day, slot))
            if course:
                bg_color, _ = PHASE_COLORS.get(course.phase, ("#4A5568", "#A0AEC0"))
                kind_str = "(T)" if course.kind == "teorica" else ""
                html_table += f"<td><div class='cell-occupied' style='background:{bg_color}'>{course.code} {kind_str}</div></td>"
            else:
                html_table += "<td></td>"
        html_table += "</tr>"

    html_table += "</tbody></table>"
    st.markdown(html_table, unsafe_allow_html=True)
