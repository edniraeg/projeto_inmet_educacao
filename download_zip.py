import requests
import zipfile
import io

# URL do arquivo zip
url = "https://portal.inmet.gov.br/uploads/dadoshistoricos/2024.zip"

# Faz o download
response = requests.get(url)

if response.status_code == 200:
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        # Filtrar arquivos que começam com 'INMET_N_AM_'
        arquivos_am = [f for f in zip_file.namelist() if f.startswith('INMET_N_AM_')]

        print(f"Total de arquivos com prefixo 'INMET_N_AM_': {len(arquivos_am)}\n")

        # Extrair esses arquivos para uma pasta local (ex: './dados_amazonas')
        pasta_destino = "./dados_amazonas_2024"
        zip_file.extractall(path=pasta_destino, members=arquivos_am)

        for arquivo in arquivos_am:
            print(f"Extraído: {arquivo}")
else:
    print(f"Erro ao baixar o arquivo: {response.status_code}")
