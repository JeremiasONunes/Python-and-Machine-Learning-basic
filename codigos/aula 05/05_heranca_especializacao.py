# Aula 05 - Tópico 3: Herança e Especialização
# Demonstração de herança simples, super() e sobrescrita de métodos

print("=== HERANÇA E ESPECIALIZAÇÃO ===\n")

# Classe base
class Veiculo:
    def __init__(self, marca, modelo, ano):
        """Inicializa veículo base"""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    
    def ligar(self):
        """Liga o veículo"""
        self.ligado = True
        return f"{self.modelo} ligado"
    
    def desligar(self):
        """Desliga o veículo"""
        self.ligado = False
        return f"{self.modelo} desligado"
    
    def info(self):
        """Informações básicas"""
        status = "Ligado" if self.ligado else "Desligado"
        return f"{self.marca} {self.modelo} ({self.ano}) - {status}"

# Classe derivada - Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        """Inicializa carro usando super()"""
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def abrir_porta(self):
        """Método específico do carro"""
        return f"Porta do {self.modelo} aberta"
    
    def info(self):
        """Sobrescreve método da classe pai"""
        info_base = super().info()
        return f"{info_base} - {self.portas} portas"

# Classe derivada - Moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        """Inicializa moto"""
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def empinar(self):
        """Método específico da moto"""
        if self.ligado:
            return f"{self.modelo} empinando!"
        return "Moto precisa estar ligada"
    
    def info(self):
        """Sobrescreve método da classe pai"""
        info_base = super().info()
        return f"{info_base} - {self.cilindradas}cc"

# Hierarquia para domínio médico
class Pessoa:
    def __init__(self, nome, idade, telefone):
        """Classe base para pessoas"""
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
    
    def apresentar(self):
        """Apresentação básica"""
        return f"Olá, eu sou {self.nome}"
    
    def info(self):
        """Informações básicas"""
        return f"{self.nome}, {self.idade} anos, Tel: {self.telefone}"

class Profissional(Pessoa):
    def __init__(self, nome, idade, telefone, registro, especialidade):
        """Profissional da saúde"""
        super().__init__(nome, idade, telefone)
        self.registro = registro
        self.especialidade = especialidade
    
    def apresentar(self):
        """Sobrescreve apresentação"""
        return f"Dr(a). {self.nome}, {self.especialidade}"
    
    def atender_paciente(self):
        """Método base para atendimento"""
        return f"Dr(a). {self.nome} está atendendo"

class Psicologo(Profissional):
    def __init__(self, nome, idade, telefone, crp):
        """Psicólogo especializado"""
        super().__init__(nome, idade, telefone, crp, "Psicologia")
        self.abordagem = "Cognitivo-Comportamental"
    
    def fazer_terapia(self):
        """Método específico do psicólogo"""
        return f"Sessão de terapia {self.abordagem} com {self.nome}"
    
    def atender_paciente(self):
        """Sobrescreve atendimento"""
        base = super().atender_paciente()
        return f"{base} - Sessão de psicoterapia"

class Psiquiatra(Profissional):
    def __init__(self, nome, idade, telefone, crm):
        """Psiquiatra especializado"""
        super().__init__(nome, idade, telefone, crm, "Psiquiatria")
    
    def prescrever_medicamento(self, medicamento):
        """Método específico do psiquiatra"""
        return f"Dr(a). {self.nome} prescreveu {medicamento}"
    
    def atender_paciente(self):
        """Sobrescreve atendimento"""
        base = super().atender_paciente()
        return f"{base} - Consulta psiquiátrica"

# Testando herança
if __name__ == "__main__":
    print("=== TESTANDO HERANÇA ===")
    
    # Teste veículos
    carro = Carro("Toyota", "Corolla", 2020, 4)
    moto = Moto("Honda", "CB600", 2019, 600)
    
    print(f"Carro: {carro.info()}")
    print(f"Moto: {moto.info()}")
    
    carro.ligar()
    moto.ligar()
    
    print(f"Após ligar - Carro: {carro.info()}")
    print(f"Após ligar - Moto: {moto.info()}")
    
    print(f"{carro.abrir_porta()}")
    print(f"{moto.empinar()}")
    
    # Teste profissionais
    print(f"\n=== PROFISSIONAIS ===")
    
    psicologo = Psicologo("Ana Silva", 35, "(11) 99999-1111", "CRP12345")
    psiquiatra = Psiquiatra("Carlos Santos", 45, "(11) 88888-2222", "CRM67890")
    
    print(f"{psicologo.apresentar()}")
    print(f"{psiquiatra.apresentar()}")
    
    print(f"{psicologo.atender_paciente()}")
    print(f"{psiquiatra.atender_paciente()}")
    
    print(f"{psicologo.fazer_terapia()}")
    print(f"{psiquiatra.prescrever_medicamento('Ansiolítico')}")
    
    # Verificar herança
    print(f"\n=== VERIFICAÇÃO DE HERANÇA ===")
    print(f"Psicólogo é Profissional? {isinstance(psicologo, Profissional)}")
    print(f"Psicólogo é Pessoa? {isinstance(psicologo, Pessoa)}")
    print(f"Carro é Veículo? {isinstance(carro, Veiculo)}")
    
    print("\n✅ Herança e especialização funcionando!")