# Aula 03 - Atividade Prática 3: Sistema de Horários e Especialidades
# Uso de tuplas para horários fixos e conjuntos para especialidades

print("=== SISTEMA DE HORÁRIOS E ESPECIALIDADES ===\n")

# Configurações fixas usando tuplas (imutáveis)
HORARIOS_DISPONIVEIS = (
    (8, 0),   # 08:00
    (9, 0),   # 09:00
    (10, 0),  # 10:00
    (11, 0),  # 11:00
    (14, 0),  # 14:00
    (15, 0),  # 15:00
    (16, 0),  # 16:00
    (17, 0)   # 17:00
)

DIAS_SEMANA = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

# Especialidades usando conjuntos
especialidades_clinica = {
    "Psicologia", 
    "Psiquiatria", 
    "Terapia Familiar", 
    "Neuropsicologia",
    "Terapia Cognitiva"
}

# Médicos e suas especialidades
medicos_especialidades = {
    "Dr. Silva": {"Psicologia", "Terapia Cognitiva"},
    "Dra. Costa": {"Psiquiatria", "Neuropsicologia"},
    "Dr. Santos": {"Terapia Familiar", "Psicologia"},
    "Dra. Lima": {"Psiquiatria"},
    "Dr. Ferreira": {"Neuropsicologia", "Terapia Cognitiva"}
}

# Disponibilidade por dia (usando conjuntos para facilitar operações)
disponibilidade_medicos = {
    "Segunda": {"Dr. Silva", "Dra. Costa", "Dr. Santos"},
    "Terça": {"Dra. Costa", "Dr. Santos", "Dra. Lima"},
    "Quarta": {"Dr. Silva", "Dra. Lima", "Dr. Ferreira"},
    "Quinta": {"Dr. Silva", "Dra. Costa", "Dr. Ferreira"},
    "Sexta": {"Dr. Santos", "Dra. Lima", "Dr. Ferreira"}
}

def formatar_horario(hora_tupla):
    """Converte tupla (hora, minuto) para string formatada"""
    hora, minuto = hora_tupla
    return f"{hora:02d}:{minuto:02d}"

def exibir_horarios_disponiveis():
    """Exibe todos os horários disponíveis"""
    print("🕐 HORÁRIOS DISPONÍVEIS:")
    print("-" * 30)
    
    for i, horario in enumerate(HORARIOS_DISPONIVEIS, 1):
        print(f"{i}. {formatar_horario(horario)}")

def exibir_especialidades():
    """Exibe todas as especialidades da clínica"""
    print(f"\n🏥 ESPECIALIDADES DISPONÍVEIS ({len(especialidades_clinica)}):")
    print("-" * 40)
    
    for i, especialidade in enumerate(sorted(especialidades_clinica), 1):
        print(f"{i}. {especialidade}")

def buscar_medicos_por_especialidade(especialidade):
    """Busca médicos que atendem uma especialidade específica"""
    medicos_encontrados = set()
    
    for medico, especialidades in medicos_especialidades.items():
        if especialidade in especialidades:
            medicos_encontrados.add(medico)
    
    return medicos_encontrados

def verificar_disponibilidade_dia(dia, especialidade):
    """Verifica quais médicos estão disponíveis em um dia para uma especialidade"""
    if dia not in disponibilidade_medicos:
        return set()
    
    medicos_dia = disponibilidade_medicos[dia]
    medicos_especialidade = buscar_medicos_por_especialidade(especialidade)
    
    # Interseção: médicos que estão disponíveis E atendem a especialidade
    disponiveis = medicos_dia & medicos_especialidade
    
    return disponiveis

def exibir_agenda_completa():
    """Exibe agenda completa da semana"""
    print(f"\n📅 AGENDA SEMANAL COMPLETA:")
    print("=" * 80)
    
    for dia in DIAS_SEMANA:
        print(f"\n📆 {dia.upper()}:")
        medicos_dia = disponibilidade_medicos.get(dia, set())
        
        if not medicos_dia:
            print("  Nenhum médico disponível")
            continue
        
        for medico in sorted(medicos_dia):
            especialidades = medicos_especialidades.get(medico, set())
            esp_str = ", ".join(sorted(especialidades))
            print(f"  👨‍⚕️ {medico} - {esp_str}")

def buscar_horario_especialidade():
    """Sistema interativo para buscar horários por especialidade"""
    print(f"\n🔍 BUSCA POR ESPECIALIDADE:")
    
    # Exibe especialidades disponíveis
    especialidades_lista = sorted(especialidades_clinica)
    for i, esp in enumerate(especialidades_lista, 1):
        print(f"{i}. {esp}")
    
    try:
        escolha = int(input(f"\nEscolha uma especialidade (1-{len(especialidades_lista)}): ")) - 1
        
        if 0 <= escolha < len(especialidades_lista):
            especialidade_escolhida = especialidades_lista[escolha]
            
            print(f"\n📋 DISPONIBILIDADE PARA {especialidade_escolhida.upper()}:")
            print("-" * 60)
            
            for dia in DIAS_SEMANA:
                medicos_disponiveis = verificar_disponibilidade_dia(dia, especialidade_escolhida)
                
                if medicos_disponiveis:
                    print(f"\n📆 {dia}:")
                    for medico in sorted(medicos_disponiveis):
                        print(f"  👨‍⚕️ {medico}")
                        print(f"    Horários: {', '.join(formatar_horario(h) for h in HORARIOS_DISPONIVEIS)}")
                else:
                    print(f"\n📆 {dia}: Nenhum médico disponível")
        else:
            print("❌ Opção inválida!")
    
    except ValueError:
        print("❌ Digite um número válido!")

def estatisticas_sistema():
    """Gera estatísticas do sistema"""
    print(f"\n📊 ESTATÍSTICAS DO SISTEMA:")
    print("-" * 50)
    
    # Estatísticas gerais
    total_medicos = len(medicos_especialidades)
    total_especialidades = len(especialidades_clinica)
    total_horarios = len(HORARIOS_DISPONIVEIS)
    
    print(f"Total de médicos: {total_medicos}")
    print(f"Total de especialidades: {total_especialidades}")
    print(f"Horários por dia: {total_horarios}")
    print(f"Dias de funcionamento: {len(DIAS_SEMANA)}")
    
    # Especialidade mais comum
    contador_especialidades = {}
    for especialidades in medicos_especialidades.values():
        for esp in especialidades:
            contador_especialidades[esp] = contador_especialidades.get(esp, 0) + 1
    
    if contador_especialidades:
        esp_mais_comum = max(contador_especialidades, key=contador_especialidades.get)
        print(f"\nEspecialidade com mais médicos: {esp_mais_comum} ({contador_especialidades[esp_mais_comum]} médicos)")
    
    # Dia com mais médicos
    medicos_por_dia = {dia: len(medicos) for dia, medicos in disponibilidade_medicos.items()}
    dia_mais_movimentado = max(medicos_por_dia, key=medicos_por_dia.get)
    
    print(f"Dia mais movimentado: {dia_mais_movimentado} ({medicos_por_dia[dia_mais_movimentado]} médicos)")

def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*60)
        print("        SISTEMA DE HORÁRIOS E ESPECIALIDADES")
        print("="*60)
        print("1. Ver horários disponíveis")
        print("2. Ver especialidades")
        print("3. Buscar por especialidade")
        print("4. Ver agenda completa")
        print("5. Estatísticas do sistema")
        print("6. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == "1":
            exibir_horarios_disponiveis()
        elif opcao == "2":
            exibir_especialidades()
        elif opcao == "3":
            buscar_horario_especialidade()
        elif opcao == "4":
            exibir_agenda_completa()
        elif opcao == "5":
            estatisticas_sistema()
        elif opcao == "6":
            print("\n👋 Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida!")
        
        if opcao != "6":
            input("\nPressione Enter para continuar...")

# Executa o programa
if __name__ == "__main__":
    menu_principal()