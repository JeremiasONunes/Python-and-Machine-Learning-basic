# Aula 05 - Atividade Prática 3: Hierarquia de Especialidades Médicas
# Implementação de classe base Profissional e especializações

class Profissional:
    def __init__(self, nome, registro, telefone, valor_consulta=150):
        """Classe base para profissionais da saúde"""
        self.nome = nome
        self.registro = registro
        self.telefone = telefone
        self.valor_consulta = valor_consulta
        self.agenda = []
        self.especialidade = "Geral"
    
    def agendar_consulta(self, paciente, data, horario):
        """Agenda consulta básica"""
        consulta = {
            "paciente": paciente,
            "data": data,
            "horario": horario,
            "tipo": self.especialidade,
            "valor": self.valor_consulta
        }
        self.agenda.append(consulta)
        return f"Consulta agendada com {self.nome}"
    
    def atender_paciente(self, paciente):
        """Atendimento básico"""
        return f"{self.nome} está atendendo {paciente}"
    
    def calcular_receita_mensal(self):
        """Calcula receita do mês"""
        return len(self.agenda) * self.valor_consulta
    
    def __str__(self):
        return f"{self.nome} - {self.especialidade} (R$ {self.valor_consulta})"

class Psicologo(Profissional):
    def __init__(self, nome, crp, telefone, abordagem="Cognitivo-Comportamental"):
        """Psicólogo especializado"""
        super().__init__(nome, crp, telefone, 150)
        self.especialidade = "Psicologia"
        self.abordagem = abordagem
        self.sessoes_realizadas = 0
    
    def fazer_sessao_terapia(self, paciente, duracao=50):
        """Realiza sessão de terapia"""
        self.sessoes_realizadas += 1
        return f"Sessão de {self.abordagem} com {paciente} ({duracao}min)"
    
    def atender_paciente(self, paciente):
        """Atendimento psicológico especializado"""
        base = super().atender_paciente(paciente)
        return f"{base} - Sessão de psicoterapia ({self.abordagem})"
    
    def relatorio_sessoes(self):
        """Relatório de sessões realizadas"""
        return f"Total de sessões realizadas: {self.sessoes_realizadas}"

class Psiquiatra(Profissional):
    def __init__(self, nome, crm, telefone):
        """Psiquiatra especializado"""
        super().__init__(nome, crm, telefone, 200)
        self.especialidade = "Psiquiatria"
        self.prescricoes = []
    
    def prescrever_medicamento(self, paciente, medicamento, dosagem):
        """Prescreve medicamento"""
        prescricao = {
            "paciente": paciente,
            "medicamento": medicamento,
            "dosagem": dosagem,
            "data": "hoje"  # Simplificado
        }
        self.prescricoes.append(prescricao)
        return f"Prescrito {medicamento} ({dosagem}) para {paciente}"
    
    def atender_paciente(self, paciente):
        """Atendimento psiquiátrico"""
        base = super().atender_paciente(paciente)
        return f"{base} - Consulta psiquiátrica com avaliação medicamentosa"
    
    def relatorio_prescricoes(self):
        """Relatório de prescrições"""
        return f"Total de prescrições: {len(self.prescricoes)}"

class Terapeuta(Profissional):
    def __init__(self, nome, registro, telefone, tipo_terapia="Familiar"):
        """Terapeuta especializado"""
        super().__init__(nome, registro, telefone, 120)
        self.especialidade = f"Terapia {tipo_terapia}"
        self.tipo_terapia = tipo_terapia
        self.grupos_atendidos = []
    
    def conduzir_terapia_grupo(self, participantes):
        """Conduz terapia em grupo"""
        grupo = {
            "participantes": participantes,
            "tipo": self.tipo_terapia,
            "data": "hoje"
        }
        self.grupos_atendidos.append(grupo)
        return f"Terapia {self.tipo_terapia} com {len(participantes)} participantes"
    
    def atender_paciente(self, paciente):
        """Atendimento terapêutico"""
        base = super().atender_paciente(paciente)
        return f"{base} - {self.especialidade}"
    
    def relatorio_grupos(self):
        """Relatório de grupos atendidos"""
        return f"Grupos de terapia conduzidos: {len(self.grupos_atendidos)}"

# Classe para gerenciar equipe
class EquipeProfissionais:
    def __init__(self):
        """Gerencia equipe de profissionais"""
        self.profissionais = []
    
    def adicionar_profissional(self, profissional):
        """Adiciona profissional à equipe"""
        self.profissionais.append(profissional)
        return f"{profissional.nome} adicionado à equipe"
    
    def listar_especialidades(self):
        """Lista todas as especialidades disponíveis"""
        especialidades = set(p.especialidade for p in self.profissionais)
        return list(especialidades)
    
    def calcular_receita_total(self):
        """Calcula receita total da equipe"""
        return sum(p.calcular_receita_mensal() for p in self.profissionais)
    
    def buscar_por_especialidade(self, especialidade):
        """Busca profissionais por especialidade"""
        return [p for p in self.profissionais if especialidade.lower() in p.especialidade.lower()]

# Teste da hierarquia
if __name__ == "__main__":
    print("=== HIERARQUIA DE PROFISSIONAIS ===\n")
    
    # Criar profissionais
    psicologo = Psicologo("Ana Silva", "CRP12345", "(11) 99999-1111", "Gestalt")
    psiquiatra = Psiquiatra("Carlos Santos", "CRM67890", "(11) 88888-2222")
    terapeuta = Terapeuta("Maria Costa", "REG54321", "(11) 77777-3333", "Casal")
    
    # Testar métodos específicos
    print("=== ATENDIMENTOS ===")
    print(psicologo.atender_paciente("João"))
    print(psiquiatra.atender_paciente("Pedro"))
    print(terapeuta.atender_paciente("Ana"))
    
    # Testar funcionalidades específicas
    print(f"\n=== FUNCIONALIDADES ESPECÍFICAS ===")
    print(psicologo.fazer_sessao_terapia("João", 60))
    print(psiquiatra.prescrever_medicamento("Pedro", "Ansiolítico", "10mg"))
    print(terapeuta.conduzir_terapia_grupo(["Ana", "Carlos"]))
    
    # Agendar consultas
    psicologo.agendar_consulta("João", "15/03/2024", "14:00")
    psiquiatra.agendar_consulta("Pedro", "16/03/2024", "09:00")
    
    # Criar equipe
    equipe = EquipeProfissionais()
    equipe.adicionar_profissional(psicologo)
    equipe.adicionar_profissional(psiquiatra)
    equipe.adicionar_profissional(terapeuta)
    
    print(f"\n=== EQUIPE ===")
    print(f"Especialidades: {equipe.listar_especialidades()}")
    print(f"Receita total: R$ {equipe.calcular_receita_total()}")
    
    # Buscar por especialidade
    psicologos = equipe.buscar_por_especialidade("Psicologia")
    print(f"Psicólogos na equipe: {[p.nome for p in psicologos]}")
    
    print("\n✅ Hierarquia de profissionais implementada!")