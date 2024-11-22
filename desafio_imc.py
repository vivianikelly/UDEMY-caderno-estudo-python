# Calculo de IMC - índice de Massa Corporal

'''
Qual é a sua altura em cm:
Qual é seu peso em kg:

- MENOR QUE 18,5 - MAGREZA
- ENTRE 18,5 E 24,9 - NORMAL
- ENTRE 25,0 E 29,9 SOBREPESO
- ENTRE 30,0 E 39,9 - OBESIDADE
- MAIOR QUE 40,0 - OBESIDADE GRAvE
'''

peso = float(input('Qual é seu peso em kg: '))
altura = float(input('Qual é a sua altura em cm: '))

imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu imc é: {imc: .2f} - MAGREZA.')
elif imc >= 18.5 and imc < 24.9:
    print(f'Seu imc é: {imc: .2f} - NORMAL.')
elif imc >= 25.0  and imc < 29.9:
    print(f'Seu imc é: {imc: .2f} - SOBREPESO.')
elif imc >= 30.0  and imc < 39.9:
    print(f'Seu imc é: {imc: .2f} - OBESIDADE.')
else:
    print(f'Seu imc é: {imc: .2f} - OBESIDADE GRAvE.')