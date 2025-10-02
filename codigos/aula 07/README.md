# 🐼 Aula 07 - Análise de Dados com Pandas

## 📋 Visão Geral

Esta aula introduz a biblioteca **Pandas**, a ferramenta mais importante para análise de dados em Python. Os códigos progridem desde estruturas básicas até análises exploratórias avançadas aplicadas ao contexto médico, culminando em um dashboard completo.

---

## 🎯 Objetivos de Aprendizagem

- Dominar estruturas fundamentais do Pandas (Series e DataFrame)
- Implementar pipelines completos de limpeza de dados
- Realizar análises exploratórias e agrupamentos
- Detectar padrões e correlações em dados médicos
- Criar relatórios e dashboards informativos

---

## 📚 Fundamentos Teóricos

### 🐼 O que é Pandas?

**Pandas** é uma biblioteca Python para manipulação e análise de dados estruturados. É construída sobre NumPy e oferece estruturas de dados flexíveis e ferramentas de análise.

#### **Estruturas Principais**:
- **Series**: Array unidimensional rotulado
- **DataFrame**: Estrutura bidimensional (tabela) com linhas e colunas rotuladas

#### **Capacidades**:
- Leitura/escrita de diversos formatos (CSV, Excel, JSON, SQL)
- Limpeza e transformação de dados
- Agregações e agrupamentos
- Análise estatística descritiva
- Manipulação de datas e strings

### 📊 Análise Exploratória de Dados (EDA)

**EDA** é o processo de investigar dados para descobrir padrões, detectar anomalias e testar hipóteses usando estatísticas descritivas e visualizações.

#### **Etapas da EDA**:
1. **Compreensão**: Entender estrutura e tipos de dados
2. **Limpeza**: Tratar valores ausentes, duplicatas e inconsistências
3. **Exploração**: Calcular estatísticas e identificar padrões
4. **Visualização**: Criar gráficos para insights visuais
5. **Insights**: Extrair conclusões e recomendações

---

## 📁 Códigos da Aula

### 1️⃣ **01_estruturas_pandas.py**

#### 🎯 **Conceito**: Fundamentos das Estruturas Pandas

Introduz **Series** e **DataFrame**, as estruturas fundamentais para trabalhar com dados tabulares.

#### 🔧 **Fundamentos Implementados**:
- **Series**: Criação, indexação e operações básicas
- **DataFrame**: Construção a partir de dicionários
- **Métodos de Exploração**: head(), tail(), info(), describe()
- **Indexação**: Acesso por rótulos e posições
- **Operações Básicas**: Filtragem, agregações simples

#### 📊 **Aplicação Médica**:
- Criar Series de idades de pacientes
- Construir DataFrame com dados de funcionários
- Explorar informações básicas do dataset
- Filtrar dados por critérios específicos

#### 💡 **Conceitos Aprendidos**:
- Diferença entre Series e DataFrame
- Importância dos índices rotulados
- Métodos essenciais de exploração
- Operações básicas de filtragem

---

### 2️⃣ **03_carregamento_exploracao.py**

#### 🎯 **Conceito**: Carregamento e Exploração Inicial

Sistema para carregar datasets médicos e realizar exploração inicial sistemática.

#### 🔧 **Fundamentos Implementados**:
- **Carregamento de Dados**: read_csv() com tratamento de erros
- **Exploração Inicial**: shape, info(), describe()
- **Análise Categórica**: value_counts(), distribuições percentuais
- **Análise Numérica**: Estatísticas descritivas por variável
- **Verificação de Qualidade**: Valores ausentes, duplicatas

#### 📊 **Aplicação Médica**:
- Carregar dataset de 15 pacientes com variáveis médicas
- Analisar distribuição por sexo, especialidade e cidade
- Calcular estatísticas de idade, pressão arterial e glicose
- Identificar possíveis outliers médicos

#### 💡 **Conceitos Aprendidos**:
- Importância da exploração inicial
- Análise separada de variáveis categóricas e numéricas
- Detecção precoce de problemas nos dados
- Interpretação de estatísticas médicas

---

### 3️⃣ **04_limpeza_transformacao.py**

#### 🎯 **Conceito**: Pipeline de Limpeza de Dados

Demonstra técnicas essenciais para limpar e transformar dados "sujos" em dados prontos para análise.

#### 🔧 **Fundamentos Implementados**:
- **Tratamento de Valores Ausentes**: dropna(), fillna()
- **Remoção de Duplicatas**: drop_duplicates()
- **Padronização de Texto**: str.title(), str.upper()
- **Conversão de Tipos**: to_datetime(), astype()
- **Feature Engineering**: Criação de variáveis derivadas
- **Pipeline Automatizado**: Função de limpeza reutilizável

#### 📊 **Aplicação Médica**:
- Tratar dataset com problemas intencionais
- Preencher valores ausentes com estratégias apropriadas
- Padronizar nomes de cidades e categorias
- Criar faixas etárias e categorias salariais

#### 💡 **Conceitos Aprendidos**:
- Dados reais sempre têm problemas
- Diferentes estratégias para valores ausentes
- Importância da padronização
- Automação através de pipelines

---

### 4️⃣ **05_pipeline_limpeza_medico.py**

#### 🎯 **Conceito**: Pipeline Especializado para Dados Médicos

Sistema robusto e específico para limpeza de dados médicos com classificações clínicas.

#### 🔧 **Fundamentos Implementados**:
- **Limpeza Médica Específica**: Tratamento de variáveis clínicas
- **Classificações Clínicas**: IMC, pressão arterial, glicose
- **Validação Médica**: Verificação de consistência clínica
- **Feature Engineering Médica**: Variáveis derivadas clinicamente relevantes
- **Persistência**: Salvamento de dados limpos

#### 📊 **Aplicação Médica**:
- Processar dados de 10 pacientes com problemas típicos
- Criar classificações de IMC (normal, sobrepeso, obesidade)
- Categorizar status de pressão arterial e glicose
- Gerar faixas etárias clinicamente relevantes

#### 💡 **Conceitos Aprendidos**:
- Pipelines específicos por domínio
- Importância de classificações clínicas
- Validação contextual dos dados
- Preparação para análises médicas

---

### 5️⃣ **06_agrupamento_analise.py**

#### 🎯 **Conceito**: Análise por Grupos e Agregações

Demonstra o poder do **groupby** para análises segmentadas e descoberta de padrões.

#### 🔧 **Fundamentos Implementados**:
- **GroupBy Simples**: Agrupamento por uma variável
- **Múltiplas Agregações**: agg() com diferentes funções
- **Agrupamento Múltiplo**: Grupos por várias colunas
- **Transformações**: transform() para cálculos relativos
- **Pivot Tables**: Tabelas cruzadas e crosstab
- **Ranking**: rank() dentro de grupos

#### 📊 **Aplicação Médica**:
- Analisar salários por sexo e especialidade
- Calcular estatísticas por cidade
- Criar rankings de performance
- Gerar tabelas cruzadas de especialidade vs sexo

#### 💡 **Conceitos Aprendidos**:
- Poder das análises segmentadas
- Diferentes tipos de agregações
- Importância das transformações
- Pivot tables para insights rápidos

---

### 6️⃣ **07_analise_grupos_medicos.py**

#### 🎯 **Conceito**: Análise Estatística Médica por Grupos

Sistema avançado para análise médica segmentada por especialidade, idade e condições de saúde.

#### 🔧 **Fundamentos Implementados**:
- **Análise por Especialidade**: Perfis médicos por área
- **Análise por Faixa Etária**: Padrões relacionados à idade
- **Análise Geográfica**: Diferenças por cidade
- **Análise Combinada**: Múltiplas dimensões simultaneamente
- **Detecção de Padrões**: Identificação de tendências médicas
- **Análise de Outliers**: Pacientes com valores extremos por grupo

#### 📊 **Aplicação Médica**:
- Comparar 50 pacientes por especialidade médica
- Analisar prevalência de hipertensão por faixa etária
- Identificar perfis de risco por cidade
- Calcular scores de risco cardiovascular

#### 💡 **Conceitos Aprendidos**:
- Análises médicas requerem segmentação
- Importância de múltiplas dimensões
- Detecção de padrões epidemiológicos
- Análise contextual por grupos

---

### 7️⃣ **08_analise_exploratoria_avancada.py**

#### 🎯 **Conceito**: EDA Avançada com Correlações e Outliers

Técnicas avançadas de análise exploratória incluindo correlações, detecção de outliers e segmentação.

#### 🔧 **Fundamentos Implementados**:
- **Matriz de Correlação**: corr() para identificar relacionamentos
- **Análise Categórica**: crosstab com percentuais
- **Detecção de Outliers**: Método IQR (Interquartile Range)
- **Análise de Percentis**: Distribuições detalhadas
- **Segmentação Avançada**: Criação de scores de risco
- **Análise Temporal**: Padrões por tempo (simulado)

#### 📊 **Aplicação Médica**:
- Analisar correlações entre 100 pacientes
- Detectar outliers em variáveis médicas
- Criar segmentos de risco cardiovascular
- Comparar fumantes vs não fumantes

#### 💡 **Conceitos Aprendidos**:
- Correlações revelam relacionamentos
- Outliers podem indicar casos especiais
- Segmentação melhora insights
- Análise temporal é crucial em medicina

---

### 8️⃣ **09_relatorio_eda_medico.py**

#### 🎯 **Conceito**: Relatório Completo de EDA Médica

Sistema estruturado para gerar relatórios completos de análise exploratória médica.

#### 🔧 **Fundamentos Implementados**:
- **Estrutura de Relatório**: Seções organizadas e profissionais
- **Perfil Demográfico**: Análise populacional
- **Indicadores de Saúde**: Métricas clínicas padronizadas
- **Análise de Correlações**: Relacionamentos significativos
- **Análise por Grupos**: Segmentação demográfica
- **Fatores de Risco**: Identificação e quantificação
- **Insights e Recomendações**: Conclusões acionáveis

#### 📊 **Aplicação Médica**:
- Processar 200 pacientes com dados completos
- Calcular prevalências de hipertensão, diabetes e obesidade
- Identificar correlações clinicamente relevantes
- Gerar recomendações baseadas em evidências

#### 💡 **Conceitos Aprendidos**:
- Relatórios estruturados comunicam melhor
- Métricas clínicas padronizadas são essenciais
- Insights devem gerar ações
- Análise populacional vs individual

---

### 9️⃣ **10_desafio_dashboard.py**

#### 🎯 **Conceito**: Dashboard Interativo com Pandas

Sistema completo que integra todas as análises em um dashboard interativo para monitoramento em tempo real.

#### 🔧 **Fundamentos Implementados**:
- **Dashboard Textual**: Interface de usuário em console
- **Métricas em Tempo Real**: KPIs atualizados
- **Sistema de Alertas**: Identificação automática de casos críticos
- **Visualização Textual**: Gráficos de barras em ASCII
- **Menu Interativo**: Navegação por diferentes seções
- **Resumo Executivo**: Síntese para tomada de decisão

#### 📊 **Aplicação Médica**:
- Monitorar 150 pacientes em tempo real
- Alertas automáticos para casos críticos
- Distribuição por especialidades com visualização
- KPIs de saúde populacional

#### 💡 **Conceitos Aprendidos**:
- Dashboards facilitam monitoramento
- Alertas automáticos são cruciais
- Visualização simples pode ser eficaz
- Integração de múltiplas análises

---

## 🔬 Conceitos Teóricos Detalhados

### 📊 **Operações Fundamentais do Pandas**

#### **Indexação e Seleção**
```python
df['coluna']          # Selecionar coluna
df.loc[linha, coluna] # Por rótulo
df.iloc[i, j]         # Por posição
df[df['idade'] > 30]  # Filtragem condicional
```

#### **Agregações**
```python
df.groupby('categoria').agg({
    'valor': ['mean', 'sum', 'count'],
    'idade': 'mean'
})
```

#### **Transformações**
```python
df['nova_coluna'] = df['coluna'].apply(lambda x: x * 2)
df.groupby('grupo')['valor'].transform('mean')
```

### 🧹 **Pipeline de Limpeza de Dados**

#### **Etapas Essenciais**:
1. **Identificação**: Detectar problemas nos dados
2. **Valores Ausentes**: Estratégias de preenchimento ou remoção
3. **Duplicatas**: Identificação e remoção
4. **Inconsistências**: Padronização de formatos
5. **Outliers**: Detecção e tratamento
6. **Validação**: Verificação de qualidade final

#### **Estratégias para Valores Ausentes**:
- **Remoção**: Quando poucos casos
- **Média/Mediana**: Para variáveis numéricas
- **Moda**: Para variáveis categóricas
- **Interpolação**: Para séries temporais
- **Modelo Preditivo**: Para casos complexos

### 📈 **Análise Exploratória Sistemática**

#### **Variáveis Numéricas**:
- Estatísticas descritivas (média, mediana, desvio)
- Distribuição (histogramas, boxplots)
- Outliers (método IQR, z-score)
- Correlações (matriz de correlação)

#### **Variáveis Categóricas**:
- Frequências (value_counts)
- Proporções (normalize=True)
- Tabelas cruzadas (crosstab)
- Associações (qui-quadrado)

---

## 🚀 Como Executar

### **Pré-requisitos**
```bash
pip install pandas numpy
```

### **Execução Sequencial**
```bash
python 01_estruturas_pandas.py              # Estruturas básicas
python 03_carregamento_exploracao.py        # Exploração inicial
python 04_limpeza_transformacao.py          # Limpeza de dados
python 05_pipeline_limpeza_medico.py        # Pipeline médico
python 06_agrupamento_analise.py            # Análise por grupos
python 07_analise_grupos_medicos.py         # Grupos médicos
python 08_analise_exploratoria_avancada.py  # EDA avançada
python 09_relatorio_eda_medico.py           # Relatório completo
python 10_desafio_dashboard.py              # Dashboard interativo
```

---

## 📊 Resultados Esperados

### **Estruturas e Operações**
- Domínio completo de Series e DataFrame
- Fluência em indexação e filtragem
- Competência em agregações e transformações

### **Limpeza de Dados**
- Pipelines robustos e reutilizáveis
- Tratamento adequado de problemas comuns
- Validação sistemática de qualidade

### **Análise Exploratória**
- Identificação de padrões e tendências
- Detecção de outliers e anomalias
- Insights acionáveis para tomada de decisão

### **Relatórios e Dashboards**
- Comunicação eficaz de resultados
- Monitoramento em tempo real
- Alertas automáticos para casos críticos

---

## 🎓 Aplicações no Sistema Lunysse

### **Gestão de Pacientes**
- **Perfis Demográficos**: Análise da população atendida
- **Indicadores de Saúde**: Monitoramento de métricas clínicas
- **Detecção de Riscos**: Identificação precoce de casos críticos
- **Relatórios Médicos**: Análises para equipe clínica

### **Gestão Operacional**
- **Dashboard Executivo**: KPIs para gestores
- **Análise de Demanda**: Padrões de consultas por especialidade
- **Otimização de Recursos**: Alocação baseada em dados
- **Qualidade de Dados**: Monitoramento da integridade

### **Pesquisa e Desenvolvimento**
- **Estudos Epidemiológicos**: Análise de tendências populacionais
- **Análise de Eficácia**: Avaliação de tratamentos
- **Segmentação de Pacientes**: Grupos para cuidados personalizados
- **Predição de Riscos**: Base para modelos de ML

---

## 📚 Próximos Passos

1. **Visualização Avançada**: Matplotlib e Seaborn para gráficos
2. **Machine Learning**: Scikit-learn para modelos preditivos
3. **Análise Temporal**: Séries temporais com Pandas
4. **Big Data**: Dask para datasets grandes
5. **Dashboards Web**: Streamlit ou Dash para interfaces

---

## 🔗 Recursos Adicionais

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Python for Data Analysis](https://wesmckinney.com/book/) - Livro do criador do Pandas
- [Kaggle Learn - Pandas](https://www.kaggle.com/learn/pandas)

---

## 💡 Boas Práticas em Análise de Dados Médicos

### **Qualidade dos Dados**
- **Validação Contínua**: Verificar consistência regularmente
- **Documentação**: Registrar todas as transformações
- **Backup**: Manter versões originais dos dados
- **Auditoria**: Rastrear mudanças nos dados

### **Análise Responsável**
- **Contexto Clínico**: Sempre considerar relevância médica
- **Privacidade**: Proteger informações sensíveis
- **Interpretação Cuidadosa**: Evitar conclusões precipitadas
- **Validação Externa**: Confirmar achados com especialistas

### **Comunicação Eficaz**
- **Linguagem Clara**: Evitar jargão técnico desnecessário
- **Visualizações Apropriadas**: Escolher gráficos adequados
- **Insights Acionáveis**: Focar em resultados úteis
- **Limitações**: Sempre mencionar restrições da análise

---

**💡 Lembre-se**: Pandas é uma ferramenta poderosa, mas a qualidade da análise depende da compreensão do contexto médico e da aplicação cuidadosa das técnicas apropriadas!