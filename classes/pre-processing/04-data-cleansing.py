
import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt


# Tratando dados inconsistentes e faltantes

base_credit = pd.read_csv("../src/databases/credit_data.csv")

"""
1. Localizando os dados:

    .loc[df_label]:
        Faz uma busca do 'df_label' informado e retorna um pandas DataFrame.
        Caso a função não encontre o label, retorna um KeyError

2. Corrigindo os dados inconsistentes:

    Há algumas técnicas para corrigir os dados inconsistentes:

    2.1. Apagar a coluna com os dados defeituosos
    2.2. Apagar os registros com os dados defeituosos
    2.3. Preencher os valores inconsistentes manualmente(RECOMENDÁVEL)
    2.4. Preencher os valores com a média dos valores

3. Corrigindo dados faltantes:

"""

# Localizando idades com valores negativos
"""
negative_ages = base_credit.loc[base_credit['age'] < 0]
print(negative_ages)
"""

# Outra maneira de fazer a localização:
"""
negative_ages = base_credit[base_credit['age'] < 0]
print(negative_ages)
"""

# Corringindo os dados: apagando a coluna
"""
base_credit_without_age = base_credit.drop('age', axis=1)
print(base_credit_without_age)
"""

# Corringindo os dados: apagando os registros com os dados errados
"""
base_credit_withou_wrong_data = base_credit.drop(base_credit[base_credit['age'] < 0].index)
print(base_credit_withou_wrong_data)
"""

# Corringindo os dados: preenchendo com a média
# base_credit_mean = base_credit.mean() # Retorna a média dos valores de todas as colunas
# Fazendo a média das idades(excluindo os dados incorretos)
age_mean = base_credit['age'][base_credit['age'] > 0].mean()
# Substituindo os dados incorretos com o valor da média
base_credit.loc[base_credit['age'] < 0, 'age'] = age_mean
print(base_credit.head(30))
