# 🏗️ Aula 05 - Programação Orientada a Objetos

## 📋 Visão Geral

Esta aula introduz os conceitos fundamentais da **Programação Orientada a Objetos (POO)** em Python. Os códigos progridem desde classes básicas até sistemas complexos com herança, encapsulamento, composição e padrões de design aplicados ao contexto médico.

---

## 🎯 Objetivos de Aprendizagem

- Dominar conceitos fundamentais de POO (classes, objetos, métodos)
- Implementar encapsulamento e métodos especiais
- Aplicar herança e especialização de classes
- Utilizar composição para criar sistemas integrados
- Desenvolver sistemas médicos robustos e escaláveis

---

## 📚 Fundamentos Teóricos

### 🏗️ O que é Programação Orientada a Objetos?

**POO** é um paradigma de programação baseado no conceito de "objetos", que contêm dados (atributos) e código (métodos). É uma forma de organizar e estruturar código de maneira mais natural e reutilizável.

#### **Pilares da POO**:
1. **Encapsulamento**: Proteção e controle de acesso aos dados
2. **Herança**: Reutilização de código através de hierarquias
3. **Polimorfismo**: Múltiplas formas de um mesmo comportamento
4. **Abstração**: Simplificação de conceitos complexos

### 🔧 Conceitos Fundamentais

#### **Classe vs Objeto**:
- **Classe**: Modelo ou "molde" que define estrutura e comportamento
- **Objeto**: Instância específica de uma classe

#### **Atributos e Métodos**:
- **Atributos**: Variáveis que armazenam dados do objeto
- **Métodos**: Funções que definem comportamentos do objeto

#### **Construtor (__init__)**:
Método especial chamado automaticamente quando um objeto é criado.

### 🔒 Encapsulamento

#### **Níveis de Acesso**:
- **Público**: Acesso livre (padrão)
- **Protegido**: `_atributo` (convenção, não obrigatório)
- **Privado**: `__atributo` (name mangling)

#### **Propriedades (@property)**:
Permitem controlar acesso a atributos através de getters e setters.

### 🧬 Herança

#### **Herança Simples**:
```python
class Profissional(Pessoa):
    def __init__(self, nome, registro):
        super().__init__(nome)
        self.registro = registro
```

#### **Sobrescrita de Métodos**:
Classes filhas podem redefinir métodos da classe pai.

### 🔗 Composição

**Composição** é uma alternativa à herança onde objetos contêm outros objetos como componentes.

```python
class Paciente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco  # Composição
```

---

## 📁 Códigos da Aula

### 1️⃣ **01_classes_objetos_basicos.py**

#### 🎯 **Conceito**: Fundamentos de Classes e Objetos

Introduz os conceitos básicos de definição de classes, construtor e métodos.

#### 🔧 **Fundamentos Implementados**:
- **Definição de Classes**: class, __init__, self
- **Atributos de Instância**: Variáveis específicas de cada objeto
- **Métodos**: Funções que operam nos dados do objeto
- **Instanciação**: Criação de objetos a partir de classes
- **Múltiplos Objetos**: Várias instâncias da mesma classe

#### 📊 **Aplicação Médica**:
- Classe Pessoa com apresentação e aniversário
- Classe ContaBancaria com depósitos e saques
- Classe Paciente com agendamento de consultas
- Sistema básico de gerenciamento de pacientes

#### 💡 **Conceitos Aprendidos**:
- Classes organizam código de forma natural
- Objetos mantêm estado independente
- Métodos encapsulam comportamentos
- Reutilização através de múltiplas instâncias

---

### 2️⃣ **02_classes_sistema_medico.py**

#### 🎯 **Conceito**: Classes Fundamentais do Sistema Médico

Desenvolvimento das classes principais para um sistema médico básico.

#### 🔧 **Fundamentos Implementados**:
- **Classe Paciente**: Dados pessoais e histórico de consultas
- **Classe Medico**: Informações profissionais e agenda
- **Classe Agendamento**: Relacionamento entre paciente e médico
- **Validação de Dados**: Métodos para verificar consistência
- **Relacionamentos**: Objetos que referenciam outros objetos

#### 📊 **Aplicação Médica**:
- Cadastro completo de pacientes com CPF e telefone
- Registro de médicos com CRM e especialidade
- Sistema de agendamentos com data, horário e tipo
- Validação de dados médicos essenciais

#### 💡 **Conceitos Aprendidos**:
- Classes modelam entidades do mundo real
- Relacionamentos entre objetos são naturais
- Validação garante integridade dos dados
- Métodos específicos para cada responsabilidade

---

### 3️⃣ **03_encapsulamento_metodos_especiais.py**

#### 🎯 **Conceito**: Encapsulamento e Métodos Especiais

Demonstra proteção de dados e métodos especiais para comportamentos customizados.

#### 🔧 **Fundamentos Implementados**:
- **Atributos Protegidos**: `_atributo` (convenção)
- **Atributos Privados**: `__atributo` (name mangling)
- **Propriedades**: @property, @setter para controle de acesso
- **Métodos Especiais**: __str__, __repr__, __eq__, __len__
- **Validação**: Controle rigoroso de entrada de dados

#### 📊 **Aplicação Médica**:
- ContaBancaria com saldo protegido
- Produto com preço validado
- PacienteSeguro com CPF privado e idade controlada
- Comparações e representações customizadas

#### 💡 **Conceitos Aprendidos**:
- Encapsulamento protege integridade dos dados
- Propriedades oferecem controle fino de acesso
- Métodos especiais customizam comportamentos
- Validação previne estados inválidos

---

### 4️⃣ **04_classes_com_encapsulamento.py**

#### 🎯 **Conceito**: Refatoração com Encapsulamento Completo

Refatoração das classes médicas aplicando encapsulamento e métodos especiais.

#### 🔧 **Fundamentos Implementados**:
- **Encapsulamento Completo**: Todos os atributos protegidos
- **Propriedades Médicas**: Controle de acesso a dados sensíveis
- **Validação Rigorosa**: Verificação de idade, telefone, etc.
- **Métodos Especiais**: Representação e comparação adequadas
- **Estado Controlado**: Ativação/desativação de médicos

#### 📊 **Aplicação Médica**:
- Paciente com dados protegidos e validados
- Médico com status ativo/inativo controlado
- Agendamento com estados bem definidos
- Sistema robusto contra dados inválidos

#### 💡 **Conceitos Aprendidos**:
- Encapsulamento melhora robustez do sistema
- Propriedades facilitam manutenção
- Validação é essencial em sistemas médicos
- Estados controlados previnem inconsistências

---

### 5️⃣ **05_heranca_especializacao.py**

#### 🎯 **Conceito**: Herança e Especialização

Demonstra herança simples, super() e sobrescrita de métodos.

#### 🔧 **Fundamentos Implementados**:
- **Classe Base**: Veiculo com comportamentos comuns
- **Classes Derivadas**: Carro e Moto especializados
- **super()**: Chamada de métodos da classe pai
- **Sobrescrita**: Redefinição de métodos em classes filhas
- **Hierarquia Médica**: Pessoa → Profissional → Especialistas

#### 📊 **Aplicação Médica**:
- Pessoa como classe base para todos
- Profissional herdando de Pessoa
- Psicologo e Psiquiatra especializando Profissional
- Métodos específicos para cada especialidade

#### 💡 **Conceitos Aprendidos**:
- Herança promove reutilização de código
- super() mantém funcionalidade da classe pai
- Especialização adiciona comportamentos específicos
- Hierarquias modelam relacionamentos naturais

---

### 6️⃣ **06_hierarquia_profissionais.py**

#### 🎯 **Conceito**: Hierarquia Completa de Especialidades

Sistema completo de herança para profissionais de saúde mental.

#### 🔧 **Fundamentos Implementados**:
- **Classe Base Profissional**: Comportamentos comuns
- **Especializações**: Psicologo, Psiquiatra, Terapeuta
- **Métodos Específicos**: Funcionalidades únicas por especialidade
- **Polimorfismo**: Mesmo método, comportamentos diferentes
- **Gerenciamento**: EquipeProfissionais para coordenação

#### 📊 **Aplicação Médica**:
- Profissional base com agenda e valor de consulta
- Psicologo com sessões de terapia e abordagens
- Psiquiatra com prescrições de medicamentos
- Terapeuta com terapias em grupo
- Sistema de busca por especialidade

#### 💡 **Conceitos Aprendidos**:
- Hierarquias complexas são naturais em medicina
- Polimorfismo permite tratamento uniforme
- Especialização adiciona valor específico
- Gerenciamento coordena diferentes tipos

---

### 7️⃣ **07_composicao_sistema.py**

#### 🎯 **Conceito**: Composição vs Herança

Demonstra composição como alternativa à herança para relacionamentos.

#### 🔧 **Fundamentos Implementados**:
- **Composição Básica**: Pessoa tem Endereco
- **Composição Complexa**: Carro tem Motor
- **Delegação**: Métodos que delegam para componentes
- **Sistema Médico**: Paciente, Consulta, Profissional relacionados
- **Gerenciamento**: SistemaClinica coordenando tudo

#### 📊 **Aplicação Médica**:
- Paciente com Endereco (composição)
- Consulta relacionando Paciente e Profissional
- SistemaClinica gerenciando todos os componentes
- Relatórios baseados em relacionamentos

#### 💡 **Conceitos Aprendidos**:
- Composição é mais flexível que herança
- Relacionamentos modelam mundo real
- Delegação mantém responsabilidades claras
- Sistemas integrados coordenam componentes

---

### 8️⃣ **08_sistema_clinica_integrado.py**

#### 🎯 **Conceito**: Sistema Completo Integrado

Sistema médico completo usando composição para máxima flexibilidade.

#### 🔧 **Fundamentos Implementados**:
- **Arquitetura por Composição**: Componentes independentes
- **Busca e Relacionamento**: Métodos para conectar entidades
- **Agendamento Inteligente**: Sistema que valida e conecta
- **Relatórios Avançados**: Análises por especialidade e período
- **Estatísticas**: Métricas de performance do sistema

#### 📊 **Aplicação Médica**:
- Sistema completo de clínica com múltiplos profissionais
- Agendamento automático com validação
- Relatórios financeiros por especialidade
- Estatísticas gerais de operação
- Busca inteligente de pacientes e profissionais

#### 💡 **Conceitos Aprendidos**:
- Sistemas reais requerem integração complexa
- Composição facilita manutenção e extensão
- Relatórios são essenciais para gestão
- Busca e relacionamento automatizam operações

---

### 9️⃣ **09_desafio_observer.py**

#### 🎯 **Conceito**: Padrão Observer para Notificações

Implementação do padrão Observer para sistema de notificações automáticas.

#### 🔧 **Fundamentos Implementados**:
- **Padrão Observer**: Subject e Observer abstratos
- **Notificações Automáticas**: Eventos disparam ações
- **Múltiplos Observadores**: Diferentes sistemas reagindo
- **Desacoplamento**: Componentes independentes mas coordenados
- **Sistemas Especializados**: Notificação, Auditoria, Financeiro

#### 📊 **Aplicação Médica**:
- Paciente observável que notifica eventos
- Sistema de notificações SMS/Email automático
- Auditoria registrando todos os eventos
- Sistema financeiro calculando receitas
- Lembretes automáticos para consultas

#### 💡 **Conceitos Aprendidos**:
- Padrões de design resolvem problemas comuns
- Observer permite reação automática a eventos
- Desacoplamento melhora manutenibilidade
- Sistemas médicos requerem múltiplas reações

---

## 🔬 Conceitos Teóricos Detalhados

### 🏗️ **Princípios SOLID**

#### **S - Single Responsibility**
Cada classe deve ter uma única responsabilidade.

#### **O - Open/Closed**
Classes abertas para extensão, fechadas para modificação.

#### **L - Liskov Substitution**
Objetos de classes derivadas devem substituir objetos da classe base.

#### **I - Interface Segregation**
Interfaces específicas são melhores que interfaces gerais.

#### **D - Dependency Inversion**
Dependa de abstrações, não de implementações concretas.

### 🔒 **Encapsulamento Avançado**

#### **Níveis de Proteção**:
```python
class Exemplo:
    def __init__(self):
        self.publico = "Todos podem acessar"
        self._protegido = "Convenção de proteção"
        self.__privado = "Name mangling aplicado"
```

#### **Propriedades Inteligentes**:
```python
@property
def idade(self):
    return self._idade

@idade.setter
def idade(self, valor):
    if 0 <= valor <= 120:
        self._idade = valor
    else:
        raise ValueError("Idade inválida")
```

### 🧬 **Herança vs Composição**

#### **Quando usar Herança**:
- Relacionamento "é um" (Psicologo é um Profissional)
- Comportamentos compartilhados
- Hierarquias naturais

#### **Quando usar Composição**:
- Relacionamento "tem um" (Paciente tem Endereco)
- Flexibilidade de mudança
- Múltiplas funcionalidades

### 🎭 **Polimorfismo**

```python
def atender_paciente(profissional, paciente):
    # Funciona com qualquer tipo de profissional
    return profissional.atender_paciente(paciente)
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
python 01_classes_objetos_basicos.py        # Conceitos básicos
python 02_classes_sistema_medico.py         # Classes médicas
python 03_encapsulamento_metodos_especiais.py  # Encapsulamento
python 04_classes_com_encapsulamento.py     # Refatoração
python 05_heranca_especializacao.py         # Herança
python 06_hierarquia_profissionais.py       # Hierarquia completa
python 07_composicao_sistema.py             # Composição
python 08_sistema_clinica_integrado.py      # Sistema integrado
python 09_desafio_observer.py               # Padrão Observer
```

---

## 📊 Resultados Esperados

### **Fundamentos**
- Domínio completo de classes e objetos
- Compreensão de encapsulamento e proteção
- Fluência em herança e especialização

### **Sistemas Médicos**
- Classes robustas para entidades médicas
- Validação rigorosa de dados clínicos
- Relacionamentos bem modelados

### **Arquitetura Avançada**
- Sistemas integrados e escaláveis
- Padrões de design aplicados
- Código reutilizável e manutenível

---

## 🎓 Aplicações no Sistema Lunysse

### **Modelagem de Entidades**
- **Pacientes**: Dados pessoais, histórico, preferências
- **Profissionais**: Especialidades, agenda, qualificações
- **Consultas**: Agendamentos, prontuários, resultados
- **Clínica**: Configurações, relatórios, estatísticas

### **Arquitetura do Sistema**
- **Camada de Domínio**: Classes de negócio bem definidas
- **Encapsulamento**: Proteção de dados sensíveis
- **Herança**: Especialização de profissionais
- **Composição**: Relacionamentos flexíveis

### **Funcionalidades Avançadas**
- **Notificações**: Sistema automático de alertas
- **Auditoria**: Rastreamento de todas as ações
- **Relatórios**: Análises baseadas em objetos
- **Validação**: Garantia de integridade dos dados

### **Escalabilidade**
- **Novos Tipos**: Fácil adição de especialidades
- **Funcionalidades**: Extensão sem quebrar código existente
- **Integrações**: Composição facilita conexões
- **Manutenção**: Código organizado e testável

---

## 📚 Próximos Passos

1. **Padrões de Design**: Strategy, Factory, Singleton
2. **Testes Unitários**: Pytest para classes médicas
3. **Persistência**: Salvamento de objetos em banco de dados
4. **APIs**: Exposição de classes via REST
5. **Interface Gráfica**: Tkinter ou web para interação

---

## 🔗 Recursos Adicionais

- [Python OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Real Python OOP](https://realpython.com/python3-object-oriented-programming/)
- [Design Patterns in Python](https://refactoring.guru/design-patterns/python)
- [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

---

## 💡 Boas Práticas em POO

### **Design de Classes**
- **Responsabilidade Única**: Cada classe tem um propósito claro
- **Nomes Descritivos**: Classes e métodos com nomes significativos
- **Coesão Alta**: Elementos relacionados ficam juntos
- **Acoplamento Baixo**: Dependências mínimas entre classes

### **Encapsulamento**
- **Dados Privados**: Proteger informações sensíveis
- **Interface Pública**: Métodos claros para interação
- **Validação**: Sempre validar entradas
- **Consistência**: Manter estado válido sempre

### **Herança e Composição**
- **Herança Parcimoniosa**: Usar apenas quando apropriado
- **Composição Preferível**: Mais flexível na maioria dos casos
- **Hierarquias Rasas**: Evitar muitos níveis de herança
- **Polimorfismo**: Aproveitar comportamentos uniformes

### **Código Médico**
- **Validação Clínica**: Sempre verificar valores médicos
- **Auditoria**: Registrar mudanças em dados sensíveis
- **Privacidade**: Proteger informações dos pacientes
- **Conformidade**: Seguir regulamentações de saúde

---

**💡 Lembre-se**: POO não é apenas sobre sintaxe, mas sobre modelar o mundo real de forma que o código seja intuitivo, reutilizável e fácil de manter. Em sistemas médicos, isso é especialmente importante para garantir confiabilidade e segurança!