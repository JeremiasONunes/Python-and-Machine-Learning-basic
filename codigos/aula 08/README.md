# 📊 Aula 08 - Machine Learning e Visualização de Dados

## 📋 Visão Geral

Esta aula introduz os conceitos fundamentais de **Machine Learning** e **Visualização de Dados** aplicados ao contexto médico. Os códigos progridem desde visualizações básicas até um sistema completo de ML para classificação de risco cardiovascular.

---

## 🎯 Objetivos de Aprendizagem

- Dominar visualização de dados com Matplotlib
- Compreender conceitos básicos de Machine Learning
- Implementar pipeline completo de preparação de dados
- Treinar e avaliar modelos de classificação
- Criar sistemas integrados de ML para medicina

---

## 📚 Fundamentos Teóricos

### 📈 Visualização de Dados

**Visualização de dados** é a representação gráfica de informações para facilitar a compreensão de padrões, tendências e insights.

#### **Tipos de Gráficos**:
- **Linha**: Tendências ao longo do tempo
- **Barras**: Comparação entre categorias
- **Dispersão**: Relação entre variáveis
- **Histograma**: Distribuição de frequências
- **Matriz de Confusão**: Performance de classificação

### 🤖 Machine Learning Supervisionado

**Machine Learning Supervisionado** aprende padrões a partir de dados rotulados para fazer predições em novos dados.

#### **Processo de ML**:
1. **Coleta de Dados**: Obter dataset representativo
2. **Preparação**: Limpeza, transformação e normalização
3. **Divisão**: Separar treino, validação e teste
4. **Treinamento**: Ajustar modelo aos dados
5. **Avaliação**: Medir performance com métricas
6. **Deploy**: Implementar em produção

#### **Algoritmos de Classificação**:
- **Random Forest**: Ensemble de árvores de decisão
- **Regressão Logística**: Modelo linear probabilístico
- **Árvore de Decisão**: Regras hierárquicas de decisão

---

## 📁 Códigos da Aula

### 1️⃣ **01_matplotlib_basico.py**

#### 🎯 **Conceito**: Fundamentos de Visualização

Introduz os conceitos básicos do **Matplotlib** para criar visualizações médicas eficazes.

#### 🔧 **Fundamentos Implementados**:
- **Gráficos de Linha**: Monitoramento de sinais vitais
- **Gráficos de Barras**: Distribuição por especialidades
- **Dispersão**: Correlação idade vs pressão arterial
- **Histogramas**: Distribuição de idades
- **Subplots**: Múltiplas visualizações
- **Personalização**: Cores, legendas, anotações

#### 📊 **Aplicação Médica**:
- Visualizar distribuição de pacientes por especialidade
- Analisar correlação entre idade e pressão arterial
- Monitorar batimentos cardíacos ao longo de 24h
- Identificar padrões em dados de saúde

#### 💡 **Conceitos Aprendidos**:
- Importância da visualização na análise médica
- Escolha do gráfico adequado para cada tipo de dado
- Personalização para comunicação eficaz
- Interpretação visual de tendências

---

### 2️⃣ **02_introducao_ml.py**

#### 🎯 **Conceito**: Fundamentos de Machine Learning

Apresenta os conceitos básicos de ML e preparação inicial de dados médicos.

#### 🔧 **Fundamentos Implementados**:
- **Tipos de ML**: Supervisionado, não-supervisionado, por reforço
- **Dataset Médico**: Criação de dados sintéticos realistas
- **Features e Target**: Separação de variáveis preditoras e objetivo
- **Train/Test Split**: Divisão estratificada dos dados
- **Normalização**: StandardScaler para padronização
- **Análise Exploratória**: Estatísticas descritivas

#### 📊 **Aplicação Médica**:
- Criar dataset com 9 variáveis médicas relevantes
- Definir risco cardiovascular como target
- Balancear classes de risco (baixo/médio/alto)
- Preparar dados para algoritmos de ML

#### 💡 **Conceitos Aprendidos**:
- Diferença entre features e target
- Importância da divisão treino/teste
- Necessidade de normalização
- Análise de distribuição de classes

---

### 3️⃣ **03_preparacao_dados_ml.py**

#### 🎯 **Conceito**: Pipeline Completo de Preparação

Sistema robusto para preparar dados médicos reais com problemas típicos.

#### 🔧 **Fundamentos Implementados**:
- **Tratamento de Valores Ausentes**: SimpleImputer com mediana
- **Codificação Categórica**: LabelEncoder para variáveis não-numéricas
- **Detecção de Outliers**: Clipping baseado em percentis
- **Feature Engineering**: Criação de variáveis derivadas
- **Validação de Qualidade**: Verificação de duplicatas e consistência

#### 📊 **Aplicação Médica**:
- Tratar dados médicos com valores ausentes
- Codificar variáveis como sexo, cidade, atividade física
- Criar features derivadas (pressão média, grupos de idade)
- Garantir qualidade dos dados para ML

#### 💡 **Conceitos Aprendidos**:
- Dados reais sempre têm problemas
- Importância da limpeza sistemática
- Feature engineering aumenta performance
- Validação de qualidade é essencial

---

### 4️⃣ **04_classificador_risco_medico.py**

#### 🎯 **Conceito**: Classificador Médico Especializado

Sistema completo para classificar pacientes por nível de risco cardiovascular.

#### 🔧 **Fundamentos Implementados**:
- **Random Forest**: Algoritmo ensemble robusto
- **Classificação Multiclasse**: 3 níveis de risco
- **Feature Importance**: Identificação de variáveis mais importantes
- **Relatórios Personalizados**: Análise individual de pacientes
- **Interpretabilidade**: Explicação das predições

#### 📊 **Aplicação Médica**:
- Classificar risco cardiovascular em baixo/médio/alto
- Usar 10 variáveis médicas relevantes
- Gerar relatórios individuais com recomendações
- Identificar fatores de risco mais importantes

#### 💡 **Conceitos Aprendidos**:
- Random Forest é interpretável e robusto
- Importância das features guia decisões clínicas
- Classificação multiclasse é mais realista
- Relatórios personalizados aumentam utilidade

---

### 5️⃣ **05_avaliacao_metricas.py**

#### 🎯 **Conceito**: Avaliação Rigorosa de Modelos

Sistema completo para avaliar performance de modelos ML com múltiplas métricas.

#### 🔧 **Fundamentos Implementados**:
- **Métricas Múltiplas**: Acurácia, Precisão, Recall, F1-Score
- **Matriz de Confusão**: Análise detalhada de erros
- **Métricas Macro/Weighted**: Tratamento de classes desbalanceadas
- **Visualizações**: Gráficos de performance
- **Interpretação**: Análise qualitativa dos resultados

#### 📊 **Aplicação Médica**:
- Avaliar modelos com dados médicos desbalanceados
- Analisar tipos de erros (falsos positivos/negativos)
- Visualizar performance por classe de risco
- Interpretar resultados para tomada de decisão clínica

#### 💡 **Conceitos Aprendidos**:
- Acurácia não é suficiente para dados desbalanceados
- Precisão vs Recall: trade-off importante
- Matriz de confusão revela padrões de erro
- Interpretação contextual é crucial em medicina

---

### 6️⃣ **06_sistema_completo_ml.py**

#### 🎯 **Conceito**: Sistema Integrado de ML

Sistema end-to-end que integra todos os conceitos em uma solução completa.

#### 🔧 **Fundamentos Implementados**:
- **Múltiplos Algoritmos**: Comparação de Random Forest, Logistic Regression, Decision Tree
- **Cross-Validation**: Validação cruzada para robustez
- **Visualização Integrada**: Dashboard completo de resultados
- **Seleção Automática**: Escolha do melhor modelo
- **Relatório Final**: Análise completa do sistema

#### 📊 **Aplicação Médica**:
- Comparar 3 algoritmos diferentes
- Selecionar automaticamente o melhor modelo
- Visualizar comparação de performance
- Gerar relatório executivo para stakeholders

#### 💡 **Conceitos Aprendidos**:
- Comparação de algoritmos é essencial
- Cross-validation aumenta confiabilidade
- Visualização facilita comunicação
- Sistemas integrados são mais robustos

---

## 🔬 Conceitos Teóricos Detalhados

### 📊 **Métricas de Avaliação**

#### **Acurácia**
```python
Acurácia = (VP + VN) / (VP + VN + FP + FN)
```
- **Uso**: Visão geral da performance
- **Limitação**: Inadequada para dados desbalanceados

#### **Precisão**
```python
Precisão = VP / (VP + FP)
```
- **Significado**: "Dos que classifiquei como positivo, quantos realmente são?"
- **Uso**: Quando falsos positivos são custosos

#### **Recall (Sensibilidade)**
```python
Recall = VP / (VP + FN)
```
- **Significado**: "Dos que são realmente positivos, quantos identifiquei?"
- **Uso**: Quando falsos negativos são perigosos (medicina)

#### **F1-Score**
```python
F1 = 2 × (Precisão × Recall) / (Precisão + Recall)
```
- **Significado**: Média harmônica entre precisão e recall
- **Uso**: Balanceamento entre precisão e recall

### 🎛️ **Algoritmos de Classificação**

#### **Random Forest**
- **Vantagens**: Robusto, interpretável, lida com overfitting
- **Desvantagens**: Pode ser lento, menos preciso que deep learning
- **Uso**: Dados tabulares, interpretabilidade importante

#### **Regressão Logística**
- **Vantagens**: Rápido, probabilístico, interpretável
- **Desvantagens**: Assume linearidade, sensível a outliers
- **Uso**: Baseline, dados lineares, probabilidades calibradas

#### **Árvore de Decisão**
- **Vantagens**: Muito interpretável, não precisa normalização
- **Desvantagens**: Propenso a overfitting, instável
- **Uso**: Regras de negócio, explicabilidade máxima

### 🚫 **Problemas Comuns em ML Médico**

#### **Dados Desbalanceados**
- **Problema**: Classes minoritárias são ignoradas
- **Soluções**: Class weights, SMOTE, métricas adequadas

#### **Overfitting**
- **Problema**: Modelo memoriza treino, não generaliza
- **Soluções**: Cross-validation, regularização, mais dados

#### **Data Leakage**
- **Problema**: Informação do futuro vaza para o modelo
- **Soluções**: Validação temporal, feature engineering cuidadosa

---

## 🚀 Como Executar

### **Pré-requisitos**
```bash
pip install pandas numpy matplotlib scikit-learn
```

### **Execução Sequencial**
```bash
python 01_matplotlib_basico.py           # Visualizações básicas
python 02_introducao_ml.py               # Conceitos de ML
python 03_preparacao_dados_ml.py         # Pipeline de dados
python 04_classificador_risco_medico.py  # Classificador especializado
python 05_avaliacao_metricas.py          # Métricas de avaliação
python 06_sistema_completo_ml.py         # Sistema integrado
```

---

## 📊 Resultados Esperados

### **Visualizações**
- Gráficos médicos informativos e bem formatados
- Identificação de padrões e correlações
- Comunicação eficaz de insights

### **Modelos de ML**
- Acurácia: 80-90% (dependendo da complexidade dos dados)
- Precisão/Recall balanceados
- Interpretabilidade adequada para uso clínico

### **Sistema Completo**
- Comparação objetiva de algoritmos
- Seleção automática do melhor modelo
- Relatórios executivos completos

---

## 🎓 Aplicações no Sistema Lunysse

Estes conceitos podem ser aplicados no sistema Lunysse para:

### **Visualização**
- **Dashboards Médicos**: Painéis de controle para gestores
- **Relatórios de Pacientes**: Gráficos de evolução clínica
- **Análise Epidemiológica**: Tendências de saúde populacional

### **Machine Learning**
- **Triagem Inteligente**: Classificação automática de urgência
- **Predição de Risco**: Identificação precoce de complicações
- **Otimização de Recursos**: Alocação eficiente baseada em dados
- **Suporte à Decisão**: Assistência aos profissionais de saúde

---

## 📚 Próximos Passos

1. **Deep Learning**: Redes neurais para problemas complexos
2. **Séries Temporais**: Análise de dados longitudinais
3. **Processamento de Imagens**: ML para radiologia
4. **NLP Médico**: Análise de textos clínicos
5. **MLOps**: Deploy e monitoramento em produção

---

## 🔗 Recursos Adicionais

- [Scikit-learn Documentation](https://scikit-learn.org)
- [Matplotlib Gallery](https://matplotlib.org/gallery/)
- [Pandas User Guide](https://pandas.pydata.org/docs/)
- [ML in Healthcare](https://www.nature.com/articles/s41591-018-0300-7)

---

## ⚠️ Considerações Éticas em ML Médico

### **Responsabilidades**
- **Validação Rigorosa**: Testes extensivos antes do uso clínico
- **Transparência**: Explicabilidade das decisões do modelo
- **Bias**: Cuidado com vieses nos dados de treinamento
- **Privacidade**: Proteção de dados sensíveis dos pacientes

### **Limitações**
- **Não Substitui Médicos**: ML é ferramenta de apoio, não substituição
- **Contexto Clínico**: Sempre considerar o contexto individual
- **Monitoramento Contínuo**: Performance pode degradar com o tempo
- **Regulamentação**: Seguir normas de dispositivos médicos

---

**💡 Lembre-se**: Machine Learning em medicina requer validação rigorosa, interpretabilidade e consideração ética. O objetivo é auxiliar profissionais de saúde, não substituí-los!