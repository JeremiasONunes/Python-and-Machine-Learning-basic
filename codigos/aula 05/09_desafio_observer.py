# Aula 05 - Desafio: Sistema de Notificações com Padrão Observer
# Implementação simples do padrão Observer para notificações entre classes

print("=== PADRÃO OBSERVER - SISTEMA DE NOTIFICAÇÕES ===\n")

class Observer:
    """Interface para observadores"""
    def notificar(self, evento, dados):
        """Método que será chamado quando houver notificação"""
        pass

class Subject:
    """Classe base para objetos observáveis"""
    def __init__(self):
        self._observers = []
    
    def adicionar_observer(self, observer):
        """Adiciona um observador"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remover_observer(self, observer):
        """Remove um observador"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notificar_observers(self, evento, dados=None):
        """Notifica todos os observadores"""
        for observer in self._observers:
            observer.notificar(evento, dados)

class Paciente(Subject):
    """Paciente que pode ser observado"""
    def __init__(self, nome, telefone):
        super().__init__()
        self.nome = nome
        self.telefone = telefone
        self.consultas = []
    
    def agendar_consulta(self, consulta):
        """Agenda consulta e notifica observadores"""
        self.consultas.append(consulta)
        self.notificar_observers("consulta_agendada", {
            "paciente": self.nome,
            "consulta": consulta
        })
    
    def cancelar_consulta(self, consulta_id):
        """Cancela consulta e notifica"""
        self.notificar_observers("consulta_cancelada", {
            "paciente": self.nome,
            "consulta_id": consulta_id
        })

class SistemaNotificacao(Observer):
    """Sistema de notificações por SMS/Email"""
    def __init__(self, nome):
        self.nome = nome
        self.notificacoes_enviadas = []
    
    def notificar(self, evento, dados):
        """Processa notificação recebida"""
        if evento == "consulta_agendada":
            mensagem = f"Consulta agendada para {dados['paciente']}"
            self.enviar_notificacao(mensagem)
        
        elif evento == "consulta_cancelada":
            mensagem = f"Consulta cancelada para {dados['paciente']}"
            self.enviar_notificacao(mensagem)
    
    def enviar_notificacao(self, mensagem):
        """Simula envio de notificação"""
        self.notificacoes_enviadas.append(mensagem)
        print(f"📱 {self.nome}: {mensagem}")

class SistemaAuditoria(Observer):
    """Sistema de auditoria que registra eventos"""
    def __init__(self):
        self.logs = []
    
    def notificar(self, evento, dados):
        """Registra evento no log"""
        log_entry = f"[LOG] {evento}: {dados}"
        self.logs.append(log_entry)
        print(f"📝 Auditoria: {log_entry}")

class SistemaFinanceiro(Observer):
    """Sistema financeiro que calcula receitas"""
    def __init__(self):
        self.receita_prevista = 0
        self.receita_perdida = 0
    
    def notificar(self, evento, dados):
        """Atualiza valores financeiros"""
        if evento == "consulta_agendada":
            valor = 150  # Valor padrão
            self.receita_prevista += valor
            print(f"💰 Financeiro: +R$ {valor} (Total previsto: R$ {self.receita_prevista})")
        
        elif evento == "consulta_cancelada":
            valor = 150
            self.receita_perdida += valor
            print(f"💸 Financeiro: -R$ {valor} perdidos (Total perdido: R$ {self.receita_perdida})")

class Agendamento(Subject):
    """Agendamento observável"""
    def __init__(self, paciente, profissional, data, horario):
        super().__init__()
        self.id = id(self)
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.horario = horario
        self.status = "Agendado"
    
    def confirmar(self):
        """Confirma agendamento"""
        self.status = "Confirmado"
        self.notificar_observers("agendamento_confirmado", {
            "agendamento_id": self.id,
            "paciente": self.paciente,
            "data": self.data
        })
    
    def cancelar(self):
        """Cancela agendamento"""
        self.status = "Cancelado"
        self.notificar_observers("agendamento_cancelado", {
            "agendamento_id": self.id,
            "paciente": self.paciente
        })

class GerenciadorLembrete(Observer):
    """Gerencia lembretes de consulta"""
    def __init__(self):
        self.lembretes = []
    
    def notificar(self, evento, dados):
        """Cria lembretes baseados em eventos"""
        if evento == "agendamento_confirmado":
            lembrete = f"Lembrete: {dados['paciente']} tem consulta em {dados['data']}"
            self.lembretes.append(lembrete)
            print(f"⏰ Lembrete criado: {lembrete}")

# Teste do padrão Observer
if __name__ == "__main__":
    print("=== TESTANDO PADRÃO OBSERVER ===")
    
    # Criar sistemas observadores
    notificacao = SistemaNotificacao("SMS/Email")
    auditoria = SistemaAuditoria()
    financeiro = SistemaFinanceiro()
    lembretes = GerenciadorLembrete()
    
    # Criar paciente observável
    paciente = Paciente("Ana Silva", "(11) 99999-1111")
    
    # Registrar observadores no paciente
    paciente.adicionar_observer(notificacao)
    paciente.adicionar_observer(auditoria)
    paciente.adicionar_observer(financeiro)
    
    # Testar eventos do paciente
    print("\n=== EVENTOS DO PACIENTE ===")
    paciente.agendar_consulta("Consulta Psicologia - 15/03/2024")
    paciente.cancelar_consulta("001")
    
    # Criar agendamento observável
    agendamento = Agendamento("João Santos", "Dr. Carlos", "16/03/2024", "14:00")
    
    # Registrar observadores no agendamento
    agendamento.adicionar_observer(notificacao)
    agendamento.adicionar_observer(lembretes)
    
    # Testar eventos do agendamento
    print("\n=== EVENTOS DO AGENDAMENTO ===")
    agendamento.confirmar()
    agendamento.cancelar()
    
    # Verificar resultados
    print(f"\n=== RESULTADOS ===")
    print(f"Notificações enviadas: {len(notificacao.notificacoes_enviadas)}")
    print(f"Logs de auditoria: {len(auditoria.logs)}")
    print(f"Receita prevista: R$ {financeiro.receita_prevista}")
    print(f"Receita perdida: R$ {financeiro.receita_perdida}")
    print(f"Lembretes criados: {len(lembretes.lembretes)}")
    
    print("\n✅ Padrão Observer implementado com sucesso!")