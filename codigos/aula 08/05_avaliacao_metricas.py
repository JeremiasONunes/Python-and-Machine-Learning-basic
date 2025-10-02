# Aula 08 - Tópico 4: Avaliação e Métricas de Modelos
# Demonstração de métricas de avaliação e interpretação de resultados

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, confusion_matrix, classification_report)

print("=== AVALIAÇÃO E MÉTRICAS DE MODELOS ===\n")

# Criar dados simulados
def criar_dados_avaliacao():
    """Cria dados para demonstrar métricas"""
    
    np.random.seed(42)
    n = 300
    
    # Features
    X = np.random.randn(n, 5)
    
    # Target com classes desbalanceadas (mais realista)
    y = np.zeros(n)
    
    # Criar padrão: combinação de features determina a classe
    for i in range(n):
        score = X[i, 0] * 0.5 + X[i, 1] * 0.3 + X[i, 2] * 0.2
        
        if score > 1.0:
            y[i] = 2  # Classe minoritária (alto risco)
        elif score > 0.2:
            y[i] = 1  # Classe intermediária
        else:
            y[i] = 0  # Classe majoritária (baixo risco)
    
    return X, y.astype(int)

def calcular_metricas_detalhadas(y_true, y_pred, classes=['Baixo', 'Médio', 'Alto']):
    """Calcula todas as métricas importantes"""
    
    print("=== MÉTRICAS DE AVALIAÇÃO ===")
    
    # 1. Acurácia
    accuracy = accuracy_score(y_true, y_pred)
    print(f"🎯 Acurácia Geral: {accuracy:.3f}")
    print("   (Proporção de predições corretas)")
    
    # 2. Métricas por classe
    precision = precision_score(y_true, y_pred, average=None, zero_division=0)
    recall = recall_score(y_true, y_pred, average=None, zero_division=0)
    f1 = f1_score(y_true, y_pred, average=None, zero_division=0)
    
    print(f"\n📊 Métricas por Classe:")
    for i, classe in enumerate(classes):
        print(f"  {classe}:")
        print(f"    Precisão: {precision[i]:.3f} (VP / (VP + FP))")
        print(f"    Recall:   {recall[i]:.3f} (VP / (VP + FN))")
        print(f"    F1-Score: {f1[i]:.3f} (Média harmônica)")
    
    # 3. Métricas médias
    precision_macro = precision_score(y_true, y_pred, average='macro', zero_division=0)
    recall_macro = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1_macro = f1_score(y_true, y_pred, average='macro', zero_division=0)
    
    precision_weighted = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall_weighted = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1_weighted = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    print(f"\n📈 Métricas Médias:")
    print(f"  Macro (não ponderada):")
    print(f"    Precisão: {precision_macro:.3f}")
    print(f"    Recall:   {recall_macro:.3f}")
    print(f"    F1-Score: {f1_macro:.3f}")
    
    print(f"  Weighted (ponderada por classe):")
    print(f"    Precisão: {precision_weighted:.3f}")
    print(f"    Recall:   {recall_weighted:.3f}")
    print(f"    F1-Score: {f1_weighted:.3f}")
    
    return {
        'accuracy': accuracy,
        'precision_macro': precision_macro,
        'recall_macro': recall_macro,
        'f1_macro': f1_macro
    }

def analisar_matriz_confusao(y_true, y_pred, classes=['Baixo', 'Médio', 'Alto']):
    """Analisa e visualiza matriz de confusão"""
    
    print(f"\n=== MATRIZ DE CONFUSÃO ===")
    
    cm = confusion_matrix(y_true, y_pred)
    
    # Exibir matriz
    print("Matriz de Confusão (Linhas=Real, Colunas=Predito):")
    print("        ", end="")
    for classe in classes:
        print(f"{classe:>8}", end="")
    print()
    
    for i, classe_real in enumerate(classes):
        print(f"{classe_real:8}", end="")
        for j in range(len(classes)):
            print(f"{cm[i, j]:8}", end="")
        print()
    
    # Análise detalhada
    print(f"\nAnálise da Matriz:")
    total = cm.sum()
    
    for i, classe in enumerate(classes):
        vp = cm[i, i]  # Verdadeiros Positivos
        fn = cm[i, :].sum() - vp  # Falsos Negativos
        fp = cm[:, i].sum() - vp  # Falsos Positivos
        vn = total - vp - fn - fp  # Verdadeiros Negativos
        
        print(f"  {classe}:")
        print(f"    VP: {vp}, FN: {fn}, FP: {fp}, VN: {vn}")
        
        if vp + fp > 0:
            precisao = vp / (vp + fp)
            print(f"    Precisão: {precisao:.3f}")
        
        if vp + fn > 0:
            recall = vp / (vp + fn)
            print(f"    Recall: {recall:.3f}")

def visualizar_resultados(y_true, y_pred, classes=['Baixo', 'Médio', 'Alto']):
    """Cria visualizações dos resultados"""
    
    print(f"\n=== VISUALIZAÇÕES ===")
    
    # Configurar subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Avaliação do Modelo de Classificação', fontsize=14, fontweight='bold')
    
    # 1. Matriz de Confusão
    cm = confusion_matrix(y_true, y_pred)
    im1 = ax1.imshow(cm, interpolation='nearest', cmap='Blues')
    ax1.set_title('Matriz de Confusão')
    ax1.set_xlabel('Predito')
    ax1.set_ylabel('Real')
    
    # Adicionar valores na matriz
    for i in range(len(classes)):
        for j in range(len(classes)):
            ax1.text(j, i, str(cm[i, j]), ha='center', va='center', 
                    color='white' if cm[i, j] > cm.max()/2 else 'black')
    
    ax1.set_xticks(range(len(classes)))
    ax1.set_yticks(range(len(classes)))
    ax1.set_xticklabels(classes)
    ax1.set_yticklabels(classes)
    
    # 2. Distribuição das Classes
    unique, counts = np.unique(y_true, return_counts=True)
    ax2.bar([classes[i] for i in unique], counts, color='skyblue', alpha=0.7)
    ax2.set_title('Distribuição Real das Classes')
    ax2.set_ylabel('Frequência')
    
    # Adicionar valores nas barras
    for i, count in enumerate(counts):
        ax2.text(i, count + 0.5, str(count), ha='center', va='bottom')
    
    # 3. Métricas por Classe
    precision = precision_score(y_true, y_pred, average=None, zero_division=0)
    recall = recall_score(y_true, y_pred, average=None, zero_division=0)
    f1 = f1_score(y_true, y_pred, average=None, zero_division=0)
    
    x_pos = np.arange(len(classes))
    width = 0.25
    
    ax3.bar(x_pos - width, precision, width, label='Precisão', alpha=0.7)
    ax3.bar(x_pos, recall, width, label='Recall', alpha=0.7)
    ax3.bar(x_pos + width, f1, width, label='F1-Score', alpha=0.7)
    
    ax3.set_title('Métricas por Classe')
    ax3.set_xlabel('Classes')
    ax3.set_ylabel('Score')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(classes)
    ax3.legend()
    ax3.set_ylim(0, 1)
    
    # 4. Comparação Predito vs Real
    pred_counts = np.bincount(y_pred, minlength=len(classes))
    real_counts = np.bincount(y_true, minlength=len(classes))
    
    x_pos = np.arange(len(classes))
    width = 0.35
    
    ax4.bar(x_pos - width/2, real_counts, width, label='Real', alpha=0.7)
    ax4.bar(x_pos + width/2, pred_counts, width, label='Predito', alpha=0.7)
    
    ax4.set_title('Distribuição: Real vs Predito')
    ax4.set_xlabel('Classes')
    ax4.set_ylabel('Frequência')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels(classes)
    ax4.legend()
    
    plt.tight_layout()
    plt.show()

def interpretar_resultados(metricas, y_true, y_pred):
    """Interpreta os resultados do modelo"""
    
    print(f"\n=== INTERPRETAÇÃO DOS RESULTADOS ===")
    
    accuracy = metricas['accuracy']
    f1_macro = metricas['f1_macro']
    
    # Avaliação geral
    print("📋 Avaliação Geral do Modelo:")
    
    if accuracy >= 0.9:
        print("  🟢 Excelente: Acurácia muito alta")
    elif accuracy >= 0.8:
        print("  🟡 Bom: Acurácia satisfatória")
    elif accuracy >= 0.7:
        print("  🟠 Regular: Acurácia moderada")
    else:
        print("  🔴 Ruim: Acurácia baixa")
    
    # Análise do F1-Score
    if f1_macro >= 0.8:
        print("  🟢 F1-Score macro indica bom desempenho balanceado")
    elif f1_macro >= 0.6:
        print("  🟡 F1-Score macro indica desempenho moderado")
    else:
        print("  🔴 F1-Score macro indica necessidade de melhorias")
    
    # Recomendações
    print(f"\n💡 Recomendações:")
    
    if accuracy < 0.8:
        print("  • Coletar mais dados de treinamento")
        print("  • Experimentar outros algoritmos")
        print("  • Melhorar engenharia de features")
    
    # Análise de classes desbalanceadas
    unique, counts = np.unique(y_true, return_counts=True)
    min_class = counts.min()
    max_class = counts.max()
    
    if max_class / min_class > 3:
        print("  • Classes desbalanceadas detectadas")
        print("  • Considerar técnicas de balanceamento")
        print("  • Usar métricas ponderadas")
    
    print("  • Validar com dados externos")
    print("  • Monitorar performance em produção")

# Demonstração completa
if __name__ == "__main__":
    
    print("Criando dados para avaliação...")
    X, y = criar_dados_avaliacao()
    
    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Treinar modelo
    print("Treinando modelo Random Forest...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    
    # Fazer predições
    y_pred = modelo.predict(X_test)
    
    # Avaliar modelo
    classes = ['Baixo Risco', 'Médio Risco', 'Alto Risco']
    
    metricas = calcular_metricas_detalhadas(y_test, y_pred, classes)
    analisar_matriz_confusao(y_test, y_pred, classes)
    
    # Relatório do sklearn
    print(f"\n=== RELATÓRIO SKLEARN ===")
    print(classification_report(y_test, y_pred, target_names=classes))
    
    # Visualizar resultados
    visualizar_resultados(y_test, y_pred, classes)
    
    # Interpretar resultados
    interpretar_resultados(metricas, y_test, y_pred)
    
    print(f"\n✅ Avaliação completa do modelo concluída!")

print("\n✅ Demonstração de métricas de avaliação concluída!")