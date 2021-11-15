#Calculo do Volume de uma esfera

#Entrada do Raio da esfera
raio_esfera = float(input("Digite o raio da esfera em centímetro: "))

#Calculo do volume da esfera
volume = round(4*3.14*(raio_esfera**3)/3 , 2) 

#Saída do volume da esfera
print("Uma esfera com raio {} cm terá um Volume de {} cm3".format(raio_esfera, volume))

