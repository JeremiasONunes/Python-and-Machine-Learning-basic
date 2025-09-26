# Aula 01 - Atividade Prática 3: Calculadora de Estatísticas do Paciente
# Cálculos matemáticos aplicados ao contexto clínico

from datetime import datetime

print("=== CALCULADORA DE ESTATÍSTICAS DO PACIENTE ===\n")

# Coleta de dados
nome = input("Nome do paciente: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
ano_nascimento = int(input("Ano de nascimento: "))
ano_inicio_tratamento = int(input("Ano de início do tratamento: "))

# Cálculos
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
imc = peso / (altura ** 2)
tempo_tratamento = ano_atual - ano_inicio_tratamento

# Classificação do IMC
if imc < 18.5:
    classificacao_imc = "Abaixo do peso"
elif imc < 25:
    classificacao_imc = "Peso normal"
elif imc < 30:
    classificacao_imc = "Sobrepeso"
else:
    classificacao_imc = "Obesidade"

# Exibição dos resultados
print("\n" + "="*60)
print("           RELATÓRIO DE ESTATÍSTICAS")
print("="*60)
print(f"Paciente: {nome}")
print(f"Idade atual: {idade} anos")
print(f"IMC: {imc:.2f} ({classificacao_imc})")
print(f"Tempo de tratamento: {tempo_tratamento} anos")
print("="*60)