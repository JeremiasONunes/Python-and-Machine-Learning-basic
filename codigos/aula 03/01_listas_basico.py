# Aula 03 - Tópico 1: Listas - Armazenamento Sequencial
# Demonstração de criação, manipulação e métodos de listas

print("=== LISTAS EM PYTHON ===\n")

# Criação de listas
pacientes = ["Ana Silva", "João Santos", "Maria Costa"]
idades = [25, 34, 28]
lista_vazia = []

print(f"Pacientes: {pacientes}")
print(f"Idades: {idades}")
print(f"Lista vazia: {lista_vazia}")

# Indexação e acesso
print(f"\nPrimeiro paciente: {pacientes[0]}")
print(f"Último paciente: {pacientes[-1]}")
print(f"Segunda idade: {idades[1]}")

# Fatiamento (slicing)
print(f"\nPrimeiros 2 pacientes: {pacientes[:2]}")
print(f"Do segundo em diante: {pacientes[1:]}")
print(f"Idades invertidas: {idades[::-1]}")

# Métodos principais
print("\n=== MÉTODOS DE LISTAS ===")

# Adicionar elementos
pacientes.append("Pedro Lima")
print(f"Após append: {pacientes}")

pacientes.insert(1, "Carlos Souza")
print(f"Após insert: {pacientes}")

# Remover elementos
pacientes.remove("João Santos")
print(f"Após remove: {pacientes}")

ultimo = pacientes.pop()
print(f"Removido: {ultimo}, Lista: {pacientes}")

# Buscar elementos
if "Ana Silva" in pacientes:
    posicao = pacientes.index("Ana Silva")
    print(f"Ana Silva está na posição {posicao}")

# Contar e ordenar
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nNúmeros: {numeros}")
print(f"Quantidade de 1s: {numeros.count(1)}")

numeros.sort()
print(f"Ordenados: {numeros}")

numeros.reverse()
print(f"Invertidos: {numeros}")

# Lista de listas
dados_pacientes = [
    ["Ana Silva", 25, "Psicologia"],
    ["Pedro Lima", 34, "Psiquiatria"],
    ["Maria Costa", 28, "Terapia"]
]

print(f"\nDados estruturados:")
for paciente in dados_pacientes:
    nome, idade, tratamento = paciente
    print(f"  {nome}, {idade} anos - {tratamento}")

# Operações com listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print(f"\nConcatenação: {lista1} + {lista2} = {concatenada}")

repetida = lista1 * 3
print(f"Repetição: {lista1} * 3 = {repetida}")

# Tamanho e verificações
print(f"\nTamanho da lista pacientes: {len(pacientes)}")
print(f"Lista vazia? {len(lista_vazia) == 0}")
print(f"Maior idade: {max(idades)}")
print(f"Menor idade: {min(idades)}")
print(f"Soma das idades: {sum(idades)}")