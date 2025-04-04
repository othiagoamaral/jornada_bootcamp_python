import csv

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo csv e returna uma lista de dicionários
    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos(lista_input: list[dict]) -> list[dict]:
    """
    Função que filtra produtos do dicionário
    """
    lista_produto_filtrados = []
    for produto in lista_input:
        if produto.get("entregue") == "False":
            lista_produto_filtrados.append(produto)
    return lista_produto_filtrados

def somar_valores_produtos(lista_produtos_filtrados: list[dict]) -> int:
    """
    Função que soma os produtos filtrados
    """
    valor_soma = 0
    for produto in lista_produtos_filtrados:
        valor_soma += int(produto.get("price"))
    return valor_soma



