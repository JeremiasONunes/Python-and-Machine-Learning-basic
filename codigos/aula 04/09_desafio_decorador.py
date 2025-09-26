# Aula 04 - Desafio: Decorador de Tempo de Execução
# Decorador simples para medir tempo de execução das funções

import time
import functools

print("=== DECORADOR DE TEMPO ===\n")

def medir_tempo(func):
    """
    Decorador que mede o tempo de execução de uma função
    
    Args:
        func: Função a ser decorada
    
    Returns:
        function: Função decorada
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        
        tempo_execucao = fim - inicio
        print(f"⏱️ {func.__name__} executou em {tempo_execucao:.4f} segundos")
        
        return resultado
    
    return wrapper

# Funções de exemplo para testar o decorador
@medir_tempo
def calcular_imc(peso, altura):
    """Calcula IMC com delay simulado"""
    time.sleep(0.1)  # Simula processamento
    return peso / (altura ** 2)

@medir_tempo
def processar_lista_pacientes(pacientes):
    """Processa lista de pacientes"""
    time.sleep(0.05)  # Simula processamento
    
    idades = [p["idade"] for p in pacientes]
    media = sum(idades) / len(idades)
    
    return {
        "total": len(pacientes),
        "idade_media": media,
        "idade_min": min(idades),
        "idade_max": max(idades)
    }

@medir_tempo
def buscar_paciente(pacientes, nome):
    """Busca paciente por nome"""
    time.sleep(0.02)  # Simula busca
    
    for paciente in pacientes:
        if nome.lower() in paciente["nome"].lower():
            return paciente
    
    return None

@medir_tempo
def calcular_receita_total(agendamentos):
    """Calcula receita total"""
    time.sleep(0.03)  # Simula cálculo
    
    return sum(ag["valor"] for ag in agendamentos if ag["status"] == "Concluída")

# Dados de teste
pacientes_teste = [
    {"nome": "Ana Silva", "idade": 25},
    {"nome": "João Santos", "idade": 34},
    {"nome": "Maria Costa", "idade": 28},
    {"nome": "Pedro Lima", "idade": 45},
    {"nome": "Carlos Souza", "idade": 67}
]

agendamentos_teste = [
    {"valor": 150, "status": "Concluída"},
    {"valor": 200, "status": "Concluída"},
    {"valor": 120, "status": "Cancelada"},
    {"valor": 180, "status": "Concluída"}
]

# Decorador com parâmetros (versão avançada)
def medir_tempo_detalhado(unidade="segundos"):
    """
    Decorador parametrizado para medir tempo
    
    Args:
        unidade: "segundos" ou "milissegundos"
    """
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fim = time.time()
            
            tempo = fim - inicio
            
            if unidade == "milissegundos":
                tempo *= 1000
                print(f"⏱️ {func.__name__} executou em {tempo:.2f} ms")
            else:
                print(f"⏱️ {func.__name__} executou em {tempo:.4f} s")
            
            return resultado
        
        return wrapper
    return decorador

@medir_tempo_detalhado("milissegundos")
def operacao_rapida():
    """Operação rápida medida em milissegundos"""
    return sum(range(1000))

# Testes
if __name__ == "__main__":
    print("=== TESTANDO DECORADOR ===")
    
    # Teste 1: Calcular IMC
    imc = calcular_imc(70, 1.75)
    print(f"IMC calculado: {imc:.2f}\n")
    
    # Teste 2: Processar pacientes
    stats = processar_lista_pacientes(pacientes_teste)
    print(f"Estatísticas: {stats}\n")
    
    # Teste 3: Buscar paciente
    paciente_encontrado = buscar_paciente(pacientes_teste, "Ana")
    print(f"Paciente encontrado: {paciente_encontrado}\n")
    
    # Teste 4: Calcular receita
    receita = calcular_receita_total(agendamentos_teste)
    print(f"Receita total: R$ {receita}\n")
    
    # Teste 5: Decorador parametrizado
    resultado = operacao_rapida()
    print(f"Resultado operação: {resultado}\n")
    
    print("✅ Todos os testes executados com medição de tempo!")
    
    # Demonstração sem decorador
    print("\n=== SEM DECORADOR (para comparação) ===")
    
    def calcular_imc_sem_decorador(peso, altura):
        return peso / (altura ** 2)
    
    inicio = time.time()
    imc_sem_decorador = calcular_imc_sem_decorador(70, 1.75)
    fim = time.time()
    
    print(f"Tempo manual: {fim - inicio:.4f} segundos")
    print(f"IMC: {imc_sem_decorador:.2f}")
    
    print("\n🎯 O decorador automatiza a medição de tempo!")