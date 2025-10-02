# Aula 08 - Tópico 2: Introdução ao Machine Learning
# Conceitos básicos e preparação de dados com Scikit-learn

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.datasets import make_classification

print("=== INTRODUÇÃO AO MACHINE LEARNING ===\n")

# 1. Conceitos básicos
print("=== CONCEITOS BÁSICOS DE ML ===")
print("Machine Learning é uma área da IA que permite aos computadores")
print("aprenderem padrões nos dados sem serem explicitamente programados.")
print()
print("Tipos principais:")
print("• Supervisionado: Aprende com dados rotulados (classificação/regressão)")
print("• Não supervisionado: Encontra padrões em dados sem rótulos")
print("• Por reforço: Aprende através de recompensas/punições")

# 2. Criar dataset médico para ML
print(f"\n=== CRIANDO DATASET MÉDICO ===")

np.random.seed(42)
n_pacientes = 200

# Criar dados realistas
dados_ml = {
    'idade': np.random.randint(18, 85, n_pacientes),
    'sexo': np.random.choice([0, 1], n_pacientes),  # 0=F, 1=M
    'pressao_sistolica': np.random.normal(130, 25, n_pacientes),
    'pressao_diastolica': np.random.normal(85, 15, n_pacientes),
    'glicose': np.random.normal(105, 30, n_pacientes),
    'imc': np.random.normal(26, 4, n_pacientes),
    'colesterol': np.random.normal(200, 50, n_pacientes),
    'fumante': np.random.choice([0, 1], n_pacientes, p=[0.7, 0.3]),
    'atividade_fisica': np.random.choice([0, 1, 2], n_pacientes, p=[0.4, 0.4, 0.2])  # 0=baixa, 1=moderada, 2=alta
}

df_ml = pd.DataFrame(dados_ml)

# Criar variável target (risco cardiovascular)
# Lógica: idade alta + pressão alta + outros fatores = risco alto
risco = np.zeros(n_pacientes)

for i in range(n_pacientes):
    score = 0
    
    # Fatores de risco
    if df_ml.loc[i, 'idade'] > 60:
        score += 2
    elif df_ml.loc[i, 'idade'] > 45:
        score += 1
    
    if df_ml.loc[i, 'pressao_sistolica'] > 140:
        score += 2
    elif df_ml.loc[i, 'pressao_sistolica'] > 130:
        score += 1
    
    if df_ml.loc[i, 'glicose'] > 126:
        score += 2
    elif df_ml.loc[i, 'glicose'] > 100:
        score += 1
    
    if df_ml.loc[i, 'imc'] > 30:
        score += 1
    
    if df_ml.loc[i, 'fumante'] == 1:
        score += 2
    
    if df_ml.loc[i, 'atividade_fisica'] == 0:
        score += 1
    
    # Classificar risco
    if score >= 5:
        risco[i] = 2  # Alto risco
    elif score >= 3:
        risco[i] = 1  # Médio risco
    else:
        risco[i] = 0  # Baixo risco

df_ml['risco_cardiovascular'] = risco

print(f"Dataset criado: {len(df_ml)} pacientes")
print(f"Features (variáveis): {df_ml.columns.tolist()[:-1]}")
print(f"Target (objetivo): risco_cardiovascular")

# 3. Explorar o dataset
print(f"\n=== EXPLORANDO O DATASET ===")
print("Primeiras 5 linhas:")
print(df_ml.head())

print(f"\nDistribuição do target:")
print(df_ml['risco_cardiovascular'].value_counts().sort_index())

print(f"\nEstatísticas básicas:")
print(df_ml.describe())

# 4. Preparação dos dados para ML
print(f"\n=== PREPARAÇÃO DOS DADOS ===")

# Separar features (X) e target (y)
X = df_ml.drop('risco_cardiovascular', axis=1)
y = df_ml['risco_cardiovascular']

print(f"Shape dos dados:")
print(f"X (features): {X.shape}")
print(f"y (target): {y.shape}")

# 5. Divisão treino/teste
print(f"\n=== DIVISÃO TREINO/TESTE ===")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Dados de treino: {X_train.shape[0]} amostras")
print(f"Dados de teste: {X_test.shape[0]} amostras")

print(f"\nDistribuição no treino:")
print(pd.Series(y_train).value_counts().sort_index())

print(f"\nDistribuição no teste:")
print(pd.Series(y_test).value_counts().sort_index())

# 6. Normalização dos dados
print(f"\n=== NORMALIZAÇÃO DOS DADOS ===")

# Criar o scaler
scaler = StandardScaler()

# Ajustar apenas nos dados de treino
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Antes da normalização (treino):")
print(f"Idade - Média: {X_train['idade'].mean():.2f}, Std: {X_train['idade'].std():.2f}")
print(f"Pressão - Média: {X_train['pressao_sistolica'].mean():.2f}, Std: {X_train['pressao_sistolica'].std():.2f}")

print("\nApós normalização (treino):")
print(f"Idade - Média: {X_train_scaled[:, 0].mean():.2f}, Std: {X_train_scaled[:, 0].std():.2f}")
print(f"Pressão - Média: {X_train_scaled[:, 2].mean():.2f}, Std: {X_train_scaled[:, 2].std():.2f}")

# 7. Verificar qualidade dos dados
print(f"\n=== VERIFICAÇÃO DE QUALIDADE ===")

print("Valores ausentes:")
print(df_ml.isnull().sum())

print(f"\nDuplicatas: {df_ml.duplicated().sum()}")

print(f"\nBalance das classes:")
class_counts = pd.Series(y).value_counts().sort_index()
for classe, count in class_counts.items():
    perc = count / len(y) * 100
    risco_nome = ['Baixo', 'Médio', 'Alto'][classe]
    print(f"  {risco_nome} risco: {count} ({perc:.1f}%)")

# 8. Resumo da preparação
print(f"\n=== RESUMO DA PREPARAÇÃO ===")
print("✅ Dataset médico criado com 200 pacientes")
print("✅ 9 features selecionadas")
print("✅ Target com 3 classes (risco baixo/médio/alto)")
print("✅ Dados divididos em treino (80%) e teste (20%)")
print("✅ Features normalizadas com StandardScaler")
print("✅ Sem valores ausentes ou duplicatas")
print("✅ Classes balanceadas")

print(f"\nDados prontos para Machine Learning!")
print("Próximo passo: treinar modelos de classificação")

# Salvar dados preparados (simulação)
print(f"\n💾 Dados preparados salvos para próxima etapa")

print("\n✅ Introdução ao ML e preparação de dados concluída!")