# 🔧 Aula 04 - Funções e Modularização

## 📋 Visão Geral

Esta aula introduz os conceitos fundamentais de **Funções** e **Modularização** em Python. Os códigos progridem desde funções básicas até sistemas modulares complexos, decoradores e programação funcional aplicados ao contexto médico.

---

## 🎯 Objetivos de Aprendizagem

- Dominar definição e uso de funções em Python
- Compreender parâmetros, argumentos e retornos
- Aplicar escopo de variáveis e organização modular
- Utilizar funções lambda e programação funcional
- Desenvolver sistemas médicos bem estruturados e reutilizáveis

---

## 📚 Fundamentos Teóricos

### 🔧 O que são Funções?

**Funções** são blocos de código reutilizáveis que executam tarefas específicas. Elas são fundamentais para organizar código, evitar repetição e criar programas modulares.

#### **Vantagens das Funções**:
- **Reutilização**: Código escrito uma vez, usado várias vezes
- **Organização**: Divisão de problemas complexos em partes menores
- **Manutenção**: Facilita correções e melhorias
- **Testabilidade**: Permite testes isolados de funcionalidades

### 🏗️ Anatomia de uma Função

```python
def nome_funcao(parametros):
    """Documentação da função"""
    # Corpo da função
    return resultado  # Opcional
```

#### **Componentes**:
- **def**: Palavra-chave para definir função
- **nome_funcao**: Identificador da função
- **parametros**: Entradas da função (opcional)
- **docstring**: Documentação (boa prática)
- **return**: Valor de retorno (opcional)

### 📥 Parâmetros e Argumentos

#### **Tipos de Parâmetros**:
- **Posicionais**: Ordem importa
- **Nomeados**: Especificados por nome
- **Padrão**: Valores default
- **Variáveis**: *args (posicionais), **kwargs (nomeados)

#### **Exemplos**:
```python
def funcao(obrigatorio, padrao="valor", *args, **kwargs):
    pass

# Chamadas
funcao("valor1")                    # Posicional
funcao("valor1", padrao="novo")     # Nomeado
funcao("valor1", "extra1", "extra2") # *args
funcao("valor1", chave="valor")     # **kwargs
```

### 🌐 Escopo de Variáveis

#### **Tipos de Escopo**:
- **Local**: Dentro da função
- **Global**: No módulo
- **Nonlocal**: Em função aninhada
- **Built-in**: Funções internas do Python

#### **Regra LEGB**:
1. **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

### 📦 Modularização

**Modularização** é a prática de dividir código em módulos (arquivos) separados para melhor organização e reutilização.

#### **Benefícios**:
- **Organização**: Código estruturado logicamente
- **Reutilização**: Módulos podem ser importados
- **Colaboração**: Equipes trabalham em módulos diferentes
- **Manutenção**: Mudanças isoladas por funcionalidade

### λ Programação Funcional

**Funções Lambda** são funções anônimas de uma linha, úteis para operações simples.

```python
# Lambda
quadrado = lambda x: x ** 2

# Equivalente com def
def quadrado(x):
    return x ** 2
```

#### **Funções de Alta Ordem**:
- **map()**: Aplica função a cada elemento
- **filter()**: Filtra elementos por condição
- **sorted()**: Ordena usando função como chave

---

## 📁 Códigos da Aula

### 1️⃣ **01_funcoes_basicas.py**

#### 🎯 **Conceito**: Fundamentos de Definição e Estrutura

Introduz sintaxe básica de funções, parâmetros e documentação.

#### 🔧 **Fundamentos Implementados**:
- **Definição Básica**: def, parâmetros, return
- **Tipos de Parâmetros**: Obrigatórios, opcionais, padrão
- **Documentação**: Docstrings com Args e Returns
- **Chamadas**: Posicionais e nomeadas
- **Validação**: Funções para verificar dados

#### 📊 **Aplicação Médica**:
- Saudação personalizada para pacientes
- Cálculo de idade a partir do ano de nascimento
- Cálculo de IMC com peso e altura
- Agendamento de consultas com valores padrão
- Validação de formato de telefone

#### 💡 **Conceitos Aprendidos**:
- Funções organizam código logicamente
- Parâmetros padrão aumentam flexibilidade
- Documentação é essencial para manutenção
- Validação garante integridade dos dados

---

### 2️⃣ **02_biblioteca_medica.py**

#### 🎯 **Conceito**: Biblioteca de Funções Médicas

Desenvolvimento de biblioteca especializada para cálculos médicos.

#### 🔧 **Fundamentos Implementados**:
- **Cálculos Médicos**: IMC, idade, frequência cardíaca máxima
- **Classificações**: Pressão arterial, peso corporal
- **Validações**: CPF, dados médicos
- **Documentação Completa**: Args, Returns, exemplos
- **Múltiplos Retornos**: Tuplas com valores e classificações

#### 📊 **Aplicação Médica**:
- Calcular IMC com classificação automática
- Determinar idade exata a partir de data de nascimento
- Validar formato de CPF brasileiro
- Calcular frequência cardíaca máxima por gênero
- Classificar pressão arterial por diretrizes médicas

#### 💡 **Conceitos Aprendidos**:
- Bibliotecas especializadas aumentam produtividade
- Múltiplos retornos fornecem informações completas
- Validação de dados é crucial em medicina
- Classificações automáticas auxiliam diagnósticos

---

### 3️⃣ **03_parametros_avancados.py**

#### 🎯 **Conceito**: Parâmetros Avançados e Flexibilidade

Demonstra *args, **kwargs e múltiplos retornos para máxima flexibilidade.

#### 🔧 **Fundamentos Implementados**:
- ***args**: Argumentos posicionais variáveis
- ****kwargs**: Argumentos nomeados variáveis
- **Combinação**: *args e **kwargs juntos
- **Múltiplos Retornos**: Tuplas e dicionários
- **Flexibilidade**: Funções que se adaptam aos dados

#### 📊 **Aplicação Médica**:
- Calcular média de notas variáveis
- Criar pacientes com dados flexíveis
- Processar consultas com opções configuráveis
- Analisar idades com estatísticas completas
- Gerar relatórios com dados dinâmicos

#### 💡 **Conceitos Aprendidos**:
- *args permite número variável de argumentos
- **kwargs oferece máxima flexibilidade
- Múltiplos retornos enriquecem informações
- Flexibilidade facilita reutilização

---

### 4️⃣ **04_processador_estatistico.py**

#### 🎯 **Conceito**: Processador Estatístico Flexível

Sistema avançado para processar dados médicos com estatísticas completas.

#### 🔧 **Fundamentos Implementados**:
- **Processamento Flexível**: Aceita diferentes tipos de dados
- **Estatísticas Avançadas**: Média, mediana, desvio padrão
- **Classificações**: Faixas etárias automáticas
- **Filtros Dinâmicos**: Múltiplos critérios de filtragem
- **Análise Completa**: Consultas com filtros opcionais

#### 📊 **Aplicação Médica**:
- Processar dados de pacientes com opções configuráveis
- Calcular estatísticas médicas completas
- Classificar pacientes por faixa etária
- Analisar consultas com filtros múltiplos
- Gerar relatórios estatísticos detalhados

#### 💡 **Conceitos Aprendidos**:
- Flexibilidade permite múltiplos casos de uso
- Estatísticas avançadas fornecem insights
- Filtros dinâmicos aumentam utilidade
- Processamento inteligente adapta-se aos dados

---

### 5️⃣ **05_escopo_variaveis.py**

#### 🎯 **Conceito**: Escopo e Gerenciamento de Variáveis

Demonstra escopo local vs global e boas práticas de gerenciamento.

#### 🔧 **Fundamentos Implementados**:
- **Variáveis Globais**: Acesso e modificação com global
- **Variáveis Locais**: Escopo limitado à função
- **Conflitos de Nome**: Precedência local sobre global
- **Funções Aninhadas**: Escopo de função dentro de função
- **Modificação Segura**: Técnicas para alterar estado global

#### 📊 **Aplicação Médica**:
- Contador global de pacientes
- Informações da clínica acessíveis globalmente
- Cálculos locais sem interferência
- Demonstração de conflitos e soluções
- Gerenciamento de listas globais

#### 💡 **Conceitos Aprendidos**:
- Escopo determina visibilidade de variáveis
- global permite modificação de variáveis globais
- Variáveis locais têm precedência
- Boas práticas evitam conflitos

---

### 6️⃣ **06_modulos_organizados.py**

#### 🎯 **Conceito**: Organização Modular do Sistema

Sistema modular simulando múltiplos arquivos para organização profissional.

#### 🔧 **Fundamentos Implementados**:
- **Módulos Simulados**: Classes representando módulos separados
- **Separação de Responsabilidades**: Cada módulo tem função específica
- **Integração**: Sistema principal coordenando módulos
- **Reutilização**: Componentes independentes e reutilizáveis
- **Organização**: Estrutura clara e manutenível

#### 📊 **Aplicação Médica**:
- Módulo Utils para validações e cálculos
- Módulo Pacientes para gerenciamento de cadastros
- Módulo Agendamentos para consultas
- Sistema principal integrando tudo
- Demonstração de arquitetura modular

#### 💡 **Conceitos Aprendidos**:
- Modularização melhora organização
- Separação de responsabilidades facilita manutenção
- Integração coordena componentes
- Arquitetura modular é escalável

---

### 7️⃣ **07_funcoes_lambda.py**

#### 🎯 **Conceito**: Programação Funcional com Lambda

Introduz funções lambda e programação funcional para processamento de dados.

#### 🔧 **Fundamentos Implementados**:
- **Funções Lambda**: Sintaxe e uso básico
- **map()**: Aplicar função a todos elementos
- **filter()**: Filtrar elementos por condição
- **sorted()**: Ordenação com função personalizada
- **Aplicações Práticas**: Processamento de dados médicos

#### 📊 **Aplicação Médica**:
- Cálculos simples com lambda (quadrado, soma)
- Filtrar pacientes por idade
- Ordenar pacientes por nome ou idade
- Processar consultas com transformações
- Encontrar valores máximos e mínimos

#### 💡 **Conceitos Aprendidos**:
- Lambda é útil para operações simples
- map, filter, sorted são poderosos com lambda
- Programação funcional é concisa
- Evitar lambda para lógica complexa

---

### 8️⃣ **08_sistema_filtros.py**

#### 🎯 **Conceito**: Sistema de Filtros Funcionais

Sistema completo usando programação funcional para filtros e transformações.

#### 🔧 **Fundamentos Implementados**:
- **Classes de Filtros**: Organização de filtros por categoria
- **Métodos Estáticos**: Funções puras sem estado
- **Filtros Compostos**: Combinação de múltiplos critérios
- **Transformações**: Modificação de dados com map
- **Análises Estatísticas**: Processamento funcional de dados

#### 📊 **Aplicação Médica**:
- Filtrar pacientes por faixa etária e cidade
- Filtrar agendamentos por status e tipo
- Calcular receitas e aplicar descontos
- Agrupar dados por critérios diversos
- Gerar estatísticas e rankings

#### 💡 **Conceitos Aprendidos**:
- Organização em classes melhora estrutura
- Métodos estáticos são ideais para filtros
- Programação funcional é poderosa para dados
- Composição de filtros aumenta flexibilidade

---

### 9️⃣ **09_desafio_decorador.py**

#### 🎯 **Conceito**: Decoradores para Funcionalidades Transversais

Implementa decorador para medir tempo de execução de funções.

#### 🔧 **Fundamentos Implementados**:
- **Decorador Básico**: Função que modifica outra função
- **functools.wraps**: Preserva metadados da função original
- **Medição de Tempo**: Captura tempo de execução
- **Decorador Parametrizado**: Configuração do comportamento
- **Aplicação Prática**: Monitoramento de performance

#### 📊 **Aplicação Médica**:
- Medir tempo de cálculos médicos
- Monitorar performance de processamento de dados
- Decorador para diferentes unidades de tempo
- Comparação com medição manual
- Automação de monitoramento

#### 💡 **Conceitos Aprendidos**:
- Decoradores adicionam funcionalidades sem modificar código
- functools.wraps preserva informações da função
- Decoradores parametrizados são mais flexíveis
- Monitoramento automático melhora qualidade

---

## 🔬 Conceitos Teóricos Detalhados

### 🏗️ **Princípios de Design de Funções**

#### **Single Responsibility Principle**
Cada função deve ter uma única responsabilidade bem definida.

#### **DRY (Don't Repeat Yourself)**
Evitar duplicação de código através de funções reutilizáveis.

#### **Pure Functions**
Funções que sempre retornam o mesmo resultado para as mesmas entradas, sem efeitos colaterais.

### 📥 **Parâmetros Avançados**

#### **Unpacking de Argumentos**
```python
def funcao(a, b, c):
    return a + b + c

args = (1, 2, 3)
resultado = funcao(*args)  # Unpacking posicional

kwargs = {'a': 1, 'b': 2, 'c': 3}
resultado = funcao(**kwargs)  # Unpacking nomeado
```

#### **Parâmetros Keyword-Only**
```python
def funcao(a, b, *, c, d):
    # c e d devem ser passados por nome
    pass

funcao(1, 2, c=3, d=4)  # Correto
```

### 🌐 **Escopo Avançado**

#### **Closures**
```python
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator  # Acessa variável do escopo externo
    return multiplicar

dobrar = criar_multiplicador(2)
```

#### **Nonlocal**
```python
def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar
```

### λ **Programação Funcional Avançada**

#### **Reduce**
```python
from functools import reduce

# Soma todos os elementos
soma = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
```

#### **Partial Functions**
```python
from functools import partial

def multiplicar(x, y):
    return x * y

dobrar = partial(multiplicar, 2)
resultado = dobrar(5)  # 10
```

---

## 🚀 Como Executar

### **Pré-requisitos**
```bash
# Apenas Python padrão necessário
python --version  # 3.6+
```

### **Execução Sequencial**
```bash
python 01_funcoes_basicas.py              # Fundamentos básicos
python 02_biblioteca_medica.py            # Biblioteca médica
python 03_parametros_avancados.py         # Parâmetros flexíveis
python 04_processador_estatistico.py      # Processamento avançado
python 05_escopo_variaveis.py             # Escopo e variáveis
python 06_modulos_organizados.py          # Organização modular
python 07_funcoes_lambda.py               # Programação funcional
python 08_sistema_filtros.py              # Sistema de filtros
python 09_desafio_decorador.py            # Decoradores
```

---

## 📊 Resultados Esperados

### **Fundamentos**
- Domínio completo de definição e uso de funções
- Compreensão de parâmetros e argumentos
- Fluência em documentação e boas práticas

### **Organização**
- Código bem estruturado e modular
- Separação clara de responsabilidades
- Reutilização eficiente de componentes

### **Programação Funcional**
- Uso eficaz de lambda, map, filter
- Processamento elegante de dados
- Código conciso e expressivo

### **Sistemas Avançados**
- Arquiteturas modulares escaláveis
- Decoradores para funcionalidades transversais
- Código profissional e manutenível

---

## 🎓 Aplicações no Sistema Lunysse

### **Biblioteca de Funções Médicas**
- **Cálculos**: IMC, idade, frequência cardíaca
- **Validações**: CPF, telefone, dados médicos
- **Classificações**: Pressão arterial, peso, risco
- **Conversões**: Unidades, formatos, tipos

### **Arquitetura Modular**
- **Módulo Pacientes**: Cadastro e gerenciamento
- **Módulo Agendamentos**: Consultas e horários
- **Módulo Relatórios**: Estatísticas e análises
- **Módulo Utils**: Funções utilitárias

### **Processamento de Dados**
- **Filtros**: Pacientes por critérios diversos
- **Transformações**: Aplicação de descontos, cálculos
- **Análises**: Estatísticas, rankings, agrupamentos
- **Relatórios**: Geração automática de insights

### **Funcionalidades Transversais**
- **Logging**: Decorador para registrar ações
- **Autenticação**: Decorador para verificar permissões
- **Cache**: Decorador para otimizar performance
- **Validação**: Decorador para verificar dados

---

## 📚 Próximos Passos

1. **Programação Orientada a Objetos**: Classes e objetos
2. **Tratamento de Exceções**: Try/except robusto
3. **Testes Unitários**: Pytest para funções
4. **Documentação**: Sphinx para APIs
5. **Async/Await**: Programação assíncrona

---

## 🔗 Recursos Adicionais

- [Python Functions Tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python Functions](https://realpython.com/defining-your-own-python-function/)
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Python Decorators](https://realpython.com/primer-on-python-decorators/)

---

## 💡 Boas Práticas com Funções

### **Design de Funções**
- **Nome Descritivo**: Função deve ter nome claro e específico
- **Responsabilidade Única**: Uma função, uma tarefa
- **Tamanho Adequado**: Máximo 20-30 linhas por função
- **Documentação**: Sempre documentar propósito e parâmetros

### **Parâmetros e Retornos**
- **Parâmetros Claros**: Nomes descritivos e tipos óbvios
- **Valores Padrão**: Para parâmetros opcionais comuns
- **Retornos Consistentes**: Sempre mesmo tipo ou None
- **Validação**: Verificar entradas quando necessário

### **Organização e Modularização**
- **Agrupamento Lógico**: Funções relacionadas juntas
- **Módulos Temáticos**: Separar por funcionalidade
- **Imports Limpos**: Importar apenas o necessário
- **Namespace**: Evitar poluição do namespace global

### **Código Médico**
- **Validação Rigorosa**: Dados médicos devem ser validados
- **Unidades Claras**: Sempre especificar unidades de medida
- **Referências**: Usar valores de referência médicos
- **Precisão**: Cuidado com arredondamentos em cálculos

---

**💡 Lembre-se**: Funções bem projetadas são a base de código limpo, reutilizável e manutenível. Em sistemas médicos, isso é especialmente importante para garantir confiabilidade e facilitar auditorias!