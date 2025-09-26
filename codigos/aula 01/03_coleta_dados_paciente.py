# Aula 01 - Atividade Prática 2: Sistema de Coleta de Dados de Paciente
# Coleta e exibição formatada de dados

print("=== SISTEMA DE CADASTRO DE PACIENTE ===\n")

# Coleta de dados do paciente
nome_paciente = input("Digite o nome do paciente: ")
idade_paciente = int(input("Digite a idade do paciente: "))
telefone_paciente = input("Digite o telefone do paciente: ")
email_paciente = input("Digite o email do paciente: ")

# Exibição formatada dos dados
print("\n" + "="*50)
print("           DADOS DO PACIENTE")
print("="*50)
print(f"Nome: {nome_paciente}")
print(f"Idade: {idade_paciente} anos")
print(f"Telefone: {telefone_paciente}")
print(f"Email: {email_paciente}")
print("="*50)

# Informações adicionais
print(f"\nPaciente {nome_paciente} cadastrado com sucesso!")
print(f"Tipo de dados - Nome: {type(nome_paciente)}")
print(f"Tipo de dados - Idade: {type(idade_paciente)}")