# Aula 04 - Atividade Prática 3: Módulos Organizados
# Exemplo de como organizar código em módulos separados

# Este arquivo demonstra como importar e usar módulos
# Na prática, cada módulo seria um arquivo separado

print("=== SISTEMA MODULAR ===\n")

# Simulação do módulo utils.py
class Utils:
    @staticmethod
    def validar_cpf(cpf):
        """Valida formato de CPF"""
        import re
        return bool(re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf))
    
    @staticmethod
    def calcular_idade(data_nascimento):
        """Calcula idade a partir da data"""
        from datetime import date
        dia, mes, ano = map(int, data_nascimento.split('/'))
        nascimento = date(ano, mes, dia)
        hoje = date.today()
        
        idade = hoje.year - nascimento.year
        if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
            idade -= 1
        return idade

# Simulação do módulo pacientes.py
class GerenciadorPacientes:
    def __init__(self):
        self.pacientes = []
    
    def adicionar_paciente(self, nome, cpf, data_nascimento):
        """Adiciona novo paciente"""
        if not Utils.validar_cpf(cpf):
            return False, "CPF inválido"
        
        idade = Utils.calcular_idade(data_nascimento)
        
        paciente = {
            "id": len(self.pacientes) + 1,
            "nome": nome,
            "cpf": cpf,
            "idade": idade,
            "data_nascimento": data_nascimento
        }
        
        self.pacientes.append(paciente)
        return True, f"Paciente {nome} adicionado com sucesso"
    
    def buscar_paciente(self, nome):
        """Busca paciente por nome"""
        for paciente in self.pacientes:
            if nome.lower() in paciente["nome"].lower():
                return paciente
        return None
    
    def listar_pacientes(self):
        """Lista todos os pacientes"""
        return self.pacientes

# Simulação do módulo agendamentos.py
class GerenciadorAgendamentos:
    def __init__(self):
        self.agendamentos = []
    
    def agendar_consulta(self, paciente_id, data, horario, tipo="Psicologia"):
        """Agenda nova consulta"""
        agendamento = {
            "id": len(self.agendamentos) + 1,
            "paciente_id": paciente_id,
            "data": data,
            "horario": horario,
            "tipo": tipo,
            "status": "Agendado"
        }
        
        self.agendamentos.append(agendamento)
        return agendamento
    
    def listar_agendamentos(self):
        """Lista todos os agendamentos"""
        return self.agendamentos
    
    def cancelar_agendamento(self, agendamento_id):
        """Cancela um agendamento"""
        for agendamento in self.agendamentos:
            if agendamento["id"] == agendamento_id:
                agendamento["status"] = "Cancelado"
                return True
        return False

# Sistema principal que usa os módulos
class SistemaLunysse:
    def __init__(self):
        self.gerenciador_pacientes = GerenciadorPacientes()
        self.gerenciador_agendamentos = GerenciadorAgendamentos()
    
    def cadastrar_paciente_completo(self, nome, cpf, data_nascimento):
        """Cadastra paciente usando módulo de pacientes"""
        sucesso, mensagem = self.gerenciador_pacientes.adicionar_paciente(nome, cpf, data_nascimento)
        return sucesso, mensagem
    
    def agendar_para_paciente(self, nome_paciente, data, horario, tipo="Psicologia"):
        """Agenda consulta para um paciente"""
        paciente = self.gerenciador_pacientes.buscar_paciente(nome_paciente)
        
        if not paciente:
            return None, "Paciente não encontrado"
        
        agendamento = self.gerenciador_agendamentos.agendar_consulta(
            paciente["id"], data, horario, tipo
        )
        
        return agendamento, "Consulta agendada com sucesso"

# Teste do sistema modular
if __name__ == "__main__":
    sistema = SistemaLunysse()
    
    print("=== TESTANDO SISTEMA MODULAR ===")
    
    # Cadastrar pacientes
    sucesso1, msg1 = sistema.cadastrar_paciente_completo("Ana Silva", "123.456.789-00", "15/05/1990")
    sucesso2, msg2 = sistema.cadastrar_paciente_completo("João Santos", "987.654.321-00", "20/08/1985")
    
    print(f"Cadastro 1: {msg1}")
    print(f"Cadastro 2: {msg2}")
    
    # Listar pacientes
    pacientes = sistema.gerenciador_pacientes.listar_pacientes()
    print(f"\nPacientes cadastrados: {len(pacientes)}")
    for p in pacientes:
        print(f"  {p['nome']} - {p['idade']} anos")
    
    # Agendar consultas
    ag1, msg_ag1 = sistema.agendar_para_paciente("Ana Silva", "15/03/2024", "14:00", "Psicologia")
    ag2, msg_ag2 = sistema.agendar_para_paciente("João Santos", "16/03/2024", "09:00", "Psiquiatria")
    
    print(f"\nAgendamento 1: {msg_ag1}")
    print(f"Agendamento 2: {msg_ag2}")
    
    # Listar agendamentos
    agendamentos = sistema.gerenciador_agendamentos.listar_agendamentos()
    print(f"\nAgendamentos: {len(agendamentos)}")
    for ag in agendamentos:
        print(f"  ID {ag['id']}: Paciente {ag['paciente_id']} - {ag['data']} às {ag['horario']}")
    
    print("\n✅ Sistema modular funcionando!")