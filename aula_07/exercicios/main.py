from funcoes import calcular_media, filtrar_acima_de


# 1. Calcular Média de Valores em uma Lista
print('Output do execício 01:')
valor_media = calcular_media([5,10,15])
print(valor_media)

# 2. Filtrar Dados Acima de um Limite
print('Output do execício 02:')
lista_inicial = [2,5,8,11,15,19]
limite = 7

lista_dados_acima_limite = filtrar_acima_de(lista_inicial, limite)
print(lista_dados_acima_limite)