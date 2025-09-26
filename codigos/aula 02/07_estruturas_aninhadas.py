# Aula 02 - Tópico 4: Estruturas Aninhadas e Controle de Fluxo
# Demonstração de estruturas combinadas, break e continue

print("=== ESTRUTURAS ANINHADAS ===\n")

# If dentro de for
print("Análise de notas por turma:")
turmas = {
    "Turma A": [8.5, 7.2, 9.1, 6.8, 8.9],
    "Turma B": [7.5, 8.3, 6.9, 9.2, 7.8],
    "Turma C": [6.2, 7.9, 8.1, 7.4, 8.6]
}

for turma, notas in turmas.items():
    print(f"\n{turma}:")
    aprovados = 0
    
    for nota in notas:
        if nota >= 7.0:
            status = "Aprovado"
            aprovados += 1
        else:
            status = "Reprovado"
        
        print(f"  Nota {nota}: {status}")
    
    print(f"  Total aprovados: {aprovados}/{len(notas)}")

# Break e continue em loops aninhados
print("\n=== CONTROLE DE FLUXO ===")

# Busca em matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

procurado = 5
encontrado = False

print(f"Procurando o número {procurado} na matriz:")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == procurado:
            print(f"Encontrado na posição [{i}][{j}]")
            encontrado = True
            break
    
    if encontrado:
        break

# Continue com condições
print("\nProcessando apenas números pares:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 != 0:  # Se for ímpar
        continue
    
    # Só processa números pares
    quadrado = numero ** 2
    print(f"{numero}² = {quadrado}")

# Estrutura complexa: validação com loops
print("\n=== VALIDAÇÃO AVANÇADA ===")

tentativas_maximas = 3
tentativa = 0
senha_correta = "123456"

while tentativa < tentativas_maximas:
    senha = input(f"Digite a senha (tentativa {tentativa + 1}/{tentativas_maximas}): ")
    
    if senha == senha_correta:
        print("✅ Acesso liberado!")
        break
    else:
        tentativa += 1
        if tentativa < tentativas_maximas:
            print(f"❌ Senha incorreta. Restam {tentativas_maximas - tentativa} tentativas.")
        else:
            print("❌ Acesso bloqueado! Muitas tentativas incorretas.")

# Loop com else (executa se não houver break)
print("\nBusca com else:")
lista_nomes = ["Ana", "João", "Maria", "Pedro"]
nome_procurado = "Carlos"

for nome in lista_nomes:
    if nome == nome_procurado:
        print(f"Nome {nome_procurado} encontrado!")
        break
else:
    print(f"Nome {nome_procurado} não está na lista.")