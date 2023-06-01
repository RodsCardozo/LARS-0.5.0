
import pandas as pd
import os, sys

nome_arquivo = input(f'Insira o nome da pasta: ')

# Lista todos os arquivos CSV em um diretório específico
arquivos_csv = []
n = 14
for i in range(0,n+1):
    nome = (f"{nome_arquivo}/resultado_temp_{i}.csv")
    arquivos_csv.append(nome)

print(arquivos_csv)

# Cria uma lista vazia para armazenar os DataFrames de cada arquivo CSV
dataframes = []

# Loop pelos arquivos CSV e carrega cada um em um DataFrame separado
for arquivo in arquivos_csv:
    df = pd.read_csv(arquivo)
    dataframes.append(df)

# Concatena os DataFrames em um único DataFrame
df_final = pd.concat(dataframes)

# Salva o DataFrame final em um arquivo CSV
df_final.to_csv(f'{nome_arquivo}/resultado.csv', index=False)

# Plot dos resultados

df_final = pd.read_csv(f'{nome_arquivo}/resultado.csv')
'''import matplotlib.pyplot as plt
import numpy as np



fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='Tempratura [k]',
       title='Temperatura da Face 1')
ax.grid()

fig.savefig(f'{nome_arquivo}/temp_face1.png')
plt.show()'''
import matplotlib.pyplot as plt
import numpy as np
# Defina o tamanho do gráfico
plt.figure(figsize=(8, 6))
s = np.array(df_final['Face1'])
print(len(s))
t = np.linspace(0,len(s), len(s))
print(len(t))
# Plotando os dados
plt.plot(t, df_final['Face1'], label='Face1')
plt.plot(t, df_final['Face2'], label='Face2')
plt.plot(t, df_final['Face3'], label='Face3')
plt.plot(t, df_final['Face4'], label='Face4')
plt.plot(t, df_final['Face5'], label='Face5')
plt.plot(t, df_final['Face6'], label='Face6')


# Adicione um título ao gráfico
plt.title('Gráfico de Dados')

# Adicione rótulos aos eixos x e y
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicione uma legenda
plt.legend()

# Exiba o gráfico
plt.show()

plt.savefig(f'{nome_arquivo}/temp_face1.png')