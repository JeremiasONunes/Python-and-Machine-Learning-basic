# Aula 04 - Tópico 1: Definição e Estrutura de Funções
# Demonstração de sintaxe básica de funções

print("=== FUNÇÕES BÁSICAS ===\n")

# Função simples sem parâmetros
def saudacao():
    """Exibe uma saudação simples"""
    print("Bem-vindo ao Sistema Lunysse!")

# Função com parâmetro
def saudar_paciente(nome):
    """Saúda um paciente específico"""
    print(f"Olá, {nome}! Como está se sentindo hoje?")

# Função com retorno
def calcular_idade(ano_nascimento):
    """Calcula idade baseada no ano de nascimento"""
    from datetime import datetime
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

# Função com múltiplos parâmetros
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal"""
    imc = peso / (altura ** 2)
    return round(imc, 2)

# Função com parâmetros padrão
def agendar_consulta(paciente, data, horario="14:00", tipo="Psicologia"):
    """Agenda uma consulta com valores padrão"""
    return {
        "paciente": paciente,
        "data": data,
        "horario": horario,
        "tipo": tipo
    }

# Função com documentação completa
def validar_telefone(telefone):
    """
    Valida formato de telefone brasileiro
    
    Args:
        telefone (str): Número de telefone no formato (XX) XXXXX-XXXX
    
    Returns:
        bool: True se válido, False caso contrário
    """
    import re
    padrao = r'\(\d{2}\) \d{5}-\d{4}'
    return bool(re.match(padrao, telefone))

# Testando as funções
print("=== TESTANDO FUNÇÕES ===")

# Função sem parâmetros
saudacao()

# Função com parâmetro
saudar_paciente("Ana Silva")

# Função com retorno
idade = calcular_idade(1990)
print(f"Idade calculada: {idade} anos")

# Múltiplos parâmetros
imc = calcular_imc(70, 1.75)
print(f"IMC calculado: {imc}")

# Parâmetros padrão
consulta1 = agendar_consulta("João Santos", "15/03/2024")
consulta2 = agendar_consulta("Maria Costa", "16/03/2024", "09:00", "Psiquiatria")

print(f"Consulta 1: {consulta1}")
print(f"Consulta 2: {consulta2}")

# Validação
telefone_valido = validar_telefone("(11) 99999-9999")
telefone_invalido = validar_telefone("11999999999")

print(f"Telefone válido: {telefone_valido}")
print(f"Telefone inválido: {telefone_invalido}")

# Chamadas com argumentos nomeados
consulta3 = agendar_consulta(
    paciente="Pedro Lima",
    data="17/03/2024",
    tipo="Terapia",
    horario="16:00"
)
print(f"Consulta 3: {consulta3}")

print("\n=== HELP DA FUNÇÃO ===")
help(calcular_imc)