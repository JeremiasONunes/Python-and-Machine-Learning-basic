# Aula 01 - Desafio para próxima aula: Cálculo de tempo entre datas
# Script para calcular duração de tratamentos

from datetime import datetime, date

print("=== CALCULADORA DE DURAÇÃO DE TRATAMENTO ===\n")

# Entrada de dados
print("📅 Data de início do tratamento:")
dia_inicio = int(input("Dia: "))
mes_inicio = int(input("Mês: "))
ano_inicio = int(input("Ano: "))

print("\n📅 Data de fim do tratamento (ou data atual):")
dia_fim = int(input("Dia: "))
mes_fim = int(input("Mês: "))
ano_fim = int(input("Ano: "))

# Criação das datas
data_inicio = date(ano_inicio, mes_inicio, dia_inicio)
data_fim = date(ano_fim, mes_fim, dia_fim)

# Cálculo da diferença
diferenca = data_fim - data_inicio
dias_totais = diferenca.days

# Conversões
anos = dias_totais // 365
meses = (dias_totais % 365) // 30
dias = (dias_totais % 365) % 30

# Exibição dos resultados
print("\n" + "="*50)
print("        DURAÇÃO DO TRATAMENTO")
print("="*50)
print(f"Data de início: {data_inicio.strftime('%d/%m/%Y')}")
print(f"Data de fim: {data_fim.strftime('%d/%m/%Y')}")
print(f"Total de dias: {dias_totais}")
print(f"Duração: {anos} anos, {meses} meses e {dias} dias")
print("="*50)