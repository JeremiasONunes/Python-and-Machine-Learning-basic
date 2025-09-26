# Aula 03 - Atividade Prática 4: Sistema Integrado com Todas as Estruturas
# Sistema completo usando listas, dicionários, tuplas, conjuntos e list comprehension

from datetime import datetime, date
import random

print("=== SISTEMA LUNYSSE INTEGRADO ===\n")

# Configurações usando tuplas (imutáveis)
HORARIOS_FUNCIONAMENTO = (
    (8, 0), (9, 0), (10, 0), (11, 0),
    (14, 0), (15, 0), (16, 0), (17, 0)
)

DIAS_SEMANA = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

# Especialidades usando conjuntos
ESPECIALIDADES = {
    "Psicologia", "Psiquiatria", "Terapia Familiar", 
    "Neuropsicologia", "Terapia Cognitiva"
}

# Base de dados principal - lista de dicionários
pacientes_db = [
    {
        "id": "001",
        "nome": "Ana Silva",
        "idade": 25,
        "telefone": "(11) 99999-1111",
        "especialidade_preferida": "Psicologia",
        "consultas": [
            {"data": "15/03/2024", "tipo": "Psicologia", "valor": 150},
            {"data": "22/03/2024", "tipo": "Psicologia", "valor": 150}
        ]
    },
    {
        "id": "002", 
        "nome": "João Santos",
        "idade": 34,
        "telefone": "(11) 88888-2222",
        "especialidade_preferida": "Psiquiatria",
        "consultas": [
            {"data": "20/03/2024", "tipo": "Psiquiatria", "valor": 200}
        ]
    },
    {
        "id": "003",
        "nome": "Maria Costa", 
        "idade": 28,
        "telefone": "(11) 77777-3333",
        "especialidade_preferida": "Terapia Familiar",
        "consultas": []
    }
]

def formatar_horario(hora_tupla):
    """Converte tupla (hora, minuto) para string"""
    hora, minuto = hora_tupla
    return f"{hora:02d}:{minuto:02d}"

def filtrar_pacientes_por_idade(idade_min=0, idade_max=100):
    """Filtra pacientes por faixa etária usando list comprehension"""
    return [
        paciente for paciente in pacientes_db
        if idade_min <= paciente["idade"] <= idade_max
    ]

def buscar_pacientes_por_especialidade(especialidade):
    """Busca pacientes por especialidade preferida"""
    return [
        paciente for paciente in pacientes_db
        if paciente["especialidade_preferida"] == especialidade
    ]

def calcular_receita_total():
    """Calcula receita total usando list comprehension aninhada"""
    return sum(
        consulta["valor"]
        for paciente in pacientes_db
        for consulta in paciente["consultas"]
    )

def obter_especialidades_ativas():
    """Retorna conjunto de especialidades que têm pacientes"""
    return {
        paciente["especialidade_preferida"]
        for paciente in pacientes_db
    }

def gerar_relatorio_completo():
    """Gera relatório completo usando todas as estruturas"""
    print("📊 RELATÓRIO COMPLETO DO SISTEMA")
    print("=" * 60)
    
    # Estatísticas gerais
    total_pacientes = len(pacientes_db)
    total_consultas = sum(len(p["consultas"]) for p in pacientes_db)
    receita_total = calcular_receita_total()
    
    print(f"Total de pacientes: {total_pacientes}")
    print(f"Total de consultas: {total_consultas}")
    print(f"Receita total: R$ {receita_total:.2f}")
    
    # Análise por faixa etária usando list comprehension
    jovens = len(filtrar_pacientes_por_idade(0, 29))
    adultos = len(filtrar_pacientes_por_idade(30, 59))
    idosos = len(filtrar_pacientes_por_idade(60, 100))
    
    print(f"\n👥 DISTRIBUIÇÃO POR IDADE:")
    print(f"Jovens (0-29): {jovens}")
    print(f"Adultos (30-59): {adultos}")
    print(f"Idosos (60+): {idosos}")
    
    # Especialidades mais procuradas
    contador_especialidades = {}
    for paciente in pacientes_db:
        esp = paciente["especialidade_preferida"]
        contador_especialidades[esp] = contador_especialidades.get(esp, 0) + 1
    
    print(f"\n🏥 ESPECIALIDADES MAIS PROCURADAS:")
    for esp, qtd in sorted(contador_especialidades.items(), key=lambda x: x[1], reverse=True):
        print(f"{esp}: {qtd} paciente(s)")
    
    # Receita por especialidade usando dict comprehension
    receita_por_esp = {
        esp: sum(
            consulta["valor"]
            for paciente in pacientes_db
            if paciente["especialidade_preferida"] == esp
            for consulta in paciente["consultas"]
        )
        for esp in obter_especialidades_ativas()
    }
    
    print(f"\n💰 RECEITA POR ESPECIALIDADE:")
    for esp, receita in receita_por_esp.items():
        print(f"{esp}: R$ {receita:.2f}")

def listar_pacientes_filtrado():
    """Lista pacientes com filtros usando list comprehension"""
    print("\n🔍 FILTROS DISPONÍVEIS:")
    print("1. Todos os pacientes")
    print("2. Jovens (até 29 anos)")
    print("3. Adultos (30-59 anos)")
    print("4. Idosos (60+ anos)")
    print("5. Por especialidade")
    
    opcao = input("Escolha um filtro (1-5): ")
    
    if opcao == "1":
        pacientes_filtrados = pacientes_db
        titulo = "TODOS OS PACIENTES"
    elif opcao == "2":
        pacientes_filtrados = filtrar_pacientes_por_idade(0, 29)
        titulo = "PACIENTES JOVENS"
    elif opcao == "3":
        pacientes_filtrados = filtrar_pacientes_por_idade(30, 59)
        titulo = "PACIENTES ADULTOS"
    elif opcao == "4":
        pacientes_filtrados = filtrar_pacientes_por_idade(60, 100)
        titulo = "PACIENTES IDOSOS"
    elif opcao == "5":
        print("\nEspecialidades disponíveis:")
        for i, esp in enumerate(sorted(ESPECIALIDADES), 1):
            print(f"{i}. {esp}")
        
        try:
            esp_idx = int(input("Escolha uma especialidade: ")) - 1
            especialidades_lista = sorted(ESPECIALIDADES)
            
            if 0 <= esp_idx < len(especialidades_lista):
                esp_escolhida = especialidades_lista[esp_idx]
                pacientes_filtrados = buscar_pacientes_por_especialidade(esp_escolhida)
                titulo = f"PACIENTES DE {esp_escolhida.upper()}"
            else:
                print("❌ Opção inválida!")
                return
        except ValueError:
            print("❌ Digite um número válido!")
            return
    else:
        print("❌ Opção inválida!")
        return
    
    # Exibe resultados
    print(f"\n📋 {titulo} ({len(pacientes_filtrados)}):")
    print("-" * 60)
    
    if not pacientes_filtrados:
        print("Nenhum paciente encontrado com os critérios selecionados.")
        return
    
    for paciente in pacientes_filtrados:
        consultas_qtd = len(paciente["consultas"])
        print(f"ID: {paciente['id']} | {paciente['nome']} ({paciente['idade']} anos)")
        print(f"  Especialidade: {paciente['especialidade_preferida']}")
        print(f"  Consultas: {consultas_qtd}")
        print("-" * 60)

def adicionar_paciente_interativo():
    """Adiciona novo paciente ao sistema"""
    print("\n➕ CADASTRO DE NOVO PACIENTE:")
    
    # Gerar novo ID
    ids_existentes = {int(p["id"]) for p in pacientes_db}
    novo_id = str(max(ids_existentes) + 1).zfill(3)
    
    nome = input("Nome completo: ")
    idade = int(input("Idade: "))
    telefone = input("Telefone: ")
    
    # Escolher especialidade
    print("\nEspecialidades disponíveis:")
    especialidades_lista = sorted(ESPECIALIDADES)
    for i, esp in enumerate(especialidades_lista, 1):
        print(f"{i}. {esp}")
    
    try:
        esp_idx = int(input("Escolha uma especialidade: ")) - 1
        if 0 <= esp_idx < len(especialidades_lista):
            especialidade = especialidades_lista[esp_idx]
        else:
            print("❌ Especialidade inválida! Usando Psicologia como padrão.")
            especialidade = "Psicologia"
    except ValueError:
        print("❌ Entrada inválida! Usando Psicologia como padrão.")
        especialidade = "Psicologia"
    
    # Criar novo paciente
    novo_paciente = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "especialidade_preferida": especialidade,
        "consultas": []
    }
    
    pacientes_db.append(novo_paciente)
    print(f"\n✅ Paciente {nome} cadastrado com ID: {novo_id}")

def buscar_pacientes_avancado():
    """Busca avançada usando múltiplos critérios"""
    termo = input("\n🔍 Digite parte do nome para buscar: ").lower()
    
    # Busca usando list comprehension
    resultados = [
        paciente for paciente in pacientes_db
        if termo in paciente["nome"].lower()
    ]
    
    if resultados:
        print(f"\n✅ Encontrados {len(resultados)} paciente(s):")
        for paciente in resultados:
            print(f"  {paciente['id']} - {paciente['nome']} ({paciente['especialidade_preferida']})")
    else:
        print("❌ Nenhum paciente encontrado.")

def menu_principal():
    """Menu principal do sistema integrado"""
    while True:
        print("\n" + "="*60)
        print("           SISTEMA LUNYSSE INTEGRADO")
        print("="*60)
        print("1. Relatório completo")
        print("2. Listar pacientes (com filtros)")
        print("3. Buscar pacientes")
        print("4. Cadastrar novo paciente")
        print("5. Estatísticas rápidas")
        print("6. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == "1":
            gerar_relatorio_completo()
        elif opcao == "2":
            listar_pacientes_filtrado()
        elif opcao == "3":
            buscar_pacientes_avancado()
        elif opcao == "4":
            adicionar_paciente_interativo()
        elif opcao == "5":
            # Estatísticas rápidas usando comprehensions
            print(f"\n⚡ ESTATÍSTICAS RÁPIDAS:")
            print(f"Pacientes cadastrados: {len(pacientes_db)}")
            print(f"Média de idade: {sum(p['idade'] for p in pacientes_db) / len(pacientes_db):.1f} anos")
            print(f"Especialidades ativas: {len(obter_especialidades_ativas())}")
            print(f"Receita total: R$ {calcular_receita_total():.2f}")
        elif opcao == "6":
            print("\n👋 Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida!")
        
        if opcao != "6":
            input("\nPressione Enter para continuar...")

# Executa o programa
if __name__ == "__main__":
    menu_principal()