#Programa para calcular a área de uma parede

#Entrada dos dados (Largura e altura)
altura = input("Digite a altura da parede:\n")
largura = input("Digite a largura da parede:\n")

#Troca de "," por "." caso o usúario não use as normas americanas
altura = float(altura.replace(",","."))
largura = float(largura.replace(",","."))


#Calculo da área da parede
area = altura * largura

#Saída dos dados (Área, altura e largura)
print(f"A área de uma parede com {altura} M de altura e {largura} M de largura é de:\n {area:.2f} M²")
