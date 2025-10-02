# 🔢 Aula 06 - Computação Científica com NumPy

## 📋 Visão Geral

Esta aula introduz o **NumPy** (Numerical Python), a biblioteca fundamental para computação científica em Python. Os códigos progridem desde conceitos básicos de arrays até análises temporais avançadas e detecção de anomalias em dados médicos.

---

## 🎯 Objetivos de Aprendizagem

- Dominar arrays NumPy e suas propriedades fundamentais
- Implementar operações matemáticas e estatísticas eficientes
- Aplicar indexação avançada e broadcasting
- Manipular arrays multidimensionais para dados médicos
- Desenvolver algoritmos de análise temporal e detecção de anomalias

---

## 📚 Fundamentos Teóricos

### 🔢 O que é NumPy?

**NumPy** é a biblioteca base para computação científica em Python, fornecendo:

- **Arrays N-dimensionais**: Estruturas de dados homogêneas e eficientes
- **Operações Vetorizadas**: Cálculos rápidos em arrays inteiros
- **Broadcasting**: Operações entre arrays de diferentes formas
- **Funções Matemáticas**: Biblioteca completa de funções científicas
- **Integração**: Base para outras bibliotecas (Pandas, Scikit-learn, Matplotlib)

#### **Vantagens sobre Listas Python**:
- **Performance**: 10-100x mais rápido que listas Python
- **Memória**: Uso mais eficiente de memória
- **Funcionalidade**: Operações matemáticas nativas
- **Interoperabilidade**: Padrão para dados científicos

### 🏗️ Estrutura de Arrays

#### **Propriedades Fundamentais**:
- **Shape**: Dimensões do array (linhas, colunas, etc.)
- **Size**: Número total de elementos
- **Ndim**: Número de dimensões
- **Dtype**: Tipo de dados (int32, float64, etc.)

#### **Tipos de Arrays**:
- **1D**: Vetores (listas de valores)
- **2D**: Matrizes (tabelas de dados)
- **3D+**: Tensores (dados multidimensionais)

### 🧮 Operações Fundamentais

#### **Operações Elemento a Elemento**:
```python
a + b    # Soma
a * b    # Multiplicação
a ** 2   # Potenciação
np.sqrt(a)  # Raiz quadrada
```

#### **Operações de Agregação**:
```python
np.sum(a)     # Soma total
np.mean(a)    # Média
np.std(a)     # Desvio padrão
np.max(a)     # Valor máximo
```

#### **Broadcasting**:
Permite operações entre arrays de diferentes formas seguindo regras específicas.

---

## 📁 Códigos da Aula

### 1️⃣ **01_fundamentos_numpy.py**

#### 🎯 **Conceito**: Fundamentos e Criação de Arrays

Introduz os conceitos básicos do NumPy e métodos de criação de arrays.

#### 🔧 **Fundamentos Implementados**:
- **Criação de Arrays**: array(), zeros(), ones(), arange(), linspace()
- **Propriedades**: shape, size, ndim, dtype
- **Tipos de Dados**: int32, float64, especificação explícita
- **Arrays Aleatórios**: random.random(), random.randint()
- **Operações Básicas**: sum(), mean(), max(), min()
- **Indexação**: Acesso por índices e slicing
- **Reshape**: Mudança de forma dos arrays

#### 📊 **Aplicação Médica**:
- Criar arrays para armazenar dados de pacientes
- Demonstrar diferentes tipos de dados médicos
- Operações básicas em medições clínicas

#### 💡 **Conceitos Aprendidos**:
- Arrays são mais eficientes que listas Python
- Importância dos tipos de dados corretos
- Operações vetorizadas são mais rápidas
- Reshape permite reorganizar dados

---

### 2️⃣ **02_dados_vitais_numpy.py**

#### 🎯 **Conceito**: Sistema de Dados Vitais

Sistema prático para armazenar e analisar sinais vitais usando arrays 2D.

#### 🔧 **Fundamentos Implementados**:
- **Arrays 2D**: Organização matricial de dados médicos
- **Indexação 2D**: Acesso por paciente e por medição
- **Análise por Coluna**: Estatísticas por tipo de medição
- **Detecção de Condições**: Identificação de valores anormais
- **Expansão de Dados**: vstack() para adicionar novos pacientes
- **Cálculos Derivados**: IMC a partir de peso e altura

#### 📊 **Aplicação Médica**:
- Armazenar dados de 5 pacientes com 4 medições cada
- Identificar pacientes com pressão alta e febre
- Calcular estatísticas por tipo de medição
- Adicionar novos pacientes ao sistema

#### 💡 **Conceitos Aprendidos**:
- Arrays 2D são ideais para dados tabulares
- Indexação permite análises flexíveis
- Operações booleanas facilitam filtragem
- Expansão dinâmica de datasets

---

### 3️⃣ **03_operacoes_matematicas.py**

#### 🎯 **Conceito**: Operações Matemáticas e Estatísticas

Demonstra o poder computacional do NumPy para cálculos científicos.

#### 🔧 **Fundamentos Implementados**:
- **Operações Aritméticas**: +, -, *, /, ** elemento a elemento
- **Operações com Escalar**: Broadcasting automático
- **Funções Matemáticas**: sqrt(), log(), exp(), sin(), cos()
- **Estatísticas Básicas**: mean(), median(), std(), var()
- **Percentis**: percentile() para análise de distribuições
- **Agregações 2D**: Operações por eixo (axis=0, axis=1)
- **Funções de Comparação**: maximum(), minimum()

#### 📊 **Aplicação Médica**:
- Calcular estatísticas de sinais vitais
- Aplicar funções matemáticas em dados clínicos
- Analisar distribuições de medições
- Comparar valores entre pacientes

#### 💡 **Conceitos Aprendidos**:
- NumPy oferece biblioteca matemática completa
- Operações vetorizadas são muito eficientes
- Estatísticas por eixo permitem análises flexíveis
- Percentis são úteis para análise médica

---

### 4️⃣ **04_analisador_exames.py**

#### 🎯 **Conceito**: Analisador Estatístico de Exames

Sistema especializado para análise de exames laboratoriais com detecção de anomalias.

#### 🔧 **Fundamentos Implementados**:
- **Valores de Referência**: Definição de faixas normais
- **Detecção de Anomalias**: Comparação com valores de referência
- **Análise de Percentis**: Distribuição detalhada dos resultados
- **Múltiplas Alterações**: Identificação de pacientes com vários problemas
- **Score de Risco**: Algoritmo simples de pontuação
- **Classificação de Risco**: Baixo, moderado, alto

#### 📊 **Aplicação Médica**:
- Analisar 5 pacientes com 4 exames laboratoriais
- Detectar valores fora dos padrões de referência
- Calcular score de risco cardiovascular
- Identificar pacientes que precisam de atenção

#### 💡 **Conceitos Aprendidos**:
- Importância de valores de referência médicos
- Análise de múltiplas variáveis simultaneamente
- Scores de risco simplificam decisões clínicas
- Detecção automática melhora eficiência

---

### 5️⃣ **05_indexacao_avancada.py**

#### 🎯 **Conceito**: Indexação Avançada e Broadcasting

Técnicas avançadas de indexação para análises complexas de dados.

#### 🔧 **Fundamentos Implementados**:
- **Indexação Booleana**: Filtragem por condições lógicas
- **Múltiplas Condições**: Operadores & (and) e | (or)
- **Fancy Indexing**: Indexação com arrays de índices
- **Indexação 2D**: Acesso complexo em matrizes
- **Broadcasting**: Operações entre arrays de diferentes formas
- **Função where()**: Indexação condicional avançada
- **Substituição Condicional**: Modificação baseada em critérios

#### 📊 **Aplicação Médica**:
- Filtrar pacientes por múltiplos critérios
- Classificar por faixas etárias
- Substituir valores anômalos
- Análise segmentada de populações

#### 💡 **Conceitos Aprendidos**:
- Indexação booleana é muito poderosa
- Broadcasting permite operações flexíveis
- where() é versátil para condições complexas
- Técnicas avançadas aumentam produtividade

---

### 6️⃣ **06_filtros_medicos.py**

#### 🎯 **Conceito**: Sistema de Filtros Médicos Avançados

Sistema completo de filtragem para identificar pacientes com condições específicas.

#### 🔧 **Fundamentos Implementados**:
- **Critérios Médicos**: Definições clínicas padronizadas
- **Filtros Individuais**: Hipertensão, diabetes, obesidade, idade
- **Filtros Combinados**: Múltiplas condições simultaneamente
- **Grupos de Risco**: Classificação por nível de risco
- **Estatísticas por Grupo**: Análise segmentada
- **Filtros Personalizados**: Critérios específicos de acompanhamento

#### 📊 **Aplicação Médica**:
- Filtrar 8 pacientes por condições médicas
- Identificar grupos de alto risco
- Calcular estatísticas por segmento
- Determinar necessidade de acompanhamento

#### 💡 **Conceitos Aprendidos**:
- Filtros médicos seguem critérios clínicos
- Combinação de condições é comum em medicina
- Segmentação facilita cuidados personalizados
- Automação melhora triagem de pacientes

---

### 7️⃣ **07_arrays_multidimensionais.py**

#### 🎯 **Conceito**: Arrays Multidimensionais

Manipulação avançada de arrays 2D, 3D e operações de forma.

#### 🔧 **Fundamentos Implementados**:
- **Arrays 2D**: Criação e manipulação de matrizes
- **Arrays Especiais**: zeros(), ones(), eye() (identidade)
- **Reshape Avançado**: Mudança de forma com cálculo automático
- **Transpose**: Transposição de matrizes
- **Arrays 3D**: Estruturas tridimensionais (tensores)
- **Operações por Eixo**: Estatísticas em dimensões específicas
- **Concatenação**: vstack(), hstack() para juntar arrays
- **Divisão**: hsplit(), vsplit() para separar arrays

#### 📊 **Aplicação Médica**:
- Organizar dados médicos em estruturas complexas
- Manipular dados temporais multidimensionais
- Realizar operações matriciais em dados clínicos
- Reorganizar dados para diferentes análises

#### 💡 **Conceitos Aprendidos**:
- Arrays multidimensionais organizam dados complexos
- Reshape é fundamental para reorganização
- Operações por eixo permitem análises flexíveis
- Concatenação e divisão facilitam manipulação

---

### 8️⃣ **08_analise_temporal.py**

#### 🎯 **Conceito**: Análise de Evolução Temporal

Sistema avançado para analisar evolução de sinais vitais ao longo do tempo.

#### 🔧 **Fundamentos Implementados**:
- **Dados Temporais 3D**: (pacientes, dias, medições)
- **Análise de Tendências**: Comparação entre primeiro e último dia
- **Estatísticas Temporais**: Médias por dia e por paciente
- **Detecção de Dias Críticos**: Identificação de valores anômalos
- **Análise de Variabilidade**: Desvio padrão temporal
- **Comparação entre Pacientes**: Rankings de evolução
- **Estabilidade**: Classificação por variabilidade

#### 📊 **Aplicação Médica**:
- Monitorar 3 pacientes por 7 dias
- Analisar 4 sinais vitais por dia
- Detectar tendências de melhora ou piora
- Identificar pacientes mais estáveis

#### 💡 **Conceitos Aprendidos**:
- Dados temporais requerem estruturas 3D
- Tendências são mais importantes que valores absolutos
- Variabilidade indica estabilidade clínica
- Comparações temporais guiam tratamentos

---

### 9️⃣ **09_desafio_deteccao_anomalias.py**

#### 🎯 **Conceito**: Detecção de Anomalias

Algoritmos avançados para detectar anomalias em sinais vitais usando apenas NumPy.

#### 🔧 **Fundamentos Implementados**:
- **Método Z-Score**: Detecção baseada em desvios padrão
- **Método IQR**: Detecção usando quartis e outliers
- **Mudanças Súbitas**: Detecção de variações abruptas
- **Consolidação**: Combinação de múltiplos métodos
- **Classificação de Severidade**: Níveis de anomalia
- **Análise Temporal**: Anomalias ao longo do tempo

#### 📊 **Aplicação Médica**:
- Detectar anomalias em 30 dias de dados
- Aplicar 3 métodos diferentes de detecção
- Classificar severidade das anomalias
- Consolidar resultados para decisão clínica

#### 💡 **Conceitos Aprendidos**:
- Múltiplos métodos aumentam confiabilidade
- Z-score é eficaz para distribuições normais
- IQR é robusto para dados não-normais
- Detecção de mudanças identifica eventos agudos

---

## 🔬 Conceitos Teóricos Detalhados

### 📊 **Performance e Otimização**

#### **Vetorização**
```python
# Lento (loop Python)
result = []
for i in range(len(array)):
    result.append(array[i] * 2)

# Rápido (vetorizado)
result = array * 2
```

#### **Broadcasting Rules**
1. Arrays são alinhados pela direita
2. Dimensões de tamanho 1 são expandidas
3. Dimensões incompatíveis geram erro

### 🎯 **Indexação Avançada**

#### **Indexação Booleana**
```python
# Condição simples
mask = array > 5
filtered = array[mask]

# Múltiplas condições
mask = (array > 5) & (array < 10)
filtered = array[mask]
```

#### **Fancy Indexing**
```python
# Índices específicos
indices = [0, 2, 4]
selected = array[indices]

# Indexação 2D
rows = [0, 2]
cols = [1, 3]
selected = array[rows, cols]
```

### 📈 **Análise Estatística**

#### **Medidas de Tendência Central**
- **Média**: Valor médio dos dados
- **Mediana**: Valor central ordenado
- **Moda**: Valor mais frequente

#### **Medidas de Dispersão**
- **Desvio Padrão**: Variabilidade dos dados
- **Variância**: Quadrado do desvio padrão
- **Amplitude**: Diferença entre máximo e mínimo

#### **Percentis**
- **Q1 (25%)**: Primeiro quartil
- **Q2 (50%)**: Mediana
- **Q3 (75%)**: Terceiro quartil
- **IQR**: Q3 - Q1 (amplitude interquartil)

---

## 🚀 Como Executar

### **Pré-requisitos**
```bash
pip install numpy
```

### **Execução Sequencial**
```bash
python 01_fundamentos_numpy.py              # Conceitos básicos
python 02_dados_vitais_numpy.py             # Sistema de dados vitais
python 03_operacoes_matematicas.py          # Operações matemáticas
python 04_analisador_exames.py              # Análise de exames
python 05_indexacao_avancada.py             # Indexação avançada
python 06_filtros_medicos.py                # Filtros médicos
python 07_arrays_multidimensionais.py       # Arrays multidimensionais
python 08_analise_temporal.py               # Análise temporal
python 09_desafio_deteccao_anomalias.py     # Detecção de anomalias
```

---

## 📊 Resultados Esperados

### **Fundamentos**
- Domínio completo de criação e manipulação de arrays
- Compreensão de propriedades e tipos de dados
- Fluência em operações básicas

### **Análise de Dados**
- Capacidade de organizar dados médicos eficientemente
- Habilidade para calcular estatísticas relevantes
- Competência em detecção de padrões anômalos

### **Técnicas Avançadas**
- Proficiência em indexação complexa
- Domínio de arrays multidimensionais
- Expertise em análise temporal

### **Aplicações Médicas**
- Sistemas funcionais para dados clínicos
- Algoritmos de detecção de anomalias
- Análises estatísticas clinicamente relevantes

---

## 🎓 Aplicações no Sistema Lunysse

### **Armazenamento de Dados**
- **Arrays Estruturados**: Organização eficiente de dados de pacientes
- **Dados Temporais**: Histórico de sinais vitais e exames
- **Matrizes de Correlação**: Análise de relacionamentos entre variáveis

### **Análise Clínica**
- **Detecção de Anomalias**: Identificação automática de valores críticos
- **Análise Estatística**: Cálculo de métricas populacionais
- **Filtros Inteligentes**: Segmentação de pacientes por critérios clínicos
- **Monitoramento Temporal**: Acompanhamento de evolução clínica

### **Otimização de Performance**
- **Cálculos Rápidos**: Processamento eficiente de grandes volumes
- **Memória Otimizada**: Uso eficiente de recursos computacionais
- **Algoritmos Escaláveis**: Soluções que crescem com o sistema

### **Preparação para ML**
- **Pré-processamento**: Normalização e transformação de dados
- **Feature Engineering**: Criação de variáveis derivadas
- **Validação**: Verificação de qualidade dos dados
- **Pipeline de Dados**: Fluxo automatizado de processamento

---

## 📚 Próximos Passos

1. **Pandas**: Análise de dados estruturados e séries temporais
2. **Matplotlib**: Visualização de dados e gráficos científicos
3. **Scikit-learn**: Machine learning e análise preditiva
4. **SciPy**: Funções científicas avançadas e otimização
5. **Statsmodels**: Análise estatística e modelagem

---

## 🔗 Recursos Adicionais

- [NumPy Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [NumPy Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
- [Scientific Python Lectures](https://scipy-lectures.org/)

---

## 💡 Boas Práticas com NumPy

### **Performance**
- **Use Vetorização**: Evite loops Python quando possível
- **Tipos Apropriados**: Escolha dtype correto para economizar memória
- **Broadcasting**: Aproveite para operações eficientes
- **Views vs Copies**: Entenda quando dados são copiados

### **Código Limpo**
- **Nomes Descritivos**: Use nomes claros para arrays
- **Documentação**: Comente operações complexas
- **Modularização**: Separe lógica em funções
- **Validação**: Verifique shapes e tipos quando necessário

### **Dados Médicos**
- **Validação Clínica**: Sempre valide valores contra referências médicas
- **Unidades Consistentes**: Mantenha unidades padronizadas
- **Tratamento de Ausentes**: Defina estratégias para dados faltantes
- **Auditoria**: Mantenha rastro de transformações nos dados

---

**💡 Lembre-se**: NumPy é a base de todo o ecossistema científico Python. Dominar seus conceitos é essencial para análises eficientes e desenvolvimento de soluções robustas em saúde digital!