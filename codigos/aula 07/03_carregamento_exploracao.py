# Aula 07 - Atividade Prática 1: Carregamento e Exploração de Dataset Médico
# Sistema para carregar e explorar dados médicos de pacientes

import pandas as pd
import numpy as np

print("=== CARREGAMENTO E EXPLORAÇÃO DE DADOS MÉDICOS ===\n")

# Carregar o dataset
try:
    df = pd.read_csv('02_dataset_medico.csv')
    print("✅ Dataset carregado com sucesso!")
except FileNotFoundError:
    print("❌ Arquivo não encontrado. Criando dados simulados...")
    # Criar dados simulados se o arquivo não existir
    dados = {
        'id': range(1, 16),
        'nome': ['Ana Silva', 'João Santos', 'Maria Costa', 'Pedro Lima', 'Carlos Souza',
                'Rosa Santos', 'Lucas Oliveira', 'Fernanda Costa', 'Roberto Silva', 'Juliana Pereira',
                'Marcos Alves', 'Patricia Rocha', 'André Ferreira', 'Camila Santos', 'Ricardo Lima'],
        'idade': [25, 34, 28, 45, 67, 78, 29, 52, 41, 36, 58, 33, 47, 26, 61],
        'sexo': ['F', 'M', 'F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'São Paulo',
                  'Salvador', 'Brasília', 'Recife', 'Porto Alegre', 'Fortaleza',
                  'Curitiba', 'Manaus', 'Goiânia', 'Vitória', 'João Pessoa'],
        'especialidade': ['Psicologia', 'Psiquiatria', 'Terapia', 'Psicologia', 'Psiquiatria',
                         'Neurologia', 'Psicologia', 'Terapia', 'Psiquiatria', 'Psicologia',
                         'Neurologia', 'Terapia', 'Psiquiatria', 'Psicologia', 'Neurologia'],
        'pressao_sistolica': [120, 140, 110, 135, 160, 150, 125, 145, 130, 115, 155, 118, 142, 112, 148],
        'pressao_diastolica': [80, 90, 75, 85, 95, 88, 82, 92, 80, 75, 90, 78, 88, 72, 85],
        'glicose': [95, 130, 88, 145, 180, 200, 102, 165, 120, 98, 175, 105, 155, 92, 185],
        'imc': [22.5, 28.2, 24.1, 29.8, 31.5, 26.7, 25.3, 32.1, 27.4, 23.8, 30.2, 24.9, 28.7, 22.1, 29.5]
    }
    df = pd.DataFrame(dados)

# Exploração inicial
print(f"\n=== INFORMAÇÕES GERAIS ===")
print(f"Dimensões do dataset: {df.shape}")
print(f"Número de pacientes: {df.shape[0]}")
print(f"Número de variáveis: {df.shape[1]}")

print(f"\n=== PRIMEIRAS 5 LINHAS ===")
print(df.head())

print(f"\n=== INFORMAÇÕES DAS COLUNAS ===")
df.info()

print(f"\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(df.describe())

# Análise por variável categórica
print(f"\n=== ANÁLISE POR SEXO ===")
print(df['sexo'].value_counts())
print(f"Percentual por sexo:")
print(df['sexo'].value_counts(normalize=True) * 100)

print(f"\n=== ANÁLISE POR ESPECIALIDADE ===")
print(df['especialidade'].value_counts())

print(f"\n=== ANÁLISE POR CIDADE ===")
print(df['cidade'].value_counts().head())

# Análise de variáveis numéricas
print(f"\n=== ANÁLISE DE IDADES ===")
print(f"Idade média: {df['idade'].mean():.1f} anos")
print(f"Idade mínima: {df['idade'].min()} anos")
print(f"Idade máxima: {df['idade'].max()} anos")
print(f"Desvio padrão: {df['idade'].std():.1f} anos")

print(f"\n=== ANÁLISE DE PRESSÃO ARTERIAL ===")
print(f"Pressão sistólica média: {df['pressao_sistolica'].mean():.1f}")
print(f"Pressão diastólica média: {df['pressao_diastolica'].mean():.1f}")

# Identificar possíveis problemas
print(f"\n=== VERIFICAÇÃO DE QUALIDADE DOS DADOS ===")
print(f"Valores ausentes por coluna:")
print(df.isnull().sum())

print(f"\nDuplicatas: {df.duplicated().sum()}")

# Análise de outliers simples
print(f"\n=== POSSÍVEIS OUTLIERS ===")
print("Pacientes com pressão alta (>140/90):")
hipertensos = df[(df['pressao_sistolica'] > 140) | (df['pressao_diastolica'] > 90)]
print(f"Total: {len(hipertensos)} pacientes")
if len(hipertensos) > 0:
    print(hipertensos[['nome', 'idade', 'pressao_sistolica', 'pressao_diastolica']])

print(f"\nPacientes com glicose alta (>126):")
diabeticos = df[df['glicose'] > 126]
print(f"Total: {len(diabeticos)} pacientes")
if len(diabeticos) > 0:
    print(diabeticos[['nome', 'idade', 'glicose']])

# Resumo da exploração
print(f"\n=== RESUMO DA EXPLORAÇÃO ===")
print(f"✅ Dataset carregado: {df.shape[0]} pacientes, {df.shape[1]} variáveis")
print(f"✅ Sem valores ausentes: {df.isnull().sum().sum() == 0}")
print(f"✅ Sem duplicatas: {df.duplicated().sum() == 0}")
print(f"✅ Faixa etária: {df['idade'].min()}-{df['idade'].max()} anos")
print(f"✅ Especialidades: {df['especialidade'].nunique()} diferentes")
print(f"✅ Cidades: {df['cidade'].nunique()} diferentes")

print("\n✅ Exploração inicial concluída!")