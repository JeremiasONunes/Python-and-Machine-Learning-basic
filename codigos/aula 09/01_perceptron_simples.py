# Aula 09 - Código 1: Perceptron Simples para Classificação Médica
# Implementação básica de um neurônio artificial para classificar risco de pacientes

import numpy as np
import matplotlib.pyplot as plt

print("=== PERCEPTRON SIMPLES - CLASSIFICAÇÃO DE RISCO MÉDICO ===\n")

class PerceptronSimples:
    """Implementação básica de um perceptron para classificação binária"""
    
    def __init__(self, taxa_aprendizado=0.1, max_iteracoes=100):
        self.taxa_aprendizado = taxa_aprendizado
        self.max_iteracoes = max_iteracoes
        self.pesos = None
        self.bias = None
        
    def funcao_ativacao(self, x):
        """Função degrau: retorna 1 se x >= 0, senão 0"""
        return 1 if x >= 0 else 0
    
    def treinar(self, X, y):
        """Treina o perceptron com os dados fornecidos"""
        # Inicializar pesos e bias
        n_features = X.shape[1]
        self.pesos = np.random.uniform(-1, 1, n_features)
        self.bias = np.random.uniform(-1, 1)
        
        print("Iniciando treinamento...")
        
        for iteracao in range(self.max_iteracoes):
            erros = 0
            
            for i in range(len(X)):
                # Calcular saída
                entrada_linear = np.dot(X[i], self.pesos) + self.bias
                predicao = self.funcao_ativacao(entrada_linear)
                
                # Calcular erro
                erro = y[i] - predicao
                
                if erro != 0:
                    erros += 1
                    # Atualizar pesos e bias
                    self.pesos += self.taxa_aprendizado * erro * X[i]
                    self.bias += self.taxa_aprendizado * erro
            
            if iteracao % 20 == 0:
                print(f"Iteração {iteracao}: {erros} erros")
            
            # Se não há erros, parar o treinamento
            if erros == 0:
                print(f"Convergência alcançada na iteração {iteracao}")
                break
    
    def predizer(self, X):
        """Faz predições para novos dados"""
        predicoes = []
        for x in X:
            entrada_linear = np.dot(x, self.pesos) + self.bias
            predicao = self.funcao_ativacao(entrada_linear)
            predicoes.append(predicao)
        return np.array(predicoes)

# Criar dados médicos simples
print("Criando dados de pacientes...")
np.random.seed(42)

# Features: [idade_normalizada, pressao_normalizada]
X = np.array([
    [0.3, 0.4],  # Jovem, pressão normal
    [0.8, 0.9],  # Idoso, pressão alta
    [0.2, 0.3],  # Jovem, pressão baixa
    [0.9, 0.8],  # Idoso, pressão alta
    [0.4, 0.6],  # Meia-idade, pressão média
    [0.7, 0.7],  # Idoso, pressão alta
    [0.1, 0.2],  # Muito jovem, pressão baixa
    [0.6, 0.8]   # Idoso, pressão alta
])

# Target: 0 = Baixo risco, 1 = Alto risco
y = np.array([0, 1, 0, 1, 0, 1, 0, 1])

print(f"Dados de treinamento: {len(X)} pacientes")
print("Features: [idade_normalizada, pressao_normalizada]")
print("Target: 0=Baixo risco, 1=Alto risco\n")

# Treinar o perceptron
perceptron = PerceptronSimples(taxa_aprendizado=0.1, max_iteracoes=100)
perceptron.treinar(X, y)

# Testar o modelo
print(f"\nPesos finais: {perceptron.pesos}")
print(f"Bias final: {perceptron.bias:.3f}")

# Fazer predições
predicoes = perceptron.predizer(X)
acuracia = np.mean(predicoes == y)
print(f"\nAcurácia no conjunto de treinamento: {acuracia:.2f}")

# Testar com novos pacientes
print("\n=== TESTANDO COM NOVOS PACIENTES ===")
novos_pacientes = np.array([
    [0.5, 0.5],  # Meia-idade, pressão média
    [0.9, 0.9],  # Idoso, pressão muito alta
    [0.2, 0.1]   # Jovem, pressão muito baixa
])

novas_predicoes = perceptron.predizer(novos_pacientes)

for i, (paciente, pred) in enumerate(zip(novos_pacientes, novas_predicoes)):
    risco = "Alto risco" if pred == 1 else "Baixo risco"
    print(f"Paciente {i+1} (idade: {paciente[0]:.1f}, pressão: {paciente[1]:.1f}): {risco}")

# Visualizar resultados
plt.figure(figsize=(10, 6))

# Plotar dados de treinamento
cores = ['blue' if label == 0 else 'red' for label in y]
plt.scatter(X[:, 0], X[:, 1], c=cores, s=100, alpha=0.7, edgecolors='black')

# Plotar novos pacientes
cores_novas = ['blue' if pred == 0 else 'red' for pred in novas_predicoes]
plt.scatter(novos_pacientes[:, 0], novos_pacientes[:, 1], 
           c=cores_novas, s=150, marker='^', edgecolors='black', label='Novos pacientes')

plt.xlabel('Idade (normalizada)')
plt.ylabel('Pressão Arterial (normalizada)')
plt.title('Perceptron - Classificação de Risco Médico')
plt.legend(['Baixo risco (treino)', 'Alto risco (treino)', 'Novos pacientes'])
plt.grid(True, alpha=0.3)
plt.show()

print("\n✅ Perceptron treinado com sucesso!")
print("O modelo aprendeu a separar pacientes de alto e baixo risco baseado na idade e pressão arterial.")