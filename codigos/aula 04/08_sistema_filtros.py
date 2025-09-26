# Aula 04 - Atividade Prática 4: Sistema de Filtros e Transformações
# Sistema usando lambda para processar dados de pacientes e agendamentos

print("=== SISTEMA DE FILTROS FUNCIONAIS ===\n")

# Dados de teste
pacientes = [
    {"id": 1, "nome": "Ana Silva", "idade": 25, "cidade": "São Paulo"},
    {"id": 2, "nome": "João Santos", "idade": 34, "cidade": "Rio de Janeiro"},
    {"id": 3, "nome": "Maria Costa", "idade": 28, "cidade": "São Paulo"},
    {"id": 4, "nome": "Pedro Lima", "idade": 45, "cidade": "Belo Horizonte"},
    {"id": 5, "nome": "Carlos Souza", "idade": 67, "cidade": "São Paulo"}
]

agendamentos = [
    {"id": 1, "paciente_id": 1, "tipo": "Psicologia", "valor": 150, "status": "Concluída"},
    {"id": 2, "paciente_id": 2, "tipo": "Psiquiatria", "valor": 200, "status": "Agendada"},
    {"id": 3, "paciente_id": 3, "tipo": "Terapia", "valor": 120, "status": "Concluída"},
    {"id": 4, "paciente_id": 4, "tipo": "Psicologia", "valor": 150, "status": "Cancelada"},
    {"id": 5, "paciente_id": 5, "tipo": "Psiquiatria", "valor": 200, "status": "Concluída"}
]

class FiltrosPacientes:
    @staticmethod
    def por_faixa_etaria(pacientes, idade_min, idade_max):
        """Filtra pacientes por faixa etária"""
        return list(filter(lambda p: idade_min <= p["idade"] <= idade_max, pacientes))
    
    @staticmethod
    def por_cidade(pacientes, cidade):
        """Filtra pacientes por cidade"""
        return list(filter(lambda p: p["cidade"] == cidade, pacientes))
    
    @staticmethod
    def ordenar_por_idade(pacientes, reverso=False):
        """Ordena pacientes por idade"""
        return sorted(pacientes, key=lambda p: p["idade"], reverse=reverso)
    
    @staticmethod
    def extrair_nomes(pacientes):
        """Extrai apenas os nomes dos pacientes"""
        return list(map(lambda p: p["nome"], pacientes))

class FiltrosAgendamentos:
    @staticmethod
    def por_status(agendamentos, status):
        """Filtra agendamentos por status"""
        return list(filter(lambda a: a["status"] == status, agendamentos))
    
    @staticmethod
    def por_tipo(agendamentos, tipo):
        """Filtra agendamentos por tipo"""
        return list(filter(lambda a: a["tipo"] == tipo, agendamentos))
    
    @staticmethod
    def calcular_receita(agendamentos):
        """Calcula receita total dos agendamentos"""
        valores = map(lambda a: a["valor"], agendamentos)
        return sum(valores)
    
    @staticmethod
    def aplicar_desconto(agendamentos, percentual):
        """Aplica desconto aos valores"""
        return list(map(lambda a: {**a, "valor_desconto": a["valor"] * (1 - percentual/100)}, agendamentos))

class ProcessadorDados:
    @staticmethod
    def estatisticas_idades(pacientes):
        """Calcula estatísticas das idades"""
        idades = list(map(lambda p: p["idade"], pacientes))
        
        return {
            "media": sum(idades) / len(idades),
            "minima": min(idades),
            "maxima": max(idades),
            "total": len(idades)
        }
    
    @staticmethod
    def agrupar_por_cidade(pacientes):
        """Agrupa pacientes por cidade"""
        cidades = set(map(lambda p: p["cidade"], pacientes))
        
        resultado = {}
        for cidade in cidades:
            resultado[cidade] = list(filter(lambda p: p["cidade"] == cidade, pacientes))
        
        return resultado
    
    @staticmethod
    def top_tipos_consulta(agendamentos, top_n=3):
        """Encontra os tipos de consulta mais frequentes"""
        tipos = list(map(lambda a: a["tipo"], agendamentos))
        
        # Conta ocorrências
        contador = {}
        for tipo in tipos:
            contador[tipo] = contador.get(tipo, 0) + 1
        
        # Ordena por frequência
        ordenados = sorted(contador.items(), key=lambda x: x[1], reverse=True)
        
        return ordenados[:top_n]

# Testes do sistema
if __name__ == "__main__":
    print("=== TESTANDO FILTROS ===")
    
    # Filtros de pacientes
    jovens = FiltrosPacientes.por_faixa_etaria(pacientes, 18, 30)
    print(f"Pacientes jovens (18-30): {len(jovens)}")
    
    sp_pacientes = FiltrosPacientes.por_cidade(pacientes, "São Paulo")
    print(f"Pacientes de SP: {len(sp_pacientes)}")
    
    por_idade = FiltrosPacientes.ordenar_por_idade(pacientes)
    print(f"Mais novo: {por_idade[0]['nome']} ({por_idade[0]['idade']} anos)")
    
    # Filtros de agendamentos
    concluidas = FiltrosAgendamentos.por_status(agendamentos, "Concluída")
    print(f"Consultas concluídas: {len(concluidas)}")
    
    receita_total = FiltrosAgendamentos.calcular_receita(concluidas)
    print(f"Receita das concluídas: R$ {receita_total}")
    
    # Processamento de dados
    stats = ProcessadorDados.estatisticas_idades(pacientes)
    print(f"Idade média: {stats['media']:.1f} anos")
    
    por_cidade = ProcessadorDados.agrupar_por_cidade(pacientes)
    print(f"Cidades atendidas: {list(por_cidade.keys())}")
    
    top_tipos = ProcessadorDados.top_tipos_consulta(agendamentos)
    print(f"Tipo mais comum: {top_tipos[0][0]} ({top_tipos[0][1]} consultas)")
    
    # Transformações
    com_desconto = FiltrosAgendamentos.aplicar_desconto(agendamentos, 10)
    print(f"Primeira consulta com desconto: R$ {com_desconto[0]['valor']} → R$ {com_desconto[0]['valor_desconto']}")
    
    print("\n✅ Sistema de filtros funcionando!")