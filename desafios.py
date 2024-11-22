# desafio 01 - print

''' 
print('Olá, mundo Python!')
'''

# desafio 02 - variáveis

'''
nome = 'Viviani'
idade = 40
print(f'Olá, meu noem é {nome} e eu tenho {40} anos.')
'''

# desafio 03 - números

'''
num1 = 10
num2 = 3.5
print (type(num2))
resultado = num1 / num2
print(f'O resultado da divisão é: {resultado:.2f}')
'''

# desafio 04 - input

'''
nome = input('Qual é seu nome? ')
idade = int(input('Qual é sua idade? '))
print(f'Olá, {nome}! Você tem {idade} anos.')
'''

# desafio 05 - calculadora

'''
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
subtracao = num1 - num2
mult = num1 * num2
div = num1 / num2
expo = num1 ** num2

print(f'Os valor para soma é {soma}; para subtração: {subtracao}; multiplicação : {mult}; divisão : {div} e exponenciação: {expo:.2f}.')

'''

# desafio 06 - Lista

'''
frutas = ['maçã', 'banana', 'manga', 'uva']

print(frutas)
'''

# desafio 07 - modificando listas

'''
frutas = ['maçã', 'banana', 'manga', 'uva']

print(frutas[0])
print(frutas[-1])
'''

# desafio 08 - index de listas

'''
frutas = ['maçã', 'banana', 'manga', 'uva']

frutas[1] = ('morango')
frutas.append ('abacaxi') # append é um método
print(frutas)
'''

# desafio 09 - removendo itens da lista

'''
frutas = ['maçã', 'morango', 'manga', 'uva', 'abacaxi']

frutas.remove ('manga')
del frutas[-1]

print(frutas)
'''

# desafio 10 - listas com loops

'''
frutas = ['maçã', 'morango', 'uva']

for fruta in frutas:
    print(f'Eu gosto de {fruta}.')
'''

# desafio 11 - contando com for loop
# boas práticas usa-se variavel i de itens.

'''
for numeros in range(1, 11): #start, stop, step
    print(numeros)
'''

# desafio 12 - Nested for loop

'''
frutas = ['maçã', 'banana', 'manga']
verduras = ['batata', 'tomate', 'cebola']

for fruta in frutas:    
    for verdura in verduras:
      print(fruta, verdura)
'''

# desafio 13 - while loop

'''
numero = 1

while numero <= 10:
  print(numero) 
  numero += 1
'''

# desafio 14 - loop com break e continue

'''
print('loop com o break: ')
for numeros in range(1, 11):
    if int(numeros) >= 6:
        break            
    print(numeros)

print('\nloop com o continue:')
for numeros in range(1, 11):
    if int(numeros) == 5:
        continue
    print(numeros)
'''    

# desafio 15  - contador lista

'''
frutas = ['maçã', 'maçã', 'banana', 'manga', 'maçã']
contador = 0

for fruta in frutas:
    if fruta == 'maçã':
        contador +=1
print('Numero de maças na lista: ', contador)
'''

# desafio 16  - verif. numeros com if else

'''
numero = int(input('Digite um numero: '))

if numero > 10:
    print('O número é maior que 10')
else:
    print('O número é menor ou igual a 10')
'''

# desafio 17 - verif. de idade

'''
idade = int(input('Digite a sua idade: '))

if idade < 13:
    print('Você é uma criança.')
elif idade >= 13 and idade < 20:
    print('Você é um adolescente.')
else:
    print('Você é um adulto.')
'''

# desafio 18 - Procura em Listas

'''
pesquisa_carro = input ('Insira o nome do carro que deseja comprar: ')
estoque = ['BMW X6', 'BMW I5', 'BMW I8']

if pesquisa_carro in estoque:
  print('Em estoque')
else:
  print('Não temos este carro em estoque')
'''

# desafio 19 - Encontrando um item com while

'''
fruta_usuario = input ('Insira o nome de uma fruta: ')

while True:
    fruta_usuario = input ('Insira o nome de uma fruta: ')
    if fruta_usuario == 'abacate':
        print('Parabens você acertou a fruta!')
    break
    '''  

# desafio 20 - par e impar (usa-se módulo (%) para verificar o resto da divisão)

'''
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

for i in numeros:
    if i % 2 == 0:
        print(f'O número {i} é par!')
    else:
        print(f'O número {i} é impar!')
        '''        

# desafio 21 - Lista de Cidades (Tuple)

'''
cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador')
pesquisa_cidade= input('Digite o nome de uma cidade: ')

if pesquisa_cidade in cidades:
  print('A cidade está na lista de cidades.')
else:
  print('A cidade não está na lista de cidades')
  '''

# desafio 22 - Pesquisa de País e Capital (dicionário)

'''
capitais = {
    'Brasil': 'Brasilia',
    'Peru': 'Lima',
    'Argentina': 'Buenos Aires', 
    'França' : 'Paris',
    'Espanha' : 'Madrid'
}

pais_usuario = input('Digite o nome de um país: ')

if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')
    '''
# desafio 23 - comparação em Sets

'''
amigos1 = {'Andreza', 'Andreia', 'Luana', 'Grazi', 'Vini'}
amigos2 = {'Grazi','Andreza', 'Maria', 'Luana', 'Elo'}

resultado = amigos1.intersection(amigos2) #retorna os valores repetidos nos 2 conjuntos
#resultado = amigos1.union(amigos2) #junta os 2 conjuntos
#resultado = amigos1.difference(amigos2) #mostra os que não são repetidos nos 2 conjuntos
print(resultado)
'''

# desafio 24 - Funções simples

'''
def quadrado(numero):
    return numero ** 2

num = int(input('Digite um número: '))
print(f'O resultado do quadrado do número {num} é {quadrado(num)}')
'''

# desafio 25 - Soma com funções

'''
def soma(a, b):
    return a + b

user_a = int(input('Digite o primeiro número: '))
user_b = int(input('Digite o segundo número: '))
print(f'A soma entre os números {user_a} e {user_b} resulta: {soma(user_a, user_b)}')
'''

# desafio 26 - calculando base e exponente

'''
def potencia(base, exponente=2):
    return base ** exponente

user_base = int(input('Digite a base para calculo da potência: '))
user_expo = input('Digite o exponente para calculo da potência (padrão 2): ')

if user_expo :
    print(f'O resultado é: {potencia(user_base, int(user_expo))}')
else:
    print(f'O resultado é: {potencia(user_base)}')
    '''

# desafio 27 - calculando fatorial

'''
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n -1)
user_mumber = int(input('Digite um número: '))
print(f'O fatorial de {user_mumber} é: {fatorial(user_mumber)}')
'''

# desafio 28 - Duas funções, chamar uma função dentro de outra.

'''
def dobro(num):
    return num * 2

def quadrado(num):
    return dobro(num) ** 2

user_number = int(input('Digite um número: '))
print(f'O dobro de {user_number} é: {dobro(user_number)} e o quadrado do dobro é: {quadrado(user_number)}')
'''

# desafio 29 - convertendo para lambda

'''
cubo = lambda x: x ** 3
user_number = int(input('Digite um número: '))
print(f'O cubo do número {user_number} é: {cubo(user_number)}')
'''

# desafio 30 - lambda multiplicando

'''
multi = lambda x, y: x * y
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(f'O resultado da multiplicação é: {multi(num1, num2)}')
'''

# desafio 31 - lambda com IF ELSE

'''
num_par_impar = lambda x: "Par" if x % 2 == 0 else "Ímpar"

user_number = int(input('Digite um número: '))
print(f'O número {user_number} é: {num_par_impar(user_number)}')

'''

# desafio 32 - lambda com for loop

'''
numeros = [1, 2, 3, 4, 5, 6]

list_quadrado = lambda num: (numeros ** 2 for numeros in num)

user_number = int(input('Digite um número: '))
print(f'O quadrado de todos os números da lista {numeros} é: {list(list_quadrado(numeros))}')
'''