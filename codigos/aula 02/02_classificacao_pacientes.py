# Aula 02 - Atividade Prática 1: Sistema de Classificação de Pacientes
# Classificação por faixa etária e prioridade de atendimento

print("=== SISTEMA DE CLASSIFICAÇÃO DE PACIENTES ===\n")

def classificar_paciente(nome, idade, sintomas_graves=False):
    # Classificação por faixa etária
    if idade < 12:
        faixa_etaria = "Criança"
        prioridade_base = 3
    elif idade < 18:
        faixa_etaria = "Adolescente"
        prioridade_base = 2
    elif idade < 60:
        faixa_etaria = "Adulto"
        prioridade_base = 1
    else:
        faixa_etaria = "Idoso"
        prioridade_base = 3
    
    # Determinação da prioridade
    if sintomas_graves:
        prioridade = "URGENTE"
    elif prioridade_base == 3:
        prioridade = "ALTA"
    elif prioridade_base == 2:
        prioridade = "MÉDIA"
    else:
        prioridade = "NORMAL"
    
    return faixa_etaria, prioridade

# Teste do sistema
pacientes = [
    ("Ana Silva", 8, False),
    ("João Santos", 16, True),
    ("Maria Costa", 35, False),
    ("Pedro Oliveira", 70, False),
    ("Carlos Lima", 45, True)
]

print("📋 RELATÓRIO DE CLASSIFICAÇÃO:")
print("-" * 60)

for nome, idade, sintomas in pacientes:
    faixa, prioridade = classificar_paciente(nome, idade, sintomas)
    
    print(f"Paciente: {nome}")
    print(f"Idade: {idade} anos ({faixa})")
    print(f"Sintomas graves: {'Sim' if sintomas else 'Não'}")
    print(f"Prioridade: {prioridade}")
    print("-" * 60)

# Sistema interativo
print("\n🏥 CLASSIFICAÇÃO INTERATIVA:")
nome = input("Nome do paciente: ")
idade = int(input("Idade: "))
sintomas = input("Sintomas graves? (s/n): ").lower() == 's'

faixa, prioridade = classificar_paciente(nome, idade, sintomas)

print(f"\n✅ RESULTADO:")
print(f"Paciente {nome} classificado como {faixa}")
print(f"Prioridade de atendimento: {prioridade}")