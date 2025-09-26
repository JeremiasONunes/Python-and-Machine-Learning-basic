# Aula 06 - Tópico 1: Fundamentos do NumPy
# Demonstração básica de criação e manipulação de arrays

import numpy as np

print("=== FUNDAMENTOS DO NUMPY ===\n")

# Criação de arrays básicos
print("=== CRIAÇÃO DE ARRAYS ===")

# Array a partir de lista
lista = [1, 2, 3, 4, 5]
array1 = np.array(lista)
print(f"Array da lista: {array1}")
print(f"Tipo: {type(array1)}")

# Arrays especiais
zeros = np.zeros(5)
ones = np.ones(4)
print(f"Zeros: {zeros}")
print(f"Ones: {ones}")

# Array com range
range_array = np.arange(0, 10, 2)
print(f"Range (0 a 10, passo 2): {range_array}")

# Array com espaçamento linear
linear = np.linspace(0, 1, 5)
print(f"Linear (0 a 1, 5 pontos): {linear}")

# Propriedades dos arrays
print(f"\n=== PROPRIEDADES ===")
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array 2D:\n{array2d}")
print(f"Shape (forma): {array2d.shape}")
print(f"Size (tamanho): {array2d.size}")
print(f"Dimensões: {array2d.ndim}")
print(f"Tipo de dados: {array2d.dtype}")

# Tipos de dados específicos
print(f"\n=== TIPOS DE DADOS ===")
int_array = np.array([1, 2, 3], dtype=np.int32)
float_array = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print(f"Inteiros: {int_array} (dtype: {int_array.dtype})")
print(f"Floats: {float_array} (dtype: {float_array.dtype})")

# Arrays aleatórios
print(f"\n=== ARRAYS ALEATÓRIOS ===")
np.random.seed(42)  # Para resultados reproduzíveis
random_array = np.random.random(5)
random_int = np.random.randint(1, 10, 5)
print(f"Aleatórios (0-1): {random_array}")
print(f"Inteiros aleatórios (1-10): {random_int}")

# Operações básicas
print(f"\n=== OPERAÇÕES BÁSICAS ===")
arr = np.array([1, 2, 3, 4, 5])
print(f"Array original: {arr}")
print(f"Soma: {arr.sum()}")
print(f"Média: {arr.mean()}")
print(f"Máximo: {arr.max()}")
print(f"Mínimo: {arr.min()}")

# Indexação básica
print(f"\n=== INDEXAÇÃO ===")
print(f"Primeiro elemento: {arr[0]}")
print(f"Último elemento: {arr[-1]}")
print(f"Primeiros 3: {arr[:3]}")
print(f"Do 2º ao 4º: {arr[1:4]}")

# Modificação de arrays
print(f"\n=== MODIFICAÇÃO ===")
arr_copy = arr.copy()
arr_copy[0] = 10
print(f"Array modificado: {arr_copy}")

# Reshape básico
print(f"\n=== RESHAPE ===")
arr_1d = np.arange(6)
arr_2d = arr_1d.reshape(2, 3)
print(f"1D: {arr_1d}")
print(f"2D (2x3):\n{arr_2d}")

print("\n✅ Fundamentos do NumPy demonstrados!")