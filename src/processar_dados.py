import os
import zipfile
import pandas as pd

PASTA_RAW = "data/raw"

def extrair_zips():
    arquivos = os.listdir(PASTA_RAW)

    zips = [f for f in arquivos if f.endswith(".zip")]

    if not zips:
        print("Nenhum arquivo ZIP encontrado.")
        return
    
    for zip_nome in zips:
        caminho_zip = os.path.join(PASTA_RAW, zip_nome)
        pasta_destino = os.path.join(PASTA_RAW, zip_nome.replace(".zip", ""))

        print(f"Extraindo {zip_nome}...")

        os.makedirs(pasta_destino, exist_ok=True)

        with zipfile.ZipFile(caminho_zip, "r") as zip_ref:
            zip_ref.extractall(pasta_destino)

    print("\nExtração concluída.")

def listar_arquivos_extraidos():
        print("\nArquivos extraídos por trimestre:\n")

        for item in os.listdir(PASTA_RAW):
            caminho = os.path.join(PASTA_RAW, item)

            if os.path.isdir(caminho) and not item.endswith(".zip"):
                print(f"{item}")

                for arquivo in os.listdir(caminho):
                    print(f" - {arquivo}")

                    
if __name__ == "__main__":
    extrair_zips()
    listar_arquivos_extraidos()