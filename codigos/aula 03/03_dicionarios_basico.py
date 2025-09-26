# Aula 03 - Tópico 2: Dicionários - Dados Estruturados
# Demonstração de criação, manipulação e métodos de dicionários

print("=== DICIONÁRIOS EM PYTHON ===\n")

# Criação de dicionários
paciente = {
    "nome": "Ana Silva",
    "idade": 25,
    "telefone": "(11) 99999-9999",
    "email": "ana@email.com"
}

print(f"Paciente: {paciente}")

# Acesso por chaves
print(f"\nNome: {paciente['nome']}")
print(f"Idade: {paciente['idade']}")

# Método get (mais seguro)
print(f"Email: {paciente.get('email', 'Não informado')}")
print(f"CPF: {paciente.get('cpf', 'Não informado')}")

# Adicionando e modificando
paciente["cpf"] = "123.456.789-00"
paciente["idade"] = 26
print(f"\nApós modificações: {paciente}")

# Métodos principais
print(f"\n=== MÉTODOS DE DICIONÁRIOS ===")
print(f"Chaves: {list(paciente.keys())}")
print(f"Valores: {list(paciente.values())}")
print(f"Itens: {list(paciente.items())}")

# Iteração
print(f"\nIterando sobre o dicionário:")
for chave, valor in paciente.items():
    print(f"  {chave}: {valor}")

# Dicionários aninhados
clinica = {
    "nome": "Clínica Lunysse",
    "endereco": {
        "rua": "Rua das Flores, 123",
        "cidade": "São Paulo",
        "cep": "01234-567"
    },
    "especialidades": ["Psicologia", "Psiquiatria", "Terapia"],
    "funcionarios": {
        "medicos": 5,
        "enfermeiros": 8,
        "administrativo": 3
    }
}

print(f"\nClínica: {clinica['nome']}")
print(f"Cidade: {clinica['endereco']['cidade']}")
print(f"Especialidades: {clinica['especialidades']}")
print(f"Total médicos: {clinica['funcionarios']['medicos']}")

# Operações úteis
print(f"\n=== OPERAÇÕES ===")
print(f"Tem 'nome'? {'nome' in paciente}")
print(f"Tem 'altura'? {'altura' in paciente}")
print(f"Quantidade de dados: {len(paciente)}")

# Removendo elementos
copia_paciente = paciente.copy()
cpf_removido = copia_paciente.pop("cpf", "Não encontrado")
print(f"CPF removido: {cpf_removido}")
print(f"Paciente sem CPF: {copia_paciente}")

# Atualizando dicionários
novos_dados = {
    "profissao": "Engenheira",
    "estado_civil": "Solteira"
}

paciente.update(novos_dados)
print(f"\nApós update: {paciente}")

# Dicionário de listas
agendamentos = {
    "segunda": ["09:00 - Ana Silva", "14:00 - João Santos"],
    "terca": ["10:00 - Maria Costa"],
    "quarta": ["08:00 - Pedro Lima", "16:00 - Carlos Souza"],
    "quinta": [],
    "sexta": ["15:00 - Ana Silva"]
}

print(f"\nAgendamentos da semana:")
for dia, consultas in agendamentos.items():
    print(f"  {dia.capitalize()}: {len(consultas)} consulta(s)")
    for consulta in consultas:
        print(f"    - {consulta}")

# Contagem com dicionários
especialidades_procuradas = ["Psicologia", "Psiquiatria", "Psicologia", 
                           "Terapia", "Psicologia", "Psiquiatria"]

contador = {}
for esp in especialidades_procuradas:
    contador[esp] = contador.get(esp, 0) + 1

print(f"\nEspecialidades mais procuradas:")
for esp, qtd in contador.items():
    print(f"  {esp}: {qtd} consultas")