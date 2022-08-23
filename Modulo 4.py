'''
Ex 3----
n1 = int (input('Digite um numero:'))
n2 = int (input('Digite outro numero:'))
soma = n1 +n2
# print('A soma e:', soma)
print('A soma entre {} e {} vale {}'.format(n1, n2 ,soma))
'''
'''
Ex 4
SEM FORMAT
dig = input('Digite qualquer coisa:')
print('O tipo primitivo deste valor e:', type(dig))
print('So tem espaços?', dig .isspace())
print('E numerico?', dig .isnumeric())
print('e alfabetico?', dig .isalpha())
print('E alfanumerico?', dig .isalnum())
print('Esta em maiuscula?', dig .isupper())
print('Esta em minuscula?', dig .islower())
print('Esta capitalizada?', dig .istitle())
--------------------------------------------
COM FORMAT
dig = input('Digite qualquer coisa:')
print('O tipo primitivo deste valor e', type(format(dig)))
print('So tem espaços? {}' .format(dig .isspace()))
print('E numerico? {}' .format(dig .isnumeric()))
print('e alfabetico? {}' .format(dig .isalpha()))
print('E alfanumerico? {}' .format(dig .isalnum()))
print('Esta em maiuscula? {}'.format(dig .isupper()))
print('Esta em minuscula? {}' .format(dig .islower()))
print('Esta capitalizada? {}' .format(dig .istitle()))
'''

