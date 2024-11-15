# Estudo Linguagem Python

Caderno de estudo referente à linguagem Python.

## Python Básico

**- Print:** Imprime o resultado de uma instrução (na tela, console).

- Podemos usar aspas simples ou duplas. 

```
print('Olá Mundo!')
```

**- Comentários:**  Pode ser usuário cerquilha (#) ou três aspas simples.

```
# Meu primeiro código..

'''
print('Olá')
'''
```

### Tipo de dados

O Python possui os seguintes tipos: str (string), int (integer), bool (booleano) e float (decimal).

**Modificando o tipo de dados**

- Int para float:<br> 
preco = float(preco)
- Float para int:<br>
preco = int(preco)
- numerico para string: <br>
preco = 10.50<br>
preco = str(preco)
- string para numerico: <br>
preco = int(preco)

Para verificar o tipo: <br>
print(type(str(10.10))) <br>
<class 'str'>

**- Variáveis:**

```
valor1 = 2
valor2 = 'Olá'

x = 2
print(x + x)
> 4
```

**- Imput:** Interação com usuário.

```
nome =  input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
idade = str(idade)
cidade = input('Onde você mora? ')

print('A ' + nome + ' tem ' + idade + ' anos de idade e mora na cidade de ' + cidade + '.')

> Qual é o seu nome? Viviani
> Qual é a sua idade? 40
> Onde você mora? Palhoça
> A Viviani tem 40 anos de idade e mora na cidade de Palhoça.
```
```
ano_nascimento = input('Em que ano você nasceu? ')
idade = 2024 - int(ano_nascimento)
print(idade)

> 40
```

**- Slice:** porção de string. Cada letra possui um index.

``` 
fruta = 'banana'

letra = fruta[1]
letra2 = fruta[2:3]
print(letra, letra2)
```

**- Formated Strings:** 

```
nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'Programador'

texto = f' O {nome} {sobrenome} é um excelente [{profissao}]'
print(texto)

>  O Marcos Silva é um excelente [Programador]
```
**- Métodos para Strings:** 

```
mensagem = 'Eu gosto de ir à praia e ir ao Cinema'
mensagem2 = ' Eu gosto de ir à praia e ir ao Cinema. '

print(mensagem.lower())
print(mensagem.capitalize())
print(mensagem.upper())
print(mensagem2.strip()) # tira espaços
print(mensagem.replace('Cinema' , 'Circo'))

> eu gosto de ir à praia e ir ao cinema
> Eu gosto de ir à praia e ir ao cinema
> EU GOSTO DE IR À PRAIA E IR AO CINEMA
> Eu gosto de ir à praia e ir ao Cinema.
> Eu gosto de ir à praia e ir ao Circo
```

## Operadores

**- Operações Matemáticas:** Existe uma ordem de execução de uma equação, conforme abaixo:

- Parenteses ( )
- Exponenciais **
- Multiplicação e Divisão
- Adição e Subtração

**- Operações de Comparação:** 
== (igual) != diferente > maior < menor >= maior igual <= menor igual

**- Operações de Atribuição:** += (mais igual) -= (menos igual) /= (divisão igual() *= (multiplicação igual) %= (resto)

## Controle de Fluxo

**- if, else, elif:** 

```
velocidade = 120

if velocidade < 110:
  print('Acima da velocidade permitida')
  print('Favor reduzir a sua velocidade')
else:
  print('Velocidade ok')

print('Fim')
```
**- Operadores Lógicos:** AND, OR

```
renda_acima_5mil = True
nome_limo = False

if renda_acima_5mil and nome_limo:
   print('Financiamento Aprovado')
else:
   print('Financiamento Negado')

>> Financiamento Negado

renda_acima_5mil = True
nome_limo = False

if renda_acima_5mil or nome_limo:
  print('Financiamento Aprovado')
else:
  print('Financiamento Negado')

>> Financiamento Aprovado
```

**- Múltiplos operadores de comparação:** usa-se and, or, <, >, etc..

```
valor = 10

if valor >= 20 and valor < 40:
  print('Produto foi aceito')
else:
  print('Produto não aceito')
```

**- For Loop - números:**

```
# imprimir de 1 a 5

for numero in range(1,6):
  print(numero)
```

**- For Loop - strings:**

```
palavra = 'Google'

for letra in palavra:
  print(f' {letra} esta dentro da palavra {palavra}')
```

**- For Loop - if e else:**

```
compra_confirmada = True
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range (3):
    if compra_confirmada:
      print(dados_compra)
      print('Detalhes enviados para o seu email')
      break
else:
  print('Falha na compra')
```

**- For Loop - Nested loops:** 

- Outer loop
  - Inner loop

```
for numero1 in range(1,6):
    print('Produto ' + str(numero1))
    for numero2 in range(5):
      print(numero1, numero2)

Produto 1
1 0
1 1
1 2
1 3
1 4
Produto 2
2 0
2 1
2 2
2 3
2 4
```
**- For Loop - Separando strings:** 

```
palavra = 'FANTASTICO'

for spaco in palavra:
  print(f' {spaco}' , end='')
  ```

**- While Loop:**  usado em loops dependentes de uma condição.

```
valor = 100
dia = 0

while valor > 20:
  dia += 1
  print(f' No dia {dia} o produto vai ser vendido por R${valor}')  
  valor -= 5
  ```

  **- Operador Ternário:** uma forma de economizar linhas de códigos.

  ```
  idade = 13

resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'

print(resultado)
```
### Diferenças entre if else, for loop e while loop
----

- _If e Else:_ Executa uma única vez, resultando verdadeiro ou falso.

- _For loop:_ Para variável gire N vezes.

- _While loop:_ Com condição, pois não sabe quantas vezes será executado, ou seja, se for isso ou aquilo gire N vezes.
----

### Funções

Function | Module | Pachage | Library |
---------| ------- | -------| ------- |
Item: maçã (cor, peso, valor) | sessão frutas (várias funções) | SUP A (grupo de módulos) | Hyper Market (biblioteca)

- Começa com palavra **def** (defined - definir)

Exempo: 

```
def boas_vindas():
  print('Olá Viviani')
  print('Temos 5 laptops em estoque')

boas_vindas ()
```

- **Variável global:** fica fora da função. Posso ter varáveis com mesmo nome em funções diferentes.

- **Parâmetro:**  são parâmetros da função, por exemplo: 

> def boas_vindas (nome, quantidade):

- **Argumento:** são os argumentos que serão chamados na função, por exemplo:

> boas_vindas ('Viviani', 18)

- **Argumentos Default e Non-Default:** 
    - Default:  Aquele que você define o valor no parâmetro.
    - Non-Default: Aquele que você não define o valor no parâmetro.

```
def boas_vindas(nome, quantidade=6):
  print('Olá {nome}.')
  print(f'Temos {str(quantidade)} laptops em estoque')

boas vindas ('Marcos')
```
Assim, no parâmetro **nome** é valor Non-Default e **quantidade=6** é valor default. E ao chamar a função não precisa incluir a quantidade. Obs.: No parâmetro, o valor padrão sempre no final.

- **Print ou Return em Funções:** O Print realiza uma tarefa (imprime na tela, sem armazenar), já o return, retorna e armazena o valor.

- **Vários argumentos xargs:** Os argumentos não são definidos. 

```
def soma (*numeros):
    reultado = 0 #iniciar num valor
    for num in numeros: #para num (2, por exemplo) em números, soma (faz loop) com resultado.
        resultado += num #soma = 0+2= 2+3= 5..
    return resultado

x = soma (2, 3, 4, 7)
print (x)
```

- **Vários argumentos xargs nomeando parâmetros:** Seria vários Argumentos (xargs) identificando o Parâmetro.

```
def agencia (**carro):
    return carro

print (agencia(marca='Gol', cor='Branca', motor=1.0))
```

Ou seja, para vários Argumentos usamos * e para para vários Parâmetros usamos **:

```
def soma (*numeros):
...
x = soma (2, 3, 4, 7)

def agencia (**carro):
...
print (agencia(marca='Gol', cor='Branca', motor=1.0))
```

## Estrutura de Dados

### Listas

Armazena mais de umas informação em variáveis.

> cidades = ['Rio de Janeiro', 'São Paulo'] - mantem a ordem dos dados (sequencia). <br>
> cidades[0] = 'Brasilia'  - muda o valor do index de Rio de Janeiro para Brasilia

#### Funções dentro de Lista

- cidades.append (´Santa Catarina') -  adiciona no final da lista
- cidades.remove (´Santa Catarina') -  remove da lista
- cidades.insert (1, ´Santa Catarina') - inserir conforme a posição
- cidades.pop (0) - retira da lista conforma posição.
- cidades.sort () - coloca a lista em ordem alfabética

#### Concatenando Listas

- uso função extend:

```
numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c']

final = numeros + letras
print(final)

> [2, 3, 4, 5, 'a', 'b', 'c']

ou:

numeros.extend(letras)
print(numeros)
```
- Lista e sublistas, como extrair itens conforme index

```
itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[0], [1])

> item2
```
#### Extrair variáveis de listas

```
produtos = {'arroz', 'feijão', 'laranja', 'banana', 1, 3}

item1, item2, item3, item4 = produtos

ou 
item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)

> arroz
> feijão
> laranja
> banana, 1, 3
```

#### Looping dentro de uma lista

```
valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f'O valor final do produto é de R${x}.')

> O valor final do produto é de R$50.
> O valor final do produto é de R$80.
> O valor final do produto é de R$110.
> O valor final do produto é de R$150.
> O valor final do produto é de R$170.    
```

#### Itens de uma lista

```
cor_cliente= input('Digite a cor desejada: ')
cores= ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
  print('Em estoque')
else:
  print('Não temos esta cor em estoque')

> Digite a cor desejada: Azul
> Em estoque
```
#### Agregando duas listas com Zip (junta duas lista)

```
cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

# var = list('comprar')
# print(var)

duas_listas = zip(cores, valores)
print (list(duas_listas))

> [('amarelo', 10), ('verde', 20), ('azul', 30), ('vermelho', 40)]
```

#### Input em uma lista

```
frutas_usuarios = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_usuarios.split(', ')
print(frutas_lista)

> Digite o nome das frutas separados por virgula: banana, maca
> ['banana', 'maca']
```
### Tuples

- Não podem ser alterados, usa parênteses. 

```
cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

> <class 'list'>
> <class 'tuple'>
```
### Arrays

- Usado quando a lista é muito grande e quando há problemas de performace. Precisa importar o módulo.

```
from array import array

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
numeros_i = [10, 20, 30, 40, 50, 60, 70, 80, 90]
numeros_f = [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
numeros_i = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
numeros_f = array('f', [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2])

print(letras)
print(numeros_i)
print(numeros_f)

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
[10, 20, 30, 40, 50, 60, 70, 80, 90]
[1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2]

> array('u', 'abcdefghi')
> array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
> array('f', [1.2000000476837158, 2.200000047683716, 3.200000047683716, 4.199999809265137, 5.199999809265137, 6.199999809265137, 7.199999809265137, 8.199999809265137, 9.199999809265137])

```
### Criando Sets

- Não usa index, similar a listas e evita duplicados. 
- É excelente para descobrir valores duplicados.

```
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1)

> {40, 10, 50, 20, 30}
```
- No exemplo acima, trouxe como resultado uma lista como set ({}) e não traz items repetidos e altera a ordem, pois perde o index.

```
print(num1 | num2) # union
> {70, 40, 10, 50, 20, 60, 30}

print(num1 - num2) # difference
> {40, 50, 30}

print(num1 ^ num2) # symmetric difference
> {70, 40, 50, 60, 30}

print(num1 & num2) # and
> {10, 20}

print(len(num1))
> 5
```
- É possível usar funcções ao set:

```
s1 = {1, 2, 3, 4, 5, 6}
s1.update([6, 7, 8, 9, 10])

print(s1)
> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - não traz 6 duas vezes.
```
### Dicionários

- Utiliza index no formato de key e value.
- Aceita string, int, bool, float.

```
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}
print(aluno)

> {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

print(aluno['nome'])
> Ana
```

#### Atualizando itens no dicionário

```
aluno.update({'endereco': 'Rua A'})
print(aluno['endereco'])

print(aluno.get('complemento', 'Valor não existe'))
> Valor não existe
```
#### Looping dentro do dicionário

```
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for x in aluno: # assim traz os keys
    print(x)

> nome
> idade
> nota_final
> aprovação

for x in aluno.values(): 
  print(x)

> Ana
> 16
> A
> True

for x in aluno.items(): # traz os dois
  print(x)

('nome', 'Ana')
('idade', 16)
('nota_final', 'A')
('aprovação', True)
```
#### Visualização itens, keys e values

```
aluno = {
  'nome': 'Ana', 
  'idade': 16, 
  'nota_final': 'A', 
  'aprovação': True,
  'Materias': ['Fisica', 'Matematica', 'Ingles']
}

print(aluno.items())
print(aluno.keys())
print(aluno.values())

> dict_items([('nome', 'Ana'), ('idade', 16), ('nota_final', 'A'), ('aprovação', True), ('Materias', ['Fisica', 'Matematica', 'Ingles'])])
> dict_keys(['nome', 'idade', 'nota_final', 'aprovação', 'Materias'])
> dict_values(['Ana', 16, 'A', True, ['Fisica', 'Matematica', 'Ingles']])
```

#### Função Lambda

- É uma função (pequena) sem nome.
- Pode ter vários argumentos, mas somente 1 expressão
- Muito utilizado dentro de outras funções
- Código mais 'clean'

```
# def somar(x):
#   return x + 10

# print(somar(2))

somar10 = lambda x: x + 10
print(somar10(2))
```
#### Lambda dentro de uma função

```
def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

print(somar(2))

> 48
```
#### Função Map numa lista

- Função que não precisa ser importada.
- Muito usado com lista, onde aplica uma função a um iterable, por item (list, tuple, dict).

```
lista1 = [1, 2, 3 ,4]

def muiti(x):
  return x * 2


lista2 = map(muiti, lista1)
print(list(lista2))

> [2, 4, 6, 8]
```
#### Função Map com Lambda

```

lista2 = map(lambda x: x * 2, lista1)
print(list(lista2))


```
#### Função filter

- Possui mesma funcionaliade do map, mas o resulta é filtrado.

```
valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(map(remover20, valores)))
> [False, False, True, True, True] 

print(list(filter(remover20, valores)))
> [34, 44, 57] # aqui já filtra os valores

print(list(filter(lambda x: x > 20, valores))) # com lambda
```
#### List Comprehension (string, números)

- Mia simples de se escrever. 
- Utilizado quando você precisa criar uma nova lista a partir de uma existente.
- expressao for iten in itens

```
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []

# for item in frutas1:
#     if 'b' in item:
#         frutas2.append(item)

frutas2 = [iten for iten in frutas1 if 'a' in iten]
print(frutas2)
```

```
#valores = []
#for x in range(6):
#   valores.append(x * 10)
#print(valores)    

valores = [x * 10 for x in range(6)]
print(valores)
```
#### Lista e Gerador Expressions

- Uma forma mais rápida para listas, dicionários, etc.
- Menos memória alocada
- Valores em bytes

```
from sys import getsizeof

numeros = [x * 10 for x in range(50)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print('====')

numeros = (x * 10 for x in range(50))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))

<class 'list'>
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490]
472
====
<class 'generator'>
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490]
208
```
## Erros

- Os erros são excelentes para testes. 
- Não realiza o 'stop' no prograna.
- Mensagens customizadas quando encontra um erro.

### Try e Except com uma Lista

```
try:  
  letras = ['a', 'b', 'c']
  print(letras[3]) # IndexError: list index out of range
except IndexError:
  print('Index não existe')

> Index não existe
```
### Try e Except com o imput

```
try:
  valor = int(input('Digite o valor de seu produto: '))
  print(valor)
except ValueError:
  print('Favor digitar um valor em números')

> Digite o valor de seu produto: gg
> Favor digitar um valor em números 

```

### Else (executa quando tiver erro) e Finally (sempre será executado)

```
try:
  valor = int(input('Digite o valor de seu produto: '))
  print(valor)
except ValueError:
  print('Favor digitar um valor em números')
 else:
  print('Usuário digitou um valor correto')
  resultado = valor * 2
  print(resultado)
  
> Digite o valor de seu produto: 12
> 12
> Usuário digitou um valor correto
> 24
```

```
try:
  valor = int(input('Digite o valor de seu produto: '))
  print(valor)
except ValueError:
  print('Favor digitar um valor em números')
finally:
  print('Código ok')
  
> Digite o valor de seu produto: 2
> 2
> Código ok


> Digite o valor de seu produto: hh
> Favor digitar um valor em números
> Código ok
```

## OOP - Orientado a objetos

### Classes

    - Utilizamos para criar Objetos (instances)
    - Objetos são partes dentro de uma Class (instancias)
    - Classe são utilizadas para agrupar dados e funções, podendo reutilizar

#### Exemplo:

Class: Frutas <br>
Objects: Abacate, Banana..


### Criando objetos dentro de uma classe

```
# criar a classe
class Funcionarios:
  pass

# criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criar os parametros do usuario1
usuario1.nome = 'Elena'
usuario1.sobreNome = 'Cabral'
usuario1.data_nascimento = '12/01/2009'

# criar os parametros do usuario2
usuario2.nome = 'Carol'
usuario2.sobreNome = 'Silva'
usuario2.data_nascimento = '15/10/2005'

# print
print(usuario1.nome)
```

### Criando Construtores

- Reduzir a passagem de paramentos.

Para iniciar um construtor é necessário definir conforme abaixo:

```
def __init__(argumentos) 
```

- No argumento é necessário incluir o self, o qual siginifica que será usado os objetos (usuario1 e usuario2, por exemplo).

```
# criar a classe
class Funcionarios:

  def __init__(self, nome, sobrenome, data_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.data_nascimento = data_nascimento    

# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')

# print
print(usuario1.nome)
print(usuario2.nome)
```

### Adicionando mais funções a classe

- Criado função nome_completo e para chamar a função usamos:

> print(Funcionarios.nome_completo(usuario1)) -> Classe -> Função -> Objeto

```
# criar a classe
class Funcionarios:

  def __init__(self, nome, sobrenome, data_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.data_nascimento = data_nascimento    

  def nome_completo(self):
      return self.nome + ' ' + self.sobrenome
    
# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')

# print
# print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
```
### Nova função, calcular idade

- Alterado data_nascimento para ano_nascimento. E foi importado o módulo datetime.

```
from datetime import datetime

# criar a classe
class Funcionarios:

  def __init__(self, nome, sobrenome, ano_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.ano_nascimento = ano_nascimento    

  def nome_completo(self):
      return self.nome + ' ' + self.sobrenome

  def idade_funcionario(self):
      ano_atual = datetime.now().year
      self.ano_nascimento = int(ano_atual - self.ano_nascimento)
      return self.ano_nascimento      
    
# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005)

# print
print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))
```

## Módulos (Arquivos)

- main.py: é o módulo/arquivo principal. Serve para chamar as demais funções.

### Importando um módulo

#### Diferença entre import e from

- Import: Importa tudo que existe no módulo. Isso consume muita memória. Para importar apenas algumas funções, usamos from.

> import funcoes

- From: Importa apenas a função desejada.

> from funcoes import somar

### Criando e importando Packages

```
O main.py somente enxerga os aqruivos estão no mesmo nível. Se tiver uma pasta (Package) é necessário criar um arquivo chamado __init__.py.

Neste caso, para importar ficaria:

from items.cadastro import cliente

- items (Package)
- cadastro (arquivo)
- cliente (funcao)
```
