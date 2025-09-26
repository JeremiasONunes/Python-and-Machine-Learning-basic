# Aula 06 - Atividade Prática 1: Sistema de Dados Vitais com NumPy
# Armazenamento e organização de medições médicas usando arrays

import numpy as np

print("=== SISTEMA DE DADOS VITAIS ===\n")

# Simulação de dados vitais de 5 pacientes
# Cada linha = um paciente, colunas = [pressão_sistólica, pressão_diastólica, temperatura, peso]

# Criação dos dados
dados_vitais = np.array([
    [120, 80, 36.5, 70.2],  # Paciente 1
    [130, 85, 37.1, 68.5],  # Paciente 2
    [110, 75, 36.8, 72.0],  # Paciente 3
    [140, 90, 36.2, 75.5],  # Paciente 4
    [125, 82, 37.0, 69.8]   # Paciente 5
])

nomes_pacientes = ["Ana Silva", "João Santos", "Maria Costa", "Pedro Lima", "Carlos Souza"]
medidas = ["Pressão Sistólica", "Pressão Diastólica", "Temperatura", "Peso"]

print("=== DADOS COLETADOS ===")
print(f"Shape dos dados: {dados_vitais.shape}")
print(f"Total de pacientes: {dados_vitais.shape[0]}")
print(f"Medições por paciente: {dados_vitais.shape[1]}")

# Exibir dados organizados
print(f"\n=== MEDIÇÕES POR PACIENTE ===")
for i, nome in enumerate(nomes_pacientes):
    print(f"{nome}:")
    for j, medida in enumerate(medidas):
        valor = dados_vitais[i, j]
        print(f"  {medida}: {valor}")
    print()

# Análise por tipo de medição
print("=== ANÁLISE POR MEDIÇÃO ===")
for j, medida in enumerate(medidas):
    coluna = dados_vitais[:, j]  # Pega toda a coluna j
    print(f"{medida}:")
    print(f"  Média: {coluna.mean():.2f}")
    print(f"  Mínimo: {coluna.min():.2f}")
    print(f"  Máximo: {coluna.max():.2f}")
    print()

# Identificar valores anormais (exemplo simples)
print("=== VALORES ANORMAIS ===")

# Pressão alta (sistólica > 130 ou diastólica > 85)
pressao_alta = (dados_vitais[:, 0] > 130) | (dados_vitais[:, 1] > 85)
pacientes_pressao_alta = np.where(pressao_alta)[0]

print("Pacientes com pressão alta:")
for idx in pacientes_pressao_alta:
    nome = nomes_pacientes[idx]
    sistolica = dados_vitais[idx, 0]
    diastolica = dados_vitais[idx, 1]
    print(f"  {nome}: {sistolica}/{diastolica}")

# Febre (temperatura > 37.0)
febre = dados_vitais[:, 2] > 37.0
pacientes_febre = np.where(febre)[0]

print(f"\nPacientes com febre:")
for idx in pacientes_febre:
    nome = nomes_pacientes[idx]
    temp = dados_vitais[idx, 2]
    print(f"  {nome}: {temp}°C")

# Adicionar novos dados
print(f"\n=== ADICIONANDO NOVO PACIENTE ===")
novo_paciente = np.array([[115, 78, 36.7, 71.2]])
dados_atualizados = np.vstack([dados_vitais, novo_paciente])

print(f"Dados anteriores: {dados_vitais.shape}")
print(f"Dados atualizados: {dados_atualizados.shape}")

# Calcular IMC (peso / altura²) - assumindo altura fixa para simplicidade
alturas = np.array([1.65, 1.78, 1.62, 1.80, 1.75, 1.70])  # Incluindo novo paciente
pesos = dados_atualizados[:, 3]
imc = pesos / (alturas ** 2)

print(f"\n=== CÁLCULO DE IMC ===")
nomes_completos = nomes_pacientes + ["Novo Paciente"]
for i, nome in enumerate(nomes_completos):
    print(f"{nome}: IMC = {imc[i]:.2f}")

# Estatísticas gerais
print(f"\n=== ESTATÍSTICAS GERAIS ===")
print(f"IMC médio: {imc.mean():.2f}")
print(f"Temperatura média: {dados_atualizados[:, 2].mean():.2f}°C")
print(f"Peso médio: {dados_atualizados[:, 3].mean():.2f} kg")

print("\n✅ Sistema de dados vitais implementado!")