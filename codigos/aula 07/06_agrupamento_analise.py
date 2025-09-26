# Aula 07 - Tópico 3: Análise e Agrupamento de Dados
# Demonstração de groupby, agregações e análises por grupos

import pandas as pd
import numpy as np

print("=== ANÁLISE E AGRUPAMENTO DE DADOS ===\n")

# Criar dataset de exemplo
dados = {
    'nome': ['Ana', 'João', 'Maria', 'Pedro', 'Carlos', 'Rosa', 'Lucas', 'Fernanda'],
    'idade': [25, 34, 28, 45, 67, 78, 29, 52],
    'sexo': ['F', 'M', 'F', 'M', 'M', 'F', 'M', 'F'],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 
              'São Paulo', 'Salvador', 'Rio de Janeiro', 'São Paulo'],
    'especialidade': ['Psicologia', 'Psiquiatria', 'Terapia', 'Psicologia', 
                     'Psiquiatria', 'Neurologia', 'Psicologia', 'Terapia'],
    'salario': [5000, 6500, 5500, 7000, 8000, 4500, 5200, 6800],
    'anos_experiencia': [3, 8, 5, 15, 25, 30, 4, 12]
}

df = pd.DataFrame(dados)
print("=== DATASET ORIGINAL ===")
print(df)

# 1. Agrupamento simples
print(f"\n=== AGRUPAMENTO POR SEXO ===")
grupo_sexo = df.groupby('sexo')

# Estatísticas por grupo
print("Idade média por sexo:")
print(grupo_sexo['idade'].mean())

print("\nSalário médio por sexo:")
print(grupo_sexo['salario'].mean())

# 2. Múltiplas agregações
print(f"\n=== MÚLTIPLAS AGREGAÇÕES ===")
estatisticas_sexo = grupo_sexo.agg({
    'idade': ['mean', 'min', 'max'],
    'salario': ['mean', 'sum', 'count'],
    'anos_experiencia': 'mean'
})

print("Estatísticas completas por sexo:")
print(estatisticas_sexo)

# 3. Agrupamento por múltiplas colunas
print(f"\n=== AGRUPAMENTO POR CIDADE E SEXO ===")
grupo_cidade_sexo = df.groupby(['cidade', 'sexo'])
print("Contagem por cidade e sexo:")
print(grupo_cidade_sexo.size())

print("\nSalário médio por cidade e sexo:")
print(grupo_cidade_sexo['salario'].mean())

# 4. Agrupamento por especialidade
print(f"\n=== ANÁLISE POR ESPECIALIDADE ===")
grupo_esp = df.groupby('especialidade')

print("Estatísticas por especialidade:")
stats_esp = grupo_esp.agg({
    'idade': 'mean',
    'salario': ['mean', 'count'],
    'anos_experiencia': 'mean'
})
print(stats_esp)

# 5. Filtros em grupos
print(f"\n=== FILTROS EM GRUPOS ===")

# Filtrar apenas grupos com mais de 1 pessoa
grupos_grandes = df.groupby('cidade').filter(lambda x: len(x) > 1)
print("Cidades com mais de 1 pessoa:")
print(grupos_grandes[['nome', 'cidade']])

# 6. Transformações em grupos
print(f"\n=== TRANSFORMAÇÕES ===")

# Calcular salário relativo à média da cidade
df['salario_relativo'] = df.groupby('cidade')['salario'].transform(
    lambda x: x / x.mean()
)

print("Salário relativo à média da cidade:")
print(df[['nome', 'cidade', 'salario', 'salario_relativo']])

# 7. Pivot Tables
print(f"\n=== PIVOT TABLES ===")

# Tabela cruzada: especialidade vs sexo
pivot_esp_sexo = pd.crosstab(df['especialidade'], df['sexo'])
print("Crosstab - Especialidade vs Sexo:")
print(pivot_esp_sexo)

# Pivot table com valores
pivot_salario = df.pivot_table(
    values='salario', 
    index='especialidade', 
    columns='sexo', 
    aggfunc='mean'
)
print("\nPivot Table - Salário médio por especialidade e sexo:")
print(pivot_salario)

# 8. Ranking dentro de grupos
print(f"\n=== RANKING DENTRO DE GRUPOS ===")

# Ranking de salário dentro de cada especialidade
df['ranking_salario'] = df.groupby('especialidade')['salario'].rank(
    method='dense', ascending=False
)

print("Ranking de salário por especialidade:")
print(df[['nome', 'especialidade', 'salario', 'ranking_salario']].sort_values(['especialidade', 'ranking_salario']))

# 9. Análise de percentis por grupo
print(f"\n=== PERCENTIS POR GRUPO ===")

percentis_cidade = df.groupby('cidade')['salario'].describe()
print("Percentis de salário por cidade:")
print(percentis_cidade)

# 10. Exemplo prático: análise de performance
print(f"\n=== ANÁLISE DE PERFORMANCE ===")

# Criar categoria de experiência
df['nivel_experiencia'] = df['anos_experiencia'].apply(
    lambda x: 'Júnior' if x < 5 else 'Pleno' if x < 15 else 'Sênior'
)

# Análise por nível de experiência
analise_exp = df.groupby('nivel_experiencia').agg({
    'salario': ['mean', 'min', 'max'],
    'idade': 'mean',
    'nome': 'count'
}).round(2)

print("Análise por nível de experiência:")
print(analise_exp)

print("\n✅ Análise e agrupamento demonstrados!")