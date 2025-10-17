import os
import pandas as pd

pasta = r'C:\Users\lobat\Documents\lendo_dados_com_python\dados_amazonas_2024'

arquivos = [f for f in os.listdir(pasta) if f.startswith('INMET_N_AM_') and f.endswith('.CSV')]

lista_dfs = []
for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta, arquivo)
    # Lê o CSV pulando as 8 primeiras linhas
    df = pd.read_csv(caminho_arquivo, encoding='latin1', sep=';', skiprows=8)
    
    # Adiciona coluna 'fonte' com o nome do arquivo
    df['fonte'] = arquivo
    
    lista_dfs.append(df)

# Concatena todos os DataFrames
df_consolidado = pd.concat(lista_dfs, ignore_index=True)

print(df_consolidado.tail())

# Exporta para CSV sem o índice (index=False)
arquivo_saida = r'C:\Users\lobat\Documents\lendo_dados_com_python\INMET_2024.csv'
df_consolidado.to_csv(arquivo_saida, sep=';', index=False, encoding='latin1')

print(f"Arquivo exportado com sucesso para: {arquivo_saida}")