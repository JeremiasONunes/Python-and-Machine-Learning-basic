# Aula 09 - Código 3: Sistema Completo de IA Médica
# Sistema integrado com rede neural para análise de risco de pacientes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import joblib
import os

print("=== SISTEMA COMPLETO DE IA MÉDICA ===\n")

class SistemaIAMedica:
    """Sistema completo de IA para análise de risco médico"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = ['idade', 'pressao_sistolica', 'glicose', 'imc', 'colesterol']
        self.risk_categories = ['Baixo Risco', 'Médio Risco', 'Alto Risco']
        self.is_trained = False
    
    def criar_dataset(self, n_pacientes=1500):
        """Cria dataset médico sintético"""
        print(f"Criando dataset com {n_pacientes} pacientes...")
        
        np.random.seed(42)
        
        # Gerar dados realistas
        dados = {
            'idade': np.random.randint(18, 85, n_pacientes),
            'pressao_sistolica': np.random.normal(130, 25, n_pacientes),
            'glicose': np.random.normal(100, 30, n_pacientes),
            'imc': np.random.normal(26, 6, n_pacientes),
            'colesterol': np.random.normal(200, 45, n_pacientes)
        }
        
        df = pd.DataFrame(dados)
        
        # Garantir valores realistas
        df['pressao_sistolica'] = np.clip(df['pressao_sistolica'], 80, 200)
        df['glicose'] = np.clip(df['glicose'], 60, 300)
        df['imc'] = np.clip(df['imc'], 15, 50)
        df['colesterol'] = np.clip(df['colesterol'], 120, 350)
        
        # Calcular risco baseado em diretrizes médicas
        def calcular_risco_medico(row):
            score = 0
            
            # Idade
            if row['idade'] > 65: score += 3
            elif row['idade'] > 50: score += 2
            elif row['idade'] > 35: score += 1
            
            # Pressão arterial
            if row['pressao_sistolica'] > 160: score += 3
            elif row['pressao_sistolica'] > 140: score += 2
            elif row['pressao_sistolica'] > 130: score += 1
            
            # Glicose
            if row['glicose'] > 140: score += 3
            elif row['glicose'] > 126: score += 2
            elif row['glicose'] > 100: score += 1
            
            # IMC
            if row['imc'] > 35: score += 2
            elif row['imc'] > 30: score += 1
            
            # Colesterol
            if row['colesterol'] > 260: score += 2
            elif row['colesterol'] > 240: score += 1
            
            # Classificar risco
            if score >= 7: return 2  # Alto risco
            elif score >= 4: return 1  # Médio risco
            else: return 0  # Baixo risco
        
        df['categoria_risco'] = df.apply(calcular_risco_medico, axis=1)
        
        print(f"Dataset criado com sucesso!")
        print(f"Distribuição de risco:")
        for i, categoria in enumerate(self.risk_categories):
            count = sum(df['categoria_risco'] == i)
            print(f"  {categoria}: {count} pacientes ({count/len(df)*100:.1f}%)")
        
        return df
    
    def construir_modelo(self):
        """Constrói arquitetura da rede neural"""
        print("\nConstruindo rede neural...")
        
        model = keras.Sequential([
            # Camada de entrada com mais neurônios
            layers.Dense(32, activation='relu', input_shape=(5,), name='entrada'),
            layers.Dropout(0.3),  # Regularização
            
            # Primeira camada oculta
            layers.Dense(16, activation='relu', name='oculta1'),
            layers.Dropout(0.2),
            
            # Segunda camada oculta
            layers.Dense(8, activation='relu', name='oculta2'),
            
            # Camada de saída
            layers.Dense(3, activation='softmax', name='saida')
        ])
        
        # Compilar com otimizador Adam
        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        self.model = model
        print("Modelo construído com sucesso!")
        return model
    
    def treinar(self, df):
        """Treina o modelo com os dados"""
        print("\n=== INICIANDO TREINAMENTO ===")
        
        # Preparar dados
        X = df[self.feature_names].values
        y = df['categoria_risco'].values
        
        # Dividir dados
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Normalizar
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Callbacks para otimização
        callbacks = [
            keras.callbacks.EarlyStopping(
                monitor='val_accuracy',
                patience=15,
                restore_best_weights=True
            ),
            keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=10
            )
        ]
        
        # Treinar
        history = self.model.fit(
            X_train_scaled, y_train,
            epochs=100,
            batch_size=32,
            validation_split=0.2,
            callbacks=callbacks,
            verbose=1
        )
        
        # Avaliar
        test_loss, test_accuracy = self.model.evaluate(X_test_scaled, y_test, verbose=0)
        print(f"\nAcurácia final no teste: {test_accuracy:.3f}")
        
        # Relatório detalhado
        y_pred = np.argmax(self.model.predict(X_test_scaled), axis=1)
        print("\nRelatório de Classificação:")
        print(classification_report(y_test, y_pred, target_names=self.risk_categories))
        
        self.is_trained = True
        return history, X_test_scaled, y_test
    
    def analisar_paciente(self, dados_paciente):
        """Analisa um paciente individual"""
        if not self.is_trained:
            print("❌ Modelo não foi treinado ainda!")
            return None
        
        # Preparar dados
        if isinstance(dados_paciente, dict):
            dados_array = np.array([[dados_paciente[feature] for feature in self.feature_names]])
        else:
            dados_array = np.array([dados_paciente])
        
        # Normalizar
        dados_scaled = self.scaler.transform(dados_array)
        
        # Predição
        probabilidades = self.model.predict(dados_scaled)[0]
        categoria_pred = np.argmax(probabilidades)
        
        return {
            'categoria': self.risk_categories[categoria_pred],
            'probabilidades': {
                self.risk_categories[i]: prob 
                for i, prob in enumerate(probabilidades)
            },
            'confianca': probabilidades[categoria_pred]
        }
    
    def salvar_modelo(self, caminho='modelo_ia_medica'):
        """Salva o modelo treinado"""
        if not self.is_trained:
            print("❌ Modelo não foi treinado ainda!")
            return
        
        # Criar diretório se não existir
        os.makedirs(caminho, exist_ok=True)
        
        # Salvar modelo Keras
        self.model.save(os.path.join(caminho, 'modelo_neural.h5'))
        
        # Salvar scaler
        joblib.dump(self.scaler, os.path.join(caminho, 'scaler.pkl'))
        
        print(f"✅ Modelo salvo em: {caminho}")

# Demonstração do sistema
print("Inicializando Sistema de IA Médica...")
sistema = SistemaIAMedica()

# Criar dataset
df = sistema.criar_dataset(1500)

# Construir e treinar modelo
modelo = sistema.construir_modelo()
history, X_test, y_test = sistema.treinar(df)

# Testar com pacientes exemplo
print("\n=== ANÁLISE DE PACIENTES EXEMPLO ===")

pacientes_teste = [
    {
        'nome': 'João (Jovem Saudável)',
        'dados': {'idade': 25, 'pressao_sistolica': 115, 'glicose': 85, 'imc': 23, 'colesterol': 180}
    },
    {
        'nome': 'Maria (Risco Moderado)',
        'dados': {'idade': 55, 'pressao_sistolica': 145, 'glicose': 110, 'imc': 28, 'colesterol': 230}
    },
    {
        'nome': 'Carlos (Alto Risco)',
        'dados': {'idade': 70, 'pressao_sistolica': 170, 'glicose': 150, 'imc': 35, 'colesterol': 280}
    }
]

for paciente in pacientes_teste:
    resultado = sistema.analisar_paciente(paciente['dados'])
    
    print(f"\n👤 {paciente['nome']}:")
    print(f"   Categoria: {resultado['categoria']}")
    print(f"   Confiança: {resultado['confianca']:.1%}")
    print(f"   Probabilidades:")
    for categoria, prob in resultado['probabilidades'].items():
        print(f"     {categoria}: {prob:.1%}")

# Salvar modelo
sistema.salvar_modelo()

print("\n✅ Sistema de IA Médica completo e funcional!")
print("O sistema pode agora analisar novos pacientes e fornecer predições de risco em tempo real.")