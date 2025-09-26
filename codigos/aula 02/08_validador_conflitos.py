# Aula 02 - Atividade Prática 4: Validador de Conflitos de Agendamento
# Sistema que identifica conflitos de horário em agendamentos

print("=== VALIDADOR DE CONFLITOS DE AGENDAMENTO ===\n")

# Base de dados de agendamentos
agendamentos = [
    {"id": 1, "paciente": "Ana Silva", "data": "15/03/2024", "horario": "14:00", "duracao": 60},
    {"id": 2, "paciente": "João Santos", "data": "15/03/2024", "horario": "14:30", "duracao": 45},
    {"id": 3, "paciente": "Maria Costa", "data": "15/03/2024", "horario": "16:00", "duracao": 60},
    {"id": 4, "paciente": "Pedro Lima", "data": "16/03/2024", "horario": "09:00", "duracao": 30},
    {"id": 5, "paciente": "Carlos Souza", "data": "15/03/2024", "horario": "15:45", "duracao": 30}
]

def converter_horario_minutos(horario):
    """Converte horário HH:MM para minutos desde 00:00"""
    horas, minutos = map(int, horario.split(':'))
    return horas * 60 + minutos

def verificar_conflito(ag1, ag2):
    """Verifica se dois agendamentos têm conflito de horário"""
    # Só verifica se são na mesma data
    if ag1['data'] != ag2['data']:
        return False
    
    # Converte horários para minutos
    inicio1 = converter_horario_minutos(ag1['horario'])
    fim1 = inicio1 + ag1['duracao']
    
    inicio2 = converter_horario_minutos(ag2['horario'])
    fim2 = inicio2 + ag2['duracao']
    
    # Verifica sobreposição
    return not (fim1 <= inicio2 or fim2 <= inicio1)

def encontrar_conflitos():
    """Encontra todos os conflitos na lista de agendamentos"""
    conflitos = []
    
    for i in range(len(agendamentos)):
        for j in range(i + 1, len(agendamentos)):
            if verificar_conflito(agendamentos[i], agendamentos[j]):
                conflitos.append((agendamentos[i], agendamentos[j]))
    
    return conflitos

def exibir_agendamentos():
    """Exibe todos os agendamentos organizados por data"""
    print("📅 AGENDAMENTOS CADASTRADOS:")
    print("-" * 80)
    
    # Agrupa por data
    por_data = {}
    for ag in agendamentos:
        data = ag['data']
        if data not in por_data:
            por_data[data] = []
        por_data[data].append(ag)
    
    # Exibe organizadamente
    for data, ags in por_data.items():
        print(f"\n📆 {data}:")
        
        # Ordena por horário
        ags_ordenados = sorted(ags, key=lambda x: converter_horario_minutos(x['horario']))
        
        for ag in ags_ordenados:
            fim_minutos = converter_horario_minutos(ag['horario']) + ag['duracao']
            fim_horas = fim_minutos // 60
            fim_mins = fim_minutos % 60
            fim_horario = f"{fim_horas:02d}:{fim_mins:02d}"
            
            print(f"  {ag['horario']}-{fim_horario} | {ag['paciente']} ({ag['duracao']}min)")

def validar_novo_agendamento():
    """Valida um novo agendamento contra conflitos"""
    print("\n➕ VALIDAR NOVO AGENDAMENTO:")
    
    paciente = input("Nome do paciente: ")
    data = input("Data (dd/mm/aaaa): ")
    horario = input("Horário (hh:mm): ")
    duracao = int(input("Duração em minutos: "))
    
    novo_ag = {
        "id": len(agendamentos) + 1,
        "paciente": paciente,
        "data": data,
        "horario": horario,
        "duracao": duracao
    }
    
    # Verifica conflitos com agendamentos existentes
    conflitos_encontrados = []
    for ag_existente in agendamentos:
        if verificar_conflito(novo_ag, ag_existente):
            conflitos_encontrados.append(ag_existente)
    
    if conflitos_encontrados:
        print(f"\n❌ CONFLITO DETECTADO!")
        print(f"O agendamento de {paciente} conflita com:")
        
        for conflito in conflitos_encontrados:
            print(f"  - {conflito['paciente']} ({conflito['horario']} - {conflito['duracao']}min)")
        
        return False
    else:
        print(f"\n✅ Agendamento válido! Sem conflitos detectados.")
        agendamentos.append(novo_ag)
        return True

# Programa principal
exibir_agendamentos()

print("\n🔍 ANÁLISE DE CONFLITOS:")
conflitos = encontrar_conflitos()

if conflitos:
    print(f"❌ Encontrados {len(conflitos)} conflito(s):")
    print("-" * 80)
    
    for i, (ag1, ag2) in enumerate(conflitos, 1):
        print(f"\nConflito {i}:")
        print(f"  • {ag1['paciente']} - {ag1['data']} às {ag1['horario']} ({ag1['duracao']}min)")
        print(f"  • {ag2['paciente']} - {ag2['data']} às {ag2['horario']} ({ag2['duracao']}min)")
else:
    print("✅ Nenhum conflito encontrado!")

# Teste interativo
validar_novo_agendamento()