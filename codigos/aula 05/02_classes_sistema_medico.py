# Aula 05 - Atividade Prática 1: Classes Fundamentais do Sistema Médico
# Desenvolvimento das classes Paciente, Medico e Agendamento

from datetime import datetime

class Paciente:
    def __init__(self, nome, idade, cpf, telefone):
        """Inicializa um paciente"""
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.historico_consultas = []
    
    def cadastrar(self):
        """Confirma cadastro do paciente"""
        return f"Paciente {self.nome} cadastrado com sucesso!"
    
    def exibir_info(self):
        """Exibe informações do paciente"""
        info = f"Nome: {self.nome}\n"
        info += f"Idade: {self.idade} anos\n"
        info += f"CPF: {self.cpf}\n"
        info += f"Telefone: {self.telefone}\n"
        info += f"Consultas realizadas: {len(self.historico_consultas)}"
        return info
    
    def validar_dados(self):
        """Valida dados básicos do paciente"""
        if not self.nome or len(self.nome) < 2:
            return False, "Nome inválido"
        if self.idade < 0 or self.idade > 120:
            return False, "Idade inválida"
        if len(self.cpf) != 14:  # XXX.XXX.XXX-XX
            return False, "CPF inválido"
        return True, "Dados válidos"

class Medico:
    def __init__(self, nome, crm, especialidade, telefone):
        """Inicializa um médico"""
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.telefone = telefone
        self.agenda = []
    
    def cadastrar(self):
        """Confirma cadastro do médico"""
        return f"Dr(a). {self.nome} cadastrado(a) - CRM: {self.crm}"
    
    def exibir_info(self):
        """Exibe informações do médico"""
        info = f"Dr(a). {self.nome}\n"
        info += f"CRM: {self.crm}\n"
        info += f"Especialidade: {self.especialidade}\n"
        info += f"Telefone: {self.telefone}\n"
        info += f"Agendamentos: {len(self.agenda)}"
        return info
    
    def validar_dados(self):
        """Valida dados do médico"""
        if not self.nome or len(self.nome) < 2:
            return False, "Nome inválido"
        if not self.crm or len(self.crm) < 4:
            return False, "CRM inválido"
        if not self.especialidade:
            return False, "Especialidade obrigatória"
        return True, "Dados válidos"
    
    def adicionar_agendamento(self, agendamento_id):
        """Adiciona agendamento à agenda do médico"""
        self.agenda.append(agendamento_id)

class Agendamento:
    def __init__(self, paciente, medico, data, horario, tipo="Consulta"):
        """Inicializa um agendamento"""
        self.id = id(self)  # ID único baseado no objeto
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.horario = horario
        self.tipo = tipo
        self.status = "Agendado"
    
    def cadastrar(self):
        """Confirma o agendamento"""
        self.paciente.historico_consultas.append(self.id)
        self.medico.adicionar_agendamento(self.id)
        return f"Agendamento #{self.id} criado com sucesso!"
    
    def exibir_info(self):
        """Exibe informações do agendamento"""
        info = f"Agendamento #{self.id}\n"
        info += f"Paciente: {self.paciente.nome}\n"
        info += f"Médico: Dr(a). {self.medico.nome}\n"
        info += f"Data: {self.data} às {self.horario}\n"
        info += f"Tipo: {self.tipo}\n"
        info += f"Status: {self.status}"
        return info
    
    def validar_dados(self):
        """Valida dados do agendamento"""
        if not self.data or not self.horario:
            return False, "Data e horário obrigatórios"
        if not self.paciente or not self.medico:
            return False, "Paciente e médico obrigatórios"
        return True, "Agendamento válido"
    
    def confirmar(self):
        """Confirma a consulta"""
        self.status = "Confirmado"
        return f"Consulta confirmada para {self.data}"
    
    def cancelar(self):
        """Cancela o agendamento"""
        self.status = "Cancelado"
        return f"Agendamento cancelado"

# Teste das classes
if __name__ == "__main__":
    print("=== SISTEMA MÉDICO - CLASSES FUNDAMENTAIS ===\n")
    
    # Criar paciente
    paciente1 = Paciente("Ana Silva", 25, "123.456.789-00", "(11) 99999-1111")
    print(paciente1.cadastrar())
    
    valido, msg = paciente1.validar_dados()
    print(f"Validação: {msg}")
    
    # Criar médico
    medico1 = Medico("Carlos Santos", "CRM12345", "Psicologia", "(11) 88888-2222")
    print(f"\n{medico1.cadastrar()}")
    
    # Criar agendamento
    agendamento1 = Agendamento(paciente1, medico1, "15/03/2024", "14:00", "Consulta Inicial")
    print(f"\n{agendamento1.cadastrar()}")
    
    # Exibir informações
    print(f"\n=== INFORMAÇÕES ===")
    print(f"PACIENTE:\n{paciente1.exibir_info()}")
    print(f"\nMÉDICO:\n{medico1.exibir_info()}")
    print(f"\nAGENDAMENTO:\n{agendamento1.exibir_info()}")
    
    # Confirmar consulta
    print(f"\n{agendamento1.confirmar()}")
    print(f"Status atual: {agendamento1.status}")
    
    print("\n✅ Classes fundamentais implementadas!")