# Aula 02 - Tópico 3: Laços de Repetição - While
# Demonstração da estrutura while e condições de parada

print("=== LAÇOS WHILE ===\n")

# While básico - contagem
print("Contagem com while:")
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

# While com condição de entrada
print("\nValidação de entrada:")
numero = 0
while numero <= 0:
    numero = int(input("Digite um número positivo: "))
    if numero <= 0:
        print("Número deve ser positivo!")

print(f"Número válido: {numero}")

# While com break
print("\nBusca com break:")
numeros = [1, 3, 7, 12, 8, 15, 4]
procurado = 12
i = 0

while i < len(numeros):
    if numeros[i] == procurado:
        print(f"Número {procurado} encontrado na posição {i}")
        break
    i += 1
else:
    print(f"Número {procurado} não encontrado")

# While com continue
print("\nProcessamento com continue:")
valores = [1, -2, 3, -4, 5, -6, 7]
i = 0
soma_positivos = 0

while i < len(valores):
    if valores[i] < 0:
        i += 1
        continue
    
    soma_positivos += valores[i]
    print(f"Adicionando {valores[i]} à soma")
    i += 1

print(f"Soma dos positivos: {soma_positivos}")

# While infinito controlado
print("\nMenu simples:")
opcao = ""
while opcao != "sair":
    print("\nOpções: info, ajuda, sair")
    opcao = input("Digite uma opção: ").lower()
    
    if opcao == "info":
        print("Sistema de demonstração Python")
    elif opcao == "ajuda":
        print("Digite 'sair' para encerrar")
    elif opcao == "sair":
        print("Encerrando...")
    else:
        print("Opção inválida!")