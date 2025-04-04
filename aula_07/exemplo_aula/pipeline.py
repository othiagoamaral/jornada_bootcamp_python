from etl import ler_csv, filtrar_produtos, somar_valores_produtos

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_filtrados = filtrar_produtos(lista_de_produtos)
soma_dos_valores = somar_valores_produtos(produtos_filtrados)
print(soma_dos_valores)