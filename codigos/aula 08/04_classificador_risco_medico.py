# Aula 08 - Atividade Prática 3: Classificador de Risco Médico
# Sistema completo para classificar pacientes por nível de risco

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("=== CLASSIFICADOR DE RISCO MÉDICO ===\n")

class ClassificadorRiscoMedico:
    """Sistema completo para classificação de risco cardiovascular"""
    
    def __init__(self):
        self.modelo = None
        self.scaler = StandardScaler()
        self.feature_names = []
        self.classes = ['Baixo Risco', 'Médio Risco', 'Alto Risco']
        
    def criar_dataset_medico(self, n_pacientes=400):
        """Cria dataset médico realista"""
        
        np.random.seed(42)
        
        # Gerar dados base
        dados = {
            'idade': np.random.randint(18, 85, n_pacientes),
            'sexo': np.random.choice([0, 1], n_pacientes),  # 0=F, 1=M
            'pressao_sistolica': np.random.normal(130, 25, n_pacientes),
            'pressao_diastolica': np.random.normal(85, 15, n_pacientes),
            'glicose': np.random.normal(105, 30, n_pacientes),
            'imc': np.random.normal(26, 4, n_pacientes),
            'colesterol_total': np.random.normal(200, 50, n_pacientes),
            'fumante': np.random.choice([0, 1], n_pacientes, p=[0.75, 0.25]),
            'atividade_fisica': np.random.choice([0, 1, 2], n_pacientes, p=[0.3, 0.5, 0.2]),  # 0=baixa, 1=moderada, 2=alta
            'historico_familiar': np.random.choice([0, 1], n_pacientes, p=[0.7, 0.3])
        }
        
        df = pd.DataFrame(dados)
        
        # Adicionar correlações realistas
        df.loc[df['idade'] > 60, 'pressao_sistolica'] += 15
        df.loc[df['imc'] > 30, 'glicose'] += 20
        df.loc[df['fumante'] == 1, 'colesterol_total'] += 25
        
        # Calcular risco cardiovascular
        df['risco_cardiovascular'] = self._calcular_risco_cardiovascular(df)
        
        return df
    
    def _calcular_risco_cardiovascular(self, df):
        """Calcula risco cardiovascular baseado em guidelines médicos"""
        
        riscos = []
        
        for _, paciente in df.iterrows():
            score = 0
            
            # Fatores de idade
            if paciente['idade'] >= 65:
                score += 3
            elif paciente['idade'] >= 55:
                score += 2
            elif paciente['idade'] >= 45:
                score += 1
            
            # Pressão arterial
            if paciente['pressao_sistolica'] >= 160 or paciente['pressao_diastolica'] >= 100:
                score += 3
            elif paciente['pressao_sistolica'] >= 140 or paciente['pressao_diastolica'] >= 90:
                score += 2
            elif paciente['pressao_sistolica'] >= 130 or paciente['pressao_diastolica'] >= 80:
                score += 1
            
            # Glicose
            if paciente['glicose'] >= 126:
                score += 3  # Diabetes
            elif paciente['glicose'] >= 100:
                score += 1  # Pré-diabetes
            
            # IMC
            if paciente['imc'] >= 35:
                score += 2
            elif paciente['imc'] >= 30:
                score += 1
            
            # Colesterol
            if paciente['colesterol_total'] >= 240:
                score += 2
            elif paciente['colesterol_total'] >= 200:
                score += 1
            
            # Fatores de estilo de vida
            if paciente['fumante'] == 1:
                score += 3
            
            if paciente['atividade_fisica'] == 0:  # Sedentário
                score += 1
            
            if paciente['historico_familiar'] == 1:
                score += 2
            
            # Classificar risco
            if score >= 8:
                riscos.append(2)  # Alto risco
            elif score >= 4:
                riscos.append(1)  # Médio risco
            else:
                riscos.append(0)  # Baixo risco
        
        return riscos
    
    def preparar_dados(self, df):
        """Prepara dados para treinamento"""
        
        # Selecionar features
        self.feature_names = [
            'idade', 'sexo', 'pressao_sistolica', 'pressao_diastolica',
            'glicose', 'imc', 'colesterol_total', 'fumante', 
            'atividade_fisica', 'historico_familiar'
        ]
        
        X = df[self.feature_names]
        y = df['risco_cardiovascular']
        
        return X, y
    
    def treinar_modelo(self, X, y):
        """Treina o modelo de classificação"""
        
        print("=== TREINAMENTO DO MODELO ===")
        
        # Dividir dados
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Normalizar dados
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Treinar Random Forest (melhor para interpretabilidade)
        self.modelo = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        )
        
        self.modelo.fit(X_train_scaled, y_train)
        
        # Avaliar modelo
        y_pred = self.modelo.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Acurácia do modelo: {accuracy:.3f}")
        
        # Relatório detalhado
        print(f"\nRelatório de classificação:")
        print(classification_report(y_test, y_pred, target_names=self.classes))
        
        # Matriz de confusão
        cm = confusion_matrix(y_test, y_pred)
        print(f"\nMatriz de confusão:")
        print("Predito ->", "Baixo", "Médio", "Alto")
        for i, classe in enumerate(self.classes):
            print(f"{classe:10}", *cm[i])
        
        # Importância das features
        print(f"\nImportância das features:")
        importances = self.modelo.feature_importances_
        feature_importance = list(zip(self.feature_names, importances))
        feature_importance.sort(key=lambda x: x[1], reverse=True)
        
        for feature, importance in feature_importance:
            feature_readable = self._traduzir_feature(feature)
            print(f"  {feature_readable}: {importance:.3f}")
        
        return X_test_scaled, y_test, y_pred
    
    def _traduzir_feature(self, feature):
        """Traduz nomes das features para português"""
        traducoes = {
            'idade': 'Idade',
            'sexo': 'Sexo',
            'pressao_sistolica': 'Pressão Sistólica',
            'pressao_diastolica': 'Pressão Diastólica',
            'glicose': 'Glicose',
            'imc': 'IMC',
            'colesterol_total': 'Colesterol Total',
            'fumante': 'Fumante',
            'atividade_fisica': 'Atividade Física',
            'historico_familiar': 'Histórico Familiar'
        }
        return traducoes.get(feature, feature)
    
    def classificar_paciente(self, dados_paciente):
        """Classifica um novo paciente"""
        
        if self.modelo is None:
            raise ValueError("Modelo não foi treinado ainda!")
        
        # Preparar dados
        dados_array = np.array(dados_paciente).reshape(1, -1)
        dados_scaled = self.scaler.transform(dados_array)
        
        # Fazer predição
        predicao = self.modelo.predict(dados_scaled)[0]
        probabilidades = self.modelo.predict_proba(dados_scaled)[0]
        
        return predicao, probabilidades
    
    def gerar_relatorio_paciente(self, dados_paciente, nome_paciente="Paciente"):
        """Gera relatório completo para um paciente"""
        
        predicao, probabilidades = self.classificar_paciente(dados_paciente)
        
        print(f"\n=== RELATÓRIO DE RISCO - {nome_paciente.upper()} ===")
        
        # Dados do paciente
        print("Dados do paciente:")
        for i, feature in enumerate(self.feature_names):
            feature_nome = self._traduzir_feature(feature)
            valor = dados_paciente[i]
            
            # Formatação especial para alguns campos
            if feature == 'sexo':
                valor = 'Masculino' if valor == 1 else 'Feminino'
            elif feature == 'fumante':
                valor = 'Sim' if valor == 1 else 'Não'
            elif feature == 'atividade_fisica':
                atividades = ['Baixa', 'Moderada', 'Alta']
                valor = atividades[int(valor)]
            elif feature == 'historico_familiar':
                valor = 'Sim' if valor == 1 else 'Não'
            
            print(f"  {feature_nome}: {valor}")
        
        # Resultado da classificação
        risco_classe = self.classes[predicao]
        confianca = probabilidades[predicao] * 100
        
        print(f"\n🎯 CLASSIFICAÇÃO DE RISCO: {risco_classe}")
        print(f"📊 Confiança: {confianca:.1f}%")
        
        print(f"\nProbabilidades por classe:")
        for i, classe in enumerate(self.classes):
            prob = probabilidades[i] * 100
            print(f"  {classe}: {prob:.1f}%")
        
        # Recomendações
        print(f"\n💡 RECOMENDAÇÕES:")
        if predicao == 2:  # Alto risco
            print("  • Consulta médica urgente recomendada")
            print("  • Monitoramento intensivo necessário")
            print("  • Mudanças imediatas no estilo de vida")
        elif predicao == 1:  # Médio risco
            print("  • Acompanhamento médico regular")
            print("  • Implementar mudanças no estilo de vida")
            print("  • Monitoramento periódico")
        else:  # Baixo risco
            print("  • Manter hábitos saudáveis")
            print("  • Check-ups anuais")
            print("  • Prevenção primária")

# Demonstração do sistema
if __name__ == "__main__":
    
    # Criar classificador
    classificador = ClassificadorRiscoMedico()
    
    # 1. Criar dataset
    print("1. Criando dataset médico...")
    df = classificador.criar_dataset_medico(400)
    
    print(f"Dataset criado: {len(df)} pacientes")
    print(f"Distribuição de risco:")
    print(df['risco_cardiovascular'].value_counts().sort_index())
    
    # 2. Preparar dados
    print(f"\n2. Preparando dados...")
    X, y = classificador.preparar_dados(df)
    
    # 3. Treinar modelo
    print(f"\n3. Treinando modelo...")
    X_test, y_test, y_pred = classificador.treinar_modelo(X, y)
    
    # 4. Exemplo de classificação
    print(f"\n4. Exemplo de classificação...")
    
    # Paciente de alto risco
    paciente_alto_risco = [65, 1, 160, 95, 140, 32, 250, 1, 0, 1]
    classificador.gerar_relatorio_paciente(paciente_alto_risco, "João Silva")
    
    # Paciente de baixo risco
    paciente_baixo_risco = [30, 0, 110, 70, 85, 22, 180, 0, 2, 0]
    classificador.gerar_relatorio_paciente(paciente_baixo_risco, "Ana Costa")
    
    print("\n✅ Classificador de risco médico implementado com sucesso!")

print("\n✅ Sistema de classificação de risco cardiovascular concluído!")