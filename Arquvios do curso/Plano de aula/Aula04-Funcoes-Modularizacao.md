# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Funções e Modularização

📌 **Disciplina:** Python Básico e Fundamentos de Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 4  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Definição e chamada de funções  
- Parâmetros e argumentos (posicionais, nomeados, padrão)  
- Retorno de valores e múltiplos retornos  
- Escopo de variáveis (local vs global)  
- Funções lambda e funções de alta ordem  

### 🎯 Objetivo Geral
Criar funções reutilizáveis e organizar código de forma modular para desenvolver sistemas maintíveis e escaláveis

### 💡 Habilidades e Competências
✅ Desenvolver funções com diferentes tipos de parâmetros  
✅ Implementar modularização para reutilização de código  
✅ Compreender e aplicar escopo de variáveis  
✅ Utilizar funções lambda para operações simples  

### 📌 Materiais Necessários
📌 Ambiente Python configurado  
📌 Códigos das aulas anteriores para refatoração  
📌 VSCode para organização de módulos  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Problematização:**  
"Como evitar repetir o mesmo código várias vezes no sistema de agendamentos? Como criar um código que outros desenvolvedores possam facilmente entender e reutilizar?" Discussão sobre modularização e reutilização.

---

### **Tópico 1: Definição e Estrutura de Funções (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Interativa:**  
Sintaxe de funções (def, return), parâmetros posicionais e nomeados, valores padrão, documentação com docstrings.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar biblioteca de funções para cálculos médicos  
📝 **Tarefa:**  
- **Metodologia Ativa - Aprendizagem Baseada em Problemas:**  
Desenvolver funções para calcular IMC, idade a partir da data de nascimento, e validar dados de entrada com documentação completa.

**Parte do Projeto Construída:** Biblioteca de funções utilitárias para cálculos médicos

---

### **Tópico 2: Parâmetros Avançados e Múltiplos Retornos (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Guiada:**  
*args e **kwargs, unpacking de argumentos, retorno de múltiplos valores usando tuplas e dicionários.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar funções flexíveis de processamento  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação em Pares:**  
Criar funções que processem dados de pacientes com parâmetros flexíveis e retornem estatísticas completas (média, mediana, desvio).

**Parte do Projeto Construída:** Processador estatístico flexível de dados médicos

---

### **Tópico 3: Escopo de Variáveis e Organização (50min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Prática:**  
Variáveis locais vs globais, palavra-chave global, boas práticas de escopo, organização em módulos separados.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Refatorar código anterior em módulos organizados  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Problemas:**  
Reorganizar todo o código das aulas anteriores em módulos separados (pacientes.py, agendamentos.py, utils.py).

**Parte do Projeto Construída:** Estrutura modular do sistema com separação de responsabilidades

---

### **Tópico 4: Funções Lambda e Aplicações Práticas (50min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Interativa:**  
Sintaxe lambda, uso com map(), filter(), sorted(), casos de uso apropriados vs funções normais.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar processamento funcional de dados  
📝 **Tarefa:**  
- **Metodologia Ativa - Projeto Colaborativo:**  
Criar sistema de filtros e transformações usando lambda para processar listas de pacientes e agendamentos.

**Parte do Projeto Construída:** Sistema de filtros e transformações funcionais

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Roda de Conversa:**  
Análise da modularização realizada, discussão sobre legibilidade e maintibilidade do código. Comparação entre diferentes abordagens.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Gamificação:**  
Criar um decorador simples que registre o tempo de execução das funções desenvolvidas.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Exemplos de refatoração de código  
- Estrutura de projeto modular  
- Documentação de boas práticas  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Criação correta de funções com diferentes parâmetros  
✅ Compreensão de escopo de variáveis  
✅ Organização modular do código  
✅ Uso apropriado de funções lambda  

### **Avaliação Somativa (Entregáveis):**
✅ Biblioteca de funções utilitárias documentada  
✅ Código refatorado em módulos organizados  
✅ Sistema de processamento funcional implementado  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Código perfeitamente modularizado, funções bem documentadas, uso eficiente de recursos  
- **Bom (7-8):** Boa modularização, funções funcionais com documentação adequada  
- **Satisfatório (6-7):** Funções básicas implementadas, organização inicial dos módulos  
- **Insatisfatório (<6):** Dificuldades na criação de funções ou organização modular  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio completo de funções Python  
- Compreensão de escopo e modularização  
- Uso eficiente de funções lambda  

🎯 **Aplicação Prática:**  
- Código reutilizável e maintível  
- Estrutura modular de projetos  
- Processamento funcional de dados  

🎯 **Competências Profissionais:**  
- Arquitetura de software básica  
- Documentação técnica  
- Boas práticas de programação  

### **Conexão com o Projeto:**  
A modularização é fundamental para o desenvolvimento do sistema Lunysse, permitindo separar responsabilidades e facilitar manutenção e expansão futuras.

### **Preparação para Próxima Aula:**  
As funções desenvolvidas serão organizadas em classes para implementar programação orientada a objetos, criando uma estrutura ainda mais robusta.