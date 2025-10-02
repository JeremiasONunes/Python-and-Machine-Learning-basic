# Aula 08 - Atividade Prática 4: Sistema Completo de ML com Visualização
# Sistema integrado que treina, avalia e visualiza resultados de modelos ML

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("=== SISTEMA COMPLETO DE MACHINE LEARNING ===\n")

class SistemaMLCompleto:
    """Sistema completo de ML para análise médica"""
    
    def __init__(self):
        self.modelos = {}
        self.scaler = StandardScaler()
        self.melhor_modelo = None
        self.X_test = None
        self.y_test = None
        
    def criar_dataset_completo(self):
        """Cria dataset médico completo"""
        
        np.random.seed(42)
        n = 500
        
        dados = {
            'idade': np.random.randint(20, 80, n),
            'sexo': np.random.choice([0, 1], n),
            'pressao_sistolica': np.random.normal(130, 25, n),
            'glicose': np.random.normal(105, 30, n),
            'imc': np.random.normal(26, 4, n),
            'colesterol': np.random.normal(200, 50, n),
            'fumante': np.random.choice([0, 1], n, p=[0.7, 0.3]),
            'exercicio_semanal': np.random.randint(0, 8, n),
            'historico_familiar': np.random.choice([0, 1], n, p=[0.6, 0.4])
        }
        
        df = pd.DataFrame(dados)
        
        # Criar target realista
        risco = []
        for _, row in df.iterrows():
            score = 0
            
            # Fatores de risco
            if row['idade'] > 60: score += 2
            elif row['idade'] > 45: score += 1
            
            if row['pressao_sistolica'] > 140: score += 2
            elif row['pressao_sistolica'] > 130: score += 1
            
            if row['glicose'] > 126: score += 2
            elif row['glicose'] > 100: score += 1
            
            if row['imc'] > 30: score += 1
            if row['fumante'] == 1: score += 2
            if row['exercicio_semanal'] < 2: score += 1
            if row['historico_familiar'] == 1: score += 1
            
            # Classificar
            risco.append(1 if score >= 4 else 0)
        
        df['risco_alto'] = risco
        return df
    
    def preparar_dados(self, df):
        """Prepara dados para ML"""
        
        print("=== PREPARAÇÃO DOS DADOS ===")
        
        X = df.drop('risco_alto', axis=1)
        y = df['risco_alto']
        
        print(f"Features: {X.columns.tolist()}")
        print(f"Target: risco_alto (0=Baixo, 1=Alto)")
        print(f"Distribuição: Baixo={sum(y==0)}, Alto={sum(y==1)}")
        
        return X, y
    
    def treinar_multiplos_modelos(self, X, y):
        """Treina múltiplos modelos e compara performance"""
        
        print(f"\n=== TREINAMENTO DE MÚLTIPLOS MODELOS ===")
        
        # Dividir dados
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Normalizar
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Salvar dados de teste
        self.X_test = X_test_scaled
        self.y_test = y_test
        
        # Definir modelos
        modelos_config = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'Regressão Logística': LogisticRegression(random_state=42, max_iter=1000),
            'Árvore de Decisão': DecisionTreeClassifier(random_state=42, max_depth=10)
        }
        
        # Treinar e avaliar cada modelo
        resultados = {}
        
        for nome, modelo in modelos_config.items():
            print(f"\nTreinando {nome}...")
            
            # Treinar
            if nome == 'Random Forest' or nome == 'Árvore de Decisão':
                modelo.fit(X_train, y_train)  # Não precisa de normalização
                y_pred = modelo.predict(X_test)
            else:
                modelo.fit(X_train_scaled, y_train)  # Precisa de normalização
                y_pred = modelo.predict(X_test_scaled)
            
            # Avaliar
            accuracy = accuracy_score(y_test, y_pred)
            
            # Cross-validation
            if nome == 'Random Forest' or nome == 'Árvore de Decisão':
                cv_scores = cross_val_score(modelo, X_train, y_train, cv=5)
            else:
                cv_scores = cross_val_score(modelo, X_train_scaled, y_train, cv=5)
            
            # Salvar resultados
            resultados[nome] = {
                'modelo': modelo,
                'accuracy': accuracy,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'y_pred': y_pred
            }
            
            self.modelos[nome] = modelo
            
            print(f"  Acurácia: {accuracy:.3f}")
            print(f"  CV Score: {cv_scores.mean():.3f} (±{cv_scores.std():.3f})")
        
        # Encontrar melhor modelo
        melhor_nome = max(resultados.keys(), key=lambda k: resultados[k]['cv_mean'])
        self.melhor_modelo = melhor_nome
        
        print(f"\n🏆 Melhor modelo: {melhor_nome}")
        
        return resultados
    
    def visualizar_comparacao_modelos(self, resultados):
        """Visualiza comparação entre modelos"""
        
        print(f"\n=== VISUALIZAÇÃO DA COMPARAÇÃO ===")
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Comparação de Modelos de Machine Learning', fontsize=16, fontweight='bold')
        
        # 1. Acurácia dos modelos
        nomes = list(resultados.keys())
        accuracies = [resultados[nome]['accuracy'] for nome in nomes]
        cv_means = [resultados[nome]['cv_mean'] for nome in nomes]
        
        x_pos = np.arange(len(nomes))
        width = 0.35
        
        ax1.bar(x_pos - width/2, accuracies, width, label='Teste', alpha=0.8, color='skyblue')
        ax1.bar(x_pos + width/2, cv_means, width, label='Cross-Validation', alpha=0.8, color='lightcoral')
        
        ax1.set_title('Acurácia dos Modelos')
        ax1.set_xlabel('Modelos')
        ax1.set_ylabel('Acurácia')
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels(nomes, rotation=45)
        ax1.legend()
        ax1.set_ylim(0, 1)
        
        # Adicionar valores nas barras
        for i, (acc, cv) in enumerate(zip(accuracies, cv_means)):
            ax1.text(i - width/2, acc + 0.01, f'{acc:.3f}', ha='center', va='bottom')
            ax1.text(i + width/2, cv + 0.01, f'{cv:.3f}', ha='center', va='bottom')
        
        # 2. Matriz de confusão do melhor modelo
        melhor_pred = resultados[self.melhor_modelo]['y_pred']
        cm = confusion_matrix(self.y_test, melhor_pred)
        
        im = ax2.imshow(cm, interpolation='nearest', cmap='Blues')
        ax2.set_title(f'Matriz de Confusão - {self.melhor_modelo}')
        ax2.set_xlabel('Predito')
        ax2.set_ylabel('Real')
        
        # Adicionar valores
        for i in range(2):
            for j in range(2):
                ax2.text(j, i, str(cm[i, j]), ha='center', va='center',
                        color='white' if cm[i, j] > cm.max()/2 else 'black', fontweight='bold')
        
        ax2.set_xticks([0, 1])
        ax2.set_yticks([0, 1])
        ax2.set_xticklabels(['Baixo Risco', 'Alto Risco'])
        ax2.set_yticklabels(['Baixo Risco', 'Alto Risco'])
        
        # 3. Distribuição de predições
        real_counts = np.bincount(self.y_test)
        pred_counts = np.bincount(melhor_pred)
        
        classes = ['Baixo Risco', 'Alto Risco']
        x_pos = np.arange(len(classes))
        
        ax3.bar(x_pos - width/2, real_counts, width, label='Real', alpha=0.8)
        ax3.bar(x_pos + width/2, pred_counts, width, label='Predito', alpha=0.8)
        
        ax3.set_title('Distribuição: Real vs Predito')
        ax3.set_xlabel('Classes')
        ax3.set_ylabel('Frequência')
        ax3.set_xticks(x_pos)
        ax3.set_xticklabels(classes)
        ax3.legend()
        
        # 4. Importância das features (Random Forest)
        if 'Random Forest' in self.modelos:
            rf_model = self.modelos['Random Forest']
            importances = rf_model.feature_importances_
            
            # Nomes das features
            feature_names = ['Idade', 'Sexo', 'Pressão', 'Glicose', 'IMC', 
                           'Colesterol', 'Fumante', 'Exercício', 'Hist. Familiar']
            
            # Ordenar por importância
            indices = np.argsort(importances)[::-1]
            
            ax4.bar(range(len(importances)), importances[indices], alpha=0.8, color='green')
            ax4.set_title('Importância das Features (Random Forest)')
            ax4.set_xlabel('Features')
            ax4.set_ylabel('Importância')
            ax4.set_xticks(range(len(importances)))
            ax4.set_xticklabels([feature_names[i] for i in indices], rotation=45)
        
        plt.tight_layout()
        plt.show()
    
    def gerar_relatorio_final(self, resultados):
        """Gera relatório final do sistema"""
        
        print(f"\n=== RELATÓRIO FINAL DO SISTEMA ML ===")
        
        print(f"🎯 Objetivo: Classificação de Risco Cardiovascular")
        print(f"📊 Dataset: {len(self.y_test) * 5} pacientes (80% treino, 20% teste)")
        print(f"🔧 Modelos testados: {len(resultados)}")
        
        print(f"\n📈 Performance dos Modelos:")
        for nome, resultado in resultados.items():
            print(f"  {nome}:")
            print(f"    Acurácia: {resultado['accuracy']:.3f}")
            print(f"    CV Score: {resultado['cv_mean']:.3f} (±{resultado['cv_std']:.3f})")
        
        print(f"\n🏆 Melhor Modelo: {self.melhor_modelo}")
        melhor_resultado = resultados[self.melhor_modelo]
        print(f"   Acurácia final: {melhor_resultado['accuracy']:.3f}")
        
        # Relatório detalhado do melhor modelo
        print(f"\n📋 Relatório Detalhado ({self.melhor_modelo}):")
        y_pred_melhor = melhor_resultado['y_pred']
        print(classification_report(self.y_test, y_pred_melhor, 
                                  target_names=['Baixo Risco', 'Alto Risco']))
        
        # Recomendações
        print(f"💡 Recomendações:")
        if melhor_resultado['accuracy'] >= 0.85:
            print("  ✅ Modelo pronto para uso clínico")
        elif melhor_resultado['accuracy'] >= 0.75:
            print("  ⚠️ Modelo necessita validação adicional")
        else:
            print("  ❌ Modelo precisa de melhorias significativas")
        
        print("  📚 Próximos passos:")
        print("    • Validar com dados externos")
        print("    • Implementar monitoramento contínuo")
        print("    • Coletar feedback médico")
        print("    • Considerar ensemble de modelos")

# Executar sistema completo
if __name__ == "__main__":
    
    # Criar sistema
    sistema = SistemaMLCompleto()
    
    # 1. Criar dataset
    print("1. Criando dataset médico...")
    df = sistema.criar_dataset_completo()
    
    # 2. Preparar dados
    print("\n2. Preparando dados...")
    X, y = sistema.preparar_dados(df)
    
    # 3. Treinar modelos
    print("\n3. Treinando múltiplos modelos...")
    resultados = sistema.treinar_multiplos_modelos(X, y)
    
    # 4. Visualizar resultados
    print("\n4. Criando visualizações...")
    sistema.visualizar_comparacao_modelos(resultados)
    
    # 5. Gerar relatório
    print("\n5. Gerando relatório final...")
    sistema.gerar_relatorio_final(resultados)
    
    print(f"\n✅ Sistema completo de ML implementado com sucesso!")
    print(f"🎯 Modelo {sistema.melhor_modelo} selecionado para produção")

print("\n✅ Sistema completo de Machine Learning concluído!")