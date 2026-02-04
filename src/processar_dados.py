import os
import zipfile
import pandas as pd

PASTA_RAW = "data/raw"
PASTA_OUTPUT = "data/output"
TRIMESTRES = ["2T2024", "3T2024", "4T2024"]

def extrair_zips():
    for arquivo in os.listdir(PASTA_RAW):
        if arquivo.endswith(".zip"):
            caminho_zip = os.path.join(PASTA_RAW, arquivo)
            trimestre = arquivo.replace(".zip", "")
            pasta_destino = os.path.join(PASTA_RAW, trimestre)

            if os.path.exists(pasta_destino) and os.listdir(pasta_destino):
                print(f"{arquivo} já extraído, pulando...")
                continue

            print(f"Extraindo {arquivo}...")
            os.makedirs(pasta_destino, exist_ok=True)

            with zipfile.ZipFile(caminho_zip, "r") as zip_ref:
                zip_ref.extractall(pasta_destino)

    print("\nExtração concluída.\n")



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


def processar_despesas(df):
    df_despesas = df[
        df["DESCRICAO"]
        .str.contains("EVENTOS|SINIST", case=False, na=False)
        ].copy()
    
    df_despesas["Ano"] = df_despesas["DATA"].str[:4]
    df_despesas["Trimestre"] = df_despesas["TRIMESTRE"]

    df_consolidado = (
        df_despesas.groupby(["REG_ANS", "Ano", "Trimestre"], as_index=False)
        ["VL_SALDO_FINAL"]
        .sum()
    )

    df_consolidado = df_consolidado.rename(columns={
        "REG_ANS": "CNPJ",
        "VL_SALDO_FINAL": "ValorDespesas"
    })

    return df_consolidado


def salvar_csv_zip(df):
    os.makedirs(PASTA_OUTPUT, exist_ok=True)

    caminho_csv = os.path.join(PASTA_OUTPUT, "consolidado_despesas.csv")
    caminho_zip = os.path.join(PASTA_OUTPUT, "consolidado_despesas.zip")

    df.to_csv(caminho_csv, index=False, sep=";", encoding="utf-8")
    print(f"\nCSV salvo em: {caminho_csv}")

    with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(caminho_csv, arcname="consolidado_despesas.csv")

        print(f"Arquivo ZIP criado em: {caminho_zip}")

   
if __name__ == "__main__":
    extrair_zips()
    listar_arquivos_extraidos()

    df = carregar_todos_csvs()

    print("\nColunas do DataFrame final:")
    print (df.columns)
    print("\nTotal de registros:", len(df))

    df_consolidado = processar_despesas(df)

    print("\nPreview do DataFrame consolidado:")
    print(df_consolidado.head())
    print("\nTotal de linhas consolidadas:", len(df_consolidado))

    salvar_csv_zip(df_consolidado) 