# Aula 04 - Tópico 4: Funções Lambda
# Demonstração de funções lambda e aplicações práticas

print("=== FUNÇÕES LAMBDA ===\n")

# Lambda básica
quadrado = lambda x: x ** 2
soma = lambda a, b: a + b
eh_par = lambda n: n % 2 == 0

print("=== LAMBDAS BÁSICAS ===")
print(f"Quadrado de 5: {quadrado(5)}")
print(f"Soma 3 + 7: {soma(3, 7)}")
print(f"8 é par? {eh_par(8)}")
print(f"7 é par? {eh_par(7)}")

# Usando lambda com map()
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
dobrados = list(map(lambda x: x * 2, numeros))

print(f"\n=== MAP COM LAMBDA ===")
print(f"Números: {numeros}")
print(f"Quadrados: {quadrados}")
print(f"Dobrados: {dobrados}")

# Usando lambda com filter()
idades = [15, 25, 17, 30, 45, 16, 60, 22]
maiores_idade = list(filter(lambda idade: idade >= 18, idades))
idosos = list(filter(lambda idade: idade >= 60, idades))

print(f"\n=== FILTER COM LAMBDA ===")
print(f"Todas idades: {idades}")
print(f"Maiores de idade: {maiores_idade}")
print(f"Idosos: {idosos}")

# Usando lambda com sorted()
pacientes = [
    {"nome": "Ana Silva", "idade": 25},
    {"nome": "João Santos", "idade": 34},
    {"nome": "Maria Costa", "idade": 28},
    {"nome": "Pedro Lima", "idade": 45}
]

# Ordenar por idade
por_idade = sorted(pacientes, key=lambda p: p["idade"])
por_nome = sorted(pacientes, key=lambda p: p["nome"])

print(f"\n=== SORTED COM LAMBDA ===")
print("Ordenado por idade:")
for p in por_idade:
    print(f"  {p['nome']} - {p['idade']} anos")

print("Ordenado por nome:")
for p in por_nome:
    print(f"  {p['nome']} - {p['idade']} anos")

# Aplicações práticas com dados médicos
consultas = [
    {"paciente": "Ana", "valor": 150, "tipo": "Psicologia"},
    {"paciente": "João", "valor": 200, "tipo": "Psiquiatria"},
    {"paciente": "Maria", "valor": 120, "tipo": "Terapia"},
    {"paciente": "Pedro", "valor": 180, "tipo": "Psiquiatria"}
]

print(f"\n=== APLICAÇÕES PRÁTICAS ===")

# Filtrar consultas caras (> 150)
consultas_caras = list(filter(lambda c: c["valor"] > 150, consultas))
print(f"Consultas > R$ 150: {len(consultas_caras)}")

# Calcular desconto de 10%
com_desconto = list(map(lambda c: {**c, "valor_desconto": c["valor"] * 0.9}, consultas))
print("Valores com desconto:")
for c in com_desconto:
    print(f"  {c['paciente']}: R$ {c['valor']} → R$ {c['valor_desconto']:.2f}")

# Agrupar por tipo (usando lambda como chave)
tipos_unicos = list(set(map(lambda c: c["tipo"], consultas)))
print(f"Tipos de consulta: {tipos_unicos}")

# Encontrar consulta mais cara
mais_cara = max(consultas, key=lambda c: c["valor"])
print(f"Consulta mais cara: {mais_cara['paciente']} - R$ {mais_cara['valor']}")

# Lambda vs função normal
def calcular_imc_funcao(peso, altura):
    return peso / (altura ** 2)

calcular_imc_lambda = lambda peso, altura: peso / (altura ** 2)

print(f"\n=== LAMBDA VS FUNÇÃO NORMAL ===")
print(f"IMC (função): {calcular_imc_funcao(70, 1.75):.2f}")
print(f"IMC (lambda): {calcular_imc_lambda(70, 1.75):.2f}")

# Quando NÃO usar lambda (código complexo)
# Ruim: lambda muito complexa
# classificar_imc = lambda imc: "Baixo" if imc < 18.5 else "Normal" if imc < 25 else "Alto"

# Melhor: função normal para lógica complexa
def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

imc_teste = 22.5
print(f"IMC {imc_teste}: {classificar_imc(imc_teste)}")