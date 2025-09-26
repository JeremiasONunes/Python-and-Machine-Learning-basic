# Aula 06 - Desafio: Detecção de Anomalias em Sinais Vitais
# Algoritmo simples para detectar anomalias usando apenas NumPy

import numpy as np

print("=== DETECTOR DE ANOMALIAS ===\n")

# Simulação de sinais vitais com algumas anomalias
np.random.seed(42)

# Gerar dados normais + algumas anomalias
dias = 30
sinais_normais = {
    "pressao_sistolica": np.random.normal(120, 10, dias),
    "pressao_diastolica": np.random.normal(80, 8, dias),
    "frequencia_cardiaca": np.random.normal(72, 12, dias),
    "temperatura": np.random.normal(36.5, 0.3, dias)
}

# Inserir algumas anomalias intencionais
sinais_normais["pressao_sistolica"][5] = 180  # Pico de pressão
sinais_normais["pressao_sistolica"][15] = 90   # Pressão muito baixa
sinais_normais["frequencia_cardiaca"][10] = 120  # Taquicardia
sinais_normais["temperatura"][20] = 38.5        # Febre

print("=== DADOS COLETADOS ===")
for sinal, valores in sinais_normais.items():
    print(f"{sinal}: {len(valores)} medições")

# Método 1: Detecção por Z-Score
print(f"\n=== MÉTODO 1: Z-SCORE ===")
print("Anomalia se |z-score| > 2")

def detectar_anomalias_zscore(dados, threshold=2):
    """Detecta anomalias usando z-score"""
    media = np.mean(dados)
    desvio = np.std(dados)
    z_scores = np.abs((dados - media) / desvio)
    anomalias = z_scores > threshold
    return anomalias, z_scores

for sinal, valores in sinais_normais.items():
    anomalias, z_scores = detectar_anomalias_zscore(valores)
    indices_anomalias = np.where(anomalias)[0]
    
    print(f"\n{sinal}:")
    print(f"  Média: {np.mean(valores):.2f}")
    print(f"  Desvio: {np.std(valores):.2f}")
    
    if len(indices_anomalias) > 0:
        print(f"  Anomalias encontradas: {len(indices_anomalias)}")
        for idx in indices_anomalias:
            valor = valores[idx]
            z_score = z_scores[idx]
            print(f"    Dia {idx+1}: {valor:.2f} (z-score: {z_score:.2f})")
    else:
        print("  Nenhuma anomalia detectada")

# Método 2: Detecção por Percentis (IQR)
print(f"\n=== MÉTODO 2: PERCENTIS (IQR) ===")
print("Anomalia se valor < Q1-1.5*IQR ou valor > Q3+1.5*IQR")

def detectar_anomalias_iqr(dados):
    """Detecta anomalias usando método IQR"""
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    anomalias = (dados < limite_inferior) | (dados > limite_superior)
    return anomalias, limite_inferior, limite_superior

for sinal, valores in sinais_normais.items():
    anomalias, lim_inf, lim_sup = detectar_anomalias_iqr(valores)
    indices_anomalias = np.where(anomalias)[0]
    
    print(f"\n{sinal}:")
    print(f"  Limites: {lim_inf:.2f} - {lim_sup:.2f}")
    
    if len(indices_anomalias) > 0:
        print(f"  Anomalias encontradas: {len(indices_anomalias)}")
        for idx in indices_anomalias:
            valor = valores[idx]
            tipo = "BAIXO" if valor < lim_inf else "ALTO"
            print(f"    Dia {idx+1}: {valor:.2f} ({tipo})")
    else:
        print("  Nenhuma anomalia detectada")

# Método 3: Detecção por Mudança Súbita
print(f"\n=== MÉTODO 3: MUDANÇA SÚBITA ===")
print("Anomalia se mudança > 2 * desvio padrão das diferenças")

def detectar_mudancas_subitas(dados, threshold=2):
    """Detecta mudanças súbitas entre medições consecutivas"""
    diferencas = np.diff(dados)
    desvio_dif = np.std(diferencas)
    mudancas_grandes = np.abs(diferencas) > threshold * desvio_dif
    
    # Índices ajustados (diff reduz o array em 1)
    indices_mudancas = np.where(mudancas_grandes)[0] + 1
    return indices_mudancas, diferencas

for sinal, valores in sinais_normais.items():
    indices_mudancas, diferencas = detectar_mudancas_subitas(valores)
    
    print(f"\n{sinal}:")
    print(f"  Desvio das diferenças: {np.std(diferencas):.2f}")
    
    if len(indices_mudancas) > 0:
        print(f"  Mudanças súbitas: {len(indices_mudancas)}")
        for idx in indices_mudancas:
            valor_anterior = valores[idx-1]
            valor_atual = valores[idx]
            mudanca = valor_atual - valor_anterior
            print(f"    Dia {idx}: {valor_anterior:.2f} → {valor_atual:.2f} (Δ{mudanca:+.2f})")
    else:
        print("  Nenhuma mudança súbita detectada")

# Resumo consolidado
print(f"\n=== RESUMO CONSOLIDADO ===")

for sinal, valores in sinais_normais.items():
    print(f"\n{sinal}:")
    
    # Aplicar todos os métodos
    anom_zscore, _ = detectar_anomalias_zscore(valores)
    anom_iqr, _, _ = detectar_anomalias_iqr(valores)
    mudancas, _ = detectar_mudancas_subitas(valores)
    
    # Consolidar anomalias
    anomalias_consolidadas = set()
    anomalias_consolidadas.update(np.where(anom_zscore)[0])
    anomalias_consolidadas.update(np.where(anom_iqr)[0])
    anomalias_consolidadas.update(mudancas)
    
    if anomalias_consolidadas:
        print(f"  Dias com anomalias: {sorted(list(anomalias_consolidadas))}")
        
        # Classificar severidade
        for dia in sorted(anomalias_consolidadas):
            valor = valores[dia]
            metodos = []
            
            if anom_zscore[dia]:
                metodos.append("Z-Score")
            if anom_iqr[dia]:
                metodos.append("IQR")
            if dia in mudancas:
                metodos.append("Mudança")
            
            severidade = "ALTA" if len(metodos) > 1 else "MÉDIA"
            print(f"    Dia {dia+1}: {valor:.2f} - {severidade} ({', '.join(metodos)})")
    else:
        print("  Nenhuma anomalia detectada por nenhum método")

print("\n✅ Detecção de anomalias concluída!")