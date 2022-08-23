'''
-------------------------
Ex 5
-------------------------
n1 = int (input('Um valor:'))
n2 = int (input('Outro valor:'))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
exp = n1 ** n2

print('A soma entre e {}, a subtração e {}, o produto e {}'.format(soma, sub, mult), end=' ')
print('A divisão e {:.3f}, a divisão inteira e {} e a exponenciação e {}'.format( div, divInt, exp))
'''

'''
-------------------------
EX 6 antecessor e sucessor
-------------------------
n1 = int (input('Digite um numero:'))
ant = n1 - 1
dps = n1 + 1
print('Antecessor | Numero | Sucessor \n')
print('{:=^11}|{:=^8}|{:=^9}' .format(ant,n1,dps))
ou -----USa apenas uma variavel fazendo format(n, (n-1), (n+1))
'''
'''
-------------------------
Ex 7 dobro trilo e raiz
-------------------------
from math import sqrt
n1 = float (input('Digite um numero:'))
db = n1 * 2
tp = n1 * 3
raiz = sqrt(n1)
print('O dobro e {}, o triplo e {} e a raiz quadrada e {:.3f}' .format(db, tp, raiz))
'''

'''
-------------------------
EX 8 media aluno
-------------------------
n1 = float (input('Digite a nota 1:'))
n2 = float (input('Digite a nota 2:'))
media = (n1+n2) / 2
print('A media do aluno e: {}' .format(media))
'''

'''
-------------------------
EX 9 metros em centimetros e milimetros
-------------------------

n1 = float(input('Digite um valor em metros:'))
cent = n1 * 100
mil =  cent * 10
print('A medida digitada equivale a {} centimetros e {} milimetros' .format(cent, mil))
'''
'''
-------------------------
EX 10 reais em dolares
-------------------------

n1 = float(input('Digite quantos voce tem na carteira:'))
vlr = n1 / 3.27
print('Voce pode comprar {:.2f} dolares' .format(vlr))
'''

'''
-------------------------
EX 11 Litros de tinta
-------------------------
larg = float(input('Qual a largura da parede:'))
alt = float(input('Qual a altura da parede:'))
area = larg * alt
tinta = area / 2
print('A parede tem area {} Metros quadrados.\n' .format(area))
print('Sera necessario {} litros de tinta' .format(tinta))
'''

'''
-------------------------
EX 12 5 por cento de desconto
-------------------------
n1 = float(input('Qual o preço do produto?'))
novo = n1 - (n1 * 5)/100
print('O produto com 5 por cento de desconto e: {}' .format(novo))
'''

'''
-------------------------
EX 13 15 por cento de aumento
-------------------------
n1 = float(input('Digite o salario atual:'))
novo = (n1 * 15)/100
salf = novo + n1
print('Salario antigo:{}' .format(n1))
print('Salario novo(15 por cento de aumento):{}' .format(salf))
'''





