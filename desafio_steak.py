# Desafio com if, elif, else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues. O usuário deverá fornecer a temperatura.

Temperaura - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)

Criar prompts para o usuário: Qual a temperatura da carne?
Para temperatura menos que 48ºC - Cozinhar por mais alguns minutos
Para temperatura acima de 71ºC - Carne bem passada, reduz a temperatura
'''
temperatura = int(input('Qual a temperatura da carne? '))
#temperatura = int(temperatura)    
    
if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura >= 48 and temperatura <= 53:
    print('Selada')
elif temperatura >= 54 and temperatura <= 59:
    print('Ao ponto para o mal')
elif temperatura >= 60 and temperatura <= 64:
    print('Ao ponto')
elif temperatura >= 65 and temperatura <= 70:
    print('Ao ponto para o bem')
elif temperatura == 71:    
    print('Bem passada')
else:    
    print('Bem passada, reduz a temperatura')