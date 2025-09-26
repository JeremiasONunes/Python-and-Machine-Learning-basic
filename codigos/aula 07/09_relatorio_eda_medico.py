# Aula 07 - Atividade Prática 4: Relatório de Análise Exploratória Médica
# Sistema completo de EDA para gerar insights médicos

import pandas as pd
import numpy as np

print("=== RELATÓRIO DE ANÁLISE EXPLORATÓRIA MÉDICA ===\n")

# Carregar ou criar dados médicos expandidos
np.random.seed(42)
n_pacientes = 200

# Criar dataset mais realista
dados = {
    'id': range(1, n_pacientes + 1),
    'idade': np.random.randint(18, 85, n_pacientes),
    'sexo': np.random.choice(['M', 'F'], n_pacientes),
    'especialidade': np.random.choice(['Psicologia', 'Psiquiatria', 'Cardiologia', 'Neurologia'], n_pacientes),
    'pressao_sistolica': np.random.normal(130, 25, n_pacientes),
    'pressao_diastolica': np.random.normal(85, 15, n_pacientes),
    'glicose': np.random.normal(105, 35, n_pacientes),
    'imc': np.random.normal(26, 5, n_pacientes),
    'colesterol': np.random.normal(200, 50, n_pacientes),
    'fumante': np.random.choice([True, False], n_pacientes, p=[0.25, 0.75]),
    'atividade_fisica': np.random.choice(['Baixa', 'Moderada', 'Alta'], n_pacientes, p=[0.4, 0.4, 0.2])
}

df = pd.DataFrame(dados)

# Adicionar correlações realistas
df.loc[df['idade'] > 60, 'pressao_sistolica'] += 20
df.loc[df['imc'] > 30, 'glicose'] += 25
df.loc[df['fumante'] == True, 'colesterol'] += 30

print(f"📊 Dataset: {df.shape[0]} pacientes, {df.shape[1]} variáveis")

# ===== SEÇÃO 1: PERFIL DEMOGRÁFICO =====
print(f"\n" + "="*60)
print("📋 SEÇÃO 1: PERFIL DEMOGRÁFICO")
print("="*60)

print(f"Distribuição por sexo:")
sexo_dist = df['sexo'].value_counts()
sexo_perc = df['sexo'].value_counts(normalize=True) * 100
for sexo in sexo_dist.index:
    print(f"  {sexo}: {sexo_dist[sexo]} ({sexo_perc[sexo]:.1f}%)")

print(f"\nDistribuição por especialidade:")
esp_dist = df['especialidade'].value_counts()
for esp in esp_dist.index:
    print(f"  {esp}: {esp_dist[esp]} pacientes")

print(f"\nEstatísticas de idade:")
print(f"  Média: {df['idade'].mean():.1f} anos")
print(f"  Mediana: {df['idade'].median():.1f} anos")
print(f"  Faixa: {df['idade'].min()}-{df['idade'].max()} anos")

# ===== SEÇÃO 2: INDICADORES DE SAÚDE =====
print(f"\n" + "="*60)
print("🏥 SEÇÃO 2: INDICADORES DE SAÚDE")
print("="*60)

indicadores = ['pressao_sistolica', 'pressao_diastolica', 'glicose', 'imc', 'colesterol']

for indicador in indicadores:
    media = df[indicador].mean()
    std = df[indicador].std()
    print(f"\n{indicador.replace('_', ' ').title()}:")
    print(f"  Média: {media:.2f} ± {std:.2f}")
    print(f"  Faixa: {df[indicador].min():.2f} - {df[indicador].max():.2f}")

# Classificações clínicas
df['status_pressao'] = df.apply(
    lambda row: 'Hipertensão' if row['pressao_sistolica'] >= 140 or row['pressao_diastolica'] >= 90
    else 'Pré-hipertensão' if row['pressao_sistolica'] >= 130 or row['pressao_diastolica'] >= 80
    else 'Normal', axis=1
)

df['status_glicose'] = df['glicose'].apply(
    lambda x: 'Diabetes' if x >= 126 else 'Pré-diabetes' if x >= 100 else 'Normal'
)

df['categoria_imc'] = df['imc'].apply(
    lambda x: 'Abaixo' if x < 18.5 else 'Normal' if x < 25 else 'Sobrepeso' if x < 30 else 'Obesidade'
)

print(f"\nClassificações clínicas:")
print(f"Status da pressão arterial:")
print(df['status_pressao'].value_counts())

print(f"\nStatus da glicose:")
print(df['status_glicose'].value_counts())

print(f"\nCategoria do IMC:")
print(df['categoria_imc'].value_counts())

# ===== SEÇÃO 3: CORRELAÇÕES E PADRÕES =====
print(f"\n" + "="*60)
print("🔗 SEÇÃO 3: CORRELAÇÕES E PADRÕES")
print("="*60)

# Matriz de correlação
correlacoes = df[indicadores + ['idade']].corr()

print("Correlações significativas (|r| > 0.3):")
for i in range(len(correlacoes.columns)):
    for j in range(i+1, len(correlacoes.columns)):
        corr_val = correlacoes.iloc[i, j]
        if abs(corr_val) > 0.3:
            var1 = correlacoes.columns[i]
            var2 = correlacoes.columns[j]
            intensidade = "Forte" if abs(corr_val) > 0.7 else "Moderada"
            direcao = "positiva" if corr_val > 0 else "negativa"
            print(f"  {var1} ↔ {var2}: {corr_val:.3f} ({intensidade} {direcao})")

# ===== SEÇÃO 4: ANÁLISE POR GRUPOS =====
print(f"\n" + "="*60)
print("👥 SEÇÃO 4: ANÁLISE POR GRUPOS")
print("="*60)

# Por sexo
print("Diferenças por sexo:")
analise_sexo = df.groupby('sexo')[indicadores].mean()
for indicador in indicadores:
    diff = analise_sexo.loc['M', indicador] - analise_sexo.loc['F', indicador]
    print(f"  {indicador}: M={analise_sexo.loc['M', indicador]:.1f}, F={analise_sexo.loc['F', indicador]:.1f} (Δ={diff:+.1f})")

# Por especialidade
print(f"\nPerfil por especialidade:")
analise_esp = df.groupby('especialidade').agg({
    'idade': 'mean',
    'pressao_sistolica': 'mean',
    'imc': 'mean'
}).round(1)
print(analise_esp)

# ===== SEÇÃO 5: FATORES DE RISCO =====
print(f"\n" + "="*60)
print("⚠️ SEÇÃO 5: FATORES DE RISCO")
print("="*60)

# Análise de fumantes
fumantes_stats = df.groupby('fumante')[indicadores].mean()
print("Impacto do tabagismo:")
for indicador in indicadores:
    fumante_val = fumantes_stats.loc[True, indicador]
    nao_fumante_val = fumantes_stats.loc[False, indicador]
    diff = fumante_val - nao_fumante_val
    print(f"  {indicador}: Fumante={fumante_val:.1f}, Não fumante={nao_fumante_val:.1f} (Δ={diff:+.1f})")

# Análise por atividade física
print(f"\nImpacto da atividade física:")
atividade_stats = df.groupby('atividade_fisica')[['imc', 'pressao_sistolica']].mean().round(1)
print(atividade_stats)

# ===== SEÇÃO 6: INSIGHTS E RECOMENDAÇÕES =====
print(f"\n" + "="*60)
print("💡 SEÇÃO 6: INSIGHTS E RECOMENDAÇÕES")
print("="*60)

# Calcular prevalências
prev_hipertensao = (df['status_pressao'] == 'Hipertensão').mean() * 100
prev_diabetes = (df['status_glicose'] == 'Diabetes').mean() * 100
prev_obesidade = (df['categoria_imc'] == 'Obesidade').mean() * 100
prev_fumantes = df['fumante'].mean() * 100

print("PRINCIPAIS ACHADOS:")
print(f"• Prevalência de hipertensão: {prev_hipertensao:.1f}%")
print(f"• Prevalência de diabetes: {prev_diabetes:.1f}%")
print(f"• Prevalência de obesidade: {prev_obesidade:.1f}%")
print(f"• Prevalência de tabagismo: {prev_fumantes:.1f}%")

# Identificar grupos de alto risco
alto_risco = df[
    (df['status_pressao'] == 'Hipertensão') |
    (df['status_glicose'] == 'Diabetes') |
    (df['categoria_imc'] == 'Obesidade')
]

print(f"\nGRUPOS DE ALTO RISCO:")
print(f"• {len(alto_risco)} pacientes ({len(alto_risco)/len(df)*100:.1f}%) têm pelo menos um fator de risco")

# Especialidade com maior risco
risco_por_esp = df.groupby('especialidade').apply(
    lambda x: ((x['status_pressao'] == 'Hipertensão') | 
               (x['status_glicose'] == 'Diabetes')).mean() * 100
).round(1)

print(f"• Risco por especialidade:")
for esp, risco in risco_por_esp.items():
    print(f"  - {esp}: {risco}%")

print(f"\nRECOMENDAÇÕES:")
print("• Implementar programa de controle de hipertensão")
print("• Intensificar rastreamento de diabetes")
print("• Criar programa antitabagismo")
print("• Promover atividade física regular")
print("• Monitoramento especial para pacientes de alto risco")

print(f"\n" + "="*60)
print("✅ RELATÓRIO DE EDA CONCLUÍDO")
print("="*60)

# Salvar resumo
resumo = {
    'total_pacientes': len(df),
    'idade_media': df['idade'].mean(),
    'prevalencia_hipertensao': prev_hipertensao,
    'prevalencia_diabetes': prev_diabetes,
    'prevalencia_obesidade': prev_obesidade,
    'pacientes_alto_risco': len(alto_risco)
}

print(f"\nResumo executivo salvo: {resumo}")

print("\n✅ Análise exploratória médica concluída!")