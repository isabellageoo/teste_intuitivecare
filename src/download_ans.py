from datetime import datetime

def listar_ultimos_trimestres():
    """
    A ANS não permite listagem automática de arquivos ou diretórios.
    Portanto, os trimestres são definidos com base no calendário.
    """

    hoje = datetime.today()
    ano = hoje.year
    mes = hoje.month

    if mes <= 3:
        trimestres = [(ano - 1, "4T"), (ano - 1, "3T"), (ano - 1, "2T")]
    elif mes <= 6:
        trimestre = [(ano, "1T"), (ano - 1, "4T"), (ano - 1, "3T")]
    elif mes <= 9:
        trimestre = [(ano, "2T"), (ano, "1T"), (ano - 1, "4T")]
    else:
        trimestres = [(ano, "3T"), (ano, "2T"), (ano, "1T")]

    return trimestres

if __name__ == "__main__":
    print("Trimestres considerados para processamento:\n")

    trimestres = listar_ultimos_trimestres()
    for ano, trimestre in trimestres:
        print(f"Ano: {ano} - Trimestre: {trimestre}")