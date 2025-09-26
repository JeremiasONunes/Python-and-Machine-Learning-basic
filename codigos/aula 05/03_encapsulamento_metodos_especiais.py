# Aula 05 - Tópico 2: Encapsulamento e Métodos Especiais
# Demonstração de atributos privados, propriedades e métodos especiais

print("=== ENCAPSULAMENTO E MÉTODOS ESPECIAIS ===\n")

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa conta com encapsulamento"""
        self.titular = titular
        self._saldo = saldo_inicial  # Atributo protegido
        self.__numero_conta = id(self)  # Atributo privado
    
    @property
    def saldo(self):
        """Getter para saldo"""
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        """Setter para saldo com validação"""
        if valor >= 0:
            self._saldo = valor
        else:
            raise ValueError("Saldo não pode ser negativo")
    
    def depositar(self, valor):
        """Deposita valor na conta"""
        if valor > 0:
            self._saldo += valor
            return True
        return False
    
    def __str__(self):
        """Representação string amigável"""
        return f"Conta de {self.titular}: R$ {self._saldo:.2f}"
    
    def __repr__(self):
        """Representação técnica"""
        return f"ContaBancaria('{self.titular}', {self._saldo})"
    
    def __eq__(self, other):
        """Comparação de igualdade"""
        if isinstance(other, ContaBancaria):
            return self.titular == other.titular
        return False

class Produto:
    def __init__(self, nome, preco):
        """Inicializa produto"""
        self._nome = nome
        self._preco = preco
    
    @property
    def nome(self):
        """Getter para nome"""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        """Setter para nome com validação"""
        if valor and len(valor.strip()) > 0:
            self._nome = valor.strip()
        else:
            raise ValueError("Nome não pode estar vazio")
    
    @property
    def preco(self):
        """Getter para preço"""
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        """Setter para preço com validação"""
        if valor > 0:
            self._preco = valor
        else:
            raise ValueError("Preço deve ser positivo")
    
    def __str__(self):
        """String representation"""
        return f"{self._nome}: R$ {self._preco:.2f}"
    
    def __lt__(self, other):
        """Comparação menor que (para ordenação)"""
        return self._preco < other._preco

class PacienteSeguro:
    def __init__(self, nome, idade):
        """Paciente com dados protegidos"""
        self._nome = nome
        self._idade = idade
        self.__cpf = None  # Privado
        self._consultas = []
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if 0 <= valor <= 120:
            self._idade = valor
        else:
            raise ValueError("Idade inválida")
    
    def definir_cpf(self, cpf):
        """Define CPF (só pode ser definido uma vez)"""
        if self.__cpf is None:
            self.__cpf = cpf
        else:
            raise ValueError("CPF já foi definido")
    
    def __str__(self):
        return f"Paciente: {self._nome}, {self._idade} anos"
    
    def __len__(self):
        """Retorna número de consultas"""
        return len(self._consultas)
    
    def adicionar_consulta(self, consulta):
        """Adiciona consulta ao histórico"""
        self._consultas.append(consulta)

# Testando encapsulamento e métodos especiais
if __name__ == "__main__":
    print("=== TESTANDO ENCAPSULAMENTO ===")
    
    # Teste ContaBancaria
    conta1 = ContaBancaria("Ana Silva", 1000)
    conta2 = ContaBancaria("João Santos", 500)
    
    print(f"Conta 1: {conta1}")  # Usa __str__
    print(f"Representação: {repr(conta1)}")  # Usa __repr__
    
    # Teste propriedades
    print(f"Saldo inicial: R$ {conta1.saldo:.2f}")
    conta1.depositar(200)
    print(f"Após depósito: R$ {conta1.saldo:.2f}")
    
    # Teste comparação
    conta3 = ContaBancaria("Ana Silva", 2000)
    print(f"conta1 == conta3? {conta1 == conta3}")  # Usa __eq__
    
    # Teste Produto
    produto1 = Produto("Notebook", 2500.00)
    produto2 = Produto("Mouse", 50.00)
    
    print(f"\nProdutos:")
    print(f"  {produto1}")
    print(f"  {produto2}")
    
    # Ordenação usando __lt__
    produtos = [produto1, produto2]
    produtos_ordenados = sorted(produtos)
    print(f"Ordenados por preço: {[str(p) for p in produtos_ordenados]}")
    
    # Teste PacienteSeguro
    paciente = PacienteSeguro("Maria Costa", 28)
    print(f"\n{paciente}")
    
    paciente.adicionar_consulta("Consulta 1")
    paciente.adicionar_consulta("Consulta 2")
    print(f"Número de consultas: {len(paciente)}")  # Usa __len__
    
    # Teste validação
    try:
        paciente.idade = 150  # Deve dar erro
    except ValueError as e:
        print(f"Erro capturado: {e}")
    
    print("\n✅ Encapsulamento e métodos especiais funcionando!")