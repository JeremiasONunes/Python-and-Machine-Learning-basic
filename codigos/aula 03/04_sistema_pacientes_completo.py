# Aula 03 - Atividade Prática 2: Sistema Completo de Dados de Pacientes
# Estrutura de dados completa usando dicionários aninhados

from datetime import datetime

print("=== SISTEMA COMPLETO DE PACIENTES ===\n")

# Base de dados com dicionários aninhados
pacientes_db = {
    "001": {
        "dados_pessoais": {
            "nome": "Ana Silva",
            "idade": 25,
            "cpf": "123.456.789-00",
            "telefone": "(11) 99999-1111",
            "email": "ana@email.com"
        },
        "endereco": {
            "rua": "Rua das Flores, 123",
            "cidade": "São Paulo",
            "cep": "01234-567"
        },
        "historico_medico": {
            "alergias": ["Dipirona"],
            "medicamentos": ["Ansiolítico"],
            "observacoes": "Paciente com ansiedade"
        },
        "consultas": [
            {"data": "15/03/2024", "tipo": "Psicologia", "status": "Concluída"},
            {"data": "22/03/2024", "tipo": "Psicologia", "status": "Agendada"}
        ]
    },
    "002": {
        "dados_pessoais": {
            "nome": "João Santos",
            "idade": 34,
            "cpf": "987.654.321-00",
            "telefone": "(11) 88888-2222",
            "email": "joao@email.com"
        },
        "endereco": {
            "rua": "Av. Principal, 456",
            "cidade": "São Paulo",
            "cep": "05678-901"
        },
        "historico_medico": {
            "alergias": [],
            "medicamentos": [],
            "observacoes": "Primeira consulta"
        },
        "consultas": [
            {"data": "20/03/2024", "tipo": "Psiquiatria", "status": "Agendada"}
        ]
    }
}

def exibir_paciente(id_paciente):
    """Exibe dados completos de um paciente"""
    if id_paciente not in pacientes_db:
        print(f"❌ Paciente {id_paciente} não encontrado!")
        return
    
    paciente = pacientes_db[id_paciente]
    
    print(f"\n📋 DADOS DO PACIENTE - ID: {id_paciente}")
    print("="*60)
    
    # Dados pessoais
    dados = paciente["dados_pessoais"]
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']} anos")
    print(f"CPF: {dados['cpf']}")
    print(f"Telefone: {dados['telefone']}")
    print(f"Email: {dados['email']}")
    
    # Endereço
    endereco = paciente["endereco"]
    print(f"\n📍 ENDEREÇO:")
    print(f"Rua: {endereco['rua']}")
    print(f"Cidade: {endereco['cidade']}")
    print(f"CEP: {endereco['cep']}")
    
    # Histórico médico
    historico = paciente["historico_medico"]
    print(f"\n🏥 HISTÓRICO MÉDICO:")
    print(f"Alergias: {', '.join(historico['alergias']) if historico['alergias'] else 'Nenhuma'}")
    print(f"Medicamentos: {', '.join(historico['medicamentos']) if historico['medicamentos'] else 'Nenhum'}")
    print(f"Observações: {historico['observacoes']}")
    
    # Consultas
    print(f"\n📅 CONSULTAS ({len(paciente['consultas'])}):")
    for i, consulta in enumerate(paciente["consultas"], 1):
        status_icon = "✅" if consulta["status"] == "Concluída" else "🕐"
        print(f"  {i}. {consulta['data']} - {consulta['tipo']} {status_icon}")

def listar_todos_pacientes():
    """Lista resumo de todos os pacientes"""
    print(f"\n📋 TODOS OS PACIENTES ({len(pacientes_db)}):")
    print("-" * 80)
    
    for id_pac, dados in pacientes_db.items():
        nome = dados["dados_pessoais"]["nome"]
        idade = dados["dados_pessoais"]["idade"]
        consultas = len(dados["consultas"])
        print(f"ID: {id_pac} | {nome} ({idade} anos) | {consultas} consulta(s)")

def cadastrar_paciente():
    """Cadastra novo paciente"""
    print(f"\n➕ CADASTRO DE NOVO PACIENTE")
    
    # Gerar novo ID
    novo_id = str(len(pacientes_db) + 1).zfill(3)
    
    # Coleta dados pessoais
    print(f"\n👤 DADOS PESSOAIS:")
    nome = input("Nome completo: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    # Coleta endereço
    print(f"\n📍 ENDEREÇO:")
    rua = input("Rua e número: ")
    cidade = input("Cidade: ")
    cep = input("CEP: ")
    
    # Coleta histórico
    print(f"\n🏥 HISTÓRICO MÉDICO:")
    alergias = input("Alergias (separadas por vírgula): ").split(",") if input("Tem alergias? (s/n): ").lower() == "s" else []
    medicamentos = input("Medicamentos (separados por vírgula): ").split(",") if input("Usa medicamentos? (s/n): ").lower() == "s" else []
    observacoes = input("Observações: ")
    
    # Criar estrutura do paciente
    novo_paciente = {
        "dados_pessoais": {
            "nome": nome,
            "idade": idade,
            "cpf": cpf,
            "telefone": telefone,
            "email": email
        },
        "endereco": {
            "rua": rua,
            "cidade": cidade,
            "cep": cep
        },
        "historico_medico": {
            "alergias": [a.strip() for a in alergias if a.strip()],
            "medicamentos": [m.strip() for m in medicamentos if m.strip()],
            "observacoes": observacoes
        },
        "consultas": []
    }
    
    pacientes_db[novo_id] = novo_paciente
    print(f"\n✅ Paciente {nome} cadastrado com ID: {novo_id}")

def buscar_pacientes():
    """Busca pacientes por nome"""
    termo = input("\n🔍 Digite o nome ou parte do nome: ").lower()
    
    encontrados = []
    for id_pac, dados in pacientes_db.items():
        nome = dados["dados_pessoais"]["nome"].lower()
        if termo in nome:
            encontrados.append((id_pac, dados["dados_pessoais"]["nome"]))
    
    if encontrados:
        print(f"\n✅ Encontrados {len(encontrados)} paciente(s):")
        for id_pac, nome in encontrados:
            print(f"  ID: {id_pac} - {nome}")
    else:
        print("❌ Nenhum paciente encontrado.")

def estatisticas_gerais():
    """Gera estatísticas do sistema"""
    print(f"\n📊 ESTATÍSTICAS GERAIS:")
    print("-" * 40)
    
    total_pacientes = len(pacientes_db)
    total_consultas = sum(len(p["consultas"]) for p in pacientes_db.values())
    
    # Idades
    idades = [p["dados_pessoais"]["idade"] for p in pacientes_db.values()]
    media_idade = sum(idades) / len(idades) if idades else 0
    
    # Tipos de consulta
    tipos_consulta = {}
    for paciente in pacientes_db.values():
        for consulta in paciente["consultas"]:
            tipo = consulta["tipo"]
            tipos_consulta[tipo] = tipos_consulta.get(tipo, 0) + 1
    
    print(f"Total de pacientes: {total_pacientes}")
    print(f"Total de consultas: {total_consultas}")
    print(f"Média de idade: {media_idade:.1f} anos")
    
    if tipos_consulta:
        print(f"\nTipos de consulta:")
        for tipo, qtd in tipos_consulta.items():
            print(f"  {tipo}: {qtd}")

def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*60)
        print("           SISTEMA COMPLETO DE PACIENTES")
        print("="*60)
        print("1. Listar todos os pacientes")
        print("2. Exibir dados de um paciente")
        print("3. Cadastrar novo paciente")
        print("4. Buscar pacientes")
        print("5. Estatísticas gerais")
        print("6. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == "1":
            listar_todos_pacientes()
        elif opcao == "2":
            id_pac = input("Digite o ID do paciente: ")
            exibir_paciente(id_pac)
        elif opcao == "3":
            cadastrar_paciente()
        elif opcao == "4":
            buscar_pacientes()
        elif opcao == "5":
            estatisticas_gerais()
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