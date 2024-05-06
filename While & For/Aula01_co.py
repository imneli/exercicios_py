'''nota = int(input("Diga uma nota: "))
while nota < 0 or nota > 10: 
    print("Nota invalida")
    nota = int(input("Diga uma nota: "))'''


#correção exercicio 1 

'''while True: 
    nota = input("Diga uma nota: ")
    if nota.isnumeric():
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            break
        print("Nota Invalida.")'''

#correcao exercicio 2

'''nome = input("Digite seu nome: ")
while len(nome) < 3:
    nome = input("Digite seu nome: ")
while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade >= 0 and idade <= 150:
            break
        print("Idade Invalida.")

while True:
    sexo = input("Digite seu sexo f/m: ")
    if sexo != 'f' and sexo != 'm': #not sexo == 'f' or sexo == 'm'
        break
    print("Sexo invalido")

while True:
    salario = int(input("Digite seu salario: "))
    if salario.isnumeric():
        salario = int(salario) 
        if salario > 0: 
            break
        print("salario invalido!")

est_civil = input("Digite seu estado civil \n s, c, v ou d: ")
while est_civil != 's' and est_civil != 'c' and \
        est_civil != 'v' and est_civil != 'd':
    print("Resposta invalido")
    est_civil = input("Digite seu estado civil \n s, c, v ou d: ")
print("foguete nao tem ré pai ai calica")'''

#correcao exercicio 3

# 80.1.03 + 3% 80*1.03 -> 80*1.03(1+0.03)
# m -> 80*1.03m | b = 200*1.015m
# a = b
# 1.03*80m = 200*1.015m
# (1.03/1.015)m = 200/80
# mlog(1.03/1.015) = log(2.5)
# m = log(2.5)/log(1.03/1.05)

'''a = 80 #população
b = 200 #população
anos = 0
while a < b:
    a*= 1.03
    b *= 1.015
    anos += 1
print(anos)'''

#correcao exercicio 4

'''qtd = 0
soma = 0
while qtd < 5:
    num = input(f"Diga o {qtd+1}o número: ")
    if not num.isnumeric():
        print("Digite um numero")
        continue
    num = int(num)
    soma += num
    qtd += 1
print(f"A soma dos numeros que voce digitou é {soma} e a média é "
      f"{soma/qtd}")'''

#correcao exercicio 5

'''n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

while n1 < n2:
    print(n1)
    n1 += 1

while n2 < n1:
    print(n2)
    n2 += 1'''

#exercicio 14

'''intervalo25 = 0
intervalo50 = 0
intervalo75 = 0
intervalo100 = 0
while True:
    numero = float(input('Digite um número positivo entre 1 - 100: '))
    if 0 <= numero <= 25:
        intervalo25 += 1
    elif 26 <= numero <= 50:
        intervalo50 += 1
    elif 51 <= numero <= 75:
        intervalo75 += 1
    elif 76 <= numero <= 100:
        intervalo100 += 1
    elif numero < 0:
        break
    else:
        print('Número grande demais!')
print(f'Segue abaixo a quantidade de números em cada seguinte intervalo:'
      f'\n[0-25]: {intervalo25}'
      f'\n[26-50]: {intervalo50}'
      f'\n[51-75]: {intervalo75}'
      f'\n[76-100]: {intervalo100}')'''
 
 #exercicio 15

'''pop = int(input("Qual é a populaçao? "))
i = 0
joao = 0
jose = 0
henrique = 0
matheus = 0
nulo = 0
branco = 0
while i < pop:
    voto = int(input("Você vai votar em quem? "))
    if voto == 1:
        joao +=1
    elif voto == 2:
        jose +=1
    elif voto == 3:
        henrique +=1
    elif voto == 4:
        matheus +=1
    elif voto == 5:
        nulo +=1
    elif voto == 6:
        branco +=1
    i +=1
print(f"{joao} votaram no joao, {jose} votaram no jose, {henrique} votaram no henrique, {matheus} votaram no matheus, {nulo} votaram nulo e {branco} votaram em branco")
conta = (nulo / pop) + 1
print(f"{conta}% dos votos foram nulo")
conta2 = (branco / pop) + 1
print(f"{conta2}% dos votos foram brancos")
'''

#exercicio 8

'''qtd = int(input("Diga quantos numeros de fibonacci quer ver: "))
a = 1
b = 1
i = 2
print(a)
print(b)
while i < qtd: 
    c = a + b
    print(c)
    a = b
    b = c
    i += 1'''

#exercicio num 9

'''qtd = 0
par = 0
while qtd < 10:
    num = int(input(f"Digite o {qtd+1} seu numero: "))
    if num % 2 == 0:
        par +=1
    qtd +=1
print(f"Vc digitou {par} pares e {qtd - par} impares")'''



