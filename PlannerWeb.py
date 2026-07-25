def build_initial_catalog() -> List[Course]:
    """Catálogo completo baseado na Grade Curricular VET122 - 2012/2"""
    catalog: List[Course] = []

    def add(phase, code, name, total_ch, schedule, credits=None, tipo="Obrigatória"):
        """Adiciona uma disciplina com sua carga horária TOTAL"""
        catalog.append(Course(code, name, total_ch, schedule, phase=phase))
        # Define atributos extras
        catalog[-1].tipo = tipo
        catalog[-1].creditos = credits

    # =========================================================================
    # 1ª FASE
    # =========================================================================
    add("1ª Fase", "ANA1-90", "ANATOMIA I", 90, {
        "SEGUNDA": [1, 2],  # Teórica
        "TERÇA": [1, 2],    # Teórica
        "QUARTA": [3, 4],   # Prática A
        "TERÇA": [9]        # Prática A
    }, credits=5)

    add("1ª Fase", "BIOQB", "BIOQUÍMICA DE BIOMOLÉCULAS", 72, {
        "TERÇA": [7, 8],    # Teórica
        "QUARTA": [7],      # Teórica
        "QUARTA": [7],      # Prática A
        "SEXTA": [8],       # Prática B
        "QUARTA": [11]      # Prática C
    }, credits=4)

    add("1ª Fase", "DEONT", "DEONTOLOGIA", 36, {
        "QUARTA": [2]
    }, credits=2)

    add("1ª Fase", "EPIMC", "EPISTEMOLOGIA E METODOLOGIA CIENTÍFICA", 36, {
        "QUARTA": [9, 10]
    }, credits=2)

    add("1ª Fase", "ESTCA", "ESTATÍSTICA", 54, {
        "SEGUNDA": [7, 8, 9]
    }, credits=3)

    add("1ª Fase", "HISTG", "HISTOLOGIA GERAL", 72, {
        "TERÇA": [3, 4],    # Teórica
        "QUINTA": [1, 2],   # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUARTA": [3, 4],   # Prática B
        "QUINTA": [7, 8],   # Prática C
        "QUARTA": [9, 10]   # Prática D
    }, credits=4)

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
    }, credits=5)

    add("2ª Fase", "BIOQM", "BIOQUÍMICA METABÓLICA", 72, {
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [9, 10]  # Prática B
    }, credits=4)

    add("2ª Fase", "ECOLO", "ECOLOGIA", 36, {
        "QUINTA": [3, 4]
    }, credits=2)

    add("2ª Fase", "EXPER", "EXPERIMENTAÇÃO ANIMAL", 36, {}, credits=2)

    add("2ª Fase", "GENET", "GENÉTICA", 72, {
        "SEXTA": [2],       # Teórica
        "SEXTA": [3, 4],    # Prática A
        "SEXTA": [8]        # Prática B
    }, credits=4)

    add("2ª Fase", "HIST-90", "HISTOLOGIA E EMBRIOLOGIA", 90, {
        "SEGUNDA": [3, 4],  # Teórica
        "SEXTA": [1],       # Teórica
        "TERÇA": [7, 8],    # Prática A
        "TERÇA": [9, 10],   # Prática B
        "QUARTA": [7, 8],   # Prática C
        "SEXTA": [7, 8]     # Prática D
    }, credits=5)

    # =========================================================================
    # 3ª FASE
    # =========================================================================
    add("3ª Fase", "ANATT", "ANATOMIA TOPOGRÁFICA", 72, {
        # Horários a serem preenchidos
    }, credits=4)

    add("3ª Fase", "FIS-I", "FISIOLOGIA I", 90, {
        "SEGUNDA": [6],     # Teórica
        "SEXTA": [7, 8],    # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUINTA": [9, 10],  # Prática B
        "QUINTA": [3, 4],   # Prática C
        "QUINTA": [9, 10]   # Prática D (mesmo horário da B - verificar)
    }, credits=5)

    add("3ª Fase", "IMUNO", "IMUNOLOGIA", 54, {
        "SEGUNDA": [1, 2],  # Teórica
        "SEGUNDA": [11],    # Prática A
        "SEGUNDA": [12]     # Prática B
    }, credits=3)

    add("3ª Fase", "MICR", "MICROBIOLOGIA GERAL", 72, {
        "SEGUNDA": [3, 4],  # Teórica
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [9, 10], # Prática B
        "TERÇA": [7, 8],    # Prática C
        "TERÇA": [9, 10]    # Prática D
    }, credits=4)

    add("3ª Fase", "PARA1", "PARASITOLOGIA I", 72, {
        "TERÇA": [3, 4],    # Teórica
        "TERÇA": [1, 2],    # Prática A
        "TERÇA": [11, 12],  # Prática B
        "QUINTA": [3, 4],   # Prática C
        "QUINTA": [7, 8]    # Prática D
    }, credits=4)

    add("3ª Fase", "SOAMV", "SOCIOLOGIA APLICADA A MED VETERINÁRIA", 36, {
        "SEGUNDA": [3, 4]
    }, credits=2)

    # =========================================================================
    # 4ª FASE
    # =========================================================================
    add("4ª Fase", "ECOAD", "ECONOMIA E ADMINISTRAÇÃO", 72, {
        "SEXTA": [1, 2],
        "QUARTA": [7, 8]
    }, credits=4)

    add("4ª Fase", "EPIDE", "EPIDEMIOLOGIA", 36, {
        "QUINTA": [3, 4]
    }, credits=2)

    add("4ª Fase", "FARMG", "FARMACOLOGIA GERAL", 72, {
        "SEXTA": [1, 2, 3, 4, 7, 8],  # Teórica (verificar horários)
        "QUINTA": [9, 10],             # Prática A
        "SEXTA": [1, 2],               # Prática B
        "SEXTA": [3, 4],               # Prática C
        "TERÇA": [3, 4],               # Prática D
        "TERÇA": [9],                  # Prática E
        "QUARTA": [3, 4]               # Prática F
    }, credits=4)

    add("4ª Fase", "FISI2", "FISIOLOGIA II", 72, {
        "TERÇA": [1, 2],    # Teórica
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [9, 10], # Prática B
        "TERÇA": [3, 4],    # Prática C
        "QUARTA": [3, 4]    # Prática D
    }, credits=4)

    add("4ª Fase", "MELHO", "MELHORAMENTO ANIMAL", 36, {
        "QUINTA": [11, 12]
    }, credits=2)

    add("4ª Fase", "MICR-90", "MICROBIOLOGIA ESPECIAL", 90, {
        "QUARTA": [3, 4],   # Prática A
        "QUARTA": [7, 8],   # Prática B
        "QUARTA": [9]       # Prática C
    }, credits=5)

    add("4ª Fase", "NUTRI", "NUTRIÇÃO ANIMAL", 54, {
        "QUARTA": [7, 8, 9, 10, 11, 12],
        "SEGUNDA": [1, 2],
        "QUARTA": [1, 2]
    }, credits=3)

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
    }, credits=4)

    # =========================================================================
    # 5ª FASE
    # =========================================================================
    add("5ª Fase", "ALIMA", "ALIMENTOS E ALIMENTAÇÃO ANIMAL", 90, {}, credits=5)
    add("5ª Fase", "COEXT", "COMUNICAÇÃO EXTENSÃO RURAL", 36, {}, credits=2)
    add("5ª Fase", "FARMD", "FARMACODINÂMICA", 72, {}, credits=4)
    add("5ª Fase", "FORRA", "FORRAGICULTURA", 54, {}, credits=3)
    add("5ª Fase", "PACLI", "PATOLOGIA CLÍNICA VETERINÁRIA", 72, {}, credits=4)
    add("5ª Fase", "PATG-90", "PATOLOGIA GERAL", 90, {}, credits=5)
    add("5ª Fase", "SEMIO", "SEMIOLOGIA", 90, {}, credits=5)

    # =========================================================================
    # 6ª FASE
    # =========================================================================
    add("6ª Fase", "CLINR", "CLÍNICA MÉDICA DE RUMINANTES", 90, {
        "QUINTA": [1, 2, 3, 4],  # Teórica
        "QUARTA": [7, 8],        # Prática A
        "SEXTA": [9, 10],        # Prática B
        "SEXTA": [9],            # Prática C
        "QUINTA": [7, 8]         # Prática D
    }, credits=5)

    add("6ª Fase", "DOENP", "DOENÇAS PARASITÁRIAS", 72, {
        "QUARTA": [1, 2, 3, 4],  # Teórica
        "QUARTA": [7, 8],        # Prática A
        "SEXTA": [9, 10],        # Prática B
        "SEGUNDA": [11],         # Prática C
        "SÁBADO": [12],          # Prática C
        "QUINTA": [7, 8]         # Prática D
    }, credits=4)

    add("6ª Fase", "DOIC", "DOENÇAS INFECTO-CONTAGIOSAS", 90, {
        "TERÇA": [1, 2, 3, 4],   # Teórica
        "QUARTA": [5],           # Prática A
        "QUINTA": [10],          # Prática A
        "QUINTA": [7, 8],        # Prática B
        "SEXTA": [9]             # Prática C
    }, credits=5)

    add("6ª Fase", "PATE-90", "PATOLOGIA ESPECIAL", 90, {
        "SEXTA": [1, 2, 3, 4],   # Teórica
        "SEXTA": [9, 10],        # Prática A
        "QUINTA": [7, 8],        # Prática B
        "SÁBADO": [10, 11]       # Prática C
    }, credits=5)

    add("6ª Fase", "PISC", "PISCICULTURA", 36, {
        "QUARTA": [3, 4, 5]
    }, credits=2)

    add("6ª Fase", "SUINO", "SUINOCULTURA", 54, {
        "SEGUNDA": [1, 2],  # Teórica
        "SEGUNDA": [7, 8],  # Prática A
        "SEGUNDA": [8],     # Prática B
        "SEGUNDA": [9]      # Prática C
    }, credits=3)

    add("6ª Fase", "TERAP", "TERAPÊUTICA", 36, {
        "SEGUNDA": [3, 4]
    }, credits=2)

    # =========================================================================
    # 7ª FASE
    # =========================================================================
    add("7ª Fase", "ANES", "ANESTESIOLOGIA", 54, {
        "TERÇA": [1, 2],    # Teórica
        "QUARTA": [7],      # Prática A
        "QUARTA": [8],      # Prática B
        "QUARTA": [7],      # Prática C
        "QUARTA": [9]       # Prática D
    }, credits=3)

    add("7ª Fase", "BOVCO", "BOVINOCULTURA DE CORTE", 54, {
        "SÁBADO": [2, 3, 4]
    }, credits=3)

    add("7ª Fase", "CLCG", "CLÍNICA MÉDICA DE CÃES E GATOS I", 90, {
        "SEXTA": [1, 2],    # Teórica
        "QUINTA": [7, 8],   # Teórica
        "TERÇA": [7],       # Prática A
        "QUINTA": [9, 10],  # Prática C
        "QUINTA": [7, 8]    # Prática D
    }, credits=5)

    add("7ª Fase", "DIAGI", "DIAGNÓSTICO POR IMAGEM", 54, {
        "QUINTA": [5, 10],  # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUINTA": [3, 4],   # Prática B
        "QUINTA": [9, 10]   # Prática D
    }, credits=3)

    add("7ª Fase", "FRIA1", "FISIOPATOLOGIA DA REPRODUÇÃO I", 90, {
        "TERÇA": [3, 4],    # Teórica
        "QUARTA": [7],      # Prática A
        "QUARTA": [11],     # Prática B
        "QUINTA": [7, 8],   # Prática C
        "QUINTA": [9, 10]   # Prática D
    }, credits=5)

    add("7ª Fase", "SAUPU", "SAÚDE PÚBLICA VETERINÁRIA", 54, {
        "SÁBADO": [7, 8],   # Teórica
        "SÁBADO": [9],      # Prática A
        "SÁBADO": [10]      # Prática B
    }, credits=3)

    add("7ª Fase", "TECIR", "TÉCNICA CIRÚRGICA", 90, {
        "TERÇA": [9, 10],   # Teórica
        "QUARTA": [1, 2],   # Prática A
        "QUARTA": [3, 4],   # Prática B
        "QUINTA": [1, 2],   # Prática C
        "QUINTA": [3, 4]    # Prática D
    }, credits=5)

    # =========================================================================
    # 8ª FASE
    # =========================================================================
    add("8ª Fase", "AVICU", "AVICULTURA", 54, {
        "QUINTA": [7, 8],   # Teórica
        "QUINTA": [9],      # Prática A
        "QUINTA": [10],     # Prática B
        "QUINTA": [11]      # Prática C
    }, credits=3)

    add("8ª Fase", "BOVLE", "BOVINOCULTURA DE LEITE", 54, {
        "SEGUNDA": [7, 8, 9, 10]
    }, credits=3)

    add("8ª Fase", "CLIEQ", "CLÍNICA MÉDICA DE EQUÍNOS", 90, {
        "TERÇA": [1, 2, 3, 4],  # Teórica
        "SEGUNDA": [1, 2],      # Prática A
        "SEGUNDA": [3, 4],      # Prática B
        "QUINTA": [9, 10],      # Prática C
        "SEXTA": [1, 2]         # Prática D
    }, credits=5)

    add("8ª Fase", "INSP1", "INSPEÇÃO E TECN DE PROD ORIGEM ANIMAL I", 72, {
        "SEGUNDA": [11, 12],    # Teórica
        "TERÇA": [11],          # Prática A
        "TERÇA": [12]           # Prática B
    }, credits=4)

    add("8ª Fase", "OVINO", "OVINOCULTURA", 36, {
        "SÁBADO": [7, 8, 9],    # Teórica
        "SÁBADO": [9],          # Prática A
        "SÁBADO": [10]          # Prática B
    }, credits=2)

    add("8ª Fase", "PACC", "PATOLOGIA E CLÍNICA CIRÚRGICA", 108, {
        "QUINTA": [3, 4, 11],   # Teórica
        "SEXTA": [3, 4, 9, 10], # Teórica
        "SÁBADO": [3, 4],       # Teórica
        "SEGUNDA": [2],         # Prática A
        "QUARTA": [3, 4, 11],   # Prática B
        "QUINTA": [1, 2],       # Prática C
        "SEXTA": [1, 2]         # Prática D
    }, credits=6)

    add("8ª Fase", "SANSU", "SANIDADE SUÍNA", 54, {
        "TERÇA": [7, 8],    # Teórica
        "TERÇA": [9],       # Prática A
        "QUARTA": [7, 8],   # Prática B
        "QUARTA": [8]       # Prática C
    }, credits=3)

    # =========================================================================
    # 9ª FASE
    # =========================================================================
    add("9ª Fase", "CLCG2", "CLÍNICA MÉDICA DE CÃES E GATOS II", 90, {
        "TERÇA": [1, 2],    # Teórica
        "SEGUNDA": [1, 2],  # Prática A
        "SEGUNDA": [3, 4],  # Prática B
        "SEGUNDA": [9, 10], # Prática C
        "QUARTA": [3, 4]    # Prática D
    }, credits=5)

    add("9ª Fase", "DAVES", "DOENÇAS DAS AVES", 72, {
        "SÁBADO": [7, 8, 9, 10],  # Teórica
        "QUINTA": [7, 8],         # Prática A
        "SEXTA": [1, 2],          # Prática B
        "SEXTA": [3, 4]           # Prática C
    }, credits=4)

    add("9ª Fase", "FRIA2", "FISIOPATOLOGIA DA REPRODUÇÃO II", 72, {
        "SÁBADO": [12],     # Teórica
        "QUINTA": [1, 2],   # Prática A
        "QUINTA": [3, 4],   # Prática B
        "SEXTA": [1, 2],    # Prática C
        "SEXTA": [3, 4]     # Prática D
    }, credits=4)

    add("9ª Fase", "INS-2", "INSPEÇÃO E TEC PRODUTOS ORIGEM ANIMAL II", 90, {
        "QUARTA": [1, 2],   # Teórica
        "QUARTA": [3, 4],   # Prática A
        "QUARTA": [7, 8],   # Prática B
        "QUARTA": [9, 10],  # Prática C
        "QUARTA": [12]      # Prática D
    }, credits=5)

    add("9ª Fase", "OBSTE", "OBSTETRÍCIA", 72, {
        "TERÇA": [7, 8],    # Teórica
        "SEGUNDA": [1, 2],  # Prática A
        "SEGUNDA": [3, 4],  # Prática B
        "SEGUNDA": [7, 8],  # Prática C
        "SEGUNDA": [9, 10]  # Prática D
    }, credits=4)

    add("9ª Fase", "TOPTO", "TOXICOLOGIA E PLANTAS TÓXICAS", 36, {
        "TERÇA": [9, 10]
    }, credits=2)

    # ATIVIDADES COMPLEMENTARES (não tem horário)
    add("9ª Fase", "ATCO", "ATIVIDADES COMPLEMENTARES", 396, {}, credits=22, tipo="Atividade")

    # =========================================================================
    # 10ª FASE - ELETIVAS
    # =========================================================================
    add("Eletivas", "AALIM", "ANÁLISE DE ALIMENTOS PARA ANIMAIS", 54, {
        # Horários a definir
    }, credits=3, tipo="Eletiva")

    add("Eletivas", "AGVIR", "AGENTES VIRAIS DE CANINOS E FELINOS", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "ANIMP", "ANIM. PEÇONHENTOS E VEN. INT. MED. VET.", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "AQUAC", "AQUACULTURA", 36, {"SEGUNDA": [11, 12]}, credits=2, tipo="Eletiva")
    add("Eletivas", "BIOMO", "BIOLOGIA MOLECULAR", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "CARDI", "CARDIOLOGIA DE CÃES E GATOS", 36, {"SEXTA": [7, 8]}, credits=2, tipo="Eletiva")
    add("Eletivas", "CINOF", "CINOFILIA E FELINOTECNIA", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "CITOL", "CITOLOGIA DIAGNÓSTICA", 36, {"QUINTA": [4], "SEXTA": [5]}, credits=2, tipo="Eletiva")
    add("Eletivas", "COMPO", "COMPORTAMENTO E BEM ESTAR ANIMAL", 36, {"QUARTA": [7, 8]}, credits=2, tipo="Eletiva")
    add("Eletivas", "CRIA", "CRIAÇÃO DE AVES DE INTERESSE ZOOTÉCNICO", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "DERMA", "DERMATOLOGIA VETERINÁRIA", 36, {"QUINTA": [3], "SEXTA": [4]}, credits=2, tipo="Eletiva")
    add("Eletivas", "EQUIN", "EQUINOCULTURA", 36, {"SEXTA": [7, 8]}, credits=2, tipo="Eletiva")
    add("Eletivas", "ESTC", "ESTÁGIO CURRICULAR SUPERVISIONADO", 486, {"SEGUNDA": [15]}, credits=27, tipo="Estágio(Registro)")
    add("Eletivas", "FISIA", "FISIATRIA VETERINÁRIA", 36, {"TERÇA": [7, 8]}, credits=2, tipo="Eletiva")
    add("Eletivas", "GENET", "GENÉTICA MÉDICA VETERINÁRIA", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "GERAV", "GERENCIAMENTO E PRODUÇÃO AVÍCOLA", 36, {"QUINTA": [7, 8]}, credits=2, tipo="Eletiva")
    add("Eletivas", "GEREL", "GERENCIAMENTO PROD. DE BOVINOS DE LEITE", 54, {}, credits=3, tipo="Eletiva")
    add("Eletivas", "GERSU", "GERENCIAMENTO E PRODUÇÃO DE SUÍNOS", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "INSEM", "INSEMINAÇÃO ARTIFICIAL E ANDROLOGIA", 36, {}, credits=2, tipo="Eletiva")
    add("Eletivas", "LACTI", "LACTICÍNIOS", 36, {"TERÇA": [3, 4]}, credits=2, tipo="Eletiva")
    add("Eletivas", "MANFS", "MANEJO DE FAUNA SILVESTRE", 72, {}, credits=4, tipo="Eletiva")
    add("Eletivas", "MEDAS", "MEDICINA DE ANIMAIS SILVESTRES", 36, {"SEGUNDA": [9, 10]}, credits=2, tipo="Eletiva")
    add("Eletivas", "MICRA", "MICROBIOLOGIA DOS PROD. DE ORIGEM ANIMAL", 36, {"SEXTA": [7, 8]}, credits=2, tipo="Eletiva")
    add("Eletivas", "OFTAL", "OFTALMOLOGIA VETERINARIA", 36, {"QUARTA": [3, 4]}, credits=2, tipo="Eletiva")
    add("Eletivas", "TEMBR", "TEC. P/A PRODUÇÃO DE EMBRIÕES BOVINOS", 36, {}, credits=2, tipo="Eletiva")

    link_theory_to_practicals(catalog)
    return catalog
