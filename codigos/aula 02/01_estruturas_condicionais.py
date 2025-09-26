# Aula 02 - Tópico 1: Estruturas Condicionais
# Demonstração de if, elif, else e operadores

print("=== ESTRUTURAS CONDICIONAIS ===\n")

# Exemplo básico de if/else
idade = 25
if idade >= 18:
    print(f"Idade {idade}: Maior de idade")
else:
    print(f"Idade {idade}: Menor de idade")

# Exemplo com elif
nota = 8.5
if nota >= 9:
    conceito = "Excelente"
elif nota >= 7:
    conceito = "Bom"
elif nota >= 5:
    conceito = "Regular"
else:
    conceito = "Insuficiente"

print(f"Nota {nota}: {conceito}")

# Operadores de comparação
a, b = 10, 5
print(f"\n=== OPERADORES DE COMPARAÇÃO ===")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Operadores lógicos
x, y = True, False
print(f"\n=== OPERADORES LÓGICOS ===")
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# Condições compostas
temperatura = 25
chuva = False
if temperatura > 20 and not chuva:
    print("Dia perfeito para sair!")
elif temperatura > 20 and chuva:
    print("Dia quente, mas está chovendo")
else:
    print("Melhor ficar em casa")