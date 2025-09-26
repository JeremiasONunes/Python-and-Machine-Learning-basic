# Aula 04 - Atividade Prática 2: Processador Estatístico Flexível
# Funções flexíveis para processar dados médicos com estatísticas completas

import math

def processar_dados_pacientes(*dados, **opcoes):
    """
    Processa dados de pacientes com opções flexíveis
    
    Args:
        *dados: Lista de idades ou dicionários de pacientes
        **opcoes: Opções de processamento
    
    Returns:
        dict: Estatísticas processadas
    """
    # Extrai idades dos dados
    idades = []
    for item in dados:
        if isinstance(item, (int, float)):
            idades.append(item)
        elif isinstance(item, dict) and "idade" in item:
            idades.append(item["idade"])
    
    if not idades:
        return {"erro": "Nenhuma idade válida encontrada"}
    
    # Calcula estatísticas básicas
    resultado = {
        "total": len(idades),
        "media": sum(idades) / len(idades),
        "minima": min(idades),
        "maxima": max(idades)
    }
    
    # Opções adicionais
    if opcoes.get("calcular_mediana", False):
        idades_ordenadas = sorted(idades)
        n = len(idades_ordenadas)
        if n % 2 == 0:
            resultado["mediana"] = (idades_ordenadas[n//2-1] + idades_ordenadas[n//2]) / 2
        else:
            resultado["mediana"] = idades_ordenadas[n//2]
    
    if opcoes.get("calcular_desvio", False):
        media = resultado["media"]
        variancia = sum((x - media) ** 2 for x in idades) / len(idades)
        resultado["desvio_padrao"] = math.sqrt(variancia)
    
    if opcoes.get("classificar_idades", False):
        resultado["classificacao"] = classificar_por_faixa_etaria(idades)
    
    return resultado

def classificar_por_faixa_etaria(idades):
    """Classifica idades por faixa etária"""
    classificacao = {
        "jovens": 0,      # 18-29
        "adultos": 0,     # 30-59
        "idosos": 0       # 60+
    }
    
    for idade in idades:
        if 18 <= idade <= 29:
            classificacao["jovens"] += 1
        elif 30 <= idade <= 59:
            classificacao["adultos"] += 1
        elif idade >= 60:
            classificacao["idosos"] += 1
    
    return classificacao

def analisar_consultas(*consultas, **filtros):
    """
    Analisa dados de consultas com filtros opcionais
    
    Args:
        *consultas: Lista de dicionários de consultas
        **filtros: Filtros para aplicar
    
    Returns:
        tuple: (total_filtrado, receita_total, consultas_filtradas)
    """
    consultas_filtradas = list(consultas)
    
    # Aplica filtros
    if "tipo" in filtros:
        consultas_filtradas = [c for c in consultas_filtradas if c.get("tipo") == filtros["tipo"]]
    
    if "valor_minimo" in filtros:
        consultas_filtradas = [c for c in consultas_filtradas if c.get("valor", 0) >= filtros["valor_minimo"]]
    
    if "status" in filtros:
        consultas_filtradas = [c for c in consultas_filtradas if c.get("status") == filtros["status"]]
    
    # Calcula totais
    total = len(consultas_filtradas)
    receita = sum(c.get("valor", 0) for c in consultas_filtradas)
    
    return total, receita, consultas_filtradas

# Dados de teste
pacientes_teste = [
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 34},
    {"nome": "Maria", "idade": 28},
    {"nome": "Pedro", "idade": 45},
    {"nome": "Carlos", "idade": 67}
]

consultas_teste = [
    {"paciente": "Ana", "tipo": "Psicologia", "valor": 150, "status": "Concluída"},
    {"paciente": "João", "tipo": "Psiquiatria", "valor": 200, "status": "Concluída"},
    {"paciente": "Maria", "tipo": "Psicologia", "valor": 150, "status": "Cancelada"},
    {"paciente": "Pedro", "tipo": "Terapia", "valor": 120, "status": "Concluída"}
]

# Testes
if __name__ == "__main__":
    print("=== PROCESSADOR ESTATÍSTICO ===\n")
    
    # Teste com idades diretas
    stats1 = processar_dados_pacientes(25, 34, 28, 45, 67, calcular_mediana=True)
    print(f"Estatísticas básicas: {stats1}")
    
    # Teste com dicionários de pacientes
    stats2 = processar_dados_pacientes(*pacientes_teste, calcular_desvio=True, classificar_idades=True)
    print(f"Estatísticas completas: {stats2}")
    
    # Teste análise de consultas
    total, receita, filtradas = analisar_consultas(*consultas_teste, status="Concluída")
    print(f"Consultas concluídas: {total}, Receita: R$ {receita}")
    
    # Teste com filtro por tipo
    total_psi, receita_psi, _ = analisar_consultas(*consultas_teste, tipo="Psicologia")
    print(f"Consultas Psicologia: {total_psi}, Receita: R$ {receita_psi}")