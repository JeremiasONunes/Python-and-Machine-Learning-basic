# Aula 06 - Atividade Prática 4: Analisador de Evolução Temporal
# Sistema para analisar evolução dos sinais vitais usando arrays multidimensionais

import numpy as np

print("=== ANALISADOR DE EVOLUÇÃO TEMPORAL ===\n")

# Simulação de dados temporais de sinais vitais
# Dimensões: (pacientes, dias, medições)
# Medições: [pressão_sistólica, pressão_diastólica, frequência_cardíaca, temperatura]

np.random.seed(42)  # Para resultados reproduzíveis

# 3 pacientes, 7 dias, 4 medições por dia
dados_temporais = np.array([
    # Paciente 1 - Estável
    [[120, 80, 72, 36.5], [118, 78, 70, 36.4], [122, 82, 74, 36.6],
     [119, 79, 71, 36.5], [121, 81, 73, 36.5], [120, 80, 72, 36.4],
     [118, 78, 70, 36.6]],
    
    # Paciente 2 - Melhora gradual
    [[140, 90, 85, 37.2], [138, 88, 83, 37.0], [135, 85, 80, 36.8],
     [132, 82, 78, 36.7], [130, 80, 75, 36.6], [128, 78, 73, 36.5],
     [125, 76, 70, 36.5]],
    
    # Paciente 3 - Piora
    [[125, 82, 75, 36.6], [128, 85, 78, 36.8], [132, 88, 82, 37.0],
     [135, 90, 85, 37.2], [138, 92, 88, 37.4], [142, 95, 92, 37.6],
     [145, 98, 95, 37.8]]
])

pacientes = ["Ana Silva", "João Santos", "Maria Costa"]
medidas = ["Pressão Sistólica", "Pressão Diastólica", "Freq. Cardíaca", "Temperatura"]
dias = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"]

print(f"Dados coletados: {dados_temporais.shape}")
print(f"Pacientes: {dados_temporais.shape[0]}")
print(f"Dias de monitoramento: {dados_temporais.shape[1]}")
print(f"Medições por dia: {dados_temporais.shape[2]}")

# Análise por paciente
print(f"\n=== EVOLUÇÃO POR PACIENTE ===")

for p, nome in enumerate(pacientes):
    print(f"\n{nome}:")
    
    # Dados do paciente (7 dias x 4 medições)
    dados_paciente = dados_temporais[p, :, :]
    
    # Calcular tendências (diferença entre último e primeiro dia)
    primeiro_dia = dados_paciente[0, :]
    ultimo_dia = dados_paciente[-1, :]
    tendencia = ultimo_dia - primeiro_dia
    
    for m, medida in enumerate(medidas):
        valor_inicial = primeiro_dia[m]
        valor_final = ultimo_dia[m]
        mudanca = tendencia[m]
        
        if abs(mudanca) < 1:
            status = "ESTÁVEL"
        elif mudanca > 0:
            status = "AUMENTOU"
        else:
            status = "DIMINUIU"
        
        print(f"  {medida}: {valor_inicial:.1f} → {valor_final:.1f} ({status})")

# Análise estatística temporal
print(f"\n=== ESTATÍSTICAS TEMPORAIS ===")

for m, medida in enumerate(medidas):
    print(f"\n{medida}:")
    
    # Extrair dados de todos os pacientes para esta medição
    dados_medida = dados_temporais[:, :, m]  # (3 pacientes x 7 dias)
    
    # Estatísticas por dia (média entre pacientes)
    media_por_dia = np.mean(dados_medida, axis=0)
    
    print(f"  Média por dia: {media_por_dia}")
    print(f"  Tendência geral: {media_por_dia[-1] - media_por_dia[0]:.2f}")

# Identificar dias críticos
print(f"\n=== DIAS CRÍTICOS ===")

for p, nome in enumerate(pacientes):
    print(f"\n{nome}:")
    
    dados_paciente = dados_temporais[p, :, :]
    
    for d in range(len(dias)):
        # Verificar se alguma medição está fora do normal
        pressao_sys = dados_paciente[d, 0]
        pressao_dia = dados_paciente[d, 1]
        freq_card = dados_paciente[d, 2]
        temperatura = dados_paciente[d, 3]
        
        alertas = []
        
        if pressao_sys > 140 or pressao_dia > 90:
            alertas.append("Hipertensão")
        
        if freq_card > 90:
            alertas.append("Taquicardia")
        
        if temperatura > 37.0:
            alertas.append("Febre")
        
        if alertas:
            print(f"  {dias[d]}: {', '.join(alertas)}")

# Calcular variabilidade (desvio padrão ao longo do tempo)
print(f"\n=== VARIABILIDADE TEMPORAL ===")

for p, nome in enumerate(pacientes):
    print(f"\n{nome}:")
    
    dados_paciente = dados_temporais[p, :, :]
    
    for m, medida in enumerate(medidas):
        valores_tempo = dados_paciente[:, m]
        variabilidade = np.std(valores_tempo)
        
        if variabilidade < 2:
            estabilidade = "MUITO ESTÁVEL"
        elif variabilidade < 5:
            estabilidade = "ESTÁVEL"
        else:
            estabilidade = "INSTÁVEL"
        
        print(f"  {medida}: σ={variabilidade:.2f} ({estabilidade})")

# Comparação entre pacientes
print(f"\n=== COMPARAÇÃO ENTRE PACIENTES ===")

# Média geral de cada paciente ao longo dos 7 dias
for m, medida in enumerate(medidas):
    print(f"\n{medida} - Média dos 7 dias:")
    
    for p, nome in enumerate(pacientes):
        media_paciente = np.mean(dados_temporais[p, :, m])
        print(f"  {nome}: {media_paciente:.2f}")

# Identificar paciente com maior melhora/piora
print(f"\n=== RANKING DE EVOLUÇÃO ===")

for m, medida in enumerate(medidas):
    print(f"\n{medida}:")
    
    evolucoes = []
    for p, nome in enumerate(pacientes):
        primeiro = dados_temporais[p, 0, m]
        ultimo = dados_temporais[p, -1, m]
        evolucao = ultimo - primeiro
        evolucoes.append((nome, evolucao))
    
    # Ordenar por evolução
    evolucoes.sort(key=lambda x: x[1])
    
    print(f"  Maior melhora: {evolucoes[0][0]} ({evolucoes[0][1]:+.1f})")
    print(f"  Maior piora: {evolucoes[-1][0]} ({evolucoes[-1][1]:+.1f})")

print("\n✅ Análise temporal concluída!")