# Aula 05 - Tópico 1: Classes e Objetos Básicos
# Demonstração de definição de classes, __init__, atributos e métodos

print("=== CLASSES E OBJETOS BÁSICOS ===\n")

# Classe simples
class Pessoa:
    def __init__(self, nome, idade):
        """Construtor da classe"""
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        """Método para apresentação"""
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos"
    
    def fazer_aniversario(self):
        """Incrementa a idade"""
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos"

# Classe com mais funcionalidades
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa conta bancária"""
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []
    
    def depositar(self, valor):
        """Deposita valor na conta"""
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R$ {valor:.2f}")
            return True
        return False
    
    def sacar(self, valor):
        """Saca valor da conta"""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R$ {valor:.2f}")
            return True
        return False
    
    def consultar_saldo(self):
        """Retorna saldo atual"""
        return f"Saldo de {self.titular}: R$ {self.saldo:.2f}"

# Classe para o domínio médico
class Paciente:
    def __init__(self, nome, idade, telefone):
        """Inicializa paciente"""
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.consultas = []
    
    def agendar_consulta(self, data, tipo):
        """Agenda nova consulta"""
        consulta = {
            "data": data,
            "tipo": tipo,
            "status": "Agendada"
        }
        self.consultas.append(consulta)
        return f"Consulta de {tipo} agendada para {data}"
    
    def listar_consultas(self):
        """Lista todas as consultas"""
        if not self.consultas:
            return "Nenhuma consulta agendada"
        
        resultado = f"Consultas de {self.nome}:\n"
        for i, consulta in enumerate(self.consultas, 1):
            resultado += f"  {i}. {consulta['data']} - {consulta['tipo']} ({consulta['status']})\n"
        
        return resultado.strip()

# Testando as classes
if __name__ == "__main__":
    print("=== TESTANDO CLASSES ===")
    
    # Teste classe Pessoa
    pessoa1 = Pessoa("Ana Silva", 25)
    pessoa2 = Pessoa("João Santos", 34)
    
    print(pessoa1.apresentar())
    print(pessoa2.apresentar())
    print(pessoa1.fazer_aniversario())
    
    # Teste classe ContaBancaria
    conta = ContaBancaria("Maria Costa", 1000)
    print(f"\n{conta.consultar_saldo()}")
    
    conta.depositar(500)
    conta.sacar(200)
    print(conta.consultar_saldo())
    print(f"Histórico: {conta.historico}")
    
    # Teste classe Paciente
    paciente = Paciente("Pedro Lima", 45, "(11) 99999-9999")
    print(f"\n{paciente.agendar_consulta('15/03/2024', 'Psicologia')}")
    print(paciente.agendar_consulta("22/03/2024", "Psiquiatria"))
    
    print(f"\n{paciente.listar_consultas()}")
    
    # Múltiplos objetos da mesma classe
    pacientes = [
        Paciente("Ana", 25, "(11) 11111-1111"),
        Paciente("João", 34, "(11) 22222-2222"),
        Paciente("Maria", 28, "(11) 33333-3333")
    ]
    
    print(f"\n=== MÚLTIPLOS PACIENTES ===")
    for paciente in pacientes:
        print(f"{paciente.nome} - {paciente.idade} anos - {paciente.telefone}")
    
    print("\n✅ Classes e objetos funcionando!")