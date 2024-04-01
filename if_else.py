#exercicio 1 - poligonos

lados = int(input("Diga o numero de lados: "))
if lados < 3:
    print("não é um poligono")
elif lados > 5:
    print("Poligono não identificado")
else:
    if lados == 3:
        forma = 'triangulo'
    elif lados == 4:
        forma = 'quadrado'
    else:
        forma = 'pentagono'
    medida = int(input("Qual a medida do lado?"))
    perimetro = lados*medida
    print(f"O poligono é um {forma} com perimetro de {perimetro}")

# exercicio 2 - verificar impar e par

#sem while (ruim) 

n1 = int(input("1 | Digite um numero: "))
n2 = int(input("2 | Digite um numero: "))
n3 = int(input("3 | Digite um numero: "))
n4 = int(input("4 | Digite um numero: "))
n5 = int(input("5 | Digite um numero: "))
pares = 0
impares = 0
if n1%2 == 0:
    pares = pares +1
else:
    impares += 1
if n2%2 == 0:
    pares = pares +1
else:
    impares += 1
if n3%2 == 0:
    pares = pares +1
else:
    impares += 1
if n4%2 == 0:
    pares = pares +1
else:
    impares += 1
if n5%2 == 0:
   pares = pares +1
else:
    impares += 1
print(f"O numero de pares foi {pares} e o numero de impares foi {impares}")

# com while

rep = 0
pares = 0
while rep < 5: # se n informar < 5 n vai parar nunca, só vai repetir pq vai continuar true
    num = int(input("Diga um numero: "))
    if num%2==0: #verificar se é par
        pares += 1
    rep = rep + 1
impares = 5 - pares
print(f"O numero de pares foi {pares} e o de impares foi {impares}")

# pedir senha até acertar

senha = int(input("Digite uma senha: "))
while senha != 1234:
    print('Senha incorreta.')
    senha = int(input("Digite uma senha: "))
print("senha correta.")

#exercicio senha teste

tentativa = 0
senha = int(input("Digite uma senha: "))
while senha != 1234 and tentativa < 2:
    print('Senha incorreta.')
    senha = int(input("Digite uma senha: "))
    tentativa += 1
if senha == 1234:
    print("senha correta.")  
else:
    print("senha incorreta")                                                                                                        

#pedir 10 numeros e somar todos

qt_num = 0
soma = 0
while qt_num < 10:
    num = int(input("Digite um numero: "))
    qt_num += 1
    soma += num
print(f"A soma dos valores é {soma}")

#calcular 10 numeros

qt_num = 0
i = 1
while qt_num < 10:
    num = int(input("Digite um numero: "))
    qt_num += 1
    i *= num
print(f"A soma dos valores é {i}")

'''qt_num = 0
i = 1
while qt_num < 10:
    num = int(input("Digite um numero: "))
    qt_num += 1
    i *= num
print(f"A soma dos valores é {i}")'''

i = 0
soma = 0
while i < 10:
    i += 1
    soma += num
print(f"A soma dos valores é {soma}")

#somar 10 numeros sem input

i = 11
soma = 0
while i > 0:
    i -= 1
    soma += i
    print(soma)

#palavras

i = 0
frase = ''
while i < 10:
    pal = input("Digite uma palavra: ")
    i += 1
    frase += pal
    print(frase)















    