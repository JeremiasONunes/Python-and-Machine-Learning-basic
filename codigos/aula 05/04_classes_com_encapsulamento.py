# Aula 05 - Atividade Prática 2: Classes com Encapsulamento e Representação
# Refatoração das classes médicas com proteção e métodos especiais

class Paciente:
    def __init__(self, nome, idade, cpf, telefone):
        """Inicializa paciente com encapsulamento"""
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._telefone = telefone
        self._consultas = []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if valor and len(valor.strip()) >= 2:
            self._nome = valor.strip()
        else:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if 0 <= valor <= 120:
            self._idade = valor
        else:
            raise ValueError("Idade deve estar entre 0 e 120 anos")
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        if len(valor) >= 10:
            self._telefone = valor
        else:
            raise ValueError("Telefone inválido")
    
    def adicionar_consulta(self, consulta_id):
        """Adiciona consulta ao histórico"""
        self._consultas.append(consulta_id)
    
    def __str__(self):
        """Representação amigável"""
        return f"{self._nome} ({self._idade} anos)"
    
    def __repr__(self):
        """Representação técnica"""
        return f"Paciente('{self._nome}', {self._idade}, '{self._cpf}', '{self._telefone}')"
    
    def __eq__(self, other):
        """Comparação por CPF"""
        if isinstance(other, Paciente):
            return self._cpf == other._cpf
        return False
    
    def __len__(self):
        """Retorna número de consultas"""
        return len(self._consultas)

class Medico:
    def __init__(self, nome, crm, especialidade):
        """Inicializa médico com encapsulamento"""
        self._nome = nome
        self._crm = crm
        self._especialidade = especialidade
        self._agenda = []
        self._ativo = True
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def crm(self):
        return self._crm
    
    @property
    def especialidade(self):
        return self._especialidade
    
    @property
    def ativo(self):
        return self._ativo
    
    def ativar(self):
        """Ativa o médico"""
        self._ativo = True
    
    def desativar(self):
        """Desativa o médico"""
        self._ativo = False
    
    def adicionar_agendamento(self, agendamento_id):
        """Adiciona agendamento à agenda"""
        if self._ativo:
            self._agenda.append(agendamento_id)
            return True
        return False
    
    def __str__(self):
        status = "Ativo" if self._ativo else "Inativo"
        return f"Dr(a). {self._nome} - {self._especialidade} ({status})"
    
    def __repr__(self):
        return f"Medico('{self._nome}', '{self._crm}', '{self._especialidade}')"
    
    def __eq__(self, other):
        """Comparação por CRM"""
        if isinstance(other, Medico):
            return self._crm == other._crm
        return False
    
    def __len__(self):
        """Retorna número de agendamentos"""
        return len(self._agenda)

class Agendamento:
    def __init__(self, paciente, medico, data, horario):
        """Inicializa agendamento protegido"""
        self._id = id(self)
        self._paciente = paciente
        self._medico = medico
        self._data = data
        self._horario = horario
        self._status = "Agendado"
    
    @property
    def id(self):
        return self._id
    
    @property
    def paciente(self):
        return self._paciente
    
    @property
    def medico(self):
        return self._medico
    
    @property
    def data(self):
        return self._data
    
    @property
    def horario(self):
        return self._horario
    
    @property
    def status(self):
        return self._status
    
    def confirmar(self):
        """Confirma o agendamento"""
        if self._status == "Agendado":
            self._status = "Confirmado"
            return True
        return False
    
    def cancelar(self):
        """Cancela o agendamento"""
        if self._status in ["Agendado", "Confirmado"]:
            self._status = "Cancelado"
            return True
        return False
    
    def __str__(self):
        return f"Consulta: {self._paciente.nome} com Dr(a). {self._medico.nome} em {self._data}"
    
    def __repr__(self):
        return f"Agendamento({self._paciente!r}, {self._medico!r}, '{self._data}', '{self._horario}')"
    
    def __eq__(self, other):
        """Comparação por ID"""
        if isinstance(other, Agendamento):
            return self._id == other._id
        return False

# Teste das classes refatoradas
if __name__ == "__main__":
    print("=== CLASSES COM ENCAPSULAMENTO ===\n")
    
    # Criar paciente
    paciente = Paciente("Ana Silva", 25, "123.456.789-00", "(11) 99999-1111")
    print(f"Paciente criado: {paciente}")
    print(f"Representação técnica: {repr(paciente)}")
    
    # Testar propriedades
    print(f"Nome: {paciente.nome}")
    print(f"Idade: {paciente.idade}")
    
    # Criar médico
    medico = Medico("Carlos Santos", "CRM12345", "Psicologia")
    print(f"\nMédico criado: {medico}")
    
    # Criar agendamento
    agendamento = Agendamento(paciente, medico, "15/03/2024", "14:00")
    print(f"\nAgendamento: {agendamento}")
    
    # Testar métodos
    paciente.adicionar_consulta(agendamento.id)
    medico.adicionar_agendamento(agendamento.id)
    
    print(f"Consultas do paciente: {len(paciente)}")
    print(f"Agendamentos do médico: {len(medico)}")
    
    # Testar validação
    try:
        paciente.idade = 150  # Deve dar erro
    except ValueError as e:
        print(f"\nErro capturado: {e}")
    
    # Testar status do agendamento
    print(f"\nStatus inicial: {agendamento.status}")
    agendamento.confirmar()
    print(f"Após confirmar: {agendamento.status}")
    
    print("\n✅ Classes com encapsulamento implementadas!")