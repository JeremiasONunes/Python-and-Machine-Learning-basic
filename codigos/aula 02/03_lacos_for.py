# Aula 02 - Tópico 2: Laços de Repetição - For
# Demonstração da estrutura for e função range()

print("=== LAÇOS FOR ===\n")

# For básico com range
print("Contagem de 1 a 5:")
for i in range(1, 6):
    print(f"Número: {i}")

# For com range personalizado
print("\nContagem regressiva:")
for i in range(10, 0, -2):
    print(f"Contagem: {i}")

# Iteração sobre lista
frutas = ["maçã", "banana", "laranja", "uva"]
print("\nFrutas disponíveis:")
for fruta in frutas:
    print(f"- {fruta}")

# For com enumerate (índice + valor)
print("\nFrutas com índice:")
for indice, fruta in enumerate(frutas):
    print(f"{indice + 1}. {fruta}")

# Processamento de dados
idades = [25, 30, 18, 45, 60, 12, 35]
print(f"\nIdades para processar: {idades}")

# Contadores
maiores_idade = 0
menores_idade = 0

for idade in idades:
    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print(f"Maiores de idade: {maiores_idade}")
print(f"Menores de idade: {menores_idade}")

# Soma e média
soma_idades = 0
for idade in idades:
    soma_idades += idade

media = soma_idades / len(idades)
print(f"Soma das idades: {soma_idades}")
print(f"Média de idade: {media:.1f}")

# For aninhado
print("\nTabuada do 2:")
for i in range(1, 6):
    resultado = 2 * i
    print(f"2 x {i} = {resultado}")