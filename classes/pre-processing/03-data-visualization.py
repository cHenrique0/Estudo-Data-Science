
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv("../src/databases/credit_data.csv")

""" np.unique(ar, rc) retorna os valores únicos de um array numpy.
    
    ar -> é o dataset(e a coluna)
    rc(return_counts) -> se True, retorna uma contagem dos valores.

    Neste caso, retorna um tupla contendo duas listas, a primeira lista contém as
    classes, e a segunda lista contém a quantidade de ocorrência de cada classe.
    
    - coluna 'default' -> indica se a pessoa pagou ou não o empréstimo:
        - classe 0 -> pagou
        - classe 1 -> não pagou

    OBS: A função value_counts() do pandas retorna o mesmo resultado
"""

# Faz a contagem das classes únicas
classes_count = np.unique(base_credit['default'], return_counts=True)

# Coloca tudo em um dict onde key->classes e value->contagem
classes_dict = {key: value for key, value in zip(classes_count[0], classes_count[1])}
print(classes_dict)

# plotando gráfico com a lib seaborn
""" 
sns.countplot(x=base_credit['default'])
plt.ylabel("nº de clientes")
plt.xlabel("")
plt.xticks([0, 1], ["Pagam", "Não pagam"])
plt.title("Empréstimo")
plt.show()
"""

# plotando histograma considerando a idade
"""
plt.hist(x=base_credit['age'], edgecolor='black')
plt.ylabel("nº de clientes")
plt.xlabel("Idade")
plt.title("Idade dos clientes")
plt.show()
"""

# histograma considerando a renda anual
"""
plt.hist(x=base_credit['income'], edgecolor='black')
plt.ylabel("nº de clientes")
plt.xlabel("renda")
plt.title("Renda anual")
plt.show()
"""

# histograma considerando a dívida
"""
plt.hist(x=base_credit['loan'], edgecolor='black')
plt.ylabel("nº de clientes")
plt.xlabel("divida")
plt.show()
"""

# plotando gráfico de dispersão com a lib plotly
"""
grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color='default')
grafico.show()
"""