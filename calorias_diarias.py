#Aplicação para calcular a quantidade de calorias ingeridas no dia.
consumo_total = 0
for x in range(0,10):
#O usuario deve entrar com o alimento e as calorias.
    alimento = str(input("Informe o alimento: "))
    calorias = float(input("informe as calorias: "))
#O calculo devera mostrar o total de calorias no dia.
    consumo_total = consumo_total + calorias
print("0 consumo total em calorias no seu dia foi: {} cal".format(consumo_total))





































