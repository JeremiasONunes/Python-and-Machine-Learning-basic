# Aula 07 - Desafio: Dashboard Simples com Pandas
# Sistema que combina análises Pandas para criar um dashboard textual

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("=== DASHBOARD MÉDICO LUNYSSE ===\n")

# Simular dados em tempo real
np.random.seed(42)
n_pacientes = 150

# Gerar dados do dashboard
dados_dashboard = {
    'id': range(1, n_pacientes + 1),
    'nome': [f'Paciente_{i:03d}' for i in range(1, n_pacientes + 1)],
    'idade': np.random.randint(18, 85, n_pacientes),
    'sexo': np.random.choice(['M', 'F'], n_pacientes),
    'especialidade': np.random.choice(['Psicologia', 'Psiquiatria', 'Cardiologia', 'Neurologia'], n_pacientes),
    'data_ultima_consulta': pd.date_range('2024-01-01', periods=n_pacientes, freq='D'),
    'pressao_sistolica': np.random.normal(130, 25, n_pacientes),
    'glicose': np.random.normal(105, 30, n_pacientes),
    'imc': np.random.normal(26, 4, n_pacientes),
    'status': np.random.choice(['Ativo', 'Inativo', 'Crítico'], n_pacientes, p=[0.7, 0.25, 0.05])
}

df = pd.DataFrame(dados_dashboard)

# Adicionar lógica para status crítico
df.loc[(df['pressao_sistolica'] > 160) | (df['glicose'] > 180), 'status'] = 'Crítico'

def exibir_cabecalho():
    """Exibe cabeçalho do dashboard"""
    print("🏥" + "="*70 + "🏥")
    print("                    DASHBOARD CLÍNICA LUNYSSE")
    print("                   " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("🏥" + "="*70 + "🏥")

def metricas_principais():
    """Exibe métricas principais"""
    print("\n📊 MÉTRICAS PRINCIPAIS")
    print("-" * 50)
    
    total_pacientes = len(df)
    pacientes_ativos = len(df[df['status'] == 'Ativo'])
    pacientes_criticos = len(df[df['status'] == 'Crítico'])
    idade_media = df['idade'].mean()
    
    print(f"👥 Total de Pacientes: {total_pacientes}")
    print(f"✅ Pacientes Ativos: {pacientes_ativos} ({pacientes_ativos/total_pacientes*100:.1f}%)")
    print(f"🚨 Pacientes Críticos: {pacientes_criticos} ({pacientes_criticos/total_pacientes*100:.1f}%)")
    print(f"📈 Idade Média: {idade_media:.1f} anos")

def alertas_criticos():
    """Exibe alertas para pacientes críticos"""
    print("\n🚨 ALERTAS CRÍTICOS")
    print("-" * 50)
    
    criticos = df[df['status'] == 'Crítico']
    
    if len(criticos) == 0:
        print("✅ Nenhum paciente em estado crítico")
        return
    
    print(f"⚠️ {len(criticos)} paciente(s) requer(em) atenção imediata:")
    
    for _, paciente in criticos.head(5).iterrows():
        motivos = []
        if paciente['pressao_sistolica'] > 160:
            motivos.append(f"Pressão alta ({paciente['pressao_sistolica']:.0f})")
        if paciente['glicose'] > 180:
            motivos.append(f"Glicose alta ({paciente['glicose']:.0f})")
        
        print(f"  • {paciente['nome']} ({paciente['idade']} anos) - {', '.join(motivos)}")

def distribuicao_especialidades():
    """Exibe distribuição por especialidades"""
    print("\n🏥 DISTRIBUIÇÃO POR ESPECIALIDADES")
    print("-" * 50)
    
    esp_count = df['especialidade'].value_counts()
    esp_perc = df['especialidade'].value_counts(normalize=True) * 100
    
    for esp in esp_count.index:
        count = esp_count[esp]
        perc = esp_perc[esp]
        barra = "█" * int(perc // 5)  # Barra visual simples
        print(f"{esp:15} {count:3d} ({perc:5.1f}%) {barra}")

def indicadores_saude():
    """Exibe indicadores de saúde"""
    print("\n💊 INDICADORES DE SAÚDE")
    print("-" * 50)
    
    # Calcular médias e alertas
    pressao_media = df['pressao_sistolica'].mean()
    glicose_media = df['glicose'].mean()
    imc_medio = df['imc'].mean()
    
    # Contar pacientes fora do normal
    hipertensos = len(df[df['pressao_sistolica'] > 140])
    diabeticos = len(df[df['glicose'] > 126])
    obesos = len(df[df['imc'] > 30])
    
    print(f"🩺 Pressão Sistólica Média: {pressao_media:.1f} mmHg")
    print(f"   └─ Hipertensos: {hipertensos} pacientes ({hipertensos/len(df)*100:.1f}%)")
    
    print(f"🍯 Glicose Média: {glicose_media:.1f} mg/dL")
    print(f"   └─ Diabéticos: {diabeticos} pacientes ({diabeticos/len(df)*100:.1f}%)")
    
    print(f"⚖️ IMC Médio: {imc_medio:.1f}")
    print(f"   └─ Obesos: {obesos} pacientes ({obesos/len(df)*100:.1f}%)")

def consultas_recentes():
    """Exibe estatísticas de consultas recentes"""
    print("\n📅 CONSULTAS RECENTES")
    print("-" * 50)
    
    # Últimos 7 dias
    data_limite = datetime.now() - timedelta(days=7)
    df['data_ultima_consulta'] = pd.to_datetime(df['data_ultima_consulta'])
    
    consultas_semana = df[df['data_ultima_consulta'] >= data_limite]
    
    print(f"📊 Consultas nos últimos 7 dias: {len(consultas_semana)}")
    
    # Por especialidade
    if len(consultas_semana) > 0:
        consultas_esp = consultas_semana['especialidade'].value_counts()
        print("   Por especialidade:")
        for esp, count in consultas_esp.items():
            print(f"   └─ {esp}: {count} consultas")

def ranking_idades():
    """Exibe ranking por faixas etárias"""
    print("\n👥 DISTRIBUIÇÃO POR IDADE")
    print("-" * 50)
    
    # Criar faixas etárias
    df['faixa_etaria'] = pd.cut(df['idade'], 
                               bins=[0, 30, 50, 65, 100], 
                               labels=['18-30', '31-50', '51-65', '65+'])
    
    faixas = df['faixa_etaria'].value_counts().sort_index()
    
    for faixa, count in faixas.items():
        perc = count / len(df) * 100
        barra = "▓" * int(perc // 3)
        print(f"{faixa:6} {count:3d} ({perc:5.1f}%) {barra}")

def resumo_executivo():
    """Exibe resumo executivo"""
    print("\n📋 RESUMO EXECUTIVO")
    print("-" * 50)
    
    # Calcular KPIs principais
    taxa_criticos = len(df[df['status'] == 'Crítico']) / len(df) * 100
    especialidade_popular = df['especialidade'].value_counts().index[0]
    faixa_predominante = df['faixa_etaria'].value_counts().index[0]
    
    # Identificar tendências
    risco_alto = len(df[(df['pressao_sistolica'] > 140) | (df['glicose'] > 126) | (df['imc'] > 30)])
    
    print(f"🎯 KPIs Principais:")
    print(f"   • Taxa de pacientes críticos: {taxa_criticos:.1f}%")
    print(f"   • Especialidade mais procurada: {especialidade_popular}")
    print(f"   • Faixa etária predominante: {faixa_predominante}")
    print(f"   • Pacientes com fatores de risco: {risco_alto} ({risco_alto/len(df)*100:.1f}%)")
    
    # Recomendações automáticas
    print(f"\n💡 Recomendações:")
    if taxa_criticos > 10:
        print("   • Aumentar monitoramento de pacientes críticos")
    if risco_alto / len(df) > 0.3:
        print("   • Implementar programa preventivo de saúde")
    print("   • Manter acompanhamento regular dos indicadores")

def dashboard_completo():
    """Exibe dashboard completo"""
    exibir_cabecalho()
    metricas_principais()
    alertas_criticos()
    distribuicao_especialidades()
    indicadores_saude()
    consultas_recentes()
    ranking_idades()
    resumo_executivo()
    
    print("\n" + "🏥" + "="*70 + "🏥")
    print("                    Dashboard atualizado com sucesso!")
    print("🏥" + "="*70 + "🏥")

def menu_dashboard():
    """Menu interativo do dashboard"""
    while True:
        print("\n" + "="*50)
        print("           MENU DASHBOARD LUNYSSE")
        print("="*50)
        print("1. Dashboard Completo")
        print("2. Métricas Principais")
        print("3. Alertas Críticos")
        print("4. Indicadores de Saúde")
        print("5. Distribuição por Especialidades")
        print("6. Resumo Executivo")
        print("7. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção (1-7): ")
        
        if opcao == "1":
            dashboard_completo()
        elif opcao == "2":
            exibir_cabecalho()
            metricas_principais()
        elif opcao == "3":
            exibir_cabecalho()
            alertas_criticos()
        elif opcao == "4":
            exibir_cabecalho()
            indicadores_saude()
        elif opcao == "5":
            exibir_cabecalho()
            distribuicao_especialidades()
        elif opcao == "6":
            exibir_cabecalho()
            resumo_executivo()
        elif opcao == "7":
            print("\n👋 Encerrando dashboard...")
            break
        else:
            print("❌ Opção inválida!")
        
        if opcao != "7":
            input("\nPressione Enter para continuar...")

# Executar dashboard
if __name__ == "__main__":
    menu_dashboard()

print("\n✅ Dashboard médico implementado!")