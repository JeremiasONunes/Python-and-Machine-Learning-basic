# Aula 07 - Tópico 1: Estruturas Pandas (Series e DataFrame)
# Demonstração básica das estruturas fundamentais do Pandas

import pandas as pd
import numpy as np

print("=== ESTRUTURAS PANDAS ===\n")

# Series - estrutura unidimensional
print("=== SERIES ===")
idades = pd.Series([25, 34, 28, 45, 67], name="Idades")
print(f"Series de idades:\n{idades}")
print(f"Tipo: {type(idades)}")
print(f"Valores: {idades.values}")
print(f"Índice: {idades.index}")

# Series com índice personalizado
pacientes = pd.Series([25, 34, 28], 
                     index=['Ana', 'João', 'Maria'], 
                     name='Idades')
print(f"\nSeries com índice personalizado:\n{pacientes}")
print(f"Idade da Ana: {pacientes['Ana']}")

# DataFrame - estrutura bidimensional
print(f"\n=== DATAFRAME ===")

# Criando DataFrame de diferentes formas
dados_dict = {
    'Nome': ['Ana Silva', 'João Santos', 'Maria Costa', 'Pedro Lima'],
    'Idade': [25, 34, 28, 45],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte'],
    'Salario': [5000, 6500, 5500, 7000]
}

df = pd.DataFrame(dados_dict)
print(f"DataFrame básico:\n{df}")

# Informações básicas do DataFrame
print(f"\n=== INFORMAÇÕES BÁSICAS ===")
print(f"Shape (forma): {df.shape}")
print(f"Colunas: {df.columns.tolist()}")
print(f"Tipos de dados:\n{df.dtypes}")
print(f"Índice: {df.index}")

# Métodos de exploração
print(f"\n=== MÉTODOS DE EXPLORAÇÃO ===")
print(f"Primeiras 2 linhas:\n{df.head(2)}")
print(f"\nÚltimas 2 linhas:\n{df.tail(2)}")
print(f"\nInformações gerais:")
df.info()

# Estatísticas descritivas
print(f"\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(f"Describe (apenas colunas numéricas):\n{df.describe()}")

# Acessando dados
print(f"\n=== ACESSANDO DADOS ===")
print(f"Coluna Nome:\n{df['Nome']}")
print(f"Múltiplas colunas:\n{df[['Nome', 'Idade']]}")
print(f"Primeira linha:\n{df.iloc[0]}")
print(f"Linha por índice:\n{df.loc[0]}")

# Operações básicas
print(f"\n=== OPERAÇÕES BÁSICAS ===")
print(f"Idade média: {df['Idade'].mean():.1f}")
print(f"Salário máximo: {df['Salario'].max()}")
print(f"Contagem por cidade:\n{df['Cidade'].value_counts()}")

# Adicionando nova coluna
df['Faixa_Etaria'] = df['Idade'].apply(lambda x: 'Jovem' if x < 30 else 'Adulto' if x < 50 else 'Sênior')
print(f"\nDataFrame com nova coluna:\n{df}")

# Filtragem simples
print(f"\n=== FILTRAGEM ===")
jovens = df[df['Idade'] < 30]
print(f"Pessoas jovens:\n{jovens}")

sp_pessoas = df[df['Cidade'] == 'São Paulo']
print(f"\nPessoas de São Paulo:\n{sp_pessoas}")

print("\n✅ Estruturas Pandas demonstradas!")