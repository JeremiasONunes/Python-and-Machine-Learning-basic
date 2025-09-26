# Aula 03 - Tópico 3: Tuplas e Conjuntos
# Demonstração de tuplas (imutáveis) e conjuntos (operações matemáticas)

print("=== TUPLAS E CONJUNTOS ===\n")

# TUPLAS - Dados imutáveis
print("=== TUPLAS ===")

# Criação de tuplas
coordenadas = (10.5, -23.2)
paciente_info = ("Ana Silva", 25, "Psicologia")
horarios_fixos = (8, 9, 10, 14, 15, 16, 17)

print(f"Coordenadas: {coordenadas}")
print(f"Info paciente: {paciente_info}")
print(f"Horários: {horarios_fixos}")

# Acesso por índice
print(f"\nLatitude: {coordenadas[0]}")
print(f"Nome: {paciente_info[0]}")
print(f"Primeiro horário: {horarios_fixos[0]}")

# Desempacotamento
nome, idade, tratamento = paciente_info
print(f"\nDesempacotado - Nome: {nome}, Idade: {idade}, Tratamento: {tratamento}")

# Métodos de tuplas
numeros = (1, 2, 3, 2, 4, 2, 5)
print(f"\nTupla: {numeros}")
print(f"Quantidade de 2s: {numeros.count(2)}")
print(f"Posição do primeiro 3: {numeros.index(3)}")
print(f"Tamanho: {len(numeros)}")

# Tuplas aninhadas - configurações do sistema
config_clinica = (
    ("nome", "Clínica Lunysse"),
    ("horario_funcionamento", (8, 18)),
    ("dias_semana", ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")),
    ("especialidades", ("Psicologia", "Psiquiatria", "Terapia"))
)

print(f"\nConfigurações da clínica:")
for chave, valor in config_clinica:
    print(f"  {chave}: {valor}")

# CONJUNTOS (SETS) - Operações matemáticas
print(f"\n=== CONJUNTOS ===")

# Criação de conjuntos
especialidades_clinica = {"Psicologia", "Psiquiatria", "Terapia", "Neurologia"}
especialidades_procuradas = {"Psicologia", "Cardiologia", "Terapia", "Dermatologia"}

print(f"Especialidades da clínica: {especialidades_clinica}")
print(f"Especialidades procuradas: {especialidades_procuradas}")

# Operações de conjuntos
print(f"\n=== OPERAÇÕES DE CONJUNTOS ===")

# União (todas as especialidades)
todas_especialidades = especialidades_clinica | especialidades_procuradas
print(f"União (todas): {todas_especialidades}")

# Interseção (especialidades em comum)
em_comum = especialidades_clinica & especialidades_procuradas
print(f"Interseção (em comum): {em_comum}")

# Diferença (só na clínica)
so_na_clinica = especialidades_clinica - especialidades_procuradas
print(f"Diferença (só na clínica): {so_na_clinica}")

# Diferença simétrica (não estão em ambos)
diferentes = especialidades_clinica ^ especialidades_procuradas
print(f"Diferença simétrica: {diferentes}")

# Métodos de conjuntos
pacientes_segunda = {"Ana", "João", "Maria"}
pacientes_terca = {"João", "Pedro", "Carlos"}

print(f"\nPacientes segunda: {pacientes_segunda}")
print(f"Pacientes terça: {pacientes_terca}")

# Adicionar e remover
pacientes_segunda.add("Lucas")
print(f"Após adicionar Lucas: {pacientes_segunda}")

pacientes_segunda.discard("Ana")  # Remove se existir
print(f"Após remover Ana: {pacientes_segunda}")

# Verificações
print(f"\nJoão está na segunda? {'João' in pacientes_segunda}")
print(f"Ana está na terça? {'Ana' in pacientes_terca}")

# Subconjuntos e superconjuntos
grupo_pequeno = {"João", "Maria"}
grupo_grande = {"João", "Maria", "Pedro", "Ana"}

print(f"\n{grupo_pequeno} é subconjunto de {grupo_grande}? {grupo_pequeno.issubset(grupo_grande)}")
print(f"{grupo_grande} é superconjunto de {grupo_pequeno}? {grupo_grande.issuperset(grupo_pequeno)}")

# Conjuntos disjuntos
grupo_manha = {"Ana", "João"}
grupo_tarde = {"Pedro", "Carlos"}

print(f"Grupos manhã e tarde são disjuntos? {grupo_manha.isdisjoint(grupo_tarde)}")

# Aplicação prática - análise de disponibilidade
print(f"\n=== ANÁLISE DE DISPONIBILIDADE ===")

medicos_disponiveis = {"Dr. Silva", "Dra. Costa", "Dr. Santos", "Dra. Lima"}
medicos_ferias = {"Dr. Santos", "Dra. Oliveira"}
medicos_plantao = {"Dr. Silva", "Dr. Ferreira"}

# Médicos realmente disponíveis
disponiveis_real = medicos_disponiveis - medicos_ferias
print(f"Médicos disponíveis (sem férias): {disponiveis_real}")

# Médicos em plantão que estão disponíveis
plantao_disponivel = medicos_plantao & medicos_disponiveis
print(f"Médicos em plantão disponíveis: {plantao_disponivel}")

# Conversão entre tipos
lista_especialidades = list(especialidades_clinica)
tupla_especialidades = tuple(especialidades_clinica)

print(f"\nConjunto → Lista: {lista_especialidades}")
print(f"Conjunto → Tupla: {tupla_especialidades}")

# Removendo duplicatas com set
consultas_mes = ["Psicologia", "Terapia", "Psicologia", "Psiquiatria", "Terapia", "Psicologia"]
tipos_unicos = list(set(consultas_mes))

print(f"\nConsultas do mês: {consultas_mes}")
print(f"Tipos únicos: {tipos_unicos}")
print(f"Quantidade de tipos: {len(tipos_unicos)}")