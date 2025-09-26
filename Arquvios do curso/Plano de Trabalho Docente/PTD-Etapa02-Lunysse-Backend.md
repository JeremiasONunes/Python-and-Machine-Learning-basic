# 📘 PLANO DE TRABALHO DOCENTE  

## MODELO PEDAGÓGICO SENAC  

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga horária:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## SITUAÇÃO DE APRENDIZAGEM: Projeto Integrador - Sistema Lunysse FastAPI  

**Número de aulas:** 15 aulas  
**Carga horária prevista:** 60 horas (4h por aula)  

### Contexto + Cenário  
O mercado de saúde mental tem crescido exponencialmente, demandando sistemas digitais eficientes para gestão de consultas psicológicas. Os alunos desenvolverão o sistema Lunysse, uma API completa para agendamento psicológico com análise de risco por Machine Learning, aplicando metodologia de ensino baseada em projeto real.  

### Problema  
Como desenvolver um sistema backend completo e profissional para gestão de consultas psicológicas, integrando autenticação segura, banco de dados, análise de dados e algoritmos de Machine Learning para análise de risco de pacientes?  

### Desafios  
- Estruturar arquitetura FastAPI profissional com padrões de mercado  
- Implementar autenticação JWT e segurança da informação  
- Desenvolver CRUD completo com SQLAlchemy e validações Pydantic  
- Integrar algoritmos de ML para análise de risco de pacientes  
- Criar documentação técnica e versionamento colaborativo  

### Indicadores  
**Indicador 1:** Desenvolvimento orientado a objetos para dashboards, relatórios, sessões etc.  
**Indicador 2:** Uso de SQL para manipulação e relatórios  
**Indicador 3:** Documentação do projeto web  
**Indicador 4:** Integração de segurança da informação  

---

## Elementos de Competência  

| Conhecimentos | Habilidades | Atitudes/Valores |
|---------------|-------------|------------------|
| • Arquitetura FastAPI e padrões REST<br>• SQLAlchemy ORM e modelagem de dados<br>• Autenticação JWT e segurança<br>• Pydantic para validação de dados<br>• Machine Learning aplicado à saúde | • Estruturar projetos backend profissionais<br>• Implementar APIs RESTful seguras<br>• Desenvolver algoritmos de análise de dados<br>• Documentar sistemas complexos<br>• Trabalhar com versionamento Git | • Responsabilidade com dados sensíveis<br>• Colaboração em equipe de desenvolvimento<br>• Ética no tratamento de informações de saúde<br>• Busca por excelência técnica<br>• Pensamento sistêmico e analítico |

---

## Sugestões de Atividades de Aprendizagem  

### 🎓 Aula 1 – Estrutura do Projeto e Configuração Inicial  
**Objetivo**  
Configurar estrutura profissional do projeto FastAPI e ambiente de desenvolvimento  

**Atividades**  
- Criação da estrutura de pastas (app/, routers/, models/, schemas/, services/)  
- Configuração do main.py e dependências do requirements.txt  
- Setup do ambiente virtual e variáveis de ambiente (.env)  

**Indicador trabalhado**  
✔️ Desenvolvimento orientado a objetos para dashboards, relatórios, sessões etc.  

**Descrição alinhada ao indicador**  
O aluno estrutura o projeto seguindo padrões orientados a objetos, organizando módulos para diferentes funcionalidades do sistema  

---

### 🎓 Aula 2 – Configuração do Banco de Dados e SQLAlchemy  
**Objetivo**  
Implementar configuração do banco SQLite e setup do SQLAlchemy ORM  

**Atividades**  
- Configuração do database.py com engine e SessionLocal  
- Implementação da função get_db() para dependency injection  
- Criação da Base declarativa para modelos  

**Indicador trabalhado**  
✔️ Uso de SQL para manipulação e relatórios  

**Descrição alinhada ao indicador**  
O aluno configura a base para manipulação de dados SQL através do ORM SQLAlchemy  

---

### 🎓 Aula 3 – Modelagem de Dados - Usuários e Enums  
**Objetivo**  
Criar modelos SQLAlchemy para usuários, tipos e status do sistema  

**Atividades**  
- Implementação do modelo User com tipos (psicólogo/paciente)  
- Criação dos Enums (UserType, AppointmentStatus, RequestStatus)  
- Definição de relacionamentos e constraints  

**Indicador trabalhado**  
✔️ Desenvolvimento orientado a objetos para dashboards, relatórios, sessões etc.  

**Descrição alinhada ao indicador**  
O aluno aplica conceitos de POO na modelagem de dados, definindo classes e relacionamentos entre entidades  

---

### 🎓 Aula 4 – Modelos Completos - Pacientes, Agendamentos e Solicitações  
**Objetivo**  
Completar a modelagem com todas as entidades do sistema de agendamento  

**Atividades**  
- Implementação dos modelos Patient, Appointment e Request  
- Configuração de ForeignKeys e relacionamentos entre tabelas  
- Definição de campos obrigatórios e opcionais  

**Indicador trabalhado**  
✔️ Uso de SQL para manipulação e relatórios  

**Descrição alinhada ao indicador**  
O aluno define estruturas de dados SQL complexas com relacionamentos para suporte a relatórios e consultas  

---

### 🎓 Aula 5 – Schemas Pydantic e Validação de Dados  
**Objetivo**  
Criar schemas Pydantic para validação e serialização de dados da API  

**Atividades**  
- Implementação de schemas Base, Create e Response para cada entidade  
- Configuração de validações de email, datas e campos obrigatórios  
- Setup de schemas para Token e autenticação  

**Indicador trabalhado**  
✔️ Integração de segurança da informação  

**Descrição alinhada ao indicador**  
O aluno implementa validações rigorosas de dados como primeira camada de segurança da aplicação  

---

### 🎓 Aula 6 – Utilitários e Funções de Segurança  
**Objetivo**  
Desenvolver funções auxiliares para JWT, hash de senhas e cálculos  

**Atividades**  
- Implementação de hash e verificação de senhas com bcrypt  
- Criação e verificação de tokens JWT  
- Função para cálculo de idade e outras utilidades  

**Indicador trabalhado**  
✔️ Integração de segurança da informação  

**Descrição alinhada ao indicador**  
O aluno implementa mecanismos de segurança essenciais para proteção de dados e autenticação  

---

### 🎓 Aula 7 – Sistema de Autenticação - Login e Registro  
**Objetivo**  
Implementar rotas de autenticação com login e registro de usuários  

**Atividades**  
- Desenvolvimento do router auth.py com endpoints /login e /register  
- Implementação do serviço de autenticação (auth_service.py)  
- Tratamento de erros e validações de credenciais  

**Indicador trabalhado**  
✔️ Integração de segurança da informação  

**Descrição alinhada ao indicador**  
O aluno desenvolve sistema completo de autenticação seguindo boas práticas de segurança  

---

### 🎓 Aula 8 – CRUD de Pacientes - Gestão Completa  
**Objetivo**  
Desenvolver operações CRUD completas para gestão de pacientes  

**Atividades**  
- Implementação do router patients.py com todas as operações  
- Endpoints para listar, criar, atualizar e buscar pacientes  
- Sistema de anotações e histórico de sessões  

**Indicador trabalhado**  
✔️ Desenvolvimento orientado a objetos para dashboards, relatórios, sessões etc.  

**Descrição alinhada ao indicador**  
O aluno desenvolve funcionalidades orientadas a objetos para gestão completa de pacientes e sessões  

---

### 🎓 Aula 9 – Sistema de Agendamentos - Core do Negócio  
**Objetivo**  
Implementar o sistema central de agendamentos com todas as funcionalidades  

**Atividades**  
- Desenvolvimento do router appointments.py  
- Lógica de horários disponíveis e conflitos de agenda  
- Operações de criar, atualizar, cancelar e reagendar consultas  

**Indicador trabalhado**  
✔️ Desenvolvimento orientado a objetos para dashboards, relatórios, sessões etc.  

**Descrição alinhada ao indicador**  
O aluno implementa a lógica de negócio principal usando conceitos de POO para gestão de sessões  

---

### 🎓 Aula 10 – Gestão de Solicitações e Psicólogos  
**Objetivo**  
Desenvolver sistema de solicitações de novos pacientes e listagem de psicólogos  

**Atividades**  
- Implementação do router requests.py para solicitações  
- Router psychologists.py para listagem de profissionais  
- Workflow de aprovação e rejeição de solicitações  

**Indicador trabalhado**  
✔️ Desenvolvimento orientado a objetos para dashboards, relatórios, sessões etc.  

**Descrição alinhada ao indicador**  
O aluno desenvolve funcionalidades orientadas a objetos para gestão de solicitações e profissionais  

---

### 🎓 Aula 11 – Sistema de Relatórios e Estatísticas  
**Objetivo**  
Criar sistema completo de relatórios com estatísticas e análises  

**Atividades**  
- Implementação do router reports.py  
- Desenvolvimento do report_service.py com cálculos estatísticos  
- Geração de dados para dashboards e gráficos  

**Indicador trabalhado**  
✔️ Uso de SQL para manipulação e relatórios  

**Descrição alinhada ao indicador**  
O aluno desenvolve consultas SQL complexas e serviços para geração de relatórios estatísticos  

---

### 🎓 Aula 12 – Machine Learning - Análise de Risco de Pacientes  
**Objetivo**  
Implementar algoritmo de ML para análise de risco baseada em frequência e padrões  

**Atividades**  
- Desenvolvimento do router ml_analysis.py  
- Implementação do ml_service.py com algoritmo de risco  
- Cálculo de scores e classificação de níveis de risco  

**Indicador trabalhado**  
✔️ Desenvolvimento orientado a objetos para dashboards, relatórios, sessões etc.  

**Descrição alinhada ao indicador**  
O aluno aplica conceitos de POO e ML para desenvolver sistema inteligente de análise de risco  

---

### 🎓 Aula 13 – Testes, Validações e Seed Data  
**Objetivo**  
Implementar testes da API e sistema de dados iniciais para desenvolvimento  

**Atividades**  
- Criação do seed_data.py com dados de teste  
- Desenvolvimento de testes unitários (test_api.py, test_ml.py)  
- Validações de endpoints e regras de negócio  

**Indicador trabalhado**  
✔️ Integração de segurança da informação  

**Descrição alinhada ao indicador**  
O aluno implementa testes e validações como parte das boas práticas de segurança e qualidade  

---

### 🎓 Aula 14 – Documentação Técnica e Swagger  
**Objetivo**  
Criar documentação completa do projeto com Swagger/ReDoc e README técnico  

**Atividades**  
- Configuração avançada do Swagger UI com exemplos  
- Criação de documentação técnica detalhada (DOCUMENTACAO-BACKEND.md)  
- README.md com instruções de instalação e uso  

**Indicador trabalhado**  
✔️ Documentação do projeto web  

**Descrição alinhada ao indicador**  
O aluno produz documentação técnica completa e profissional para o projeto web desenvolvido  

---

### 🎓 Aula 15 – Deploy, Versionamento e Apresentação Final  
**Objetivo**  
Finalizar projeto com versionamento Git, deploy e apresentação das funcionalidades  

**Atividades**  
- Configuração do Git/GitHub com commits organizados  
- Preparação para deploy com configurações de produção  
- Apresentação final do projeto completo funcionando  

**Indicador trabalhado**  
✔️ Documentação do projeto web  

**Descrição alinhada ao indicador**  
O aluno finaliza a documentação do projeto com versionamento e prepara para apresentação profissional  

---

## Estratégias de Avaliação para esta Situação de Aprendizagem  

### Procedimentos de Avaliação  
- **Avaliação diagnóstica:** Verificação de conhecimentos em Python, APIs e banco de dados  
- **Avaliação formativa:** Entregas incrementais a cada aula, code review entre pares  
- **Avaliação somativa:** Projeto final completo funcionando com todas as funcionalidades implementadas  

### Instrumentos de Avaliação  
- **Ficha de observação** para acompanhar desenvolvimento das funcionalidades  
- **Estudo de caso** com cenários reais de uso do sistema  
- **Autoavaliação** do progresso no desenvolvimento do projeto  
- **Avaliação entre pares** através de code review e testes cruzados  
- **Projetos e entregas práticas** com código funcional, testes e documentação  

---

## Orientações específicas para esta Situação de Aprendizagem  

- **Estabelecer ambiente colaborativo:** Trabalho em equipes para desenvolvimento de diferentes módulos  
- **Foco na aplicação prática:** Cada funcionalidade deve ser testada e validada imediatamente  
- **Suporte individualizado:** Acompanhar dificuldades específicas na implementação de cada módulo  
- **Incentivo à reflexão crítica:** Análise de arquitetura, performance e segurança do sistema  
- **Monitoramento contínuo:** Verificar funcionamento através de testes automatizados e manuais  

---

## Recursos Didáticos  

### RD Padrão  
- Computadores com Python, FastAPI e ferramentas de desenvolvimento  
- Banco de dados SQLite para desenvolvimento local  
- Postman ou Insomnia para testes de API  
- Git/GitHub para versionamento colaborativo  

### RD Complementar  
- Swagger UI para documentação interativa  
- Jupyter Notebook para análise de dados ML  
- Docker para containerização (opcional)  
- Plataformas de deploy (Heroku, Railway) para demonstração  