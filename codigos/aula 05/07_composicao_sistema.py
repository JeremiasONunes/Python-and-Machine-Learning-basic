# Aula 05 - Tópico 4: Composição e Sistema Integrado
# Demonstração de composição vs herança e relacionamentos entre classes

print("=== COMPOSIÇÃO E SISTEMA INTEGRADO ===\n")

class Endereco:
    def __init__(self, rua, cidade, cep):
        """Classe para representar endereço"""
        self.rua = rua
        self.cidade = cidade
        self.cep = cep
    
    def __str__(self):
        return f"{self.rua}, {self.cidade} - {self.cep}"

class Pessoa:
    def __init__(self, nome, idade, endereco):
        """Pessoa com composição de endereço"""
        self.nome = nome
        self.idade = idade
        self.endereco = endereco  # Composição
    
    def __str__(self):
        return f"{self.nome} ({self.idade} anos) - {self.endereco}"

class Motor:
    def __init__(self, potencia, combustivel):
        """Classe Motor para composição"""
        self.potencia = potencia
        self.combustivel = combustivel
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        return f"Motor {self.potencia}HP ligado"
    
    def desligar(self):
        self.ligado = False
        return "Motor desligado"

class Carro:
    def __init__(self, marca, modelo, motor):
        """Carro com composição de motor"""
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composição
    
    def ligar(self):
        """Delega para o motor"""
        return self.motor.ligar()
    
    def info(self):
        status = "Ligado" if self.motor.ligado else "Desligado"
        return f"{self.marca} {self.modelo} - Motor {self.motor.potencia}HP ({status})"

# Sistema médico com composição
class Paciente:
    def __init__(self, nome, idade, endereco):
        """Paciente com endereço"""
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.historico = []
    
    def adicionar_consulta(self, consulta):
        """Adiciona consulta ao histórico"""
        self.historico.append(consulta)

class Consulta:
    def __init__(self, paciente, profissional, data, tipo):
        """Consulta relaciona paciente e profissional"""
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.tipo = tipo
        self.status = "Agendada"
    
    def confirmar(self):
        """Confirma a consulta"""
        self.status = "Confirmada"
        self.paciente.adicionar_consulta(self)
    
    def __str__(self):
        return f"{self.paciente.nome} com {self.profissional.nome} - {self.data}"

class Profissional:
    def __init__(self, nome, especialidade):
        """Profissional básico"""
        self.nome = nome
        self.especialidade = especialidade
        self.consultas = []
    
    def agendar(self, consulta):
        """Adiciona consulta à agenda"""
        self.consultas.append(consulta)

class SistemaClinica:
    def __init__(self, nome_clinica):
        """Sistema que gerencia tudo por composição"""
        self.nome = nome_clinica
        self.pacientes = []
        self.profissionais = []
        self.consultas = []
    
    def cadastrar_paciente(self, nome, idade, endereco):
        """Cadastra novo paciente"""
        paciente = Paciente(nome, idade, endereco)
        self.pacientes.append(paciente)
        return paciente
    
    def cadastrar_profissional(self, nome, especialidade):
        """Cadastra novo profissional"""
        profissional = Profissional(nome, especialidade)
        self.profissionais.append(profissional)
        return profissional
    
    def agendar_consulta(self, paciente, profissional, data, tipo):
        """Agenda nova consulta"""
        consulta = Consulta(paciente, profissional, data, tipo)
        consulta.confirmar()
        
        profissional.agendar(consulta)
        self.consultas.append(consulta)
        
        return consulta
    
    def listar_pacientes(self):
        """Lista todos os pacientes"""
        return [f"{p.nome} - {p.endereco.cidade}" for p in self.pacientes]
    
    def relatorio_consultas(self):
        """Gera relatório de consultas"""
        total = len(self.consultas)
        por_tipo = {}
        
        for consulta in self.consultas:
            tipo = consulta.tipo
            por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
        
        return {
            "total": total,
            "por_tipo": por_tipo
        }

# Testando composição
if __name__ == "__main__":
    print("=== TESTANDO COMPOSIÇÃO ===")
    
    # Exemplo básico de composição
    endereco1 = Endereco("Rua das Flores, 123", "São Paulo", "01234-567")
    pessoa1 = Pessoa("Ana Silva", 25, endereco1)
    
    print(f"Pessoa: {pessoa1}")
    
    # Carro com motor
    motor_v8 = Motor(300, "Gasolina")
    carro_esportivo = Carro("Ferrari", "F40", motor_v8)
    
    print(f"Carro: {carro_esportivo.info()}")
    print(carro_esportivo.ligar())
    print(f"Após ligar: {carro_esportivo.info()}")
    
    # Sistema médico integrado
    print(f"\n=== SISTEMA CLÍNICA ===")
    
    clinica = SistemaClinica("Clínica Lunysse")
    
    # Cadastrar endereços e pacientes
    endereco_ana = Endereco("Av. Paulista, 100", "São Paulo", "01310-100")
    endereco_joao = Endereco("Rua Oscar Freire, 200", "São Paulo", "01426-000")
    
    paciente_ana = clinica.cadastrar_paciente("Ana Silva", 25, endereco_ana)
    paciente_joao = clinica.cadastrar_paciente("João Santos", 34, endereco_joao)
    
    # Cadastrar profissionais
    psicologo = clinica.cadastrar_profissional("Dr. Carlos", "Psicologia")
    psiquiatra = clinica.cadastrar_profissional("Dra. Maria", "Psiquiatria")
    
    # Agendar consultas
    consulta1 = clinica.agendar_consulta(paciente_ana, psicologo, "15/03/2024", "Psicologia")
    consulta2 = clinica.agendar_consulta(paciente_joao, psiquiatra, "16/03/2024", "Psiquiatria")
    
    # Relatórios
    print(f"Pacientes: {clinica.listar_pacientes()}")
    
    relatorio = clinica.relatorio_consultas()
    print(f"Total de consultas: {relatorio['total']}")
    print(f"Por tipo: {relatorio['por_tipo']}")
    
    # Verificar relacionamentos
    print(f"\nConsulta 1: {consulta1}")
    print(f"Paciente da consulta: {consulta1.paciente.nome}")
    print(f"Endereço do paciente: {consulta1.paciente.endereco}")
    
    print("\n✅ Composição e sistema integrado funcionando!")