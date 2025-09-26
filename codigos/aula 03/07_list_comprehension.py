# Aula 03 - Tópico 4: List Comprehension
# Demonstração de sintaxe e performance de list comprehension

import time

print("=== LIST COMPREHENSION ===\n")

# Sintaxe básica
print("=== SINTAXE BÁSICA ===")

# Lista tradicional vs comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Método tradicional
quadrados_tradicional = []
for num in numeros:
    quadrados_tradicional.append(num ** 2)

# List comprehension
quadrados_comprehension = [num ** 2 for num in numeros]

print(f"Números: {numeros}")
print(f"Quadrados (tradicional): {quadrados_tradicional}")
print(f"Quadrados (comprehension): {quadrados_comprehension}")

# Com condicionais
print(f"\n=== COM CONDICIONAIS ===")

# Apenas números pares
pares = [num for num in numeros if num % 2 == 0]
print(f"Números pares: {pares}")

# Quadrados apenas dos ímpares
quadrados_impares = [num ** 2 for num in numeros if num % 2 != 0]
print(f"Quadrados dos ímpares: {quadrados_impares}")

# Aplicação com strings
print(f"\n=== COM STRINGS ===")

pacientes = ["Ana Silva", "joão santos", "MARIA COSTA", "pedro lima"]

# Normalizar nomes (primeira letra maiúscula)
nomes_normalizados = [nome.title() for nome in pacientes]
print(f"Nomes normalizados: {nomes_normalizados}")

# Apenas nomes com mais de 8 caracteres
nomes_longos = [nome for nome in nomes_normalizados if len(nome) > 8]
print(f"Nomes longos: {nomes_longos}")

# Primeiros nomes
primeiros_nomes = [nome.split()[0] for nome in nomes_normalizados]
print(f"Primeiros nomes: {primeiros_nomes}")

# Aplicação com dicionários
print(f"\n=== COM DICIONÁRIOS ===")

idades_pacientes = [25, 34, 28, 45, 67, 19, 52]

# Classificar idades
classificacoes = [
    "Jovem" if idade < 30 else "Adulto" if idade < 60 else "Idoso"
    for idade in idades_pacientes
]

print(f"Idades: {idades_pacientes}")
print(f"Classificações: {classificacoes}")

# Criar dicionário com comprehension
pacientes_idades = {
    nome: idade 
    for nome, idade in zip(primeiros_nomes, idades_pacientes)
}
print(f"Dicionário pacientes-idades: {pacientes_idades}")

# Filtrar dicionário
adultos = {
    nome: idade 
    for nome, idade in pacientes_idades.items() 
    if 30 <= idade < 60
}
print(f"Apenas adultos: {adultos}")

# Comprehension aninhada
print(f"\n=== COMPREHENSION ANINHADA ===")

# Matriz de horários (dias x horários)
dias = ["Segunda", "Terça", "Quarta"]
horarios = ["09:00", "14:00", "16:00"]

# Todas as combinações
agenda = [
    f"{dia} às {horario}" 
    for dia in dias 
    for horario in horarios
]

print(f"Agenda completa: {agenda}")

# Matriz 3x3
matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matriz 3x3: {matriz}")

# Achatar matriz
matriz_plana = [elemento for linha in matriz for elemento in linha]
print(f"Matriz plana: {matriz_plana}")

# Comparação de performance
print(f"\n=== COMPARAÇÃO DE PERFORMANCE ===")

# Teste com lista grande
tamanho = 100000

# Método tradicional
inicio = time.time()
resultado_tradicional = []
for i in range(tamanho):
    if i % 2 == 0:
        resultado_tradicional.append(i ** 2)
tempo_tradicional = time.time() - inicio

# List comprehension
inicio = time.time()
resultado_comprehension = [i ** 2 for i in range(tamanho) if i % 2 == 0]
tempo_comprehension = time.time() - inicio

print(f"Processando {tamanho} números:")
print(f"Método tradicional: {tempo_tradicional:.4f} segundos")
print(f"List comprehension: {tempo_comprehension:.4f} segundos")
print(f"Comprehension é {tempo_tradicional/tempo_comprehension:.2f}x mais rápida")

# Casos práticos com dados médicos
print(f"\n=== CASOS PRÁTICOS ===")

# Dados simulados de consultas
consultas = [
    {"paciente": "Ana", "tipo": "Psicologia", "duracao": 60, "valor": 150},
    {"paciente": "João", "tipo": "Psiquiatria", "duracao": 45, "valor": 200},
    {"paciente": "Maria", "tipo": "Terapia", "duracao": 50, "valor": 120},
    {"paciente": "Pedro", "tipo": "Psicologia", "duracao": 60, "valor": 150},
    {"paciente": "Carlos", "tipo": "Psiquiatria", "duracao": 30, "valor": 180}
]

# Extrair apenas nomes dos pacientes
nomes_pacientes = [consulta["paciente"] for consulta in consultas]
print(f"Pacientes: {nomes_pacientes}")

# Consultas de Psicologia
psicologia = [
    consulta["paciente"] 
    for consulta in consultas 
    if consulta["tipo"] == "Psicologia"
]
print(f"Pacientes de Psicologia: {psicologia}")

# Receita total por tipo
tipos_consulta = list(set(consulta["tipo"] for consulta in consultas))
receita_por_tipo = {
    tipo: sum(
        consulta["valor"] 
        for consulta in consultas 
        if consulta["tipo"] == tipo
    )
    for tipo in tipos_consulta
}
print(f"Receita por tipo: {receita_por_tipo}")

# Consultas longas (mais de 45 minutos)
consultas_longas = [
    f"{consulta['paciente']} - {consulta['duracao']}min"
    for consulta in consultas
    if consulta["duracao"] > 45
]
print(f"Consultas longas: {consultas_longas}")

# Set comprehension
print(f"\n=== SET E DICT COMPREHENSION ===")

# Set comprehension - tipos únicos
tipos_unicos = {consulta["tipo"] for consulta in consultas}
print(f"Tipos únicos (set): {tipos_unicos}")

# Dict comprehension - paciente: valor
valores_pacientes = {
    consulta["paciente"]: consulta["valor"]
    for consulta in consultas
}
print(f"Valores por paciente: {valores_pacientes}")

# Generator expression (mais eficiente para grandes datasets)
print(f"\n=== GENERATOR EXPRESSION ===")

# Generator (usa menos memória)
quadrados_generator = (x ** 2 for x in range(10))
print(f"Generator: {quadrados_generator}")
print(f"Valores do generator: {list(quadrados_generator)}")

# Soma usando generator
soma_quadrados = sum(x ** 2 for x in range(1000000))
print(f"Soma dos quadrados (1-1000000): {soma_quadrados}")