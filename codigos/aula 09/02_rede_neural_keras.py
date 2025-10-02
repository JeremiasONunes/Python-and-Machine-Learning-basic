# Aula 09 - Código 2: Rede Neural com TensorFlow/Keras
# Primeira rede neural multicamada para classificação médica

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print("=== REDE NEURAL COM TENSORFLOW/KERAS ===\n")

# Verificar versão do TensorFlow
print(f"TensorFlow versão: {tf.__version__}")

# Criar dados médicos mais complexos
print("Criando dataset médico...")
np.random.seed(42)
n_pacientes = 1000

# Gerar dados sintéticos
dados = {
    'idade': np.random.randint(18, 80, n_pacientes),
    'pressao_sistolica': np.random.normal(130, 20, n_pacientes),
    'glicose': np.random.normal(100, 25, n_pacientes),
    'imc': np.random.normal(25, 5, n_pacientes),
    'colesterol': np.random.normal(200, 40, n_pacientes)
}

df = pd.DataFrame(dados)

# Criar target baseado em regras médicas
def calcular_risco(row):
    score = 0
    if row['idade'] > 60: score += 2
    if row['pressao_sistolica'] > 140: score += 2
    if row['glicose'] > 126: score += 2
    if row['imc'] > 30: score += 1
    if row['colesterol'] > 240: score += 1
    
    if score >= 5: return 2  # Alto risco
    elif score >= 3: return 1  # Médio risco
    else: return 0  # Baixo risco

df['categoria_risco'] = df.apply(calcular_risco, axis=1)

print(f"Dataset criado: {len(df)} pacientes")
print(f"Distribuição de risco:")
print(df['categoria_risco'].value_counts().sort_index())

# Preparar dados
X = df.drop('categoria_risco', axis=1).values
y = df['categoria_risco'].values

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Normalizar dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nDados de treino: {X_train_scaled.shape}")
print(f"Dados de teste: {X_test_scaled.shape}")

# Construir modelo neural
print("\n=== CONSTRUINDO REDE NEURAL ===")

model = keras.Sequential([
    # Camada de entrada
    layers.Dense(16, activation='relu', input_shape=(5,), name='camada_entrada'),
    
    # Camada oculta
    layers.Dense(8, activation='relu', name='camada_oculta'),
    
    # Camada de saída (3 classes)
    layers.Dense(3, activation='softmax', name='camada_saida')
])

# Compilar modelo
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Mostrar arquitetura
print("Arquitetura da rede neural:")
model.summary()

# Treinar modelo
print("\n=== TREINANDO MODELO ===")

# Callback para parar se não melhorar
early_stopping = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

# Treinar
history = model.fit(
    X_train_scaled, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=1
)

# Avaliar modelo
print("\n=== AVALIAÇÃO DO MODELO ===")

# Predições
y_pred_proba = model.predict(X_test_scaled)
y_pred = np.argmax(y_pred_proba, axis=1)

# Acurácia
test_accuracy = np.mean(y_pred == y_test)
print(f"Acurácia no teste: {test_accuracy:.3f}")

# Matriz de confusão simples
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(f"\nMatriz de Confusão:")
print(cm)

# Testar com novos pacientes
print("\n=== TESTANDO COM NOVOS PACIENTES ===")

novos_pacientes = np.array([
    [25, 120, 90, 22, 180],   # Jovem saudável
    [65, 160, 140, 32, 260],  # Idoso com fatores de risco
    [45, 135, 110, 28, 220]   # Meia-idade com risco moderado
])

# Normalizar novos dados
novos_pacientes_scaled = scaler.transform(novos_pacientes)

# Predições
predicoes_proba = model.predict(novos_pacientes_scaled)
predicoes = np.argmax(predicoes_proba, axis=1)

categorias = ['Baixo Risco', 'Médio Risco', 'Alto Risco']

for i, (paciente, pred, proba) in enumerate(zip(novos_pacientes, predicoes, predicoes_proba)):
    print(f"\nPaciente {i+1}:")
    print(f"  Dados: Idade={paciente[0]}, Pressão={paciente[1]}, Glicose={paciente[2]}")
    print(f"  Predição: {categorias[pred]}")
    print(f"  Probabilidades: {[f'{p:.2f}' for p in proba]}")

# Visualizar histórico de treinamento
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Treino')
plt.plot(history.history['val_loss'], label='Validação')
plt.title('Perda durante o Treinamento')
plt.xlabel('Época')
plt.ylabel('Perda')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Treino')
plt.plot(history.history['val_accuracy'], label='Validação')
plt.title('Acurácia durante o Treinamento')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend()

plt.tight_layout()
plt.show()

print("\n[OK] Perceptron treinado com sucesso!")
print("O modelo aprendeu a classificar pacientes em 3 categorias de risco usando múltiplas variáveis médicas.")