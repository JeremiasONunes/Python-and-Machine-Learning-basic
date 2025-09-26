# Aula 07 - Tópico 2: Limpeza e Transformação de Dados
# Demonstração de técnicas de limpeza e transformação com Pandas

import pandas as pd
import numpy as np

print("=== LIMPEZA E TRANSFORMAÇÃO DE DADOS ===\n")

# Criar dataset com problemas intencionais para demonstração
dados_sujos = {
    'nome': ['Ana Silva', 'João Santos', None, 'Pedro Lima', 'Ana Silva'],  # Valor ausente e duplicata
    'idade': [25, 34, 28, 45, 25],
    'salario': [5000, None, 5500, 7000, 5000],  # Valor ausente
    'cidade': ['São Paulo', 'rio de janeiro', 'SÃO PAULO', 'Belo Horizonte', 'São Paulo'],  # Inconsistências
    'data_nascimento': ['1999-01-15', '1990-05-20', '1996/03/10', '1979-08-25', '1999-01-15']  # Formatos diferentes
}

df = pd.DataFrame(dados_sujos)
print("=== DATASET ORIGINAL (COM PROBLEMAS) ===")
print(df)
print(f"\nInfo do dataset:")
df.info()

# 1. Identificar problemas
print(f"\n=== IDENTIFICANDO PROBLEMAS ===")
print(f"Valores ausentes:\n{df.isnull().sum()}")
print(f"Duplicatas completas: {df.duplicated().sum()}")
print(f"Tipos de dados:\n{df.dtypes}")

# 2. Tratar valores ausentes
print(f"\n=== TRATANDO VALORES AUSENTES ===")

# Opção 1: Remover linhas com valores ausentes
df_sem_na = df.dropna()
print(f"Após remover NAs: {df_sem_na.shape[0]} linhas")

# Opção 2: Preencher valores ausentes
df_preenchido = df.copy()
df_preenchido['nome'].fillna('Nome Não Informado', inplace=True)
df_preenchido['salario'].fillna(df_preenchido['salario'].mean(), inplace=True)

print("Após preencher valores ausentes:")
print(df_preenchido)

# 3. Remover duplicatas
print(f"\n=== REMOVENDO DUPLICATAS ===")
df_sem_dup = df_preenchido.drop_duplicates()
print(f"Após remover duplicatas: {df_sem_dup.shape[0]} linhas")
print(df_sem_dup)

# 4. Padronizar texto
print(f"\n=== PADRONIZANDO TEXTO ===")
df_limpo = df_sem_dup.copy()

# Padronizar nomes de cidades
df_limpo['cidade'] = df_limpo['cidade'].str.title()  # Primeira letra maiúscula
print("Cidades padronizadas:")
print(df_limpo['cidade'].unique())

# 5. Converter tipos de dados
print(f"\n=== CONVERTENDO TIPOS ===")

# Converter datas (tratando formatos diferentes)
df_limpo['data_nascimento'] = pd.to_datetime(df_limpo['data_nascimento'], 
                                           format='mixed', 
                                           errors='coerce')

print("Após conversão de datas:")
print(df_limpo[['nome', 'data_nascimento']])

# 6. Criar novas colunas derivadas
print(f"\n=== CRIANDO COLUNAS DERIVADAS ===")

# Calcular idade a partir da data de nascimento
hoje = pd.Timestamp.now()
df_limpo['idade_calculada'] = (hoje - df_limpo['data_nascimento']).dt.days // 365

# Categorizar salário
df_limpo['faixa_salarial'] = pd.cut(df_limpo['salario'], 
                                   bins=[0, 4000, 6000, float('inf')], 
                                   labels=['Baixo', 'Médio', 'Alto'])

# Categorizar idade
df_limpo['faixa_etaria'] = df_limpo['idade'].apply(
    lambda x: 'Jovem' if x < 30 else 'Adulto' if x < 50 else 'Sênior'
)

print("Dataset com novas colunas:")
print(df_limpo)

# 7. Validação final
print(f"\n=== VALIDAÇÃO FINAL ===")
print(f"Shape final: {df_limpo.shape}")
print(f"Valores ausentes:\n{df_limpo.isnull().sum()}")
print(f"Duplicatas: {df_limpo.duplicated().sum()}")
print(f"Tipos de dados:\n{df_limpo.dtypes}")

# 8. Exemplo de pipeline de limpeza
print(f"\n=== PIPELINE DE LIMPEZA ===")

def pipeline_limpeza(df):
    """Pipeline completo de limpeza de dados"""
    df_clean = df.copy()
    
    # 1. Tratar valores ausentes
    df_clean['nome'].fillna('Não Informado', inplace=True)
    df_clean['salario'].fillna(df_clean['salario'].median(), inplace=True)
    
    # 2. Remover duplicatas
    df_clean = df_clean.drop_duplicates()
    
    # 3. Padronizar texto
    df_clean['cidade'] = df_clean['cidade'].str.title()
    
    # 4. Converter tipos
    df_clean['data_nascimento'] = pd.to_datetime(df_clean['data_nascimento'], 
                                               errors='coerce')
    
    # 5. Criar variáveis derivadas
    df_clean['faixa_etaria'] = df_clean['idade'].apply(
        lambda x: 'Jovem' if x < 30 else 'Adulto' if x < 50 else 'Sênior'
    )
    
    return df_clean

# Testar pipeline
df_pipeline = pipeline_limpeza(df)
print("Resultado do pipeline:")
print(df_pipeline)

print("\n✅ Limpeza e transformação concluídas!")