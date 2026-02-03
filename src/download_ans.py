import os
import requests
from tqdm import tqdm

BASE_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
PASTA_DESTINO = "data/raw"

TRIMESTRES = [
    (2024, "4T"),
    (2024, "3T"),
    (2024, "2T"),
]

def baixar_arquivo(url, caminho_destino):
    try:
        with requests.get(url, stream=True, timeout=30) as r:
            if r.status_code != 200:
                print(f"Falha ao baixar: {url}")
                return False

            total = int(r.headers.get("content-length", 0))
            with open(caminho_destino, "wb") as f, tqdm(
                total=total,
                unit="B",
                unit_scale=True,
                desc=os.path.basename(caminho_destino)
            ) as barra:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        barra.update(len(chunk))
        return True
    except requests.RequestException as e:
        print(f"Erro de conexão: {e}")
        return False

def main():
    os.makedirs(PASTA_DESTINO, exist_ok=True)

    print("Iniciando download dos arquivos...\n")

    for ano, trimestre in TRIMESTRES:
        nome_arquivo = f"{trimestre}{ano}.zip"
        url = f"{BASE_URL}{ano}/{nome_arquivo}"
        caminho = os.path.join(PASTA_DESTINO, nome_arquivo)

        print(f"\nBaixando {nome_arquivo}")
        sucesso = baixar_arquivo(url, caminho)

        if sucesso:
            print(f"Download concluído: {nome_arquivo}\n")
        else: 
            print(f"Arquivo indisponível: {nome_arquivo}\n")

if __name__ == "__main__":
    main()