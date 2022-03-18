
import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

"""
# Fazendo a limpeza do dados(data cleansing)

1. Localizando os dados:

    .loc[df_label]:
        Faz uma busca do 'df_label' informado e retorna um pandas DataFrame.
        Caso a função não encontre o label, retorna um KeyError

2. Corrigindo os dados inconsistentes(valores inválidos):

    * Há algumas técnicas para corrigir os dados inconsistentes:

    2.1. Apagar a coluna com os dados defeituosos
    2.2. Apagar os registros com os dados defeituosos
    2.3. Preencher os valores inconsistentes manualmente(RECOMENDÁVEL)
    2.4. Preencher os valores com a média dos valores(USUAL)

3. Corrigindo dados ausentes(valores não preenchidos):

    * Dados ausentes -> NaN -> Not a Number

    df_name.isnull() -> retorna True ou False para todos os registros das colunas do dataset.
        - se True, então o valor não foi preenchido(dado ausente)
        - usando sum() junto de isnull() temos a quantidade de valores ausentes no dataset.

    pd.isnull(df_name[column]) -> retorna um dataframe com os registros com valores NaN

    * Para corrigir podemos usar a tecnica de preencher os dados ausentes com a 
    média dos valores em questão.

    df_name.fillna(value, inplace=True) -> preenche os dados NaN com o valor especificado
        - value -> valor que será preenchido
        - inplace -> se True, altera o dataframe com os novos dados

4. Dividindo os dados entre Previsores e Classes:

    O objetivo é utilizar, os dados históricos, renda(income), idade(age), 
    valor da divida(loan) para fazer a previsão se a pessoa vai ou não pagar o 
    empréstimo(default).
    Para isso, precisamos fazer a divisão dos dados.
    Cria-se duas variaveis, normalmente chamadas de x e y, onde:
        - x -> armazena os atributos previsores
        - y -> armazena a classe
"""

# Carregando os dados
base_credit = pd.read_csv("../src/databases/credit_data.csv")

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
# print(base_credit.mean()) # Retorna a média dos valores de todas as colunas
# Fazendo a média das idades(excluindo os dados incorretos)
age_mean = base_credit['age'][base_credit['age'] > 0].mean()
# Substituindo os dados incorretos com o valor da média
base_credit.loc[base_credit['age'] < 0, 'age'] = age_mean

# Localizando valores ausentes(dados não preenchidos):
# print(base_credit.isnull().sum())   # quantidade de dados ausentes em cada coluna
# print(base_credit['age'].isnull().sum()) # quantidade de dados ausentes numa coluna especifica

# Visualizando os registros não preenchidos
"""
print("ANTES de preencher com a média")
print(base_credit.loc[pd.isnull(base_credit['age'])])
"""

# Corrigindo os dados ausentes: preenchendo com a média
base_credit['age'].fillna(age_mean, inplace=True) # age_mean foi calculado na linha 74
"""
print("\nDEPOIS de preencher com a média")
print(base_credit.loc[pd.isnull(base_credit['age'])]) # retorna um DF vazio
"""

# verificando as alterações feitas atraves do id do cliente
# | (pipe) -> ou lógico
"""
print(base_credit.loc[(base_credit['clientid'] == 29) |
                      (base_credit['clientid'] == 31) |
                      (base_credit['clientid'] == 32)])
"""
# Outra forma: isin(list)
""" print(base_credit.loc[base_credit['clientid'].isin([29, 31, 32])]) """

# Dividindo os dados: Previsores x Classe
x_credit = base_credit.iloc[:, 1:4].values  # .values -> retorna um array numpy
y_credit = base_credit.iloc[:, 4].values