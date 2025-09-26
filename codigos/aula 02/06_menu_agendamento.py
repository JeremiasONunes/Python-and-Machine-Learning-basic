# Aula 02 - Atividade Prática 3: Menu Interativo do Sistema de Agendamento
# Interface de menu usando while para sistema de agendamento

print("=== SISTEMA LUNYSSE - AGENDAMENTOS ===\n")

# Base de dados simulada
agendamentos = [
    {"paciente": "Ana Silva", "data": "15/03/2024", "horario": "14:00"},
    {"paciente": "João Santos", "data": "15/03/2024", "horario": "15:30"},
    {"paciente": "Maria Costa", "data": "16/03/2024", "horario": "09:00"}
]

def exibir_menu():
    print("\n" + "="*50)
    print("           MENU DE AGENDAMENTOS")
    print("="*50)
    print("1. Cadastrar agendamento")
    print("2. Listar agendamentos")
    print("3. Buscar agendamento")
    print("4. Remover agendamento")
    print("5. Sair")
    print("="*50)

def cadastrar_agendamento():
    print("\n📅 NOVO AGENDAMENTO:")
    paciente = input("Nome do paciente: ")
    data = input("Data (dd/mm/aaaa): ")
    horario = input("Horário (hh:mm): ")
    
    novo_agendamento = {
        "paciente": paciente,
        "data": data,
        "horario": horario
    }
    
    agendamentos.append(novo_agendamento)
    print(f"✅ Agendamento para {paciente} cadastrado com sucesso!")

def listar_agendamentos():
    print(f"\n📋 AGENDAMENTOS CADASTRADOS ({len(agendamentos)}):")
    print("-" * 60)
    
    if not agendamentos:
        print("Nenhum agendamento encontrado.")
        return
    
    for i, agendamento in enumerate(agendamentos, 1):
        print(f"{i}. Paciente: {agendamento['paciente']}")
        print(f"   Data: {agendamento['data']} às {agendamento['horario']}")
        print("-" * 60)

def buscar_agendamento():
    print("\n🔍 BUSCAR AGENDAMENTO:")
    nome_busca = input("Digite o nome do paciente: ").lower()
    
    encontrados = []
    for agendamento in agendamentos:
        if nome_busca in agendamento['paciente'].lower():
            encontrados.append(agendamento)
    
    if encontrados:
        print(f"\n✅ Encontrados {len(encontrados)} agendamento(s):")
        for agendamento in encontrados:
            print(f"- {agendamento['paciente']} em {agendamento['data']} às {agendamento['horario']}")
    else:
        print("❌ Nenhum agendamento encontrado.")

def remover_agendamento():
    if not agendamentos:
        print("❌ Não há agendamentos para remover.")
        return
    
    listar_agendamentos()
    try:
        indice = int(input("\nDigite o número do agendamento para remover: ")) - 1
        if 0 <= indice < len(agendamentos):
            removido = agendamentos.pop(indice)
            print(f"✅ Agendamento de {removido['paciente']} removido com sucesso!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Digite um número válido.")

# Loop principal do menu
opcao = ""
while opcao != "5":
    exibir_menu()
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == "1":
        cadastrar_agendamento()
    elif opcao == "2":
        listar_agendamentos()
    elif opcao == "3":
        buscar_agendamento()
    elif opcao == "4":
        remover_agendamento()
    elif opcao == "5":
        print("\n👋 Encerrando sistema...")
        print("Obrigado por usar o Sistema Lunysse!")
    else:
        print("❌ Opção inválida! Tente novamente.")
    
    if opcao != "5":
        input("\nPressione Enter para continuar...")

print("\n✅ Sistema encerrado com sucesso!")