# Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

Funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

func1 = set(Funcionarios)
func2 = set(turno_dia)
func3 = set(turno_noite)
func4 = set(tem_carro)

# Funcionários que tem carro e trabalham a noite
print(func4 & func3)

# Funcionários que tem carro e trabalham durante o dia
print(func4 & func2)

# Funcionários que não tem carro
print(func4 ^ func1)