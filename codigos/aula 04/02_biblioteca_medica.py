# Aula 04 - Atividade Prática 1: Biblioteca de Funções para Cálculos Médicos
# Funções utilitárias para cálculos médicos com documentação completa

from datetime import datetime, date

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC)
    
    Args:
        peso (float): Peso em quilogramas
        altura (float): Altura em metros
    
    Returns:
        tuple: (imc, classificacao)
    """
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    return round(imc, 2), classificacao

def calcular_idade(data_nascimento):
    """
    Calcula idade a partir da data de nascimento
    
    Args:
        data_nascimento (str): Data no formato DD/MM/AAAA
    
    Returns:
        int: Idade em anos
    """
    dia, mes, ano = map(int, data_nascimento.split('/'))
    nascimento = date(ano, mes, dia)
    hoje = date.today()
    
    idade = hoje.year - nascimento.year
    if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
        idade -= 1
    
    return idade

def validar_cpf(cpf):
    """
    Valida formato básico de CPF
    
    Args:
        cpf (str): CPF no formato XXX.XXX.XXX-XX
    
    Returns:
        bool: True se formato válido
    """
    import re
    padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    return bool(re.match(padrao, cpf))

def calcular_frequencia_cardiaca_maxima(idade, genero="M"):
    """
    Calcula frequência cardíaca máxima
    
    Args:
        idade (int): Idade em anos
        genero (str): "M" para masculino, "F" para feminino
    
    Returns:
        int: Frequência cardíaca máxima
    """
    if genero.upper() == "F":
        return int(226 - idade)
    else:
        return int(220 - idade)

def classificar_pressao(sistolica, diastolica):
    """
    Classifica pressão arterial
    
    Args:
        sistolica (int): Pressão sistólica
        diastolica (int): Pressão diastólica
    
    Returns:
        str: Classificação da pressão
    """
    if sistolica < 120 and diastolica < 80:
        return "Normal"
    elif sistolica < 130 and diastolica < 80:
        return "Elevada"
    elif sistolica < 140 or diastolica < 90:
        return "Hipertensão Estágio 1"
    else:
        return "Hipertensão Estágio 2"

# Teste das funções
if __name__ == "__main__":
    print("=== BIBLIOTECA MÉDICA - TESTES ===\n")
    
    # Teste IMC
    imc, classe = calcular_imc(70, 1.75)
    print(f"IMC: {imc} - {classe}")
    
    # Teste idade
    idade = calcular_idade("15/05/1990")
    print(f"Idade: {idade} anos")
    
    # Teste CPF
    cpf_valido = validar_cpf("123.456.789-00")
    print(f"CPF válido: {cpf_valido}")
    
    # Teste frequência cardíaca
    fc_max = calcular_frequencia_cardiaca_maxima(30, "M")
    print(f"FC máxima: {fc_max} bpm")
    
    # Teste pressão
    pressao = classificar_pressao(120, 80)
    print(f"Pressão: {pressao}")