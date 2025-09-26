# Aula 01 - Tópico 2: Sintaxe Básica e Variáveis
# Demonstração de tipos de dados e variáveis

# Tipos básicos de dados
nome = "João Silva"  # string
idade = 35  # inteiro
altura = 1.75  # float
ativo = True  # boolean

# Exibindo os tipos
print("=== TIPOS DE DADOS ===")
print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"Idade: {idade} (tipo: {type(idade)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
print(f"Ativo: {ativo} (tipo: {type(ativo)})")

# Conversão de tipos
print("\n=== CONVERSÃO DE TIPOS ===")
idade_str = str(idade)
altura_int = int(altura)
print(f"Idade como string: '{idade_str}'")
print(f"Altura como inteiro: {altura_int}")