#
# Fazendo uma annalise inicial do dataset de risco de crédito
# Fonte dos dados (adaptado): https://www.kaggle.com/laotse/credit-risk-dataset
# 

import pandas as pd


# lendo o dataset
db_credit = pd.read_csv("../src/databases/credit_data.csv")

# imprime as 5 primeiras e 5 ultimas linhas do arquivo
""" print(db_credit) """

# imprime as 5 primeiras linhas do arquivo
""" print(db_credit.head()) """

# imprime as 5 ultimas linhas do arquivo
""" print(db_credit.tail()) """

# imprime uma algumas estatísticas do arquivo
""" print(db_credit.describe()) """

# aplicando um filtro para saber qual a pessoa com a maior renda anual
""" print(db_credit[db_credit['income'] == db_credit['income'].max()]) """

# aplicando um filtro para saber qual a pessoa com a menor dívida
""" print(db_credit[db_credit['loan'] == db_credit['loan'].min()]) """
