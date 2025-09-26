# Aula 03 - Atividade Prática 1: Gerenciador de Lista de Pacientes
# Sistema CRUD para gerenciar lista de pacientes

print("=== GERENCIADOR DE PACIENTES ===\n")

# Base de dados inicial
pacientes = [
    "Ana Silva",
    "João Santos", 
    "Maria Costa",
    "Pedro Lima",
    "Carlos Souza"
]

def exibir_pacientes():
    """Exibe todos os pacientes cadastrados"""
    print(f"\n📋 PACIENTES CADASTRADOS ({len(pacientes)}):")
    print("-" * 40)
    
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    
    for i, paciente in enumerate(pacientes, 1):
        print(f"{i:2d}. {paciente}")

def adicionar_paciente():
    """Adiciona novo paciente à lista"""
    nome = input("\n➕ Digite o nome do paciente: ").strip()
    
    if nome:
        if nome not in pacientes:
            pacientes.append(nome)
            print(f"✅ {nome} adicionado com sucesso!")
        else:
            print(f"❌ {nome} já está cadastrado!")
    else:
        print("❌ Nome não pode estar vazio!")

def remover_paciente():
    """Remove paciente da lista"""
    if not pacientes:
        print("❌ Não há pacientes para remover.")
        return
    
    exibir_pacientes()
    try:
        indice = int(input("\n🗑️ Digite o número do paciente para remover: ")) - 1
        
        if 0 <= indice < len(pacientes):
            removido = pacientes.pop(indice)
            print(f"✅ {removido} removido com sucesso!")
        else:
            print("❌ Número inválido!")
    except ValueError:
        print("❌ Digite um número válido!")

def buscar_paciente():
    """Busca paciente na lista"""
    termo = input("\n🔍 Digite o nome ou parte do nome: ").lower()
    
    encontrados = []
    for i, paciente in enumerate(pacientes):
        if termo in paciente.lower():
            encontrados.append((i, paciente))
    
    if encontrados:
        print(f"\n✅ Encontrados {len(encontrados)} resultado(s):")
        for i, paciente in encontrados:
            print(f"  {i+1}. {paciente}")
    else:
        print("❌ Nenhum paciente encontrado.")

def ordenar_pacientes():
    """Ordena lista de pacientes"""
    print("\n📊 OPÇÕES DE ORDENAÇÃO:")
    print("1. Ordem alfabética (A-Z)")
    print("2. Ordem alfabética reversa (Z-A)")
    
    opcao = input("Escolha (1-2): ")
    
    if opcao == "1":
        pacientes.sort()
        print("✅ Lista ordenada alfabeticamente!")
    elif opcao == "2":
        pacientes.sort(reverse=True)
        print("✅ Lista ordenada em ordem reversa!")
    else:
        print("❌ Opção inválida!")

def estatisticas():
    """Exibe estatísticas da lista"""
    print(f"\n📈 ESTATÍSTICAS:")
    print(f"Total de pacientes: {len(pacientes)}")
    
    if pacientes:
        print(f"Primeiro paciente: {pacientes[0]}")
        print(f"Último paciente: {pacientes[-1]}")
        
        # Análise de nomes
        nomes_com_silva = [p for p in pacientes if "Silva" in p]
        print(f"Pacientes com 'Silva': {len(nomes_com_silva)}")

def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*50)
        print("        GERENCIADOR DE PACIENTES")
        print("="*50)
        print("1. Listar pacientes")
        print("2. Adicionar paciente")
        print("3. Remover paciente")
        print("4. Buscar paciente")
        print("5. Ordenar lista")
        print("6. Estatísticas")
        print("7. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção (1-7): ")
        
        if opcao == "1":
            exibir_pacientes()
        elif opcao == "2":
            adicionar_paciente()
        elif opcao == "3":
            remover_paciente()
        elif opcao == "4":
            buscar_paciente()
        elif opcao == "5":
            ordenar_pacientes()
        elif opcao == "6":
            estatisticas()
        elif opcao == "7":
            print("\n👋 Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida!")
        
        if opcao != "7":
            input("\nPressione Enter para continuar...")

# Executa o programa
if __name__ == "__main__":
    menu_principal()