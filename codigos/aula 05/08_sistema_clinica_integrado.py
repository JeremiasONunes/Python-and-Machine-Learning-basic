# Aula 05 - Atividade Prática 4: Sistema Clínica Integrado
# Sistema completo usando composição para gerenciar pacientes, profissionais e agendamentos

class Paciente:
    def __init__(self, nome, idade, telefone):
        """Paciente do sistema"""
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.consultas = []
    
    def adicionar_consulta(self, consulta):
        """Adiciona consulta ao histórico"""
        self.consultas.append(consulta)
    
    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

class Profissional:
    def __init__(self, nome, especialidade, valor_consulta):
        """Profissional da clínica"""
        self.nome = nome
        self.especialidade = especialidade
        self.valor_consulta = valor_consulta
        self.agenda = []
    
    def adicionar_agendamento(self, agendamento):
        """Adiciona agendamento à agenda"""
        self.agenda.append(agendamento)
    
    def __str__(self):
        return f"Dr(a). {self.nome} - {self.especialidade}"

class Agendamento:
    def __init__(self, paciente, profissional, data, horario):
        """Agendamento de consulta"""
        self.id = id(self)
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.horario = horario
        self.status = "Agendado"
        self.valor = profissional.valor_consulta
    
    def confirmar(self):
        """Confirma o agendamento"""
        self.status = "Confirmado"
        self.paciente.adicionar_consulta(self)
        self.profissional.adicionar_agendamento(self)
    
    def cancelar(self):
        """Cancela o agendamento"""
        self.status = "Cancelado"
    
    def __str__(self):
        return f"{self.paciente.nome} → {self.profissional.nome} em {self.data} às {self.horario}"

class SistemaClinica:
    def __init__(self, nome_clinica):
        """Sistema principal da clínica"""
        self.nome = nome_clinica
        self.pacientes = []
        self.profissionais = []
        self.agendamentos = []
    
    def cadastrar_paciente(self, nome, idade, telefone):
        """Cadastra novo paciente"""
        paciente = Paciente(nome, idade, telefone)
        self.pacientes.append(paciente)
        return paciente
    
    def cadastrar_profissional(self, nome, especialidade, valor_consulta=150):
        """Cadastra novo profissional"""
        profissional = Profissional(nome, especialidade, valor_consulta)
        self.profissionais.append(profissional)
        return profissional
    
    def buscar_paciente(self, nome):
        """Busca paciente por nome"""
        for paciente in self.pacientes:
            if nome.lower() in paciente.nome.lower():
                return paciente
        return None
    
    def buscar_profissional(self, nome):
        """Busca profissional por nome"""
        for profissional in self.profissionais:
            if nome.lower() in profissional.nome.lower():
                return profissional
        return None
    
    def agendar_consulta(self, nome_paciente, nome_profissional, data, horario):
        """Agenda nova consulta"""
        paciente = self.buscar_paciente(nome_paciente)
        profissional = self.buscar_profissional(nome_profissional)
        
        if not paciente:
            return None, "Paciente não encontrado"
        
        if not profissional:
            return None, "Profissional não encontrado"
        
        agendamento = Agendamento(paciente, profissional, data, horario)
        agendamento.confirmar()
        self.agendamentos.append(agendamento)
        
        return agendamento, "Consulta agendada com sucesso"
    
    def listar_agendamentos_dia(self, data):
        """Lista agendamentos de um dia específico"""
        return [ag for ag in self.agendamentos if ag.data == data and ag.status != "Cancelado"]
    
    def calcular_receita_mensal(self):
        """Calcula receita mensal"""
        return sum(ag.valor for ag in self.agendamentos if ag.status == "Confirmado")
    
    def relatorio_especialidades(self):
        """Relatório por especialidade"""
        especialidades = {}
        
        for ag in self.agendamentos:
            if ag.status == "Confirmado":
                esp = ag.profissional.especialidade
                if esp not in especialidades:
                    especialidades[esp] = {"consultas": 0, "receita": 0}
                
                especialidades[esp]["consultas"] += 1
                especialidades[esp]["receita"] += ag.valor
        
        return especialidades
    
    def estatisticas_gerais(self):
        """Estatísticas gerais do sistema"""
        total_pacientes = len(self.pacientes)
        total_profissionais = len(self.profissionais)
        total_agendamentos = len(self.agendamentos)
        
        agendamentos_confirmados = len([ag for ag in self.agendamentos if ag.status == "Confirmado"])
        receita_total = self.calcular_receita_mensal()
        
        return {
            "pacientes": total_pacientes,
            "profissionais": total_profissionais,
            "agendamentos_total": total_agendamentos,
            "agendamentos_confirmados": agendamentos_confirmados,
            "receita_total": receita_total
        }

# Teste do sistema integrado
if __name__ == "__main__":
    print("=== SISTEMA CLÍNICA LUNYSSE ===\n")
    
    # Criar sistema
    clinica = SistemaClinica("Clínica Lunysse")
    
    # Cadastrar pacientes
    paciente1 = clinica.cadastrar_paciente("Ana Silva", 25, "(11) 99999-1111")
    paciente2 = clinica.cadastrar_paciente("João Santos", 34, "(11) 88888-2222")
    paciente3 = clinica.cadastrar_paciente("Maria Costa", 28, "(11) 77777-3333")
    
    # Cadastrar profissionais
    psicologo = clinica.cadastrar_profissional("Carlos Lima", "Psicologia", 150)
    psiquiatra = clinica.cadastrar_profissional("Ana Ferreira", "Psiquiatria", 200)
    terapeuta = clinica.cadastrar_profissional("Pedro Santos", "Terapia Familiar", 120)
    
    # Agendar consultas
    ag1, msg1 = clinica.agendar_consulta("Ana Silva", "Carlos Lima", "15/03/2024", "14:00")
    ag2, msg2 = clinica.agendar_consulta("João Santos", "Ana Ferreira", "15/03/2024", "09:00")
    ag3, msg3 = clinica.agendar_consulta("Maria Costa", "Pedro Santos", "16/03/2024", "16:00")
    
    print("=== AGENDAMENTOS ===")
    print(f"1. {msg1}")
    print(f"2. {msg2}")
    print(f"3. {msg3}")
    
    # Listar agendamentos do dia
    print(f"\n=== AGENDA DO DIA 15/03/2024 ===")
    agenda_dia = clinica.listar_agendamentos_dia("15/03/2024")
    for ag in agenda_dia:
        print(f"  {ag.horario} - {ag}")
    
    # Relatórios
    print(f"\n=== ESTATÍSTICAS GERAIS ===")
    stats = clinica.estatisticas_gerais()
    print(f"Pacientes cadastrados: {stats['pacientes']}")
    print(f"Profissionais: {stats['profissionais']}")
    print(f"Consultas confirmadas: {stats['agendamentos_confirmados']}")
    print(f"Receita total: R$ {stats['receita_total']}")
    
    # Relatório por especialidade
    print(f"\n=== RELATÓRIO POR ESPECIALIDADE ===")
    relatorio_esp = clinica.relatorio_especialidades()
    for esp, dados in relatorio_esp.items():
        print(f"{esp}: {dados['consultas']} consultas - R$ {dados['receita']}")
    
    print("\n✅ Sistema integrado funcionando perfeitamente!")