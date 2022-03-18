
# Análise da base de dados do censo
# Fonte: https://archive.ics.uci.edu/ml/datasets/adult

import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
import plotly.express as px

"""
* Analisando os atributos

    1. age(int) -> Numérica, discreta. É a idade da pessoa.
    2. workclass(string) -> Categórica, nominal. Indica a classe de trabalho.
    3. final-weight(int) -> Numérica, continua. Cálculo realizado pelo censo(como se fosse uma pontuação).
    4. education(string) -> Categórica, ordinal. Nivel de escolaridade.
    5. education-num(int) -> Numerica, discreta. Número de anos que a pessoa estudou.
    6. marital-status(string) -> Categorica, nominal. Estado civil
    7. occupation(string) -> Categorica, nominal. Profissão.
    8. relationship(string) -> Categorica, nominal. Relacionamento familiar.
    9. race(string) -> Categorica, nominal. Raça.
    10. sex(string) -> Categorica, nominal. Sexo.
    11. capital-gain(int) -> Numerica, continua. Ganho de capital.
    12. capital-lool(int) -> Numérica, continua. Perda de capital.
    13. hour-per-week(int) -> Numérica, discreta. Horas trabalhadas por semana.
    14. native-country(string) -> Categorica, nominal. País de nascimento.
    15. income(string) -> Categorica, ordinal. Possui dois valores: >50k e <=50k

    * O objetivo da analise deste dataset é determinar se uma pessoa ganha mais de
    50 mil dolares por ano.

"""

# Carregando os dados
base_census = pd.read_csv("../src/databases/census.csv")

# Verificando a existencia de valores NaN
"""print(base_census.isnull().sum())"""

# Visualização dos dados
# Contando as classes
"""print(np.unique(base_census['income'], return_counts=True))"""
# Plotando people x income
"""
sns.countplot(x=base_census['income'])
plt.show()
"""
# Plotando histograma da idade
"""
plt.hist(x=base_census['age'], ec='black')
plt.xlabel("age")
plt.ylabel("No. people")
plt.xlim(0, 100)
plt.show()
"""

# Plotando histograma dos anos estudados
"""
plt.hist(x=base_census['education-num'], ec='black')
plt.xlabel("years")
plt.ylabel("No. people")
plt.show()
"""

# Plotando histograma de horas trabalhadas por semana
"""
plt.hist(x=base_census['hour-per-week'], ec='black')
plt.xlabel("hours per week")
plt.ylabel("no. people")
plt.show()
"""

# Tree map usando plotly: agrupando pessoas por classe de trabalho e idade
"""
grafico = px.treemap(base_census, path=['workclass', 'age'])
grafico.show()
"""

# plotando: categoria paralelas
"""
grafico = px.parallel_categories(base_census, dimensions=['occupation', 'relationship'])
grafico.show()
"""