# Aula 01 - Tópico 4: Entrada e Saída de Dados
# Demonstração de input() e formatação de strings

print("=== DEMONSTRAÇÃO DE ENTRADA E SAÍDA ===\n")

# Diferentes formas de entrada
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))

# Formatação com f-strings
print(f"\nOlá {nome}!")
print(f"Você tem {idade} anos")
print(f"Seu salário é R$ {salario:.2f}")

# Formatação com .format()
print("\nUsando .format():")
print("Nome: {}, Idade: {}, Salário: R$ {:.2f}".format(nome, idade, salario))

# Formatação com % (método antigo)
print("\nUsando % (método clássico):")
print("Nome: %s, Idade: %d, Salário: R$ %.2f" % (nome, idade, salario))

# Formatação avançada
print(f"\n{nome:>20}")  # Alinhamento à direita
print(f"{nome:<20}")    # Alinhamento à esquerda
print(f"{nome:^20}")    # Centralizado
print(f"{salario:>10.2f}")  # Número formatado