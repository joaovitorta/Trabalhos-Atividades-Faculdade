# João Vitor Teixeira Amaral
# Atv 4 
# Programa para academia saber peso e altura de seus clientes

cod_cliente = float(input("Digite seu código:"))
peso = input('Digite seu peso:')
altura =  input('Digite sua altura:')

peso = peso.replace(",",".")
altura = altura.replace(",",".")


peso = float(peso)
altura = float(altura)
pessoas_total = 1

peso_total = peso
altura_total = altura

peso_inicial = peso
altura_inicial = altura
cod_inicial = cod_cliente

peso_alto = peso_baixo = peso_gordo = peso_magro = peso_inicial

altura_alto = altura_baixo = altura_gordo = altura_magro = altura_inicial

cod_alto = cod_baixo = cod_gordo = cod_magro = cod_inicial

while(cod_cliente != 0):

    cod_cliente = float(input("Digite seu código:\nOu 0 para sair\n"))
    if(cod_cliente == 0):
        break

    peso = input('Digite seu peso:')
    altura =  input('Digite sua altura:')

    peso = peso.replace(",",".")
    altura = altura.replace(",",".")

    peso = float(peso)
    altura = float(altura)

    peso_total =+ peso
    altura_total =+ altura
    pessoas_total =+ 1
    if(peso > peso_gordo):
        peso_gordo = peso
        cod_gordo = cod_cliente
        altura_gordo = altura
    elif(peso < peso_magro):
        peso_magro = peso
        cod_magro =cod_cliente
        altura_magro = altura
    if(altura > altura_alto):
        altura_alto = altura
        cod_alto = cod_cliente
        peso_alto = peso
    elif(altura < altura_baixo):
        altura_baixo = altura
        cod_baixo= cod_cliente
        peso_baixo = peso




media_peso = peso_total/pessoas_total
media_altura = altura_total/pessoas_total

print(f"O {cod_alto} é o cliente mais alto.\nAltura:{altura_alto}\nPeso:{peso_alto}")
print(f"O {cod_baixo} é o cliente mais baixo.\nAltura:{altura_baixo}\nPeso:{peso_baixo}")
print(f"O {cod_gordo} é o cliente mais gordo.\nAltura:{altura_gordo}\nPeso:{peso_gordo}")
print(f"O {cod_magro} é o cliente mais magro.\nAltura:{altura_magro}\nPeso:{peso_magro}")
print(f'Média altura:{media_altura}\nMédia peso:{media_peso}')
