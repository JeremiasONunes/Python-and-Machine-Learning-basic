# Aula 07 - Atividade Prática 3: Análise Estatística por Grupos Médicos
# Sistema de análise por especialidade, faixa etária e condições de saúde

import pandas as pd
import numpy as np

print("=== ANÁLISE ESTATÍSTICA POR GRUPOS MÉDICOS ===\n")

# Carregar ou criar dados médicos
try:
    df = pd.read_csv('dados_medicos_limpos.csv')
except FileNotFoundError:
    # Dados simulados expandidos
    np.random.seed(42)
    n_pacientes = 50
    
    dados = {
        'nome': [f'Paciente_{i}' for i in range(1, n_pacientes+1)],
        'idade': np.random.randint(18, 80, n_pacientes),
        'sexo': np.random.choice(['M', 'F'], n_pacientes),
        'especialidade': np.random.choice(['Psicologia', 'Psiquiatria', 'Terapia', 'Neurologia'], n_pacientes),
        'cidade': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'], n_pacientes),
        'pressao_sistolica': np.random.normal(130, 20, n_pacientes),
        'pressao_diastolica': np.random.normal(85, 15, n_pacientes),
        'glicose': np.random.normal(110, 30, n_pacientes),
        'imc': np.random.normal(26, 4, n_pacientes)
    }
    
    df = pd.DataFrame(dados)
    
    # Criar variáveis categóricas
    df['faixa_etaria'] = df['idade'].apply(
        lambda x: 'Jovem' if x < 30 else 'Adulto' if x < 60 else 'Idoso'
    )
    
    df['status_pressao'] = df.apply(
        lambda row: 'Hipertensão' if row['pressao_sistolica'] >= 140 or row['pressao_diastolica'] >= 90
        else 'Normal', axis=1
    )

print(f"Dataset carregado: {df.shape[0]} pacientes")
print(f"Colunas: {df.columns.tolist()}")

# 1. ANÁLISE POR ESPECIALIDADE
print(f"\n=== 📊 ANÁLISE POR ESPECIALIDADE ===")

grupo_esp = df.groupby('especialidade')

# Estatísticas básicas por especialidade
stats_esp = grupo_esp.agg({
    'idade': ['count', 'mean', 'std'],
    'pressao_sistolica': 'mean',
    'pressao_diastolica': 'mean',
    'glicose': 'mean',
    'imc': 'mean'
}).round(2)

print("Estatísticas por especialidade:")
print(stats_esp)

# Distribuição de sexo por especialidade
print(f"\nDistribuição de sexo por especialidade:")
sexo_esp = pd.crosstab(df['especialidade'], df['sexo'])
print(sexo_esp)

# 2. ANÁLISE POR FAIXA ETÁRIA
print(f"\n=== 👥 ANÁLISE POR FAIXA ETÁRIA ===")

grupo_idade = df.groupby('faixa_etaria')

# Condições de saúde por faixa etária
print("Condições de saúde por faixa etária:")
condicoes_idade = grupo_idade.agg({
    'pressao_sistolica': 'mean',
    'pressao_diastolica': 'mean',
    'glicose': 'mean',
    'imc': 'mean'
}).round(2)
print(condicoes_idade)

# Prevalência de hipertensão por idade
print(f"\nPrevalência de hipertensão por faixa etária:")
hipertensao_idade = pd.crosstab(df['faixa_etaria'], df['status_pressao'], normalize='index') * 100
print(hipertensao_idade.round(1))

# 3. ANÁLISE POR CIDADE
print(f"\n=== 🏙️ ANÁLISE POR CIDADE ===")

grupo_cidade = df.groupby('cidade')

# Perfil de saúde por cidade
print("Perfil de saúde por cidade:")
saude_cidade = grupo_cidade.agg({
    'idade': 'mean',
    'pressao_sistolica': 'mean',
    'glicose': 'mean',
    'imc': 'mean'
}).round(2)
print(saude_cidade)

# Especialidades mais procuradas por cidade
print(f"\nEspecialidades por cidade:")
esp_cidade = pd.crosstab(df['cidade'], df['especialidade'])
print(esp_cidade)

# 4. ANÁLISE COMBINADA
print(f"\n=== 🔄 ANÁLISE COMBINADA ===")

# Análise por especialidade e faixa etária
grupo_esp_idade = df.groupby(['especialidade', 'faixa_etaria'])

print("Idade média por especialidade e faixa etária:")
idade_esp_faixa = grupo_esp_idade['idade'].mean().round(1)
print(idade_esp_faixa)

# Pivot table: IMC médio por especialidade e sexo
print(f"\nIMC médio por especialidade e sexo:")
pivot_imc = df.pivot_table(
    values='imc',
    index='especialidade',
    columns='sexo',
    aggfunc='mean'
).round(2)
print(pivot_imc)

# 5. IDENTIFICAÇÃO DE PADRÕES
print(f"\n=== 🔍 IDENTIFICAÇÃO DE PADRÕES ===")

# Especialidade com maior risco cardiovascular
print("Risco cardiovascular por especialidade:")
risco_cardio = grupo_esp.agg({
    'pressao_sistolica': 'mean',
    'imc': 'mean'
}).round(2)

# Criar score de risco simples
risco_cardio['score_risco'] = (
    (risco_cardio['pressao_sistolica'] - 120) / 20 +
    (risco_cardio['imc'] - 25) / 5
).round(2)

print(risco_cardio.sort_values('score_risco', ascending=False))

# 6. ANÁLISE DE OUTLIERS POR GRUPO
print(f"\n=== ⚠️ OUTLIERS POR GRUPO ===")

# Identificar pacientes com valores extremos em cada especialidade
for esp in df['especialidade'].unique():
    dados_esp = df[df['especialidade'] == esp]
    
    # Pressão muito alta para a especialidade
    q75_pressao = dados_esp['pressao_sistolica'].quantile(0.75)
    outliers_pressao = dados_esp[dados_esp['pressao_sistolica'] > q75_pressao + 20]
    
    if len(outliers_pressao) > 0:
        print(f"\n{esp} - Pacientes com pressão alta:")
        print(outliers_pressao[['nome', 'idade', 'pressao_sistolica']])

# 7. RELATÓRIO RESUMO
print(f"\n=== 📋 RELATÓRIO RESUMO ===")

print(f"Total de pacientes analisados: {len(df)}")
print(f"Especialidades: {df['especialidade'].nunique()}")
print(f"Cidades: {df['cidade'].nunique()}")

# Estatísticas gerais
print(f"\nEstatísticas gerais:")
print(f"- Idade média: {df['idade'].mean():.1f} anos")
print(f"- Pressão sistólica média: {df['pressao_sistolica'].mean():.1f} mmHg")
print(f"- Glicose média: {df['glicose'].mean():.1f} mg/dL")
print(f"- IMC médio: {df['imc'].mean():.1f}")

# Especialidade com mais pacientes
esp_popular = df['especialidade'].value_counts().index[0]
print(f"- Especialidade mais procurada: {esp_popular}")

# Faixa etária predominante
faixa_popular = df['faixa_etaria'].value_counts().index[0]
print(f"- Faixa etária predominante: {faixa_popular}")

print("\n✅ Análise estatística por grupos concluída!")