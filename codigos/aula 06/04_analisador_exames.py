# Aula 06 - Atividade Prática 2: Analisador Estatístico de Exames Médicos
# Sistema que analisa exames laboratoriais e identifica valores anormais

import numpy as np

print("=== ANALISADOR DE EXAMES LABORATORIAIS ===\n")

# Dados simulados de exames (5 pacientes x 4 exames)
# Colunas: [Glicose, Colesterol, Triglicérides, Hemoglobina]
exames = np.array([
    [95, 180, 120, 14.2],   # Paciente 1 - Normal
    [140, 250, 200, 12.8],  # Paciente 2 - Glicose e colesterol altos
    [85, 160, 90, 15.1],    # Paciente 3 - Normal
    [200, 300, 350, 11.5],  # Paciente 4 - Todos alterados
    [110, 190, 140, 13.8]   # Paciente 5 - Levemente alterado
])

pacientes = ["Ana Silva", "João Santos", "Maria Costa", "Pedro Lima", "Carlos Souza"]
tipos_exame = ["Glicose", "Colesterol", "Triglicérides", "Hemoglobina"]

# Valores de referência (min, max)
referencias = {
    "Glicose": (70, 100),
    "Colesterol": (0, 200),
    "Triglicérides": (0, 150),
    "Hemoglobina": (12.0, 16.0)
}

print("=== DADOS DOS EXAMES ===")
print(f"Total de pacientes: {exames.shape[0]}")
print(f"Tipos de exame: {exames.shape[1]}")

# Estatísticas gerais por exame
print(f"\n=== ESTATÍSTICAS POR EXAME ===")
for i, exame in enumerate(tipos_exame):
    valores = exames[:, i]
    ref_min, ref_max = referencias[exame]
    
    print(f"{exame}:")
    print(f"  Média: {np.mean(valores):.2f}")
    print(f"  Desvio padrão: {np.std(valores):.2f}")
    print(f"  Mínimo: {np.min(valores):.2f}")
    print(f"  Máximo: {np.max(valores):.2f}")
    print(f"  Referência: {ref_min} - {ref_max}")
    print()

# Identificar valores fora do padrão
print("=== ANÁLISE DE VALORES ANORMAIS ===")

for i, exame in enumerate(tipos_exame):
    valores = exames[:, i]
    ref_min, ref_max = referencias[exame]
    
    # Encontrar valores fora da referência
    fora_padrao = (valores < ref_min) | (valores > ref_max)
    pacientes_alterados = np.where(fora_padrao)[0]
    
    if len(pacientes_alterados) > 0:
        print(f"{exame} - Valores alterados:")
        for idx in pacientes_alterados:
            nome = pacientes[idx]
            valor = valores[idx]
            if valor < ref_min:
                status = "BAIXO"
            else:
                status = "ALTO"
            print(f"  {nome}: {valor:.2f} ({status})")
        print()

# Calcular percentis para cada exame
print("=== ANÁLISE DE PERCENTIS ===")
for i, exame in enumerate(tipos_exame):
    valores = exames[:, i]
    
    p25 = np.percentile(valores, 25)
    p50 = np.percentile(valores, 50)  # Mediana
    p75 = np.percentile(valores, 75)
    
    print(f"{exame}:")
    print(f"  25º percentil: {p25:.2f}")
    print(f"  50º percentil: {p50:.2f}")
    print(f"  75º percentil: {p75:.2f}")

# Identificar pacientes com múltiplas alterações
print(f"\n=== PACIENTES COM MÚLTIPLAS ALTERAÇÕES ===")

for i, nome in enumerate(pacientes):
    alteracoes = 0
    detalhes = []
    
    for j, exame in enumerate(tipos_exame):
        valor = exames[i, j]
        ref_min, ref_max = referencias[exame]
        
        if valor < ref_min or valor > ref_max:
            alteracoes += 1
            status = "baixo" if valor < ref_min else "alto"
            detalhes.append(f"{exame} {status}")
    
    if alteracoes > 0:
        print(f"{nome}: {alteracoes} alteração(ões)")
        for detalhe in detalhes:
            print(f"  - {detalhe}")
        print()

# Calcular score de risco (exemplo simples)
print("=== SCORE DE RISCO ===")

for i, nome in enumerate(pacientes):
    score = 0
    
    # Glicose
    if exames[i, 0] > 126:
        score += 3  # Diabetes
    elif exames[i, 0] > 100:
        score += 1  # Pré-diabetes
    
    # Colesterol
    if exames[i, 1] > 240:
        score += 2
    elif exames[i, 1] > 200:
        score += 1
    
    # Triglicérides
    if exames[i, 2] > 200:
        score += 2
    elif exames[i, 2] > 150:
        score += 1
    
    # Hemoglobina
    if exames[i, 3] < 12:
        score += 1
    
    if score == 0:
        risco = "BAIXO"
    elif score <= 2:
        risco = "MODERADO"
    else:
        risco = "ALTO"
    
    print(f"{nome}: Score {score} - Risco {risco}")

print("\n✅ Análise de exames concluída!")