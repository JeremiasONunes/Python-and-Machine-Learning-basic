# Aula 07 - Atividade Prática 2: Pipeline de Limpeza de Dados Médicos
# Sistema completo de limpeza e transformação para dados médicos

import pandas as pd
import numpy as np

print("=== PIPELINE DE LIMPEZA - DADOS MÉDICOS ===\n")

# Carregar dados (simulados se necessário)
try:
    df = pd.read_csv('02_dataset_medico.csv')
except FileNotFoundError:
    # Dados simulados com alguns problemas intencionais
    dados = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'nome': ['Ana Silva', 'João Santos', None, 'Pedro Lima', 'Carlos Souza',
                'Rosa Santos', 'Lucas Oliveira', 'Fernanda Costa', 'Roberto Silva', 'Ana Silva'],
        'idade': [25, 34, 28, 45, 67, 78, 29, 52, None, 25],
        'sexo': ['F', 'M', 'F', 'M', 'M', 'f', 'm', 'F', 'M', 'F'],
        'cidade': ['São Paulo', 'rio de janeiro', 'SÃO PAULO', 'Belo Horizonte', 'São Paulo',
                  'salvador', 'Brasília', 'recife', 'Porto Alegre', 'São Paulo'],
        'especialidade': ['Psicologia', 'Psiquiatria', 'Terapia', 'psicologia', 'Psiquiatria',
                         'Neurologia', 'PSICOLOGIA', 'Terapia', 'Psiquiatria', 'Psicologia'],
        'pressao_sistolica': [120, 140, 110, 135, 160, 150, 125, 145, 130, 120],
        'pressao_diastolica': [80, 90, 75, 85, 95, 88, 82, 92, 80, 80],
        'glicose': [95, 130, 88, 145, 180, 200, 102, 165, None, 95],
        'imc': [22.5, 28.2, 24.1, 29.8, 31.5, 26.7, 25.3, 32.1, 27.4, 22.5]
    }
    df = pd.DataFrame(dados)

print("=== DADOS ORIGINAIS ===")
print(f"Shape: {df.shape}")
print(df.head())

# Diagnóstico inicial
print(f"\n=== DIAGNÓSTICO INICIAL ===")
print(f"Valores ausentes:\n{df.isnull().sum()}")
print(f"Duplicatas: {df.duplicated().sum()}")
print(f"Tipos de dados:\n{df.dtypes}")

def pipeline_limpeza_medica(df):
    """Pipeline específico para dados médicos"""
    
    print("🔧 Iniciando pipeline de limpeza...")
    df_clean = df.copy()
    
    # 1. Tratar valores ausentes
    print("1️⃣ Tratando valores ausentes...")
    
    # Nome: preencher com "Paciente Anônimo"
    df_clean['nome'].fillna('Paciente Anônimo', inplace=True)
    
    # Idade: preencher com mediana
    if df_clean['idade'].isnull().any():
        mediana_idade = df_clean['idade'].median()
        df_clean['idade'].fillna(mediana_idade, inplace=True)
    
    # Glicose: preencher com média
    if df_clean['glicose'].isnull().any():
        media_glicose = df_clean['glicose'].mean()
        df_clean['glicose'].fillna(media_glicose, inplace=True)
    
    # 2. Padronizar texto
    print("2️⃣ Padronizando texto...")
    
    # Sexo: padronizar para maiúsculo
    df_clean['sexo'] = df_clean['sexo'].str.upper()
    
    # Cidade: primeira letra maiúscula
    df_clean['cidade'] = df_clean['cidade'].str.title()
    
    # Especialidade: primeira letra maiúscula
    df_clean['especialidade'] = df_clean['especialidade'].str.title()
    
    # 3. Remover duplicatas
    print("3️⃣ Removendo duplicatas...")
    antes_dup = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    depois_dup = len(df_clean)
    print(f"   Removidas {antes_dup - depois_dup} duplicatas")
    
    # 4. Criar variáveis derivadas
    print("4️⃣ Criando variáveis derivadas...")
    
    # Faixa etária
    df_clean['faixa_etaria'] = df_clean['idade'].apply(
        lambda x: 'Criança' if x < 18 else
                 'Jovem' if x < 30 else
                 'Adulto' if x < 60 else
                 'Idoso'
    )
    
    # Classificação IMC
    def classificar_imc(imc):
        if imc < 18.5:
            return 'Abaixo do peso'
        elif imc < 25:
            return 'Normal'
        elif imc < 30:
            return 'Sobrepeso'
        else:
            return 'Obesidade'
    
    df_clean['classificacao_imc'] = df_clean['imc'].apply(classificar_imc)
    
    # Status pressão arterial
    def classificar_pressao(sistolica, diastolica):
        if sistolica >= 140 or diastolica >= 90:
            return 'Hipertensão'
        elif sistolica >= 130 or diastolica >= 80:
            return 'Pré-hipertensão'
        else:
            return 'Normal'
    
    df_clean['status_pressao'] = df_clean.apply(
        lambda row: classificar_pressao(row['pressao_sistolica'], row['pressao_diastolica']), 
        axis=1
    )
    
    # Status glicose
    df_clean['status_glicose'] = df_clean['glicose'].apply(
        lambda x: 'Diabetes' if x >= 126 else
                 'Pré-diabetes' if x >= 100 else
                 'Normal'
    )
    
    # 5. Validação final
    print("5️⃣ Validação final...")
    
    # Verificar se ainda há valores ausentes
    valores_ausentes = df_clean.isnull().sum().sum()
    if valores_ausentes == 0:
        print("   ✅ Sem valores ausentes")
    else:
        print(f"   ⚠️ Ainda há {valores_ausentes} valores ausentes")
    
    # Verificar duplicatas
    duplicatas = df_clean.duplicated().sum()
    if duplicatas == 0:
        print("   ✅ Sem duplicatas")
    else:
        print(f"   ⚠️ Ainda há {duplicatas} duplicatas")
    
    return df_clean

# Executar pipeline
df_limpo = pipeline_limpeza_medica(df)

print(f"\n=== RESULTADO FINAL ===")
print(f"Shape final: {df_limpo.shape}")
print(f"Colunas: {df_limpo.columns.tolist()}")

# Mostrar algumas estatísticas
print(f"\n=== ESTATÍSTICAS PÓS-LIMPEZA ===")
print(f"Distribuição por faixa etária:")
print(df_limpo['faixa_etaria'].value_counts())

print(f"\nDistribuição por classificação IMC:")
print(df_limpo['classificacao_imc'].value_counts())

print(f"\nDistribuição por status de pressão:")
print(df_limpo['status_pressao'].value_counts())

print(f"\nDistribuição por status de glicose:")
print(df_limpo['status_glicose'].value_counts())

# Salvar dados limpos
df_limpo.to_csv('dados_medicos_limpos.csv', index=False)
print(f"\n💾 Dados limpos salvos em 'dados_medicos_limpos.csv'")

print("\n✅ Pipeline de limpeza concluído!")