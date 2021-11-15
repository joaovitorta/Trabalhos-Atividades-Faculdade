#Programa para calcular o IMC do úsuario 

#Entrada dos dados peso e altura
peso = input("Digite seu peso em Kg: ")
altura = input("Digite sua altura em Metros: ")

#Troco o "," pelo "." para manter a regra americana
peso = peso.replace(",", ".")
altura = altura.replace(",", ".")

#Transformo os Dados em Float para conseguir fazer o calculo
peso = float(peso)
altura = float(altura)

#Calculo do imc
imc = peso/altura**2

#O programa analisa o estado do úsuario e manda uma mensagem conforme o estado dele
if(imc <= 16.9):
    print(f"Com o imc igual a {imc:.2f}kg/m² você está abaixo do peso ideal")

elif(imc <= 24.9):
    print(f"Com o imc igual a {imc:.2f}kg/m² você está com peso ideal")

elif(imc <= 60):
    print(f"Com o imc igual a {imc:.2f}kg/m² você está Acima do peso ideal")
