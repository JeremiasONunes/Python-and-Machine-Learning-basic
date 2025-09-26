# Aula 04 - Tópico 2: Parâmetros Avançados e Múltiplos Retornos
# Demonstração de *args, **kwargs e múltiplos retornos

print("=== PARÂMETROS AVANÇADOS ===\n")

# Função com *args (argumentos posicionais variáveis)
def calcular_media(*notas):
    """Calcula média de notas variáveis"""
    if not notas:
        return 0
    return sum(notas) / len(notas)

# Função com **kwargs (argumentos nomeados variáveis)
def criar_paciente(**dados):
    """Cria dicionário de paciente com dados flexíveis"""
    paciente = {
        "nome": dados.get("nome", "Não informado"),
        "idade": dados.get("idade", 0),
        "telefone": dados.get("telefone", "Não informado")
    }
    
    # Adiciona dados extras
    for chave, valor in dados.items():
        if chave not in paciente:
            paciente[chave] = valor
    
    return paciente

# Função com *args e **kwargs
def processar_consultas(*consultas, **opcoes):
    """Processa lista de consultas com opções flexíveis"""
    total = len(consultas)
    
    if opcoes.get("mostrar_detalhes", False):
        for i, consulta in enumerate(consultas, 1):
            print(f"{i}. {consulta}")
    
    if opcoes.get("calcular_receita", False):
        receita = sum(opcoes.get("valor_padrao", 150) for _ in consultas)
        return total, receita
    
    return total

# Função com múltiplos retornos
def analisar_idades(*idades):
    """Analisa lista de idades e retorna estatísticas"""
    if not idades:
        return 0, 0, 0, 0
    
    media = sum(idades) / len(idades)
    minima = min(idades)
    maxima = max(idades)
    total = len(idades)
    
    return media, minima, maxima, total

# Função que retorna dicionário
def estatisticas_pacientes(pacientes_data):
    """Retorna estatísticas completas dos pacientes"""
    if not pacientes_data:
        return {"erro": "Nenhum dado fornecido"}
    
    idades = [p["idade"] for p in pacientes_data if "idade" in p]
    
    return {
        "total_pacientes": len(pacientes_data),
        "idade_media": sum(idades) / len(idades) if idades else 0,
        "idade_min": min(idades) if idades else 0,
        "idade_max": max(idades) if idades else 0
    }

# Testando as funções
print("=== TESTANDO FUNÇÕES ===")

# *args
media1 = calcular_media(8.5, 7.0, 9.2)
media2 = calcular_media(6.0, 7.5, 8.0, 9.0, 7.8)
print(f"Média 1: {media1:.2f}")
print(f"Média 2: {media2:.2f}")

# **kwargs
paciente1 = criar_paciente(nome="Ana Silva", idade=25, telefone="(11) 99999-9999")
paciente2 = criar_paciente(nome="João Santos", idade=34, email="joao@email.com", profissao="Engenheiro")

print(f"Paciente 1: {paciente1}")
print(f"Paciente 2: {paciente2}")

# *args e **kwargs
consultas = ["Ana - Psicologia", "João - Psiquiatria", "Maria - Terapia"]

total1 = processar_consultas(*consultas)
total2, receita = processar_consultas(*consultas, calcular_receita=True, valor_padrao=180)

print(f"Total consultas: {total1}")
print(f"Total e receita: {total2}, R$ {receita}")

# Múltiplos retornos
idades = [25, 34, 28, 45, 67, 19, 52]
media, min_idade, max_idade, qtd = analisar_idades(*idades)

print(f"Análise: Média={media:.1f}, Min={min_idade}, Max={max_idade}, Total={qtd}")

# Retorno de dicionário
dados_pacientes = [
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 34},
    {"nome": "Maria", "idade": 28}
]

stats = estatisticas_pacientes(dados_pacientes)
print(f"Estatísticas: {stats}")