# Aula 03 - Desafio: Sistema de Relatórios Avançado
# Sistema que combina todas as estruturas para gerar relatórios estatísticos

from datetime import datetime, timedelta
import random

print("=== SISTEMA DE RELATÓRIOS LUNYSSE ===\n")

# Dados simulados mais complexos
pacientes_completos = [
    {
        "id": "001",
        "nome": "Ana Silva",
        "idade": 25,
        "cidade": "São Paulo",
        "especialidade": "Psicologia",
        "consultas": [
            {"data": "01/03/2024", "valor": 150, "duracao": 60, "status": "Concluída"},
            {"data": "08/03/2024", "valor": 150, "duracao": 60, "status": "Concluída"},
            {"data": "15/03/2024", "valor": 150, "duracao": 60, "status": "Agendada"}
        ]
    },
    {
        "id": "002",
        "nome": "João Santos", 
        "idade": 34,
        "cidade": "Rio de Janeiro",
        "especialidade": "Psiquiatria",
        "consultas": [
            {"data": "05/03/2024", "valor": 200, "duracao": 45, "status": "Concluída"},
            {"data": "12/03/2024", "valor": 200, "duracao": 45, "status": "Cancelada"},
            {"data": "19/03/2024", "valor": 200, "duracao": 45, "status": "Agendada"}
        ]
    },
    {
        "id": "003",
        "nome": "Maria Costa",
        "idade": 28,
        "cidade": "São Paulo", 
        "especialidade": "Terapia Familiar",
        "consultas": [
            {"data": "03/03/2024", "valor": 120, "duracao": 50, "status": "Concluída"},
            {"data": "10/03/2024", "valor": 120, "duracao": 50, "status": "Concluída"}
        ]
    },
    {
        "id": "004",
        "nome": "Pedro Lima",
        "idade": 45,
        "cidade": "Belo Horizonte",
        "especialidade": "Neuropsicologia",
        "consultas": [
            {"data": "07/03/2024", "valor": 180, "duracao": 90, "status": "Concluída"}
        ]
    },
    {
        "id": "005",
        "nome": "Carlos Souza",
        "idade": 67,
        "cidade": "São Paulo",
        "especialidade": "Psicologia", 
        "consultas": [
            {"data": "04/03/2024", "valor": 150, "duracao": 60, "status": "Concluída"},
            {"data": "11/03/2024", "valor": 150, "duracao": 60, "status": "Concluída"},
            {"data": "18/03/2024", "valor": 150, "duracao": 60, "status": "Faltou"}
        ]
    }
]

def relatorio_financeiro():
    """Relatório financeiro detalhado"""
    print("💰 RELATÓRIO FINANCEIRO")
    print("=" * 50)
    
    # Receita por status usando dict comprehension
    receita_por_status = {
        status: sum(
            consulta["valor"]
            for paciente in pacientes_completos
            for consulta in paciente["consultas"]
            if consulta["status"] == status
        )
        for status in {"Concluída", "Agendada", "Cancelada", "Faltou"}
    }
    
    # Receita total realizada (apenas concluídas)
    receita_realizada = receita_por_status["Concluída"]
    receita_potencial = sum(receita_por_status.values())
    
    print(f"Receita realizada: R$ {receita_realizada:.2f}")
    print(f"Receita potencial: R$ {receita_potencial:.2f}")
    print(f"Taxa de conversão: {(receita_realizada/receita_potencial)*100:.1f}%")
    
    print(f"\nDetalhamento por status:")
    for status, valor in receita_por_status.items():
        if valor > 0:
            print(f"  {status}: R$ {valor:.2f}")
    
    # Receita por especialidade
    especialidades_receita = {}
    for paciente in pacientes_completos:
        esp = paciente["especialidade"]
        receita_esp = sum(
            consulta["valor"] 
            for consulta in paciente["consultas"]
            if consulta["status"] == "Concluída"
        )
        especialidades_receita[esp] = especialidades_receita.get(esp, 0) + receita_esp
    
    print(f"\nReceita por especialidade:")
    for esp, receita in sorted(especialidades_receita.items(), key=lambda x: x[1], reverse=True):
        print(f"  {esp}: R$ {receita:.2f}")

def relatorio_demografico():
    """Relatório demográfico dos pacientes"""
    print("\n👥 RELATÓRIO DEMOGRÁFICO")
    print("=" * 50)
    
    # Distribuição por faixa etária usando list comprehension
    faixas_etarias = {
        "Jovens (18-29)": len([p for p in pacientes_completos if 18 <= p["idade"] <= 29]),
        "Adultos (30-49)": len([p for p in pacientes_completos if 30 <= p["idade"] <= 49]),
        "Maduros (50-64)": len([p for p in pacientes_completos if 50 <= p["idade"] <= 64]),
        "Idosos (65+)": len([p for p in pacientes_completos if p["idade"] >= 65])
    }
    
    total_pacientes = len(pacientes_completos)
    
    print(f"Total de pacientes: {total_pacientes}")
    print(f"\nDistribuição por idade:")
    for faixa, qtd in faixas_etarias.items():
        percentual = (qtd / total_pacientes) * 100 if total_pacientes > 0 else 0
        print(f"  {faixa}: {qtd} ({percentual:.1f}%)")
    
    # Distribuição por cidade usando set e dict comprehension
    cidades = {paciente["cidade"] for paciente in pacientes_completos}
    distribuicao_cidades = {
        cidade: len([p for p in pacientes_completos if p["cidade"] == cidade])
        for cidade in cidades
    }
    
    print(f"\nDistribuição por cidade:")
    for cidade, qtd in sorted(distribuicao_cidades.items(), key=lambda x: x[1], reverse=True):
        percentual = (qtd / total_pacientes) * 100
        print(f"  {cidade}: {qtd} ({percentual:.1f}%)")
    
    # Idade média por especialidade
    print(f"\nIdade média por especialidade:")
    especialidades = {p["especialidade"] for p in pacientes_completos}
    
    for esp in sorted(especialidades):
        idades_esp = [p["idade"] for p in pacientes_completos if p["especialidade"] == esp]
        media_idade = sum(idades_esp) / len(idades_esp)
        print(f"  {esp}: {media_idade:.1f} anos")

def relatorio_operacional():
    """Relatório operacional de consultas"""
    print("\n📊 RELATÓRIO OPERACIONAL")
    print("=" * 50)
    
    # Estatísticas de consultas
    todas_consultas = [
        consulta for paciente in pacientes_completos
        for consulta in paciente["consultas"]
    ]
    
    total_consultas = len(todas_consultas)
    
    # Contagem por status usando dict comprehension
    status_count = {
        status: len([c for c in todas_consultas if c["status"] == status])
        for status in {"Concluída", "Agendada", "Cancelada", "Faltou"}
    }
    
    print(f"Total de consultas: {total_consultas}")
    print(f"\nStatus das consultas:")
    for status, qtd in status_count.items():
        if qtd > 0:
            percentual = (qtd / total_consultas) * 100
            print(f"  {status}: {qtd} ({percentual:.1f}%)")
    
    # Duração média por especialidade
    print(f"\nDuração média por especialidade:")
    for esp in {p["especialidade"] for p in pacientes_completos}:
        duracoes = [
            consulta["duracao"]
            for paciente in pacientes_completos
            if paciente["especialidade"] == esp
            for consulta in paciente["consultas"]
            if consulta["status"] == "Concluída"
        ]
        
        if duracoes:
            media_duracao = sum(duracoes) / len(duracoes)
            print(f"  {esp}: {media_duracao:.0f} minutos")
    
    # Taxa de comparecimento por faixa etária
    print(f"\nTaxa de comparecimento por faixa etária:")
    
    for faixa, idade_min, idade_max in [
        ("Jovens", 18, 29), ("Adultos", 30, 49), 
        ("Maduros", 50, 64), ("Idosos", 65, 100)
    ]:
        pacientes_faixa = [
            p for p in pacientes_completos 
            if idade_min <= p["idade"] <= idade_max
        ]
        
        if pacientes_faixa:
            consultas_faixa = [
                c for p in pacientes_faixa for c in p["consultas"]
            ]
            
            compareceram = len([c for c in consultas_faixa if c["status"] == "Concluída"])
            total_faixa = len([c for c in consultas_faixa if c["status"] in ["Concluída", "Faltou"]])
            
            if total_faixa > 0:
                taxa = (compareceram / total_faixa) * 100
                print(f"  {faixa}: {taxa:.1f}%")

def relatorio_top_pacientes():
    """Relatório dos pacientes mais ativos"""
    print("\n🏆 TOP PACIENTES")
    print("=" * 50)
    
    # Calcular métricas por paciente usando list comprehension
    metricas_pacientes = [
        {
            "nome": paciente["nome"],
            "total_consultas": len(paciente["consultas"]),
            "consultas_concluidas": len([c for c in paciente["consultas"] if c["status"] == "Concluída"]),
            "receita_gerada": sum(c["valor"] for c in paciente["consultas"] if c["status"] == "Concluída"),
            "tempo_total": sum(c["duracao"] for c in paciente["consultas"] if c["status"] == "Concluída")
        }
        for paciente in pacientes_completos
    ]
    
    # Top 3 por receita
    top_receita = sorted(metricas_pacientes, key=lambda x: x["receita_gerada"], reverse=True)[:3]
    
    print("Top 3 por receita gerada:")
    for i, paciente in enumerate(top_receita, 1):
        print(f"  {i}. {paciente['nome']}: R$ {paciente['receita_gerada']:.2f}")
    
    # Top 3 por número de consultas
    top_consultas = sorted(metricas_pacientes, key=lambda x: x["consultas_concluidas"], reverse=True)[:3]
    
    print(f"\nTop 3 por consultas concluídas:")
    for i, paciente in enumerate(top_consultas, 1):
        print(f"  {i}. {paciente['nome']}: {paciente['consultas_concluidas']} consultas")
    
    # Pacientes com maior tempo de atendimento
    top_tempo = sorted(metricas_pacientes, key=lambda x: x["tempo_total"], reverse=True)[:3]
    
    print(f"\nTop 3 por tempo de atendimento:")
    for i, paciente in enumerate(top_tempo, 1):
        horas = paciente["tempo_total"] / 60
        print(f"  {i}. {paciente['nome']}: {horas:.1f} horas")

def relatorio_personalizado():
    """Permite criar relatório personalizado"""
    print("\n🔧 RELATÓRIO PERSONALIZADO")
    print("=" * 50)
    
    print("Filtros disponíveis:")
    print("1. Por especialidade")
    print("2. Por faixa etária")
    print("3. Por cidade")
    print("4. Por status de consulta")
    
    filtro = input("Escolha um filtro (1-4): ")
    
    if filtro == "1":
        especialidades = {p["especialidade"] for p in pacientes_completos}
        print(f"\nEspecialidades: {', '.join(sorted(especialidades))}")
        esp_escolhida = input("Digite a especialidade: ")
        
        pacientes_filtrados = [p for p in pacientes_completos if p["especialidade"] == esp_escolhida]
        titulo = f"ESPECIALIDADE: {esp_escolhida.upper()}"
        
    elif filtro == "2":
        idade_min = int(input("Idade mínima: "))
        idade_max = int(input("Idade máxima: "))
        
        pacientes_filtrados = [
            p for p in pacientes_completos 
            if idade_min <= p["idade"] <= idade_max
        ]
        titulo = f"FAIXA ETÁRIA: {idade_min}-{idade_max} ANOS"
        
    elif filtro == "3":
        cidades = {p["cidade"] for p in pacientes_completos}
        print(f"\nCidades: {', '.join(sorted(cidades))}")
        cidade_escolhida = input("Digite a cidade: ")
        
        pacientes_filtrados = [p for p in pacientes_completos if p["cidade"] == cidade_escolhida]
        titulo = f"CIDADE: {cidade_escolhida.upper()}"
        
    elif filtro == "4":
        status_escolhido = input("Digite o status (Concluída/Agendada/Cancelada/Faltou): ")
        
        pacientes_filtrados = [
            p for p in pacientes_completos
            if any(c["status"] == status_escolhido for c in p["consultas"])
        ]
        titulo = f"STATUS: {status_escolhido.upper()}"
        
    else:
        print("❌ Filtro inválido!")
        return
    
    # Gerar relatório filtrado
    if pacientes_filtrados:
        print(f"\n📋 RELATÓRIO - {titulo}")
        print("-" * 60)
        print(f"Pacientes encontrados: {len(pacientes_filtrados)}")
        
        receita_total = sum(
            c["valor"] for p in pacientes_filtrados
            for c in p["consultas"] if c["status"] == "Concluída"
        )
        
        consultas_total = sum(len(p["consultas"]) for p in pacientes_filtrados)
        
        print(f"Total de consultas: {consultas_total}")
        print(f"Receita total: R$ {receita_total:.2f}")
        
        if pacientes_filtrados:
            idade_media = sum(p["idade"] for p in pacientes_filtrados) / len(pacientes_filtrados)
            print(f"Idade média: {idade_media:.1f} anos")
    else:
        print("❌ Nenhum paciente encontrado com os critérios selecionados.")

def menu_relatorios():
    """Menu principal dos relatórios"""
    while True:
        print("\n" + "="*60)
        print("           SISTEMA DE RELATÓRIOS LUNYSSE")
        print("="*60)
        print("1. Relatório Financeiro")
        print("2. Relatório Demográfico")
        print("3. Relatório Operacional")
        print("4. Top Pacientes")
        print("5. Relatório Personalizado")
        print("6. Relatório Completo")
        print("7. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção (1-7): ")
        
        if opcao == "1":
            relatorio_financeiro()
        elif opcao == "2":
            relatorio_demografico()
        elif opcao == "3":
            relatorio_operacional()
        elif opcao == "4":
            relatorio_top_pacientes()
        elif opcao == "5":
            relatorio_personalizado()
        elif opcao == "6":
            relatorio_financeiro()
            relatorio_demografico()
            relatorio_operacional()
            relatorio_top_pacientes()
        elif opcao == "7":
            print("\n👋 Encerrando sistema de relatórios...")
            break
        else:
            print("❌ Opção inválida!")
        
        if opcao != "7":
            input("\nPressione Enter para continuar...")

# Executa o programa
if __name__ == "__main__":
    menu_relatorios()