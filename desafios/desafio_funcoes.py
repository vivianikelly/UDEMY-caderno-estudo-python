# Desafio com funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura. O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'

precisa input do usuário: rendimento, altura e largura
Qual é o rendimento da lata?
Qual é a altura da parede?
Qual é a largura da parede?
'''

rendimento = float(input('Qual é o rendimento da lata? '))
altura =  float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))

def calcula_rendimento():
    area = altura * largura / rendimento
    print(f'Você necessita de {area} latas de tinta.')

calcula_rendimento()