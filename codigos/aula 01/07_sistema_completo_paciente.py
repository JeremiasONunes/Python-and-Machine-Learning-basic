# Aula 01 - Atividade Prática 4: Sistema Completo de Coleta de Dados
# Sistema interativo completo para coleta e relatório de paciente

from datetime import datetime

def exibir_cabecalho():
    print("="*70)
    print("           SISTEMA LUNYSSE - CADASTRO DE PACIENTE")
    print("="*70)

def coletar_dados_paciente():
    print("\n📋 DADOS PESSOAIS:")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    print("\n📊 DADOS CLÍNICOS:")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    ano_nascimento = int(input("Ano de nascimento: "))
    
    print("\n🏥 DADOS DO TRATAMENTO:")
    tipo_tratamento = input("Tipo de tratamento: ")
    ano_inicio = int(input("Ano de início do tratamento: "))
    
    return {
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'email': email,
        'peso': peso,
        'altura': altura,
        'ano_nascimento': ano_nascimento,
        'tipo_tratamento': tipo_tratamento,
        'ano_inicio': ano_inicio
    }

def calcular_estatisticas(dados):
    ano_atual = datetime.now().year
    idade = ano_atual - dados['ano_nascimento']
    imc = dados['peso'] / (dados['altura'] ** 2)
    tempo_tratamento = ano_atual - dados['ano_inicio']
    
    return idade, imc, tempo_tratamento

def gerar_relatorio(dados, idade, imc, tempo_tratamento):
    print("\n" + "="*70)
    print("                    RELATÓRIO DO PACIENTE")
    print("="*70)
    
    print(f"📝 Nome: {dados['nome']}")
    print(f"🆔 CPF: {dados['cpf']}")
    print(f"📞 Telefone: {dados['telefone']}")
    print(f"📧 Email: {dados['email']}")
    
    print(f"\n📊 ESTATÍSTICAS:")
    print(f"   Idade: {idade} anos")
    print(f"   IMC: {imc:.2f}")
    print(f"   Peso: {dados['peso']} kg")
    print(f"   Altura: {dados['altura']} m")
    
    print(f"\n🏥 TRATAMENTO:")
    print(f"   Tipo: {dados['tipo_tratamento']}")
    print(f"   Tempo de tratamento: {tempo_tratamento} anos")
    
    print("="*70)
    print("✅ Paciente cadastrado com sucesso no Sistema Lunysse!")

# Programa principal
if __name__ == "__main__":
    exibir_cabecalho()
    dados = coletar_dados_paciente()
    idade, imc, tempo_tratamento = calcular_estatisticas(dados)
    gerar_relatorio(dados, idade, imc, tempo_tratamento)