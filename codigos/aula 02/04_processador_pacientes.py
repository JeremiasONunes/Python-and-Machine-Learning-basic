# Aula 02 - Atividade Prática 2: Processador de Dados de Múltiplos Pacientes
# Sistema que processa lista de idades e gera estatísticas

print("=== PROCESSADOR DE DADOS DE PACIENTES ===\n")

# Base de dados simulada
pacientes_idades = [25, 34, 18, 67, 45, 12, 56, 23, 78, 41, 29, 15, 62, 38, 19]

print(f"📊 Processando {len(pacientes_idades)} pacientes...")
print(f"Idades: {pacientes_idades}\n")

# Inicialização de variáveis
soma_idades = 0
maior_idade = pacientes_idades[0]
menor_idade = pacientes_idades[0]
criancas = 0
adolescentes = 0
adultos = 0
idosos = 0

# Processamento dos dados
for idade in pacientes_idades:
    # Soma para média
    soma_idades += idade
    
    # Maior e menor idade
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    
    # Classificação por faixa etária
    if idade < 12:
        criancas += 1
    elif idade < 18:
        adolescentes += 1
    elif idade < 60:
        adultos += 1
    else:
        idosos += 1

# Cálculos finais
media_idade = soma_idades / len(pacientes_idades)
total_pacientes = len(pacientes_idades)

# Relatório de estatísticas
print("📈 ESTATÍSTICAS GERAIS:")
print("-" * 40)
print(f"Total de pacientes: {total_pacientes}")
print(f"Média de idade: {media_idade:.1f} anos")
print(f"Maior idade: {maior_idade} anos")
print(f"Menor idade: {menor_idade} anos")

print("\n👥 DISTRIBUIÇÃO POR FAIXA ETÁRIA:")
print("-" * 40)
print(f"Crianças (0-11): {criancas} ({criancas/total_pacientes*100:.1f}%)")
print(f"Adolescentes (12-17): {adolescentes} ({adolescentes/total_pacientes*100:.1f}%)")
print(f"Adultos (18-59): {adultos} ({adultos/total_pacientes*100:.1f}%)")
print(f"Idosos (60+): {idosos} ({idosos/total_pacientes*100:.1f}%)")

# Análise adicional
print("\n🔍 ANÁLISES ADICIONAIS:")
print("-" * 40)

# Pacientes acima da média
acima_media = 0
for idade in pacientes_idades:
    if idade > media_idade:
        acima_media += 1

print(f"Pacientes acima da média: {acima_media}")

# Faixa etária mais comum
faixas = [criancas, adolescentes, adultos, idosos]
nomes_faixas = ["Crianças", "Adolescentes", "Adultos", "Idosos"]
faixa_predominante = nomes_faixas[faixas.index(max(faixas))]

print(f"Faixa etária predominante: {faixa_predominante}")

# Sistema interativo para adicionar paciente
print("\n➕ ADICIONAR NOVO PACIENTE:")
nova_idade = int(input("Digite a idade do novo paciente: "))

# Atualizar estatísticas
pacientes_idades.append(nova_idade)
nova_media = sum(pacientes_idades) / len(pacientes_idades)

print(f"\n✅ Paciente adicionado!")
print(f"Nova média de idade: {nova_media:.1f} anos")
print(f"Total de pacientes: {len(pacientes_idades)}")