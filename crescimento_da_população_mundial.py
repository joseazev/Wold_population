# -*- coding: utf-8 -*-
"""Crescimento da população Mundial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G_O-anzLDZlNWCv_sTu1B5T-0Vp3gamA

# Analise do Crescimento da População Mundial

## Analise numero I

Importando bibliotecas para analise e impressão de gráfico
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/joseazev/Wold_population/main/world-population.csv', sep=',')
data.head()

""" Os dados originais estão em língua inglesa, para melhor entendimento as colunas foram traduzidas para o português.

 ```
 Também é uma demonstração que eu sei manipular os nomes das colunas
 ```
"""

colunas = ['sigla','nome','pop2022','pop2020','pop2050','pop2030','pop2015',
           'pop2010','pop2000','pop1990','pop1980','pop1970','territorio',
           'densidade','taxa_de_crescimento','porcentagem_muldial',
           'classificacao']                                                     # Tradução das colunas
data.columns = colunas                                                          # Agregação de novos nomes

data.head()

quantidade_paises = data['nome'].count()                                        # Quantidade de países que fizeram parte do estudo
colunas = data.columns                                                          # Captura de colunas
contagens = len(colunas[2:-5])                                                  # Capturando as colunas com os estudos
print(f'Foram contado a população de um total de {quantidade_paises}')          # Apresentação de quantidade de países
print(f'As contagens foram realizada em {contagens} anos ao entre 1970 e 2022') # Aprese o resultado da quantidade de anos de contagem

paises = data['nome']                                                           # Captura os nomes dos países
media_paises = []                                                               #Cria uma lista que será adicionado o nome do pais e a media de crescimento.

for pais in paises:                                                             # Inicio do loop para percorrer os países do dataframe
  
  info_pais = data[data['nome'] == pais]                                        # Recolhe a linha referente ao país
  info_pais = info_pais.T                                                       # Transforma as colunas em linha
  info_pais.drop(['sigla','nome','territorio','densidade','taxa_de_crescimento',
                  'porcentagem_muldial','classificacao'], inplace=True)         # Descarta linhas essedentes
  info_pais.columns = ['populacao']                                             # Insere um nome para a coluna value
  crescimento = []                                                              # Cria uma lista vazia 

  for i in range(len(info_pais)):                                               # Percorre todas as linhas com a contagem da população

    if i+1 == len(info_pais):                                                   # Faz o teste para ver se está na última linha
      crescimento.append(0)                                                     # Caso positivo não a conta a ser feita adiciona zero 
      break                                                                     # Finaliza o for
    
    crescimento.append(info_pais.populacao[i] - info_pais.populacao[i+1])       # calcula a diferença entre as contagens dos anos
    
  info_pais['crescimento'] = crescimento                                        # Adiciona a lista com o resultado de crescimento
  media = round(
      sum(info_pais['crescimento'])/(len(info_pais['crescimento'])-1),2)        # Calcula a média dos crescimentos arredondando o para duas casas decimais               
  media_paises.append([pais,media])                                             # Insere o país e o resultado da média

media_paises = pd.DataFrame(media_paises, 
                            columns=['pais','media_de_crescimento'])            # atribui nome a colunas
media_paises.sort_values(by=['media_de_crescimento'],ascending=False, 
                         ignore_index=True, inplace=True)                       # Ordena de forma decrescente os valores das médias

media_paises.index.name = 'Id'                                                  # Atribuir um nome para a coluna de index
media_paises

"""### Os 10 países com os maiores médias de crescimento populacional """

sns.set(rc = {'figure.figsize':(15,8)})                                         # Modificando o as dimensões do plot 
sns.barplot(x='pais',
            y='media_de_crescimento',
            data=media_paises.query("Id in [0,1,2,3,4,5,6,7,8,9,10]"),
            palette="mako")                                                     # Criação de gráfico de barra.
plt.title('Média de crescimento populacional (de 1970 à 2022)')                 # Agregação de um titulo
plt.xlabel('Países')                                                            # Etiqueta do eixo x 
plt.ylabel('Média de Crescimento Populacional')                                 # Etiqueta do Eixo y

"""### Os 10 países com os menores médias de crescimento populacional """

sns.set(rc = {'figure.figsize':(15,8)})
sns.barplot(x='pais',
            y='media_de_crescimento',
            data=media_paises.query("Id in [221,222,223,224,225,226,227,228,229,230,231]"),
            palette="flare")
plt.title('Média de crescimento populacional (de 1970 à 2022)')
plt.xlabel('Países')
plt.ylabel('Média de Crescimento Populacional')
