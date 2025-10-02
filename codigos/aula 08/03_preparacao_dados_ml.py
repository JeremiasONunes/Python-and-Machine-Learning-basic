# Aula 08 - Atividade Prática 2: Pipeline de Preparação de Dados para ML
# Sistema completo de preparação de dados médicos para Machine Learning

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

print("=== PIPELINE DE PREPARAÇÃO DE DADOS PARA ML ===\n")

class PreparadorDadosMedicos:
    """Classe para preparar dados médicos para Machine Learning"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.imputer = SimpleImputer(strategy='median')
        self.feature_names = []
        
    def criar_dataset_simulado(self, n_amostras=300):
        """Cria dataset médico simulado com alguns problemas intencionais"""
        
        np.random.seed(42)
        
        dados = {
            'idade': np.random.randint(18, 85, n_amostras),
            'sexo': np.random.choice(['M', 'F'], n_amostras),
            'cidade': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'], n_amostras),
            'pressao_sistolica': np.random.normal(130, 25, n_amostras),
            'pressao_diastolica': np.random.normal(85, 15, n_amostras),
            'glicose': np.random.normal(105, 30, n_amostras),
            'imc': np.random.normal(26, 4, n_amostras),
            'colesterol': np.random.normal(200, 50, n_amostras),
            'fumante': np.random.choice(['Sim', 'Não'], n_amostras, p=[0.3, 0.7]),
            'atividade_fisica': np.random.choice(['Baixa', 'Moderada', 'Alta'], n_amostras, p=[0.4, 0.4, 0.2])
        }
        
        df = pd.DataFrame(dados)
        
        # Adicionar alguns valores ausentes intencionalmente
        missing_indices = np.random.choice(df.index, size=int(0.05 * n_amostras), replace=False)
        df.loc[missing_indices[:len(missing_indices)//2], 'glicose'] = np.nan
        df.loc[missing_indices[len(missing_indices)//2:], 'colesterol'] = np.nan
        
        # Criar target baseado em lógica médica
        df['risco_cardiovascular'] = self._calcular_risco(df)
        
        return df
    
    def _calcular_risco(self, df):
        """Calcula risco cardiovascular baseado em fatores médicos"""
        
        risco = []
        
        for _, row in df.iterrows():
            score = 0
            
            # Idade
            if row['idade'] > 65:
                score += 3
            elif row['idade'] > 50:
                score += 2
            elif row['idade'] > 35:
                score += 1
            
            # Pressão (usando valores não-nulos)
            if pd.notna(row['pressao_sistolica']):
                if row['pressao_sistolica'] > 140:
                    score += 3
                elif row['pressao_sistolica'] > 130:
                    score += 1
            
            # Glicose
            if pd.notna(row['glicose']):
                if row['glicose'] > 126:
                    score += 2
                elif row['glicose'] > 100:
                    score += 1
            
            # IMC
            if row['imc'] > 30:
                score += 2
            elif row['imc'] > 25:
                score += 1
            
            # Fumante
            if row['fumante'] == 'Sim':
                score += 2
            
            # Atividade física
            if row['atividade_fisica'] == 'Baixa':
                score += 1
            
            # Classificar risco
            if score >= 6:
                risco.append('Alto')
            elif score >= 3:
                risco.append('Médio')
            else:
                risco.append('Baixo')
        
        return risco
    
    def analisar_dados(self, df):
        """Analisa qualidade dos dados"""
        
        print("=== ANÁLISE DOS DADOS ===")
        print(f"Shape: {df.shape}")
        print(f"Colunas: {df.columns.tolist()}")
        
        print(f"\nTipos de dados:")
        print(df.dtypes)
        
        print(f"\nValores ausentes:")
        missing = df.isnull().sum()
        for col, count in missing.items():
            if count > 0:
                perc = count / len(df) * 100
                print(f"  {col}: {count} ({perc:.1f}%)")
        
        print(f"\nDuplicatas: {df.duplicated().sum()}")
        
        print(f"\nDistribuição do target:")
        print(df['risco_cardiovascular'].value_counts())
        
        return missing
    
    def limpar_dados(self, df):
        """Limpa e trata os dados"""
        
        print(f"\n=== LIMPEZA DOS DADOS ===")
        
        df_clean = df.copy()
        
        # 1. Remover duplicatas
        antes_dup = len(df_clean)
        df_clean = df_clean.drop_duplicates()
        depois_dup = len(df_clean)
        print(f"Duplicatas removidas: {antes_dup - depois_dup}")
        
        # 2. Tratar outliers extremos
        for col in ['pressao_sistolica', 'pressao_diastolica', 'glicose', 'imc', 'colesterol']:
            Q1 = df_clean[col].quantile(0.01)
            Q3 = df_clean[col].quantile(0.99)
            
            outliers_antes = len(df_clean[(df_clean[col] < Q1) | (df_clean[col] > Q3)])
            df_clean[col] = df_clean[col].clip(lower=Q1, upper=Q3)
            
            if outliers_antes > 0:
                print(f"Outliers tratados em {col}: {outliers_antes}")
        
        # 3. Tratar valores ausentes
        colunas_numericas = ['glicose', 'colesterol', 'pressao_sistolica', 'pressao_diastolica', 'imc']
        
        for col in colunas_numericas:
            if df_clean[col].isnull().sum() > 0:
                mediana = df_clean[col].median()
                df_clean[col].fillna(mediana, inplace=True)
                print(f"Valores ausentes preenchidos em {col} com mediana: {mediana:.1f}")
        
        return df_clean
    
    def preparar_features(self, df):
        """Prepara features para ML"""
        
        print(f"\n=== PREPARAÇÃO DAS FEATURES ===")
        
        df_prep = df.copy()
        
        # 1. Codificar variáveis categóricas
        colunas_categoricas = ['sexo', 'cidade', 'fumante', 'atividade_fisica']
        
        for col in colunas_categoricas:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
            
            df_prep[col + '_encoded'] = self.label_encoders[col].fit_transform(df_prep[col])
            print(f"Codificado {col}: {dict(zip(self.label_encoders[col].classes_, 
                                              self.label_encoders[col].transform(self.label_encoders[col].classes_)))}")
        
        # 2. Criar features derivadas
        df_prep['pressao_media'] = (df_prep['pressao_sistolica'] + df_prep['pressao_diastolica']) / 2
        df_prep['idade_grupo'] = pd.cut(df_prep['idade'], bins=[0, 30, 50, 65, 100], labels=[0, 1, 2, 3])
        df_prep['imc_categoria'] = pd.cut(df_prep['imc'], bins=[0, 18.5, 25, 30, 50], labels=[0, 1, 2, 3])
        
        print("Features derivadas criadas:")
        print("  - pressao_media")
        print("  - idade_grupo")
        print("  - imc_categoria")
        
        # 3. Selecionar features finais
        features_numericas = ['idade', 'pressao_sistolica', 'pressao_diastolica', 'glicose', 
                             'imc', 'colesterol', 'pressao_media']
        features_categoricas = ['sexo_encoded', 'cidade_encoded', 'fumante_encoded', 
                               'atividade_fisica_encoded', 'idade_grupo', 'imc_categoria']
        
        self.feature_names = features_numericas + features_categoricas
        
        X = df_prep[self.feature_names]
        y = df_prep['risco_cardiovascular']
        
        return X, y
    
    def dividir_dados(self, X, y, test_size=0.2):
        """Divide dados em treino e teste"""
        
        print(f"\n=== DIVISÃO DOS DADOS ===")
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y
        )
        
        print(f"Treino: {X_train.shape[0]} amostras")
        print(f"Teste: {X_test.shape[0]} amostras")
        
        print(f"\nDistribuição no treino:")
        print(pd.Series(y_train).value_counts())
        
        return X_train, X_test, y_train, y_test
    
    def normalizar_dados(self, X_train, X_test):
        """Normaliza os dados"""
        
        print(f"\n=== NORMALIZAÇÃO ===")
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        print("Dados normalizados com StandardScaler")
        print(f"Média após normalização: {X_train_scaled.mean():.3f}")
        print(f"Desvio após normalização: {X_train_scaled.std():.3f}")
        
        return X_train_scaled, X_test_scaled

# Executar pipeline completo
if __name__ == "__main__":
    
    # Criar preparador
    preparador = PreparadorDadosMedicos()
    
    # 1. Criar dataset
    print("1. Criando dataset simulado...")
    df = preparador.criar_dataset_simulado(300)
    
    # 2. Analisar dados
    print("\n2. Analisando dados...")
    preparador.analisar_dados(df)
    
    # 3. Limpar dados
    print("\n3. Limpando dados...")
    df_limpo = preparador.limpar_dados(df)
    
    # 4. Preparar features
    print("\n4. Preparando features...")
    X, y = preparador.preparar_features(df_limpo)
    
    # 5. Dividir dados
    print("\n5. Dividindo dados...")
    X_train, X_test, y_train, y_test = preparador.dividir_dados(X, y)
    
    # 6. Normalizar
    print("\n6. Normalizando dados...")
    X_train_scaled, X_test_scaled = preparador.normalizar_dados(X_train, X_test)
    
    # Resumo final
    print(f"\n=== RESUMO FINAL ===")
    print(f"✅ Dataset criado: {len(df)} amostras")
    print(f"✅ Dados limpos e tratados")
    print(f"✅ {len(preparador.feature_names)} features preparadas")
    print(f"✅ Dados divididos: {len(X_train)} treino, {len(X_test)} teste")
    print(f"✅ Dados normalizados")
    print(f"✅ Pronto para Machine Learning!")
    
    print(f"\nFeatures selecionadas:")
    for i, feature in enumerate(preparador.feature_names):
        print(f"  {i+1}. {feature}")

print("\n✅ Pipeline de preparação de dados concluído!")