# 📊 Aula 03 - Estruturas de Dados Python

## 📋 Visão Geral

Esta aula introduz as **Estruturas de Dados** fundamentais do Python: listas, dicionários, tuplas e conjuntos. Os códigos progridem desde conceitos básicos até sistemas complexos integrados, incluindo list comprehension e aplicações práticas no contexto médico.

---

## 🎯 Objetivos de Aprendizagem

- Dominar listas para armazenamento sequencial de dados
- Utilizar dicionários para estruturação de dados complexos
- Aplicar tuplas para dados imutáveis e conjuntos para operações matemáticas
- Implementar list comprehension para processamento eficiente
- Desenvolver sistemas médicos usando estruturas de dados apropriadas

---

## 📚 Fundamentos Teóricos

### 📊 O que são Estruturas de Dados?

**Estruturas de Dados** são formas organizadas de armazenar e manipular informações em programas. Python oferece estruturas nativas poderosas e flexíveis para diferentes necessidades.

#### **Tipos Principais**:
- **Lista**: Sequência mutável e ordenada
- **Dicionário**: Mapeamento chave-valor mutável
- **Tupla**: Sequência imutável e ordenada
- **Conjunto**: Coleção mutável de elementos únicos

### 📝 Listas - Armazenamento Sequencial

**Listas** são coleções ordenadas e mutáveis que permitem duplicatas.

#### **Características**:
- **Mutáveis**: Podem ser modificadas após criação
- **Ordenadas**: Mantêm ordem de inserção
- **Indexadas**: Acesso por posição (0, 1, 2...)
- **Heterogêneas**: Podem conter diferentes tipos

#### **Operações Principais**:
```python
lista = [1, 2, 3]
lista.append(4)        # Adicionar ao final
lista.insert(0, 0)     # Inserir em posição
lista.remove(2)        # Remover por valor
elemento = lista.pop() # Remover e retornar último
```

### 🗂️ Dicionários - Dados Estruturados

**Dicionários** são coleções de pares chave-valor, ideais para dados estruturados.

#### **Características**:
- **Mutáveis**: Podem ser modificados
- **Não-ordenados**: Ordem não garantida (Python < 3.7)
- **Chaves únicas**: Cada chave aparece apenas uma vez
- **Acesso rápido**: Busca por chave é O(1)

#### **Operações Principais**:
```python
dicionario = {"nome": "Ana", "idade": 25}
dicionario["telefone"] = "123456789"  # Adicionar
valor = dicionario.get("nome", "N/A") # Buscar seguro
del dicionario["idade"]               # Remover
```

### 🔒 Tuplas - Dados Imutáveis

**Tuplas** são sequências imutáveis, ideais para dados que não devem mudar.

#### **Características**:
- **Imutáveis**: Não podem ser modificadas
- **Ordenadas**: Mantêm ordem de criação
- **Indexadas**: Acesso por posição
- **Hashable**: Podem ser chaves de dicionário

#### **Usos Comuns**:
- Coordenadas geográficas
- Configurações fixas
- Retorno múltiplo de funções
- Chaves de dicionários compostas

### 🔢 Conjuntos - Operações Matemáticas

**Conjuntos** são coleções de elementos únicos com operações matemáticas.

#### **Características**:
- **Únicos**: Não permitem duplicatas
- **Mutáveis**: Podem ser modificados
- **Não-ordenados**: Sem ordem definida
- **Operações matemáticas**: União, interseção, diferença

#### **Operações Principais**:
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1 | conjunto2        # {1, 2, 3, 4, 5}
intersecao = conjunto1 & conjunto2   # {3}
diferenca = conjunto1 - conjunto2    # {1, 2}
```

### ⚡ List Comprehension

**List Comprehension** é uma sintaxe concisa para criar listas baseadas em outras sequências.

#### **Sintaxe**:
```python
# Básica
[expressao for item in sequencia]

# Com condição
[expressao for item in sequencia if condicao]

# Aninhada
[expressao for item1 in seq1 for item2 in seq2]
```

#### **Vantagens**:
- **Performance**: Mais rápida que loops tradicionais
- **Legibilidade**: Código mais conciso
- **Pythônica**: Estilo idiomático Python

---

## 📁 Códigos da Aula

### 1️⃣ **01_listas_basico.py**

#### 🎯 **Conceito**: Fundamentos de Listas

Introduz criação, manipulação e métodos essenciais de listas.

#### 🔧 **Fundamentos Implementados**:
- **Criação**: Diferentes formas de criar listas
- **Indexação**: Acesso por posição e fatiamento
- **Métodos**: append(), insert(), remove(), pop(), sort()
- **Operações**: Concatenação, repetição, busca
- **Listas Aninhadas**: Estruturas bidimensionais

#### 📊 **Aplicação Médica**:
- Lista de pacientes cadastrados
- Idades e dados numéricos
- Dados estruturados por paciente
- Operações de busca e ordenação
- Estatísticas básicas (max, min, sum)

#### 💡 **Conceitos Aprendidos**:
- Listas são mutáveis e flexíveis
- Indexação negativa acessa do final
- Métodos modificam a lista original
- Fatiamento cria novas listas

---

### 2️⃣ **02_gerenciador_pacientes.py**

#### 🎯 **Conceito**: Sistema CRUD com Listas

Sistema completo de gerenciamento usando listas como estrutura principal.

#### 🔧 **Fundamentos Implementados**:
- **CRUD Completo**: Create, Read, Update, Delete
- **Interface Interativa**: Menu com opções do usuário
- **Busca**: Localização de pacientes por nome
- **Ordenação**: Alfabética e reversa
- **Estatísticas**: Contagem e análises básicas

#### 📊 **Aplicação Médica**:
- Cadastro de pacientes em lista
- Busca por nome ou parte do nome
- Remoção segura com confirmação
- Ordenação alfabética de nomes
- Estatísticas do sistema

#### 💡 **Conceitos Aprendidos**:
- Listas são ideais para coleções simples
- Busca linear é O(n)
- Interface do usuário melhora usabilidade
- Validação previne erros

---

### 3️⃣ **03_dicionarios_basico.py**

#### 🎯 **Conceito**: Estruturação com Dicionários

Demonstra dicionários para dados estruturados e relacionamentos complexos.

#### 🔧 **Fundamentos Implementados**:
- **Criação**: Diferentes sintaxes de dicionários
- **Acesso**: Por chave e método get() seguro
- **Modificação**: Adição, alteração e remoção
- **Iteração**: Chaves, valores e itens
- **Dicionários Aninhados**: Estruturas hierárquicas

#### 📊 **Aplicação Médica**:
- Dados completos de pacientes
- Informações da clínica estruturadas
- Agendamentos por dia da semana
- Contagem de especialidades
- Configurações do sistema

#### 💡 **Conceitos Aprendidos**:
- Dicionários organizam dados relacionados
- Acesso por chave é muito rápido
- get() evita erros de chave inexistente
- Estruturas aninhadas modelam realidade

---

### 4️⃣ **04_sistema_pacientes_completo.py**

#### 🎯 **Conceito**: Sistema Completo com Dicionários

Sistema avançado usando dicionários aninhados para dados médicos complexos.

#### 🔧 **Fundamentos Implementados**:
- **Estrutura Hierárquica**: Dicionários dentro de dicionários
- **Dados Médicos Completos**: Pessoais, endereço, histórico
- **Sistema Interativo**: Cadastro e consulta completos
- **Busca Avançada**: Por múltiplos critérios
- **Relatórios**: Estatísticas detalhadas

#### 📊 **Aplicação Médica**:
- Prontuário eletrônico básico
- Dados pessoais, endereço e histórico médico
- Lista de consultas por paciente
- Cadastro interativo completo
- Estatísticas por especialidade

#### 💡 **Conceitos Aprendidos**:
- Dicionários aninhados modelam dados complexos
- Estrutura hierárquica facilita organização
- Sistemas reais requerem dados estruturados
- Interface amigável melhora experiência

---

### 5️⃣ **05_tuplas_conjuntos.py**

#### 🎯 **Conceito**: Tuplas Imutáveis e Conjuntos Matemáticos

Demonstra tuplas para dados fixos e conjuntos para operações matemáticas.

#### 🔧 **Fundamentos Implementados**:
- **Tuplas**: Criação, acesso, desempacotamento
- **Imutabilidade**: Dados que não devem mudar
- **Conjuntos**: Criação e operações matemáticas
- **Operações de Conjunto**: União, interseção, diferença
- **Aplicações Práticas**: Configurações e análises

#### 📊 **Aplicação Médica**:
- Coordenadas geográficas fixas
- Configurações imutáveis da clínica
- Horários fixos de funcionamento
- Especialidades disponíveis vs procuradas
- Análise de disponibilidade de médicos

#### 💡 **Conceitos Aprendidos**:
- Tuplas garantem imutabilidade
- Conjuntos eliminam duplicatas automaticamente
- Operações matemáticas são poderosas
- Estruturas apropriadas para cada necessidade

---

### 6️⃣ **06_horarios_especialidades.py**

#### 🎯 **Conceito**: Sistema com Tuplas e Conjuntos

Sistema prático combinando tuplas para horários fixos e conjuntos para especialidades.

#### 🔧 **Fundamentos Implementados**:
- **Configurações Fixas**: Tuplas para horários imutáveis
- **Especialidades**: Conjuntos para operações eficientes
- **Disponibilidade**: Interseção de conjuntos
- **Busca Inteligente**: Por especialidade e dia
- **Relatórios**: Estatísticas do sistema

#### 📊 **Aplicação Médica**:
- Horários fixos de funcionamento
- Especialidades de cada médico
- Disponibilidade por dia da semana
- Busca de médicos por especialidade
- Estatísticas de cobertura

#### 💡 **Conceitos Aprendidos**:
- Tuplas são ideais para configurações
- Conjuntos facilitam operações de disponibilidade
- Interseção resolve problemas complexos
- Estruturas apropriadas simplificam lógica

---

### 7️⃣ **07_list_comprehension.py**

#### 🎯 **Conceito**: Programação Funcional com Comprehensions

Introduz list comprehension para processamento eficiente de dados.

#### 🔧 **Fundamentos Implementados**:
- **Sintaxe Básica**: Expressões simples
- **Condicionais**: Filtragem com if
- **Comprehensions Aninhadas**: Estruturas complexas
- **Performance**: Comparação com loops tradicionais
- **Variações**: Set e dict comprehension

#### 📊 **Aplicação Médica**:
- Processamento de listas de pacientes
- Filtragem por critérios médicos
- Transformação de dados
- Análise de consultas
- Geração de relatórios

#### 💡 **Conceitos Aprendidos**:
- List comprehension é mais rápida
- Sintaxe concisa melhora legibilidade
- Filtragem integrada é poderosa
- Estilo pythônico é preferível

---

### 8️⃣ **08_sistema_integrado.py**

#### 🎯 **Conceito**: Sistema Integrado com Todas as Estruturas

Sistema completo que combina listas, dicionários, tuplas, conjuntos e comprehensions.

#### 🔧 **Fundamentos Implementados**:
- **Arquitetura Híbrida**: Cada estrutura para sua função
- **Configurações**: Tuplas para dados fixos
- **Dados**: Dicionários para informações estruturadas
- **Processamento**: List comprehensions para eficiência
- **Análises**: Conjuntos para operações matemáticas

#### 📊 **Aplicação Médica**:
- Sistema Lunysse completo integrado
- Configurações fixas e dados dinâmicos
- Filtros avançados com comprehensions
- Relatórios estatísticos completos
- Interface interativa profissional

#### 💡 **Conceitos Aprendidos**:
- Diferentes estruturas para diferentes necessidades
- Integração cria sistemas poderosos
- Comprehensions melhoram performance
- Arquitetura bem planejada facilita manutenção

---

### 9️⃣ **09_desafio_relatorios.py**

#### 🎯 **Conceito**: Sistema de Relatórios Avançado

Sistema complexo de relatórios usando todas as estruturas de dados de forma otimizada.

#### 🔧 **Fundamentos Implementados**:
- **Dados Complexos**: Estruturas aninhadas realistas
- **Relatórios Múltiplos**: Financeiro, demográfico, operacional
- **Análises Avançadas**: Top pacientes, métricas personalizadas
- **Filtros Dinâmicos**: Critérios configuráveis pelo usuário
- **Performance**: Uso otimizado de comprehensions

#### 📊 **Aplicação Médica**:
- Relatórios financeiros detalhados
- Análise demográfica de pacientes
- Métricas operacionais da clínica
- Rankings de pacientes mais ativos
- Filtros personalizados por critérios

#### 💡 **Conceitos Aprendidos**:
- Sistemas reais requerem múltiplas estruturas
- Relatórios são essenciais para gestão
- Comprehensions são poderosas para análises
- Flexibilidade melhora utilidade do sistema

---

## 🔬 Conceitos Teóricos Detalhados

### 📊 **Complexidade Computacional**

#### **Operações em Listas**:
- **Acesso por índice**: O(1)
- **Busca linear**: O(n)
- **Inserção no final**: O(1) amortizado
- **Inserção no meio**: O(n)

#### **Operações em Dicionários**:
- **Acesso por chave**: O(1) médio
- **Inserção**: O(1) médio
- **Remoção**: O(1) médio
- **Iteração**: O(n)

#### **Operações em Conjuntos**:
- **Verificação de pertencimento**: O(1) médio
- **União**: O(len(s1) + len(s2))
- **Interseção**: O(min(len(s1), len(s2)))

### 🎯 **Escolha da Estrutura Apropriada**

#### **Use Listas quando**:
- Ordem importa
- Permite duplicatas
- Acesso por posição é necessário
- Dados são homogêneos

#### **Use Dicionários quando**:
- Acesso por chave é necessário
- Dados são heterogêneos e relacionados
- Busca rápida é importante
- Estrutura hierárquica é útil

#### **Use Tuplas quando**:
- Dados não devem mudar
- Agrupamento lógico é necessário
- Performance é crítica
- Hashable é requerido

#### **Use Conjuntos quando**:
- Elementos únicos são necessários
- Operações matemáticas são úteis
- Verificação rápida de pertencimento
- Remoção de duplicatas

### ⚡ **Otimização com Comprehensions**

#### **Performance**:
```python
# Lento
resultado = []
for item in lista:
    if condicao(item):
        resultado.append(transformar(item))

# Rápido
resultado = [transformar(item) for item in lista if condicao(item)]
```

#### **Legibilidade**:
- Mais conciso
- Menos linhas de código
- Intenção mais clara
- Estilo pythônico

---

## 🚀 Como Executar

### **Pré-requisitos**
```bash
# Apenas Python padrão necessário
python --version  # 3.6+
```

### **Execução Sequencial**
```bash
python 01_listas_basico.py              # Fundamentos de listas
python 02_gerenciador_pacientes.py      # Sistema CRUD com listas
python 03_dicionarios_basico.py         # Fundamentos de dicionários
python 04_sistema_pacientes_completo.py # Sistema completo
python 05_tuplas_conjuntos.py           # Tuplas e conjuntos
python 06_horarios_especialidades.py    # Sistema prático
python 07_list_comprehension.py         # Comprehensions
python 08_sistema_integrado.py          # Sistema integrado
python 09_desafio_relatorios.py         # Relatórios avançados
```

---

## 📊 Resultados Esperados

### **Fundamentos**
- Domínio completo de listas, dicionários, tuplas e conjuntos
- Compreensão de quando usar cada estrutura
- Fluência em operações básicas e avançadas

### **Sistemas Práticos**
- Sistemas CRUD funcionais
- Interfaces interativas amigáveis
- Busca e filtragem eficientes
- Relatórios informativos

### **Otimização**
- Uso eficiente de list comprehensions
- Código mais conciso e legível
- Performance melhorada
- Estilo pythônico

---

## 🎓 Aplicações no Sistema Lunysse

### **Gerenciamento de Dados**
- **Listas**: Coleções de pacientes, consultas, horários
- **Dicionários**: Dados estruturados de pacientes, configurações
- **Tuplas**: Horários fixos, coordenadas, configurações imutáveis
- **Conjuntos**: Especialidades, disponibilidade, análises

### **Processamento Eficiente**
- **Comprehensions**: Filtros de pacientes, transformações de dados
- **Operações de Conjunto**: Disponibilidade de médicos, especialidades
- **Estruturas Aninhadas**: Prontuários eletrônicos, históricos

### **Relatórios e Análises**
- **Agregações**: Receitas, estatísticas, métricas
- **Filtros Dinâmicos**: Busca por critérios múltiplos
- **Rankings**: Top pacientes, especialidades mais procuradas

### **Interface e Usabilidade**
- **Menus Interativos**: Navegação intuitiva
- **Validação**: Entrada de dados segura
- **Feedback**: Mensagens informativas ao usuário

---

## 📚 Próximos Passos

1. **Funções e Modularização**: Organizar código em funções reutilizáveis
2. **Programação Orientada a Objetos**: Classes para modelar entidades
3. **Tratamento de Exceções**: Código robusto e confiável
4. **Bibliotecas Externas**: NumPy, Pandas para análise de dados
5. **Persistência**: Salvamento em arquivos e bancos de dados

---

## 🔗 Recursos Adicionais

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Python Data Structures](https://realpython.com/python-data-structures/)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python Collections Module](https://docs.python.org/3/library/collections.html)

---

## 💡 Boas Práticas com Estruturas de Dados

### **Escolha da Estrutura**
- **Analise o Problema**: Que operações são mais frequentes?
- **Performance**: Qual estrutura é mais eficiente?
- **Legibilidade**: Qual torna o código mais claro?
- **Manutenibilidade**: Qual facilita futuras modificações?

### **Listas**
- **Use append()** para adicionar ao final (mais eficiente)
- **Evite insert(0, item)** para listas grandes (O(n))
- **Prefira list comprehensions** para transformações
- **Use enumerate()** quando precisar de índice e valor

### **Dicionários**
- **Use get()** para acesso seguro a chaves
- **Prefira dict comprehensions** para transformações
- **Use setdefault()** para valores padrão
- **Considere defaultdict** para casos especiais

### **Tuplas**
- **Use para dados imutáveis** (coordenadas, configurações)
- **Aproveite desempacotamento** para múltiplos retornos
- **Use como chaves** de dicionários quando apropriado
- **Prefira namedtuple** para estruturas mais complexas

### **Conjuntos**
- **Use para eliminar duplicatas** rapidamente
- **Aproveite operações matemáticas** (união, interseção)
- **Use in** para verificação rápida de pertencimento
- **Considere frozenset** para conjuntos imutáveis

### **Código Médico**
- **Valide Dados**: Sempre verificar consistência de dados médicos
- **Estruture Hierarquicamente**: Use dicionários aninhados para prontuários
- **Mantenha Histórico**: Listas para sequências temporais
- **Garanta Unicidade**: Conjuntos para IDs únicos e especialidades

---

**💡 Lembre-se**: A escolha da estrutura de dados correta é fundamental para código eficiente e manutenível. Em sistemas médicos, isso é especialmente importante para garantir performance e confiabilidade no acesso aos dados dos pacientes!