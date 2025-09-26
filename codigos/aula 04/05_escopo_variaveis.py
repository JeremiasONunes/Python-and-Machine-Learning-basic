# Aula 04 - Tópico 3: Escopo de Variáveis
# Demonstração de variáveis locais vs globais

print("=== ESCOPO DE VARIÁVEIS ===\n")

# Variáveis globais
contador_pacientes = 0
nome_clinica = "Clínica Lunysse"

def incrementar_contador():
    """Incrementa contador usando global"""
    global contador_pacientes
    contador_pacientes += 1
    print(f"Contador incrementado: {contador_pacientes}")

def mostrar_info_clinica():
    """Acessa variável global sem modificar"""
    print(f"Clínica: {nome_clinica}")
    print(f"Total de pacientes: {contador_pacientes}")

def exemplo_variavel_local():
    """Demonstra variável local"""
    nome_local = "Variável Local"
    contador_local = 10
    
    print(f"Dentro da função: {nome_local}")
    print(f"Contador local: {contador_local}")
    
    return contador_local

def exemplo_conflito_nomes():
    """Demonstra conflito entre variáveis locais e globais"""
    nome_clinica = "Clínica Local"  # Variável local
    
    print(f"Nome local: {nome_clinica}")
    print(f"Contador global: {contador_pacientes}")

def calcular_com_parametros(valor1, valor2):
    """Parâmetros são variáveis locais"""
    resultado = valor1 + valor2  # Variável local
    
    print(f"Parâmetros (locais): {valor1}, {valor2}")
    print(f"Resultado (local): {resultado}")
    
    return resultado

def funcao_aninhada_exemplo():
    """Demonstra função aninhada e escopo"""
    variavel_externa = "Externa"
    
    def funcao_interna():
        variavel_interna = "Interna"
        print(f"Acesso à variável externa: {variavel_externa}")
        print(f"Variável interna: {variavel_interna}")
    
    funcao_interna()
    print(f"Variável externa: {variavel_externa}")
    # print(variavel_interna)  # Erro! Não existe neste escopo

def modificar_lista_global():
    """Demonstra modificação de lista global"""
    global lista_pacientes
    
    if 'lista_pacientes' not in globals():
        lista_pacientes = []
    
    lista_pacientes.append("Novo Paciente")
    print(f"Lista modificada: {lista_pacientes}")

# Testando escopo
print("=== TESTANDO ESCOPO ===")

print(f"Contador inicial: {contador_pacientes}")
print(f"Nome da clínica: {nome_clinica}")

# Incrementar contador
incrementar_contador()
incrementar_contador()

# Mostrar informações
mostrar_info_clinica()

# Variável local
valor_retornado = exemplo_variavel_local()
print(f"Valor retornado: {valor_retornado}")

# Conflito de nomes
print("\n--- Conflito de nomes ---")
exemplo_conflito_nomes()
print(f"Nome global ainda é: {nome_clinica}")

# Parâmetros como variáveis locais
print("\n--- Parâmetros locais ---")
resultado = calcular_com_parametros(10, 20)

# Função aninhada
print("\n--- Função aninhada ---")
funcao_aninhada_exemplo()

# Modificar lista global
print("\n--- Lista global ---")
modificar_lista_global()
modificar_lista_global()

print(f"\nContador final: {contador_pacientes}")

# Demonstração de erro de escopo
def demonstrar_erro():
    """Demonstra erro de acesso a variável local"""
    try:
        print(variavel_inexistente)  # Erro!
    except NameError as e:
        print(f"Erro de escopo: {e}")

demonstrar_erro()