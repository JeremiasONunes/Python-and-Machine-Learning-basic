# 📘 Material de Estudo – Python Básico Completo

## 1. O que é Python?

### Definição e História
Python é uma linguagem de programação de alto nível criada por Guido van Rossum em 1991. O nome "Python" não vem da cobra, mas sim do grupo de comédia britânico "Monty Python's Flying Circus", mostrando desde o início a filosofia de que programar deve ser divertido e não complicado.

### Analogia: Python como uma Linguagem Universal
Imagine que você está em um país estrangeiro e precisa se comunicar. Python é como ter um tradutor universal que entende tanto você quanto o computador. Enquanto outras linguagens são como idiomas específicos e complexos, Python é como falar de forma clara e direta - quase como se você estivesse conversando com um amigo.

### Características Principais

**Interpretado vs Compilado:**
- **Interpretado**: Como ter um tradutor simultâneo - você fala e ele traduz na hora
- **Compilado**: Como traduzir um livro inteiro antes de publicar

```python
# Python é interpretado - você pode executar linha por linha
print("Olá, mundo!")  # Esta linha executa imediatamente
```

**Multiplataforma:**
Python funciona como um aplicativo universal - escreva uma vez, rode em qualquer lugar (Windows, Linux, macOS).

### Onde Python é Utilizado?

1. **Desenvolvimento Web** → Como construir sites e aplicações online
2. **Ciência de Dados** → Como um laboratório digital para analisar informações
3. **Inteligência Artificial** → Como ensinar computadores a "pensar"
4. **Automação** → Como ter um assistente digital que faz tarefas repetitivas
5. **Jogos** → Como criar mundos virtuais interativos

## 2. Tipos de Dados em Python

### Analogia: Tipos de Dados como Gavetas Organizadas
Imagine sua mesa de trabalho com diferentes gavetas. Cada gaveta guarda um tipo específico de item - uma para canetas, outra para papéis, outra para clipes. Os tipos de dados em Python funcionam da mesma forma.

### Números Inteiros (int)
Como contar objetos físicos - sempre números inteiros, sem partes quebradas.

```python
# Inteiros - números sem vírgula
idade = 25              # Idade de uma pessoa
quantidade_livros = 150 # Livros em uma biblioteca
temperatura = -5        # Temperatura pode ser negativa

# Python reconhece automaticamente que são inteiros
print(type(idade))      # <class 'int'>
```

### Números Decimais (float)
Como medir líquidos - podem ter partes fracionárias.

```python
# Float - números com vírgula (ponto em Python)
altura = 1.75           # Altura em metros
preco = 29.99          # Preço de um produto
pi = 3.14159           # Constante matemática

# Cuidado: divisão sempre resulta em float
resultado = 10 / 2      # 5.0 (não 5)
print(type(resultado))  # <class 'float'>
```

### Strings (str)
Como etiquetas ou placas - qualquer texto que você queira armazenar.

```python
# Strings - texto entre aspas
nome = "Maria Silva"           # Nome completo
cidade = 'São Paulo'          # Aspas simples também funcionam
mensagem = "Olá, mundo!"      # Mensagem de saudação

# Strings podem conter números, mas são tratadas como texto
codigo = "12345"              # Este é texto, não número
print(type(codigo))           # <class 'str'>

# Concatenação - juntar strings
nome_completo = nome + " da " + cidade
print(nome_completo)          # "Maria Silva da São Paulo"
```

### Booleanos (bool)
Como interruptores - só podem estar ligados (True) ou desligados (False).

```python
# Booleanos - apenas True ou False
maior_idade = True             # Verdadeiro
chovendo = False              # Falso
aprovado = True               # Status de aprovação

# Comparações resultam em booleanos
tem_carteira = idade >= 18    # True se idade for 18 ou mais
print(tem_carteira)           # True (pois idade = 25)
```

### Listas (list)
Como uma prateleira onde você pode adicionar, remover e reorganizar itens.

```python
# Listas - coleção ordenada e mutável
frutas = ["maçã", "banana", "uva"]        # Lista de strings
numeros = [1, 2, 3, 4, 5]                # Lista de inteiros
mista = ["João", 25, True, 1.75]         # Lista com tipos diferentes

# Listas são mutáveis - podem ser alteradas
frutas.append("laranja")                  # Adiciona no final
print(frutas)                            # ['maçã', 'banana', 'uva', 'laranja']

# Acessar elementos pelo índice (começa em 0)
primeira_fruta = frutas[0]               # "maçã"
ultima_fruta = frutas[-1]                # "laranja" (índice negativo conta do fim)
```

### Tuplas (tuple)
Como uma caixa lacrada - uma vez criada, não pode ser alterada.

```python
# Tuplas - coleção ordenada e imutável
coordenadas = (10, 20)                   # Posição X, Y
rgb_cor = (255, 0, 128)                  # Cor em RGB
dados_pessoa = ("Ana", 30, "Engenheira") # Informações fixas

# Tuplas são imutáveis - não podem ser alteradas
# coordenadas[0] = 15  # Isso causaria erro!

# Úteis para dados que não devem mudar
dimensoes_tela = (1920, 1080)           # Resolução da tela
```

### Dicionários (dict)
Como uma agenda telefônica - cada nome (chave) tem um número (valor) correspondente.

```python
# Dicionários - pares chave-valor
pessoa = {
    "nome": "João Silva",        # chave: valor
    "idade": 30,
    "profissao": "Programador",
    "salario": 5000.00
}

# Acessar valores pela chave
nome_pessoa = pessoa["nome"]             # "João Silva"
idade_pessoa = pessoa.get("idade")       # 30 (método mais seguro)

# Adicionar ou modificar
pessoa["email"] = "joao@email.com"       # Adiciona nova chave
pessoa["idade"] = 31                     # Modifica valor existente

print(pessoa)
```

## 3. Operadores

### Analogia: Operadores como Ferramentas
Os operadores são como ferramentas em uma caixa de ferramentas - cada uma tem uma função específica para trabalhar com os dados.

### Operadores Matemáticos
Como uma calculadora - fazem cálculos com números.

```python
# Operações básicas
a = 10
b = 3

soma = a + b              # 13 - Adição
subtracao = a - b         # 7  - Subtração  
multiplicacao = a * b     # 30 - Multiplicação
divisao = a / b           # 3.333... - Divisão (sempre float)

# Operações especiais
divisao_inteira = a // b  # 3 - Divisão sem resto (floor division)
resto = a % b             # 1 - Resto da divisão (módulo)
potencia = a ** b         # 1000 - Exponenciação (10³)

# Exemplo prático: verificar se número é par
numero = 8
eh_par = numero % 2 == 0  # True se resto da divisão por 2 for 0
print(f"{numero} é par: {eh_par}")
```

### Operadores de Comparação
Como uma balança - comparam valores e retornam True ou False.

```python
# Comparações retornam booleanos
x = 10
y = 5

maior = x > y             # True - x é maior que y
menor = x < y             # False - x não é menor que y
igual = x == y            # False - x não é igual a y
diferente = x != y        # True - x é diferente de y
maior_igual = x >= y      # True - x é maior ou igual a y
menor_igual = x <= y      # False - x não é menor ou igual a y

# Cuidado: = (atribuição) vs == (comparação)
idade = 18                # Atribui valor 18 à variável idade
pode_votar = idade == 18  # Compara se idade é igual a 18
```

### Operadores Lógicos
Como portões lógicos - combinam condições verdadeiras ou falsas.

```python
# Operadores lógicos
tem_carteira = True
tem_carro = False
maior_18 = True

# AND - todas as condições devem ser verdadeiras
pode_dirigir = tem_carteira and maior_18        # True
pode_viajar = tem_carteira and tem_carro        # False

# OR - pelo menos uma condição deve ser verdadeira  
tem_transporte = tem_carro or tem_carteira      # True

# NOT - inverte o valor lógico
nao_tem_carro = not tem_carro                   # True

# Exemplo prático: validação de login
usuario_correto = True
senha_correta = False
login_valido = usuario_correto and senha_correta # False
```

## 4. Estruturas de Controle

### Analogia: Estruturas como Semáforos e Rotatórias
As estruturas de controle são como o sistema de trânsito - elas decidem qual caminho o programa deve seguir.

### Condicional if - O Semáforo do Código

```python
# Estrutura básica if-else
idade = 18

if idade >= 18:                    # Se a condição for verdadeira
    print("Pode tirar carteira")   # Execute este bloco
    print("É maior de idade")
else:                              # Senão
    print("Ainda não pode dirigir") # Execute este bloco
    print("É menor de idade")

# Múltiplas condições com elif
nota = 8.5

if nota >= 9:                      # Primeira condição
    conceito = "A"
    print("Excelente!")
elif nota >= 7:                    # Segunda condição (se a primeira for falsa)
    conceito = "B" 
    print("Bom trabalho!")
elif nota >= 5:                    # Terceira condição
    conceito = "C"
    print("Aprovado")
else:                              # Se nenhuma condição for verdadeira
    conceito = "D"
    print("Reprovado")

print(f"Seu conceito é: {conceito}")
```

### Laços de Repetição - As Rotatórias do Código

#### For Loop - Quando Você Sabe Quantas Voltas Dar

```python
# For com range - como contar de 1 a 5
print("Contando de 0 a 4:")
for i in range(5):                 # range(5) = 0, 1, 2, 3, 4
    print(f"Número: {i}")

# For com range personalizado
print("\nContando de 1 a 10, de 2 em 2:")
for numero in range(1, 11, 2):     # início, fim, passo
    print(numero)                  # 1, 3, 5, 7, 9

# For com listas - percorrer cada item
frutas = ["maçã", "banana", "uva", "laranja"]
print("\nFrutas disponíveis:")
for fruta in frutas:
    print(f"- {fruta}")

# For com enumerate - quando precisar do índice também
print("\nFrutas numeradas:")
for indice, fruta in enumerate(frutas, 1):  # Começa a contar do 1
    print(f"{indice}. {fruta}")
```

#### While Loop - Quando Não Sabe Quantas Voltas Precisará

```python
# While - repete enquanto condição for verdadeira
contador = 0
print("Contagem regressiva:")
while contador < 5:                # Enquanto contador for menor que 5
    print(f"Faltam {5 - contador} segundos")
    contador += 1                  # Incrementa contador (contador = contador + 1)

print("Tempo esgotado!")

# Exemplo prático: validação de entrada
senha_correta = "123456"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso liberado!")
        break                      # Sai do loop
    else:
        tentativas += 1
        restantes = max_tentativas - tentativas
        if restantes > 0:
            print(f"Senha incorreta. Restam {restantes} tentativas.")
        else:
            print("Acesso bloqueado!")
```

## 5. Funções

### Analogia: Funções como Máquinas Especializadas
Uma função é como uma máquina que recebe ingredientes (parâmetros), processa e devolve um produto (retorno).

### Criando e Usando Funções

```python
# Função simples sem parâmetros
def saudacao():
    """Função que exibe uma saudação simples"""
    print("Olá! Bem-vindo ao programa!")

# Chamando a função
saudacao()                         # Executa a função

# Função com parâmetros
def saudacao_personalizada(nome, hora_do_dia="dia"):
    """
    Função que cria saudação personalizada
    nome: string com o nome da pessoa
    hora_do_dia: string com período do dia (padrão: 'dia')
    """
    if hora_do_dia == "manhã":
        cumprimento = "Bom dia"
    elif hora_do_dia == "tarde":
        cumprimento = "Boa tarde"
    elif hora_do_dia == "noite":
        cumprimento = "Boa noite"
    else:
        cumprimento = "Olá"
    
    mensagem = f"{cumprimento}, {nome}!"
    return mensagem                # Retorna o resultado

# Usando a função
msg1 = saudacao_personalizada("Maria", "manhã")
msg2 = saudacao_personalizada("João")  # Usa valor padrão
print(msg1)                       # "Bom dia, Maria!"
print(msg2)                       # "Olá, João!"
```

### Funções Matemáticas Práticas

```python
# Função para calcular área de retângulo
def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    area = largura * altura
    return area

# Função para verificar se número é par
def eh_par(numero):
    """Retorna True se o número for par, False caso contrário"""
    return numero % 2 == 0

# Função com múltiplos retornos
def analisar_numero(num):
    """Analisa um número e retorna várias informações"""
    eh_positivo = num > 0
    eh_negativo = num < 0
    eh_zero = num == 0
    eh_par_num = eh_par(num)
    
    return eh_positivo, eh_negativo, eh_zero, eh_par_num

# Usando as funções
area = calcular_area_retangulo(5, 3)
print(f"Área do retângulo: {area} m²")

numero = 8
print(f"{numero} é par: {eh_par(numero)}")

# Desempacotando múltiplos retornos
positivo, negativo, zero, par = analisar_numero(-4)
print(f"Número -4: positivo={positivo}, negativo={negativo}, zero={zero}, par={par}")
```

## 6. Trabalhando com Listas

### Analogia: Listas como Prateleiras Organizadas
Uma lista é como uma prateleira onde você pode colocar, tirar e reorganizar itens. Cada item tem uma posição (índice).

### Operações Básicas com Listas

```python
# Criando listas
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]
lista_vazia = []                   # Lista vazia
lista_mista = ["João", 25, True]   # Tipos diferentes

# Acessando elementos (índice começa em 0)
primeira_fruta = frutas[0]         # "maçã"
segunda_fruta = frutas[1]          # "banana"
ultima_fruta = frutas[-1]          # "uva" (índice negativo)
penultima = frutas[-2]             # "banana"

print(f"Primeira: {primeira_fruta}, Última: {ultima_fruta}")

# Fatiamento (slicing) - como cortar fatias
primeiras_duas = frutas[0:2]       # ["maçã", "banana"]
do_segundo_em_diante = frutas[1:]  # ["banana", "uva"]
ate_o_segundo = frutas[:2]         # ["maçã", "banana"]

print(f"Primeiras duas: {primeiras_duas}")
```

### Modificando Listas

```python
# Lista inicial
compras = ["pão", "leite", "ovos"]

# Adicionando itens
compras.append("queijo")           # Adiciona no final
compras.insert(1, "manteiga")      # Adiciona na posição 1
print(f"Lista após adicionar: {compras}")

# Removendo itens
compras.remove("leite")            # Remove primeira ocorrência
item_removido = compras.pop()      # Remove e retorna o último
item_posicao = compras.pop(0)      # Remove e retorna da posição 0
print(f"Removido: {item_removido}, Da posição 0: {item_posicao}")
print(f"Lista final: {compras}")

# Modificando item existente
compras[0] = "pão integral"        # Substitui item na posição 0
print(f"Após modificar: {compras}")
```

### Operações Úteis com Listas

```python
# Lista de números para exemplos
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Informações sobre a lista
tamanho = len(numeros)             # Quantidade de elementos
maior = max(numeros)               # Maior valor
menor = min(numeros)               # Menor valor
soma = sum(numeros)                # Soma de todos os elementos

print(f"Tamanho: {tamanho}, Maior: {maior}, Menor: {menor}, Soma: {soma}")

# Organizando a lista
numeros_ordenados = sorted(numeros)     # Cria nova lista ordenada
numeros.sort()                          # Ordena a lista original
numeros.reverse()                       # Inverte a ordem

print(f"Ordenados: {numeros_ordenados}")
print(f"Invertidos: {numeros}")

# Verificações
tem_cinco = 5 in numeros           # True se 5 estiver na lista
posicao_cinco = numeros.index(5)   # Posição do número 5
quantos_uns = numeros.count(1)     # Quantas vezes 1 aparece

print(f"Tem 5: {tem_cinco}, Posição do 5: {posicao_cinco}, Quantidade de 1s: {quantos_uns}")
```

### List Comprehension - Criando Listas de Forma Elegante

```python
# Forma tradicional
quadrados = []
for i in range(1, 6):
    quadrados.append(i ** 2)
print(f"Quadrados (tradicional): {quadrados}")

# List comprehension - mais concisa
quadrados_lc = [i ** 2 for i in range(1, 6)]
print(f"Quadrados (list comprehension): {quadrados_lc}")

# Com condição
pares = [i for i in range(1, 11) if i % 2 == 0]
print(f"Números pares de 1 a 10: {pares}")

# Processando lista existente
nomes = ["ana", "joão", "maria"]
nomes_maiusculos = [nome.upper() for nome in nomes]
print(f"Nomes em maiúsculo: {nomes_maiusculos}")
```

## 7. Entrada e Saída de Dados

### Analogia: Comunicação como Conversa
A entrada e saída de dados é como uma conversa - o programa pergunta (saída), o usuário responde (entrada).

### Saída de Dados - Mostrando Informações

```python
# Print básico
print("Olá, mundo!")

# Print com múltiplos valores
nome = "Maria"
idade = 25
print("Nome:", nome, "Idade:", idade)

# Formatação com f-strings (mais moderna e legível)
print(f"Olá, {nome}! Você tem {idade} anos.")

# Formatação com .format()
print("Olá, {}! Você tem {} anos.".format(nome, idade))

# Controlando a saída
print("Primeira linha", end=" ")      # Não quebra linha
print("mesma linha")

print("Item 1", "Item 2", "Item 3", sep=" | ")  # Separador customizado
```

### Entrada de Dados - Recebendo Informações

```python
# Input básico (sempre retorna string)
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Convertendo tipos
idade_str = input("Digite sua idade: ")
idade = int(idade_str)                 # Converte string para inteiro

# Ou em uma linha
altura = float(input("Digite sua altura (m): "))  # Converte para float

# Validação de entrada
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break                          # Sai do loop se conversão der certo
    except ValueError:
        print("Por favor, digite apenas números!")

print(f"Você digitou: {numero}")
```

### Exemplo Prático: Calculadora de IMC

```python
def calcular_imc():
    """Calculadora de Índice de Massa Corporal"""
    print("=== Calculadora de IMC ===")
    
    # Entrada de dados com validação
    while True:
        try:
            peso = float(input("Digite seu peso (kg): "))
            if peso <= 0:
                print("Peso deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("Digite um número válido!")
    
    while True:
        try:
            altura = float(input("Digite sua altura (m): "))
            if altura <= 0:
                print("Altura deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("Digite um número válido!")
    
    # Cálculo
    imc = peso / (altura ** 2)
    
    # Classificação
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    # Saída formatada
    print(f"\n--- Resultado ---")
    print(f"Peso: {peso:.1f} kg")
    print(f"Altura: {altura:.2f} m")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

# Executar a calculadora
calcular_imc()
```

## 8. Manipulação de Strings

### Analogia: Strings como Textos Editáveis
Trabalhar com strings é como editar um documento - você pode cortar, colar, substituir e formatar o texto.

### Operações Básicas com Strings

```python
# String básica
texto = "Python é uma linguagem incrível!"

# Informações sobre a string
tamanho = len(texto)               # Quantidade de caracteres
print(f"Tamanho: {tamanho}")

# Acessando caracteres (como lista)
primeiro_char = texto[0]           # 'P'
ultimo_char = texto[-1]            # '!'
print(f"Primeiro: '{primeiro_char}', Último: '{ultimo_char}'")

# Fatiamento
palavra = texto[0:6]               # "Python"
sem_primeiro = texto[1:]           # "ython é uma linguagem incrível!"
sem_ultimo = texto[:-1]            # "Python é uma linguagem incrível"
print(f"Primeira palavra: '{palavra}'")
```

### Métodos de Transformação

```python
texto = "  Python é INCRÍVEL!  "

# Mudança de caso
maiusculo = texto.upper()          # "  PYTHON É INCRÍVEL!  "
minusculo = texto.lower()          # "  python é incrível!  "
titulo = texto.title()             # "  Python É Incrível!  "
capitalizado = texto.capitalize()  # "  python é incrível!  "

print(f"Original: '{texto}'")
print(f"Maiúsculo: '{maiusculo}'")
print(f"Minúsculo: '{minusculo}'")

# Limpeza de espaços
limpo = texto.strip()              # Remove espaços do início e fim
print(f"Limpo: '{limpo}'")

# Substituição
novo_texto = texto.replace("INCRÍVEL", "fantástica")
print(f"Substituído: '{novo_texto}'")
```

### Divisão e Junção de Strings

```python
# Dividindo strings
frase = "Python,Java,JavaScript,C++"
linguagens = frase.split(",")      # Divide por vírgula
print(f"Linguagens: {linguagens}")

texto_palavras = "Python é uma linguagem de programação"
palavras = texto_palavras.split()  # Divide por espaços
print(f"Palavras: {palavras}")

# Juntando strings
lista_frutas = ["maçã", "banana", "uva", "laranja"]
frutas_texto = ", ".join(lista_frutas)  # Junta com vírgula e espaço
print(f"Frutas: {frutas_texto}")

# Criando uma frase
palavras_frase = ["Python", "é", "fantástico"]
frase_completa = " ".join(palavras_frase)
print(f"Frase: {frase_completa}")
```

### Verificações e Buscas

```python
email = "usuario@exemplo.com"
senha = "MinhaSenh@123"

# Verificações de conteúdo
tem_arroba = "@" in email          # True
tem_ponto = "." in email           # True
print(f"Email válido (básico): {tem_arroba and tem_ponto}")

# Verificações de tipo de caractere
eh_numerico = "123".isdigit()      # True
eh_alfabetico = "abc".isalpha()    # True
eh_alfanumerico = "abc123".isalnum()  # True
print(f"'123' é numérico: {eh_numerico}")

# Buscas
posicao_arroba = email.find("@")   # Posição do @
comeca_com = email.startswith("usuario")  # True
termina_com = email.endswith(".com")      # True
print(f"Posição do @: {posicao_arroba}")
print(f"Começa com 'usuario': {comeca_com}")
```

### Formatação Avançada

```python
# Dados para formatação
nome = "Ana Silva"
idade = 28
salario = 4500.75
aprovacao = 0.856

# F-strings com formatação
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario:.2f}")           # 2 casas decimais
print(f"Taxa de aprovação: {aprovacao:.1%}")  # Porcentagem com 1 casa

# Alinhamento e preenchimento
print(f"{'Nome':<15} {'Idade':>5} {'Salário':>10}")  # Cabeçalho alinhado
print(f"{nome:<15} {idade:>5} {salario:>10.2f}")     # Dados alinhados

# Formatação de números
numero_grande = 1234567
print(f"Número formatado: {numero_grande:,}")         # Com separadores
print(f"Número com zeros: {42:05d}")                  # 00042
```

## 9. Trabalhando com Arquivos

### Analogia: Arquivos como Gavetas de Documentos
Trabalhar com arquivos é como organizar documentos em gavetas - você pode criar novos documentos, ler os existentes, adicionar informações ou reorganizar tudo.

### Escrevendo em Arquivos

```python
# Criando e escrevendo em arquivo (sobrescreve se existir)
with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha do arquivo.\n")
    arquivo.write("Segunda linha do arquivo.\n")
    arquivo.write("Terceira linha do arquivo.\n")

print("Arquivo criado com sucesso!")

# Adicionando ao arquivo existente
with open("meu_arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Linha adicionada posteriormente.\n")
    arquivo.write("Mais uma linha adicionada.\n")

print("Conteúdo adicionado ao arquivo!")
```

### Lendo Arquivos

```python
# Lendo arquivo completo
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo_completo = arquivo.read()
    print("=== Conteúdo Completo ===")
    print(conteudo_completo)

# Lendo linha por linha
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    print("\n=== Linha por Linha ===")
    numero_linha = 1
    for linha in arquivo:
        print(f"Linha {numero_linha}: {linha.strip()}")  # strip() remove \n
        numero_linha += 1

# Lendo todas as linhas em uma lista
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print(f"\n=== Total de linhas: {len(linhas)} ===")
    for i, linha in enumerate(linhas, 1):
        print(f"{i}: {linha.strip()}")
```

### Tratamento de Erros com Arquivos

```python
def ler_arquivo_seguro(nome_arquivo):
    """Lê arquivo com tratamento de erros"""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado!")
        return None
    except PermissionError:
        print(f"Erro: Sem permissão para ler '{nome_arquivo}'!")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

# Testando a função
conteudo = ler_arquivo_seguro("arquivo_inexistente.txt")
if conteudo:
    print(conteudo)
else:
    print("Não foi possível ler o arquivo.")
```

### Exemplo Prático: Sistema de Notas

```python
def salvar_notas(nome_arquivo, notas_dict):
    """Salva notas dos alunos em arquivo"""
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("=== BOLETIM ESCOLAR ===\n")
        arquivo.write(f"{'Nome':<20} {'Nota':>6} {'Status':>10}\n")
        arquivo.write("-" * 40 + "\n")
        
        for nome, nota in notas_dict.items():
            status = "Aprovado" if nota >= 7 else "Reprovado"
            arquivo.write(f"{nome:<20} {nota:>6.1f} {status:>10}\n")

def carregar_e_mostrar_notas(nome_arquivo):
    """Carrega e exibe notas do arquivo"""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo de notas não encontrado!")

# Exemplo de uso
notas_turma = {
    "Ana Silva": 8.5,
    "João Santos": 6.2,
    "Maria Oliveira": 9.1,
    "Pedro Costa": 7.8,
    "Carla Souza": 5.9
}

# Salvar notas
salvar_notas("boletim.txt", notas_turma)
print("Boletim salvo com sucesso!")

# Carregar e mostrar
print("\n=== CONTEÚDO DO BOLETIM ===")
carregar_e_mostrar_notas("boletim.txt")
```

## 10. Bibliotecas Úteis

### Analogia: Bibliotecas como Caixas de Ferramentas Especializadas
As bibliotecas são como caixas de ferramentas especializadas - cada uma contém ferramentas específicas para diferentes tipos de trabalho.

### Biblioteca math - Matemática Avançada

```python
import math

# Constantes matemáticas
print(f"Pi: {math.pi:.4f}")
print(f"Euler (e): {math.e:.4f}")

# Funções básicas
numero = 16
print(f"Raiz quadrada de {numero}: {math.sqrt(numero)}")
print(f"Logaritmo natural de {numero}: {math.log(numero):.2f}")
print(f"Logaritmo base 10 de {numero}: {math.log10(numero):.2f}")

# Funções trigonométricas (em radianos)
angulo_graus = 45
angulo_radianos = math.radians(angulo_graus)  # Converte graus para radianos
print(f"Seno de {angulo_graus}°: {math.sin(angulo_radianos):.4f}")
print(f"Cosseno de {angulo_graus}°: {math.cos(angulo_radianos):.4f}")

# Arredondamentos especiais
valor = 3.7
print(f"Teto de {valor}: {math.ceil(valor)}")    # Arredonda para cima
print(f"Piso de {valor}: {math.floor(valor)}")   # Arredonda para baixo
```

### Biblioteca random - Números Aleatórios

```python
import random

# Número aleatório entre 0 e 1
aleatorio = random.random()
print(f"Número aleatório: {aleatorio:.4f}")

# Número inteiro aleatório em um intervalo
dado = random.randint(1, 6)  # Simula um dado
print(f"Resultado do dado: {dado}")

# Escolha aleatória de uma lista
cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
cor_escolhida = random.choice(cores)
print(f"Cor escolhida: {cor_escolhida}")

# Embaralhar uma lista
cartas = ["A", "K", "Q", "J", "10", "9", "8", "7"]
random.shuffle(cartas)  # Modifica a lista original
print(f"Cartas embaralhadas: {cartas}")

# Amostra aleatória (sem repetição)
numeros_loteria = random.sample(range(1, 61), 6)  # 6 números de 1 a 60
numeros_loteria.sort()
print(f"Números da loteria: {numeros_loteria}")
```

### Biblioteca datetime - Datas e Horas

```python
from datetime import datetime, date, time, timedelta

# Data e hora atual
agora = datetime.now()
print(f"Data e hora atual: {agora}")
print(f"Formatado: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# Apenas data
hoje = date.today()
print(f"Data de hoje: {hoje}")
print(f"Ano: {hoje.year}, Mês: {hoje.month}, Dia: {hoje.day}")

# Criando datas específicas
natal = date(2024, 12, 25)
print(f"Natal 2024: {natal}")

# Calculando diferenças
diferenca = natal - hoje
print(f"Dias até o Natal: {diferenca.days}")

# Adicionando/subtraindo tempo
daqui_uma_semana = hoje + timedelta(days=7)
mes_passado = hoje - timedelta(days=30)
print(f"Daqui uma semana: {daqui_uma_semana}")
print(f"Há um mês: {mes_passado}")

# Formatação personalizada
print(f"Hoje por extenso: {hoje.strftime('%A, %d de %B de %Y')}")
```

### Exemplo Prático: Gerador de Senhas Seguras

```python
import random
import string

def gerar_senha(tamanho=12, incluir_simbolos=True):
    """
    Gera uma senha aleatória segura
    tamanho: comprimento da senha
    incluir_simbolos: se deve incluir símbolos especiais
    """
    # Caracteres disponíveis
    letras_min = string.ascii_lowercase      # a-z
    letras_mai = string.ascii_uppercase      # A-Z
    numeros = string.digits                  # 0-9
    simbolos = "!@#$%&*"                    # Símbolos seguros
    
    # Monta conjunto de caracteres
    caracteres = letras_min + letras_mai + numeros
    if incluir_simbolos:
        caracteres += simbolos
    
    # Garante pelo menos um de cada tipo
    senha = []
    senha.append(random.choice(letras_min))  # Pelo menos uma minúscula
    senha.append(random.choice(letras_mai))  # Pelo menos uma maiúscula
    senha.append(random.choice(numeros))     # Pelo menos um número
    
    if incluir_simbolos:
        senha.append(random.choice(simbolos))  # Pelo menos um símbolo
    
    # Completa o resto da senha
    for _ in range(tamanho - len(senha)):
        senha.append(random.choice(caracteres))
    
    # Embaralha para não ter padrão
    random.shuffle(senha)
    
    return ''.join(senha)

# Testando o gerador
print("=== GERADOR DE SENHAS ===")
for i in range(3):
    senha = gerar_senha(12, True)
    print(f"Senha {i+1}: {senha}")

# Senha sem símbolos
senha_simples = gerar_senha(8, False)
print(f"Senha simples: {senha_simples}")
```

## 11. Exercícios de Fixação Expandidos

### Exercício 1: Calculadora Básica
```python
def calculadora():
    """Calculadora com as quatro operações básicas"""
    print("=== CALCULADORA ===")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero!")
                return
        else:
            print("Operação inválida!")
            return
        
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        
    except ValueError:
        print("Erro: Digite apenas números!")

calculadora()
```

### Exercício 2: Analisador de Lista
```python
def analisar_lista():
    """Analisa uma lista de números fornecida pelo usuário"""
    numeros = []
    
    print("Digite números (digite 'fim' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Digite um número válido ou 'fim'!")
    
    if not numeros:
        print("Nenhum número foi inserido!")
        return
    
    # Análises
    quantidade = len(numeros)
    soma = sum(numeros)
    media = soma / quantidade
    maior = max(numeros)
    menor = min(numeros)
    
    print(f"\n=== ANÁLISE ===")
    print(f"Números inseridos: {numeros}")
    print(f"Quantidade: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

analisar_lista()
```

### Exercício 3: Verificador de Palíndromo
```python
def eh_palindromo(texto):
    """Verifica se um texto é palíndromo (lê igual de trás para frente)"""
    # Remove espaços e converte para minúsculo
    texto_limpo = texto.replace(" ", "").lower()
    
    # Remove acentos e caracteres especiais (versão simples)
    texto_limpo = ''.join(c for c in texto_limpo if c.isalnum())
    
    # Compara com o reverso
    return texto_limpo == texto_limpo[::-1]

def testar_palindromos():
    """Testa vários exemplos de palíndromos"""
    exemplos = [
        "arara",
        "A base do teto desaba",
        "Anotaram a data da maratona",
        "python",
        "12321",
        "A grama é amarga"
    ]
    
    print("=== TESTE DE PALÍNDROMOS ===")
    for exemplo in exemplos:
        resultado = eh_palindromo(exemplo)
        status = "✓ É palíndromo" if resultado else "✗ Não é palíndromo"
        print(f"'{exemplo}' → {status}")

testar_palindromos()
```

### Exercício 4: Sistema de Cadastro
```python
def sistema_cadastro():
    """Sistema simples de cadastro de pessoas"""
    pessoas = []
    
    while True:
        print("\n=== SISTEMA DE CADASTRO ===")
        print("1. Adicionar pessoa")
        print("2. Listar pessoas")
        print("3. Buscar pessoa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            email = input("Email: ")
            
            pessoa = {
                "nome": nome,
                "idade": idade,
                "email": email
            }
            pessoas.append(pessoa)
            print(f"✓ {nome} cadastrado com sucesso!")
            
        elif opcao == "2":
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
            else:
                print(f"\n=== LISTA DE PESSOAS ({len(pessoas)}) ===")
                for i, pessoa in enumerate(pessoas, 1):
                    print(f"{i}. {pessoa['nome']} - {pessoa['idade']} anos - {pessoa['email']}")
                    
        elif opcao == "3":
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
            else:
                busca = input("Digite o nome para buscar: ").lower()
                encontrados = [p for p in pessoas if busca in p['nome'].lower()]
                
                if encontrados:
                    print(f"\n=== RESULTADOS DA BUSCA ===")
                    for pessoa in encontrados:
                        print(f"Nome: {pessoa['nome']}")
                        print(f"Idade: {pessoa['idade']} anos")
                        print(f"Email: {pessoa['email']}")
                        print("-" * 30)
                else:
                    print("Nenhuma pessoa encontrada.")
                    
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

sistema_cadastro()
```

## ✅ Conclusão

Este material expandido cobriu os fundamentos essenciais do Python com explicações detalhadas, analogias práticas e exemplos comentados. Os principais tópicos abordados foram:

1. **Fundamentos**: Tipos de dados, operadores e estruturas básicas
2. **Controle de Fluxo**: Condicionais e loops para controlar a execução
3. **Funções**: Organização e reutilização de código
4. **Estruturas de Dados**: Listas para armazenar e manipular coleções
5. **Entrada/Saída**: Interação com o usuário e formatação
6. **Strings**: Manipulação e processamento de texto
7. **Arquivos**: Persistência de dados
8. **Bibliotecas**: Ferramentas especializadas para tarefas específicas

### Próximos Passos

Com essa base sólida, você pode avançar para tópicos mais avançados:

- **Orientação a Objetos**: Classes, objetos, herança
- **Tratamento de Erros**: Try/except, debugging
- **Módulos e Pacotes**: Organização de código em projetos maiores
- **Bibliotecas Externas**: Pandas, NumPy, Requests, Flask
- **Banco de Dados**: SQLite, PostgreSQL
- **Desenvolvimento Web**: Django, Flask, FastAPI

### Dicas para Continuar Aprendendo

1. **Pratique regularmente**: Código todos os dias, mesmo que por pouco tempo
2. **Faça projetos**: Aplique o conhecimento em projetos pessoais
3. **Leia código de outros**: Explore repositórios no GitHub
4. **Participe da comunidade**: Fóruns, grupos, eventos
5. **Documente seu aprendizado**: Mantenha um registro do que aprendeu

**Lembre-se**: Programação é uma habilidade prática - quanto mais você pratica, melhor fica!