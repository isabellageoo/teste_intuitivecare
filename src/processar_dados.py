import os
import zipfile
import pandas as pd

PASTA_RAW = "data/raw"
TRIMESTRES = ["2T2024", "3T2024", "4T2024"]

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

        for trimestre in TRIMESTRES:
            pasta = os.path.join(PASTA_RAW, trimestre)
            if os.path.exists(pasta):
                print(trimestre)

            for arquivo in os.listdir(pasta):
                print(f" - {arquivo}")

def carregar_todos_csvs():
    dfs = []

    for trimestre in TRIMESTRES:
        caminho = os.path.join(PASTA_RAW, trimestre, f"{trimestre}.csv")
        print(f"\nLendo {caminho}...")

        df = pd.read_csv(caminho, sep=";", encoding="latin1")

        df["VL_SALDO_FINAL"] = (
            df["VL_SALDO_FINAL"]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

        df["TRIMESTRE"] = trimestre
        dfs.append(df)

    df_final= pd.concat(dfs, ignore_index=True)
    return df_final

   
if __name__ == "__main__":
    extrair_zips()
    listar_arquivos_extraidos()

    df = carregar_todos_csvs()

    print("\nColunas do DataFrame final:")
    print (df.columns)

    print("\nTotal de registros:", len(df))
    print("\nPrimeiras linhas do DataFrame consolidado:")
    print(df.head())