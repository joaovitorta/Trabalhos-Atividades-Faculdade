#Conversor de Fahrenheit para Celsius

#Entrada do valor em Fahrenheit
fahrenheit = float(input("Digite o Valor em graus Fahrenheit: ")) 

#Conversão de valor para celsius
celsius = (fahrenheit - 32) * 5/9, 2 #Usei o round para definir apenas 2 casas decimais

#Saída do valor em Celsius
print(f"{fahrenheit:.2f} graus Fahrenheit equiuvalem a {celsius:.2f} graus Celsius.") 