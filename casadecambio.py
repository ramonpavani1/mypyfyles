# O usuario entrara com um valor em Reais e tera a conversao em Dolares.
reais = input("Defina um valor em reais: ")
# Para fazer a conversao basta multiplicarmos o valor em Reais com a cotacao atual em Dolares.
conversao = float(reais) * 4.95
print("O valor em dolar e: ${}".format(conversao))

