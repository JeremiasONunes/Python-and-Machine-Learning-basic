# Aula 06 - Atividade Prática 3: Sistema de Filtros Médicos Avançados
# Filtros para identificar pacientes com múltiplas condições usando indexação booleana

import numpy as np

print("=== SISTEMA DE FILTROS MÉDICOS ===\n")

# Dados simulados de pacientes
# Colunas: [idade, pressão_sistólica, pressão_diastólica, glicose, imc]
dados_pacientes = np.array([
    [25, 120, 80, 95, 22.5],   # Paciente 1 - Normal
    [45, 140, 90, 130, 28.2],  # Paciente 2 - Hipertensão + pré-diabetes
    [67, 160, 95, 180, 31.5],  # Paciente 3 - Hipertensão + diabetes + obesidade
    [34, 115, 75, 88, 24.1],   # Paciente 4 - Normal
    [56, 135, 85, 145, 29.8],  # Paciente 5 - Múltiplas alterações
    [78, 150, 88, 200, 26.7],  # Paciente 6 - Idoso com diabetes
    [29, 125, 82, 102, 25.3],  # Paciente 7 - Levemente alterado
    [52, 145, 92, 165, 32.1]   # Paciente 8 - Múltiplas condições
])

nomes = ["Ana Silva", "João Santos", "Maria Costa", "Pedro Lima", 
         "Carlos Souza", "Rosa Santos", "Lucas Oliveira", "Fernanda Costa"]

print(f"Total de pacientes: {len(dados_pacientes)}")
print(f"Dados por paciente: {dados_pacientes.shape[1]}")

# Definir critérios médicos
print(f"\n=== CRITÉRIOS MÉDICOS ===")
print("- Hipertensão: Pressão ≥ 140/90")
print("- Diabetes: Glicose ≥ 126")
print("- Pré-diabetes: Glicose 100-125")
print("- Obesidade: IMC ≥ 30")
print("- Idoso: Idade ≥ 65")

# Filtro 1: Pacientes com hipertensão
print(f"\n=== FILTRO 1: HIPERTENSÃO ===")
hipertensao = (dados_pacientes[:, 1] >= 140) | (dados_pacientes[:, 2] >= 90)
pacientes_hipertensao = np.where(hipertensao)[0]

print(f"Pacientes com hipertensão: {len(pacientes_hipertensao)}")
for idx in pacientes_hipertensao:
    nome = nomes[idx]
    sistolica = dados_pacientes[idx, 1]
    diastolica = dados_pacientes[idx, 2]
    print(f"  {nome}: {sistolica:.0f}/{diastolica:.0f}")

# Filtro 2: Pacientes com diabetes ou pré-diabetes
print(f"\n=== FILTRO 2: DIABETES/PRÉ-DIABETES ===")
diabetes = dados_pacientes[:, 3] >= 126
pre_diabetes = (dados_pacientes[:, 3] >= 100) & (dados_pacientes[:, 3] < 126)

print("Diabetes:")
for idx in np.where(diabetes)[0]:
    nome = nomes[idx]
    glicose = dados_pacientes[idx, 3]
    print(f"  {nome}: Glicose {glicose:.0f}")

print("Pré-diabetes:")
for idx in np.where(pre_diabetes)[0]:
    nome = nomes[idx]
    glicose = dados_pacientes[idx, 3]
    print(f"  {nome}: Glicose {glicose:.0f}")

# Filtro 3: Pacientes obesos
print(f"\n=== FILTRO 3: OBESIDADE ===")
obesidade = dados_pacientes[:, 4] >= 30
pacientes_obesos = np.where(obesidade)[0]

print(f"Pacientes obesos: {len(pacientes_obesos)}")
for idx in pacientes_obesos:
    nome = nomes[idx]
    imc = dados_pacientes[idx, 4]
    print(f"  {nome}: IMC {imc:.1f}")

# Filtro 4: Pacientes idosos
print(f"\n=== FILTRO 4: IDOSOS ===")
idosos = dados_pacientes[:, 0] >= 65
pacientes_idosos = np.where(idosos)[0]

print(f"Pacientes idosos: {len(pacientes_idosos)}")
for idx in pacientes_idosos:
    nome = nomes[idx]
    idade = dados_pacientes[idx, 0]
    print(f"  {nome}: {idade:.0f} anos")

# Filtro combinado: Alto risco (múltiplas condições)
print(f"\n=== FILTRO COMBINADO: ALTO RISCO ===")
alto_risco = hipertensao & (diabetes | obesidade)
pacientes_alto_risco = np.where(alto_risco)[0]

print(f"Pacientes de alto risco: {len(pacientes_alto_risco)}")
for idx in pacientes_alto_risco:
    nome = nomes[idx]
    idade = dados_pacientes[idx, 0]
    pressao = f"{dados_pacientes[idx, 1]:.0f}/{dados_pacientes[idx, 2]:.0f}"
    glicose = dados_pacientes[idx, 3]
    imc = dados_pacientes[idx, 4]
    
    print(f"  {nome} ({idade:.0f} anos):")
    print(f"    Pressão: {pressao}")
    print(f"    Glicose: {glicose:.0f}")
    print(f"    IMC: {imc:.1f}")

# Estatísticas por grupo de risco
print(f"\n=== ESTATÍSTICAS POR GRUPO ===")

grupos = {
    "Normal": ~(hipertensao | diabetes | obesidade | idosos),
    "Hipertensão": hipertensao & ~diabetes & ~obesidade,
    "Diabetes": diabetes & ~hipertensao & ~obesidade,
    "Alto Risco": alto_risco
}

for grupo, condicao in grupos.items():
    count = np.sum(condicao)
    if count > 0:
        idades_grupo = dados_pacientes[condicao, 0]
        idade_media = np.mean(idades_grupo)
        print(f"{grupo}: {count} pacientes (idade média: {idade_media:.1f})")

# Filtro personalizado: Pacientes que precisam de acompanhamento
print(f"\n=== ACOMPANHAMENTO NECESSÁRIO ===")
acompanhamento = (dados_pacientes[:, 0] > 50) & (hipertensao | pre_diabetes | (dados_pacientes[:, 4] > 27))
pacientes_acompanhamento = np.where(acompanhamento)[0]

print(f"Pacientes que precisam de acompanhamento: {len(pacientes_acompanhamento)}")
for idx in pacientes_acompanhamento:
    nome = nomes[idx]
    print(f"  {nome}")

print("\n✅ Sistema de filtros médicos implementado!")