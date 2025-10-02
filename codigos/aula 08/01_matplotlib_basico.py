# Aula 08 - Tópico 1: Fundamentos do Matplotlib
# Demonstração básica de visualização de dados

import matplotlib.pyplot as plt
import numpy as np

print("=== MATPLOTLIB BÁSICO ===\n")

# Configurar estilo
plt.style.use('default')

# 1. Gráfico de linha simples
print("1. Criando gráfico de linha...")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sen(x)', color='blue', linewidth=2)
plt.title('Gráfico de Linha - Função Seno')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 2. Gráfico de barras
print("2. Criando gráfico de barras...")
especialidades = ['Psicologia', 'Psiquiatria', 'Cardiologia', 'Neurologia']
pacientes = [45, 32, 28, 15]

plt.figure(figsize=(8, 6))
bars = plt.bar(especialidades, pacientes, color=['skyblue', 'lightgreen', 'coral', 'gold'])
plt.title('Distribuição de Pacientes por Especialidade')
plt.xlabel('Especialidade')
plt.ylabel('Número de Pacientes')

# Adicionar valores nas barras
for bar, valor in zip(bars, pacientes):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             str(valor), ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Gráfico de dispersão
print("3. Criando gráfico de dispersão...")
np.random.seed(42)
idades = np.random.randint(20, 80, 50)
pressao = 90 + 0.8 * idades + np.random.normal(0, 10, 50)

plt.figure(figsize=(8, 6))
plt.scatter(idades, pressao, alpha=0.6, color='red', s=50)
plt.title('Relação entre Idade e Pressão Arterial')
plt.xlabel('Idade (anos)')
plt.ylabel('Pressão Sistólica (mmHg)')
plt.grid(True, alpha=0.3)

# Linha de tendência
z = np.polyfit(idades, pressao, 1)
p = np.poly1d(z)
plt.plot(idades, p(idades), "r--", alpha=0.8, label='Tendência')
plt.legend()
plt.show()

# 4. Histograma
print("4. Criando histograma...")
np.random.seed(42)
idades_hist = np.random.normal(45, 15, 200)

plt.figure(figsize=(8, 6))
plt.hist(idades_hist, bins=20, color='lightblue', alpha=0.7, edgecolor='black')
plt.title('Distribuição de Idades dos Pacientes')
plt.xlabel('Idade (anos)')
plt.ylabel('Frequência')
plt.axvline(np.mean(idades_hist), color='red', linestyle='--', 
            label=f'Média: {np.mean(idades_hist):.1f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 5. Subplots - múltiplos gráficos
print("5. Criando subplots...")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Subplot 1: Linha
x = np.linspace(0, 5, 50)
ax1.plot(x, np.exp(-x), 'b-')
ax1.set_title('Função Exponencial')
ax1.grid(True, alpha=0.3)

# Subplot 2: Barras
categorias = ['A', 'B', 'C', 'D']
valores = [23, 45, 56, 78]
ax2.bar(categorias, valores, color='green', alpha=0.7)
ax2.set_title('Gráfico de Barras')

# Subplot 3: Dispersão
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
ax3.scatter(x_scatter, y_scatter, alpha=0.6)
ax3.set_title('Dispersão Aleatória')

# Subplot 4: Histograma
data_hist = np.random.normal(0, 1, 1000)
ax4.hist(data_hist, bins=30, alpha=0.7, color='orange')
ax4.set_title('Distribuição Normal')

plt.tight_layout()
plt.show()

# 6. Personalização avançada
print("6. Gráfico personalizado...")
plt.figure(figsize=(10, 6))

# Dados simulados de sinais vitais
tempo = np.arange(0, 24, 0.5)  # 24 horas
batimentos = 70 + 10 * np.sin(tempo/4) + np.random.normal(0, 3, len(tempo))

plt.plot(tempo, batimentos, 'o-', color='red', markersize=4, linewidth=1.5)
plt.fill_between(tempo, 60, 100, alpha=0.2, color='green', label='Faixa Normal')
plt.title('Monitoramento de Batimentos Cardíacos - 24h', fontsize=14, fontweight='bold')
plt.xlabel('Tempo (horas)', fontsize=12)
plt.ylabel('Batimentos por Minuto', fontsize=12)
plt.ylim(50, 110)
plt.grid(True, alpha=0.3)
plt.legend()

# Adicionar anotações
plt.annotate('Pico matinal', xy=(8, max(batimentos)), xytext=(10, 95),
            arrowprops=dict(arrowstyle='->', color='blue'))

plt.tight_layout()
plt.show()

print("\n✅ Demonstração do Matplotlib concluída!")
print("Gráficos criados: linha, barras, dispersão, histograma, subplots e personalizado")