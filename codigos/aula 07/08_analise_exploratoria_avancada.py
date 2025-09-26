# Aula 07 - Tópico 4: Análise Exploratória Avançada
# Demonstração de correlações, crosstab e detecção de outliers

import pandas as pd
import numpy as np

print("=== ANÁLISE EXPLORATÓRIA AVANÇADA ===\n")

# Criar dataset médico para análise
np.random.seed(42)
n = 100

dados = {
    'idade': np.random.randint(18, 80, n),
    'pressao_sistolica': np.random.normal(130, 20, n),
    'pressao_diastolica': np.random.normal(85, 15, n),
    'glicose': np.random.normal(110, 30, n),
    'imc': np.random.normal(26, 4, n),
    'colesterol': np.random.normal(200, 40, n),
    'sexo': np.random.choice(['M', 'F'], n),
    'especialidade': np.random.choice(['Psicologia', 'Psiquiatria', 'Cardiologia'], n),
    'fumante': np.random.choice([True, False], n, p=[0.3, 0.7])
}

df = pd.DataFrame(dados)

# Adicionar algumas correlações intencionais
df.loc[df['idade'] > 50, 'pressao_sistolica'] += 20  # Idosos com pressão mais alta
df.loc[df['imc'] > 30, 'glicose'] += 30  # Obesos com glicose mais alta

print(f"Dataset criado: {df.shape}")
print(df.head())

# 1. ANÁLISE DE CORRELAÇÕES
print(f"\n=== 🔗 ANÁLISE DE CORRELAÇÕES ===")

# Matriz de correlação para variáveis numéricas
colunas_numericas = ['idade', 'pressao_sistolica', 'pressao_diastolica', 
                    'glicose', 'imc', 'colesterol']

correlacoes = df[colunas_numericas].corr()
print("Matriz de correlação:")
print(correlacoes.round(3))

# Identificar correlações fortes
print(f"\nCorrelações fortes (|r| > 0.5):")
for i in range(len(correlacoes.columns)):
    for j in range(i+1, len(correlacoes.columns)):
        corr_val = correlacoes.iloc[i, j]
        if abs(corr_val) > 0.5:
            var1 = correlacoes.columns[i]
            var2 = correlacoes.columns[j]
            print(f"  {var1} ↔ {var2}: {corr_val:.3f}")

# 2. CROSSTAB - ANÁLISE CATEGÓRICA
print(f"\n=== 📊 ANÁLISE CATEGÓRICA (CROSSTAB) ===")

# Crosstab: Sexo vs Especialidade
print("Distribuição Sexo vs Especialidade:")
crosstab_sexo_esp = pd.crosstab(df['sexo'], df['especialidade'])
print(crosstab_sexo_esp)

# Com percentuais
print(f"\nPercentuais por linha:")
crosstab_perc = pd.crosstab(df['sexo'], df['especialidade'], normalize='index') * 100
print(crosstab_perc.round(1))

# Crosstab: Fumante vs Faixa etária
df['faixa_etaria'] = df['idade'].apply(
    lambda x: 'Jovem' if x < 30 else 'Adulto' if x < 60 else 'Idoso'
)

print(f"\nFumantes por faixa etária:")
crosstab_fumante = pd.crosstab(df['faixa_etaria'], df['fumante'])
print(crosstab_fumante)

# 3. DETECÇÃO DE OUTLIERS
print(f"\n=== ⚠️ DETECÇÃO DE OUTLIERS ===")

def detectar_outliers_iqr(serie):
    """Detecta outliers usando método IQR"""
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = serie[(serie < limite_inferior) | (serie > limite_superior)]
    return outliers

# Detectar outliers em cada variável numérica
for coluna in colunas_numericas:
    outliers = detectar_outliers_iqr(df[coluna])
    if len(outliers) > 0:
        print(f"\n{coluna} - {len(outliers)} outliers:")
        print(f"  Valores: {outliers.values}")
        print(f"  Percentil 25: {df[coluna].quantile(0.25):.2f}")
        print(f"  Percentil 75: {df[coluna].quantile(0.75):.2f}")

# 4. ANÁLISE POR PERCENTIS
print(f"\n=== 📈 ANÁLISE POR PERCENTIS ===")

# Análise detalhada de percentis
for coluna in ['pressao_sistolica', 'glicose', 'imc']:
    print(f"\n{coluna}:")
    percentis = [10, 25, 50, 75, 90, 95, 99]
    for p in percentis:
        valor = df[coluna].quantile(p/100)
        print(f"  P{p}: {valor:.2f}")

# 5. ANÁLISE TEMPORAL (SIMULADA)
print(f"\n=== 📅 ANÁLISE TEMPORAL ===")

# Simular dados temporais
datas = pd.date_range('2024-01-01', periods=len(df), freq='D')
df['data_consulta'] = datas

# Análise por mês
df['mes'] = df['data_consulta'].dt.month
consultas_mes = df.groupby('mes').size()

print("Consultas por mês:")
print(consultas_mes)

# Análise por dia da semana
df['dia_semana'] = df['data_consulta'].dt.day_name()
consultas_dia = df.groupby('dia_semana').size()

print(f"\nConsultas por dia da semana:")
print(consultas_dia)

# 6. SEGMENTAÇÃO AVANÇADA
print(f"\n=== 🎯 SEGMENTAÇÃO AVANÇADA ===")

# Criar segmentos de risco
def calcular_risco_cardiovascular(row):
    """Calcula score de risco cardiovascular simples"""
    score = 0
    
    if row['idade'] > 60:
        score += 2
    elif row['idade'] > 45:
        score += 1
    
    if row['pressao_sistolica'] > 140:
        score += 2
    elif row['pressao_sistolica'] > 130:
        score += 1
    
    if row['imc'] > 30:
        score += 1
    
    if row['fumante']:
        score += 2
    
    if score >= 4:
        return 'Alto'
    elif score >= 2:
        return 'Médio'
    else:
        return 'Baixo'

df['risco_cardiovascular'] = df.apply(calcular_risco_cardiovascular, axis=1)

print("Distribuição de risco cardiovascular:")
print(df['risco_cardiovascular'].value_counts())

# Análise por segmento de risco
print(f"\nCaracterísticas por nível de risco:")
analise_risco = df.groupby('risco_cardiovascular').agg({
    'idade': 'mean',
    'pressao_sistolica': 'mean',
    'imc': 'mean',
    'fumante': lambda x: (x == True).mean() * 100  # % de fumantes
}).round(2)

print(analise_risco)

# 7. INSIGHTS E PADRÕES
print(f"\n=== 💡 INSIGHTS E PADRÕES ===")

# Padrão 1: Relação idade e pressão
correlacao_idade_pressao = df['idade'].corr(df['pressao_sistolica'])
print(f"Correlação idade-pressão: {correlacao_idade_pressao:.3f}")

# Padrão 2: IMC e glicose
correlacao_imc_glicose = df['imc'].corr(df['glicose'])
print(f"Correlação IMC-glicose: {correlacao_imc_glicose:.3f}")

# Padrão 3: Fumantes vs não fumantes
print(f"\nComparação fumantes vs não fumantes:")
comparacao_fumante = df.groupby('fumante')[colunas_numericas].mean()
print(comparacao_fumante.round(2))

print("\n✅ Análise exploratória avançada concluída!")