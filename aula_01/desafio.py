
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

# 1) Solicitar o nome do usário
nome = input('Digite o seu nome: ')

# 2) Solititar o salário do usuário
salario = float(input('Digite o seu salário: '))

# 3) Solicitar o multiplicador para cálculo do bônus
multiplicador = float(input('Digite o multiplicador do bônus: '))

# Cálculo Bônus (1.000 + Salário * Bônus): 
valor_fixo = 1000
valor_bonus = valor_fixo + (salario * multiplicador)

# Exibe o resultado para o usuário
print(f'Olá ',nome,'! O Seu Valor de Bônus é de:',valor_bonus)
print(f'Olá {nome}! O seu bônus é de {valor_bonus}')