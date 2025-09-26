# Aula 06 - Tópico 2: Operações Matemáticas e Estatísticas
# Demonstração de operações matemáticas e funções estatísticas do NumPy

import numpy as np

print("=== OPERAÇÕES MATEMÁTICAS E ESTATÍSTICAS ===\n")

# Arrays de exemplo
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 4, 6, 8, 10])

print("=== OPERAÇÕES BÁSICAS ===")
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")

# Operações elemento a elemento
print(f"Soma: {arr1 + arr2}")
print(f"Subtração: {arr2 - arr1}")
print(f"Multiplicação: {arr1 * arr2}")
print(f"Divisão: {arr2 / arr1}")
print(f"Potência: {arr1 ** 2}")

# Operações com escalar
print(f"\n=== OPERAÇÕES COM ESCALAR ===")
print(f"Array + 10: {arr1 + 10}")
print(f"Array * 3: {arr1 * 3}")
print(f"Array / 2: {arr1 / 2}")

# Funções matemáticas
print(f"\n=== FUNÇÕES MATEMÁTICAS ===")
valores = np.array([1, 4, 9, 16, 25])
print(f"Valores: {valores}")
print(f"Raiz quadrada: {np.sqrt(valores)}")
print(f"Logaritmo natural: {np.log(valores)}")
print(f"Exponencial: {np.exp([1, 2, 3])}")

# Funções trigonométricas
angulos = np.array([0, np.pi/4, np.pi/2, np.pi])
print(f"\nÂngulos: {angulos}")
print(f"Seno: {np.sin(angulos)}")
print(f"Cosseno: {np.cos(angulos)}")

# Estatísticas básicas
print(f"\n=== ESTATÍSTICAS BÁSICAS ===")
dados = np.array([10, 15, 20, 25, 30, 35, 40])
print(f"Dados: {dados}")
print(f"Média: {np.mean(dados):.2f}")
print(f"Mediana: {np.median(dados):.2f}")
print(f"Desvio padrão: {np.std(dados):.2f}")
print(f"Variância: {np.var(dados):.2f}")
print(f"Mínimo: {np.min(dados)}")
print(f"Máximo: {np.max(dados)}")

# Percentis
print(f"\n=== PERCENTIS ===")
print(f"25º percentil: {np.percentile(dados, 25):.2f}")
print(f"50º percentil (mediana): {np.percentile(dados, 50):.2f}")
print(f"75º percentil: {np.percentile(dados, 75):.2f}")

# Operações em arrays 2D
print(f"\n=== ARRAYS 2D ===")
matriz = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

print(f"Matriz:\n{matriz}")
print(f"Soma total: {np.sum(matriz)}")
print(f"Soma por linha: {np.sum(matriz, axis=1)}")
print(f"Soma por coluna: {np.sum(matriz, axis=0)}")
print(f"Média por linha: {np.mean(matriz, axis=1)}")

# Funções de agregação
print(f"\n=== AGREGAÇÕES ===")
print(f"Produto de todos: {np.prod(arr1)}")
print(f"Soma cumulativa: {np.cumsum(arr1)}")
print(f"Produto cumulativo: {np.cumprod(arr1)}")

# Arredondamento
print(f"\n=== ARREDONDAMENTO ===")
decimais = np.array([1.234, 2.567, 3.891])
print(f"Originais: {decimais}")
print(f"Arredondado: {np.round(decimais, 2)}")
print(f"Piso: {np.floor(decimais)}")
print(f"Teto: {np.ceil(decimais)}")

# Comparações
print(f"\n=== COMPARAÇÕES ===")
arr_a = np.array([1, 5, 3, 8, 2])
arr_b = np.array([2, 4, 3, 7, 1])
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"A > B: {arr_a > arr_b}")
print(f"A == B: {arr_a == arr_b}")
print(f"Máximo elemento a elemento: {np.maximum(arr_a, arr_b)}")

print("\n✅ Operações matemáticas demonstradas!")