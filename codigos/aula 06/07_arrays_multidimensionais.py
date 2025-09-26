# Aula 06 - Tópico 4: Arrays Multidimensionais
# Demonstração de arrays 2D, 3D, reshape e transpose

import numpy as np

print("=== ARRAYS MULTIDIMENSIONAIS ===\n")

# Arrays 2D
print("=== ARRAYS 2D ===")
matriz_2d = np.array([[1, 2, 3], 
                      [4, 5, 6], 
                      [7, 8, 9]])

print(f"Matriz 2D:\n{matriz_2d}")
print(f"Shape: {matriz_2d.shape}")
print(f"Dimensões: {matriz_2d.ndim}")

# Criação de arrays 2D especiais
zeros_2d = np.zeros((3, 4))
ones_2d = np.ones((2, 5))
identidade = np.eye(3)

print(f"\nZeros 2D (3x4):\n{zeros_2d}")
print(f"\nOnes 2D (2x5):\n{ones_2d}")
print(f"\nMatriz identidade 3x3:\n{identidade}")

# Reshape - mudando a forma
print(f"\n=== RESHAPE ===")
arr_1d = np.arange(12)
print(f"Array 1D: {arr_1d}")

arr_2d_reshape = arr_1d.reshape(3, 4)
print(f"Reshape para 3x4:\n{arr_2d_reshape}")

arr_2d_reshape2 = arr_1d.reshape(4, 3)
print(f"Reshape para 4x3:\n{arr_2d_reshape2}")

# Reshape automático
arr_auto = arr_1d.reshape(-1, 3)  # -1 calcula automaticamente
print(f"Reshape automático (-1, 3):\n{arr_auto}")

# Transpose - transposta
print(f"\n=== TRANSPOSE ===")
matriz_original = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matriz original (2x3):\n{matriz_original}")
print(f"Transposta (3x2):\n{matriz_original.T}")

# Arrays 3D
print(f"\n=== ARRAYS 3D ===")
array_3d = np.arange(24).reshape(2, 3, 4)
print(f"Array 3D (2x3x4):\n{array_3d}")
print(f"Shape: {array_3d.shape}")

# Acessando elementos em 3D
print(f"Elemento [0,1,2]: {array_3d[0, 1, 2]}")
print(f"Primeira 'fatia' [0,:,:]:\n{array_3d[0, :, :]}")

# Operações em arrays multidimensionais
print(f"\n=== OPERAÇÕES MULTIDIMENSIONAIS ===")
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])

print(f"Matriz A:\n{matriz_a}")
print(f"Matriz B:\n{matriz_b}")
print(f"Soma elemento a elemento:\n{matriz_a + matriz_b}")
print(f"Multiplicação matricial:\n{np.dot(matriz_a, matriz_b)}")

# Estatísticas em diferentes eixos
print(f"\n=== ESTATÍSTICAS POR EIXO ===")
dados_3d = np.random.randint(1, 10, (2, 3, 4))
print(f"Dados 3D shape {dados_3d.shape}:\n{dados_3d}")

print(f"Soma total: {np.sum(dados_3d)}")
print(f"Soma eixo 0: {np.sum(dados_3d, axis=0)}")
print(f"Soma eixo 1: {np.sum(dados_3d, axis=1)}")
print(f"Soma eixo 2: {np.sum(dados_3d, axis=2)}")

# Flatten e ravel
print(f"\n=== FLATTEN E RAVEL ===")
matriz_exemplo = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matriz original:\n{matriz_exemplo}")
print(f"Flatten: {matriz_exemplo.flatten()}")
print(f"Ravel: {matriz_exemplo.ravel()}")

# Concatenação de arrays
print(f"\n=== CONCATENAÇÃO ===")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(f"Array 1:\n{arr1}")
print(f"Array 2:\n{arr2}")
print(f"Concatenação vertical:\n{np.vstack([arr1, arr2])}")
print(f"Concatenação horizontal:\n{np.hstack([arr1, arr2])}")

# Divisão de arrays
print(f"\n=== DIVISÃO DE ARRAYS ===")
grande_array = np.arange(12).reshape(3, 4)
print(f"Array grande:\n{grande_array}")

# Dividir horizontalmente
h_split = np.hsplit(grande_array, 2)
print(f"Divisão horizontal:")
for i, parte in enumerate(h_split):
    print(f"Parte {i+1}:\n{parte}")

# Dividir verticalmente
v_split = np.vsplit(grande_array, 3)
print(f"Divisão vertical:")
for i, parte in enumerate(v_split):
    print(f"Parte {i+1}:\n{parte}")

print("\n✅ Arrays multidimensionais demonstrados!")