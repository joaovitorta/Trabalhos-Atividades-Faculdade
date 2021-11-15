#Programa para fazer um figura geometrica de acordo com o pedido do usuario
import turtle
t = turtle.Turtle()

#Defino uma função para desenhar o poligono
def desenhar_poligono(tamanho_lado, angulos, cor):
    t.color(cor)
    t.forward(tamanho_lado)
    t.left(angulos)
   

# Entrada de dados: Tamanho do lado, quantos lados tera e quantas vezes ira repetir
tamanho_lado = int(input('Qual o tamanho de cada lado dos lados da figura? ')) 
qtd_lados = int(input('Quantos lados a figura vai ter? '))
qtd_vezes = int(input('Quantas vezes?'))

#Processamento dos dados para desenhar o figura segundos as regras da geometria
angulo_max = (qtd_lados - 2) * 180
angulos = 360 / qtd_lados

#Escolha da cor
escolha_cor = int(input('Escolha uma cor:\n(0)Verde (1) Vermelho (2) Azul\n(3) Laranja (4) Roxo (5) yellow\n'))
cores = ['green', 'red', 'blue', 'orange', 'purble', 'yellow']
cor = cores[escolha_cor]

#O poligono sendo feito
for vezes in range(qtd_vezes):
    tamanho_lado += 10
    for i in range(qtd_lados):
        desenhar_poligono(tamanho_lado, angulos, cor)
        
