# Aula 06 - Tópico 3: Indexação Avançada e Broadcasting
# Demonstração de indexação booleana, fancy indexing e broadcasting

import numpy as np

print("=== INDEXAÇÃO AVANÇADA E BROADCASTING ===\n")

# Array de exemplo
arr = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])
print(f"Array original: {arr}")

# Indexação booleana
print(f"\n=== INDEXAÇÃO BOOLEANA ===")
condicao = arr > 5
print(f"Condição (> 5): {condicao}")
print(f"Valores > 5: {arr[condicao]}")

# Múltiplas condições
print(f"Valores entre 3 e 7: {arr[(arr >= 3) & (arr <= 7)]}")
print(f"Valores < 3 ou > 7: {arr[(arr < 3) | (arr > 7)]}")

# Fancy indexing (indexação com arrays)
print(f"\n=== FANCY INDEXING ===")
indices = [0, 2, 4, 6]
print(f"Índices {indices}: {arr[indices]}")

# Array 2D para exemplos mais complexos
matriz = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print(f"\n=== ARRAY 2D ===")
print(f"Matriz:\n{matriz}")

# Indexação 2D
print(f"Elemento [1,2]: {matriz[1, 2]}")
print(f"Linha 1: {matriz[1, :]}")
print(f"Coluna 2: {matriz[:, 2]}")

# Indexação booleana em 2D
print(f"\n=== INDEXAÇÃO BOOLEANA 2D ===")
condicao_2d = matriz > 50
print(f"Condição (> 50):\n{condicao_2d}")
print(f"Valores > 50: {matriz[condicao_2d]}")

# Broadcasting
print(f"\n=== BROADCASTING ===")
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[10], [20], [30]])

print(f"Array 1D: {arr_1d}")
print(f"Array 2D:\n{arr_2d}")
print(f"Soma (broadcasting):\n{arr_1d + arr_2d}")

# Broadcasting com escalar
print(f"\n=== BROADCASTING COM ESCALAR ===")
matriz_exemplo = np.array([[1, 2], [3, 4]])
print(f"Matriz:\n{matriz_exemplo}")
print(f"Matriz + 10:\n{matriz_exemplo + 10}")
print(f"Matriz * 2:\n{matriz_exemplo * 2}")

# Operações elemento a elemento vs broadcasting
print(f"\n=== COMPARAÇÃO DE OPERAÇÕES ===")
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
c = np.array([[1], [2], [3]])

print(f"a: {a}")
print(f"b: {b}")
print(f"c:\n{c}")
print(f"a + b: {a + b}")  # Elemento a elemento
print(f"a + c (broadcasting):\n{a + c}")  # Broadcasting

# Where - indexação condicional
print(f"\n=== FUNÇÃO WHERE ===")
dados = np.array([1, -2, 3, -4, 5])
print(f"Dados: {dados}")
print(f"Positivos: {np.where(dados > 0, dados, 0)}")  # Se > 0, mantém, senão 0
print(f"Índices dos positivos: {np.where(dados > 0)}")

# Exemplo prático: substituir valores
print(f"\n=== SUBSTITUIÇÃO DE VALORES ===")
temperaturas = np.array([36.2, 37.8, 36.5, 38.1, 36.9])
print(f"Temperaturas: {temperaturas}")

# Marcar febre (> 37.0)
tem_febre = temperaturas > 37.0
print(f"Tem febre: {tem_febre}")
print(f"Temperaturas com febre: {temperaturas[tem_febre]}")

# Substituir valores anormais
temp_corrigidas = np.where(temperaturas > 37.5, 37.0, temperaturas)
print(f"Temperaturas corrigidas: {temp_corrigidas}")

# Indexação avançada com múltiplas condições
print(f"\n=== MÚLTIPLAS CONDIÇÕES ===")
idades = np.array([25, 45, 67, 34, 78, 23, 56])
print(f"Idades: {idades}")

# Classificar por faixa etária
jovens = idades < 30
adultos = (idades >= 30) & (idades < 60)
idosos = idades >= 60

print(f"Jovens: {idades[jovens]}")
print(f"Adultos: {idades[adultos]}")
print(f"Idosos: {idades[idosos]}")

print("\n✅ Indexação avançada demonstrada!")