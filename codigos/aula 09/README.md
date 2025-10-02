# 🧠 Aula 09 - Redes Neurais com TensorFlow/Keras

## 📋 Visão Geral

Esta aula introduz os conceitos fundamentais de **Redes Neurais Artificiais** e sua implementação prática usando **TensorFlow/Keras** para problemas de classificação médica. Os códigos evoluem do conceito mais básico (perceptron) até um sistema completo de IA médica.

---

## 🎯 Objetivos de Aprendizagem

- Compreender os fundamentos de redes neurais artificiais
- Implementar perceptrons e redes multicamadas
- Usar TensorFlow/Keras para deep learning
- Aplicar redes neurais em problemas médicos reais

---

## 📚 Fundamentos Teóricos

### 🧠 O que são Redes Neurais?

**Redes Neurais Artificiais** são modelos computacionais inspirados no funcionamento do cérebro humano. Elas consistem em:

- **Neurônios (nós)**: Unidades de processamento que recebem entradas e produzem saídas
- **Conexões (sinapses)**: Links entre neurônios com pesos associados
- **Camadas**: Grupos de neurônios organizados hierarquicamente

### ⚡ Como Funcionam?

1. **Entrada**: Dados são alimentados na rede
2. **Processamento**: Cada neurônio calcula uma soma ponderada das entradas
3. **Ativação**: Função de ativação determina a saída do neurônio
4. **Propagação**: Saída é passada para a próxima camada
5. **Aprendizado**: Pesos são ajustados baseados no erro

### 🔢 Matemática Básica

**Neurônio artificial:**
```
saída = f(Σ(peso_i × entrada_i) + bias)
```

Onde `f` é a função de ativação (ReLU, sigmoid, softmax, etc.)

---

## 📁 Códigos da Aula

### 1️⃣ **01_perceptron_simples.py**

#### 🎯 **Conceito**: Perceptron - O Neurônio Básico

O **perceptron** é a unidade mais simples de uma rede neural, capaz de resolver problemas linearmente separáveis.

#### 🔧 **Fundamentos Implementados**:
- **Função de Ativação Degrau**: Classifica em 0 ou 1
- **Algoritmo de Aprendizado**: Ajusta pesos baseado no erro
- **Convergência**: Para quando não há mais erros

#### 📊 **Aplicação Médica**:
- Classifica pacientes em **Alto/Baixo risco**
- Usa apenas 2 variáveis: idade e pressão arterial
- Demonstra separação linear de dados

#### 💡 **Conceitos Aprendidos**:
- Como um neurônio "aprende"
- Importância da normalização de dados
- Limitações de modelos lineares

---

### 2️⃣ **02_rede_neural_keras.py**

#### 🎯 **Conceito**: Rede Neural Multicamada (MLP)

Evolução do perceptron com **múltiplas camadas** capazes de resolver problemas não-lineares complexos.

#### 🏗️ **Arquitetura Implementada**:
```
Entrada (5 features) → Dense(16, ReLU) → Dense(8, ReLU) → Dense(3, Softmax)
```

#### 🔧 **Fundamentos Implementados**:
- **Camadas Dense**: Totalmente conectadas
- **Função ReLU**: `max(0, x)` - resolve problema do gradiente
- **Softmax**: Converte saídas em probabilidades
- **Backpropagation**: Algoritmo de treinamento (automático no Keras)

#### 📊 **Aplicação Médica**:
- Classifica em **3 categorias**: Baixo/Médio/Alto risco
- Usa **5 variáveis**: idade, pressão, glicose, IMC, colesterol
- Predições probabilísticas

#### 💡 **Conceitos Aprendidos**:
- Poder das camadas ocultas
- Otimização com Adam
- Early stopping para evitar overfitting
- Validação cruzada

---

### 3️⃣ **03_sistema_ia_medica_completo.py**

#### 🎯 **Conceito**: Sistema de IA Médica Completo

Sistema **end-to-end** que integra todos os conceitos em uma aplicação prática real.

#### 🏗️ **Arquitetura Avançada**:
```
Entrada (5) → Dense(32, ReLU) → Dropout(0.3) → Dense(16, ReLU) → Dropout(0.2) → Dense(8, ReLU) → Dense(3, Softmax)
```

#### 🔧 **Fundamentos Implementados**:
- **Dropout**: Regularização para prevenir overfitting
- **Callbacks**: Early stopping e redução de learning rate
- **Normalização**: StandardScaler para melhor convergência
- **Persistência**: Salvamento e carregamento de modelos

#### 📊 **Aplicação Médica**:
- **Dataset realista**: 1500 pacientes sintéticos
- **Análise individual**: Sistema de predição em tempo real
- **Relatórios detalhados**: Métricas de performance completas

#### 💡 **Conceitos Aprendidos**:
- Regularização e generalização
- Sistemas de produção
- Análise de performance
- Deploy de modelos

---

## 🔬 Conceitos Teóricos Detalhados

### 🎯 **Funções de Ativação**

#### **ReLU (Rectified Linear Unit)**
```python
f(x) = max(0, x)
```
- **Vantagem**: Resolve problema do gradiente desaparecendo
- **Uso**: Camadas ocultas

#### **Softmax**
```python
f(x_i) = exp(x_i) / Σ(exp(x_j))
```
- **Vantagem**: Converte saídas em probabilidades
- **Uso**: Classificação multiclasse

### 📈 **Processo de Treinamento**

1. **Forward Pass**: Dados fluem da entrada para saída
2. **Cálculo do Erro**: Diferença entre predição e realidade
3. **Backward Pass**: Gradientes são calculados
4. **Atualização**: Pesos são ajustados usando otimizador

### 🎛️ **Hiperparâmetros Importantes**

- **Learning Rate**: Velocidade de aprendizado
- **Batch Size**: Quantidade de amostras por atualização
- **Epochs**: Número de passadas pelos dados
- **Dropout**: Taxa de neurônios "desligados"

### 🚫 **Problemas Comuns**

#### **Overfitting**
- **Sintoma**: Alta acurácia no treino, baixa no teste
- **Solução**: Dropout, early stopping, mais dados

#### **Underfitting**
- **Sintoma**: Baixa acurácia em treino e teste
- **Solução**: Mais camadas, mais neurônios, menos regularização

---

## 🚀 Como Executar

### **Pré-requisitos**
```bash
pip install tensorflow numpy pandas matplotlib scikit-learn joblib
```

### **Execução Sequencial**
```bash
python 01_perceptron_simples.py      # Conceitos básicos
python 02_rede_neural_keras.py       # Rede multicamada
python 03_sistema_ia_medica_completo.py  # Sistema completo
```

---

## 📊 Resultados Esperados

### **Código 1 - Perceptron**
- Convergência em ~20-40 iterações
- Separação linear clara dos dados
- Acurácia: ~85-95% (dados linearmente separáveis)

### **Código 2 - Rede Neural**
- Treinamento em ~20-30 épocas
- Classificação em 3 classes
- Acurácia: ~90-95%

### **Código 3 - Sistema Completo**
- Modelo robusto com regularização
- Análise detalhada de performance
- Sistema pronto para produção

---

## 🎓 Aplicações no Sistema Lunysse

Estes conceitos podem ser aplicados no sistema Lunysse para:

- **Triagem Automática**: Classificar urgência de pacientes
- **Diagnóstico Assistido**: Sugerir possíveis condições
- **Predição de Risco**: Identificar pacientes de alto risco
- **Otimização de Recursos**: Alocar recursos baseado em predições

---

## 📚 Próximos Passos

1. **Redes Convolucionais (CNN)**: Para análise de imagens médicas
2. **Redes Recorrentes (RNN/LSTM)**: Para séries temporais de sinais vitais
3. **Transfer Learning**: Usar modelos pré-treinados
4. **Deploy em Produção**: Integrar com FastAPI no sistema Lunysse

---

## 🔗 Recursos Adicionais

- [TensorFlow Documentation](https://tensorflow.org)
- [Keras Guide](https://keras.io)
- [Deep Learning Book](https://deeplearningbook.org)
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com)

---

**💡 Lembre-se**: Redes neurais são ferramentas poderosas, mas requerem dados de qualidade e validação cuidadosa, especialmente em aplicações médicas críticas!