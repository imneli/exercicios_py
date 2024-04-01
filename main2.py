# print("Seja bem vindo a vinharia Agnello!")
# ano = int(input("Diga sua data de nascimento: "))
# idade = 2024 - ano
# if idade < 18:
#     print("Não pode acessar a pagina.")
# else:
#     vinho1 = 'Vinho Tinto'
#     vinho2 = 'Vinho Branco'
#     vinho3 = 'Vinho Rosé'
#     preco1 = 10
#     preco2 = 20
#     preco3 = 30
#     frete = 10
#     endereco = input("Digite seu endereço: ")
#     print(f"Nossas opções de vinho são: \n{vinho1}: R${preco1}.00"
#           f"\n{vinho2}: R${preco2}.00 \n{vinho3}: R${preco3}.00")
#     opcao = input("Qual vinho você se interessou?")
#     if opcao == vinho1:
#         preco = preco1
#     elif opcao == vinho2:
#         preco = preco2
#     else: 
#         preco = preco3
#     qtd = int(input(f"Diga a quantidade de garrafas de {opcao}: "))
#     valor = qtd*preco
#     if valor >=100:
#         print("Frete grátis")
#     else:
#         valor += frete
#     print(f"Obrigado por realizar sua compra conosco"
#           f"\n Você comprou {qtd} garrafas de vinho | {opcao}"
#           f"\n Entregue no endereço: {endereco}")

# Correção prova


# exercicios

'''senha_cadastrada = '1234'
senha_tentativa = input("Digite sua senha: ")
tentativas = 1
while senha_cadastrada != senha_tentativa and tentativas < 3:
    print(f"Senha incorreta. Você tem mais {3 - tentativas} tentativas")
    senha_tentativa = input("Digite sua senha: ")
    tentativas += 1
if senha_tentativa == senha_cadastrada:
    print("Acesso Liberado")
else: 
    print("Acesso Negado. Você não possui mais tentativas")'''

'''i = 0
soma = 0
while i<100:
    i+=1
    soma += i
    print(f"i: {i}, soma: {soma}")'''

'''vinho1 = 'Vinho Tinto'
vinho2 = 'Vinho Branco'
vinho3 = 'Vinho Rosé'
print(f"Nossas opções de vinho são: \n {vinho1} \n {vinho2} \n {vinho3}")
opcao = input("Por qual vinho você se interessou? ")
while not (opcao == vinho1 or opcao == vinho2 or opcao == vinho3):
    print("Opção Invalida.")
    print(f"Nossas opções de vinho são: \n {vinho1} \n {vinho2} \n {vinho3}")
    opcao = input("Por qual vinho você se interessou") '''


# senha_cadastrada = '1234'
# senha_tentativa = int(input('Digite sua senha: '))
# while not senha_tentativa.isnumeric(): 
#     senha_tentativa = 'Digite uma senha numérica: '


#exercicio 1

'''nota = int(input("Digite sua nota: "))
while nota > 10:
    print("Nota Invalida")
    nota = input("Digite sua nota: ")
print("Nota Valida")'''

#exercicio 2

'''nome = input("Digite seu nome: ")
while len(nome) < 3:
    print("Nome invalido")
    nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
while idade > 150:
    print("Idade Invalida")
    idade = int(input("Digite sua idade: "))
salario = int(input("Digite seu salario: "))
while salario < 0:
    print("Salario invalido")
    salario = int(input("Digite seu salario: "))
sexo = input("Digite seu sexo: \n (M) | Masculino \n (F) | Feminino \n Sexo: ")
while sexo != 'F' and sexo != 'M':
    print("Sexo Invalido")
    sexo = input("Digite seu sexo: \n (M) | Masculino \n (F) | Feminino \n Sexo: ")

estado_civil = input("Digite seu Estado Civil: \n (S) | Solteiro"
                     "\n (C) | Casado \n (V) | Viuvo(a) \n (D) | Divorciado")
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = input("Digite um Estado Civil válido: \n (S) | Solteiro"
                     "\n (C) | Casado \n (V) | Viuvo(a) \n (D) | Divorciado")'''

#exercicio 3

'''populacao_pais_A = 80000
populacao_pais_B = 200000
anos = 0
while populacao_pais_A < populacao_pais_B:
    populacao_pais_A += populacao_pais_A * 0.03
    populacao_pais_B += populacao_pais_B * 0.015
    anos += 1
print(f"Foram {anos} anos")'''

#exercicio 4

'''i = 0
soma = 0
while i<5:
    i+=1
    num = int(input("Digite um numero:" ))
    soma += num
print(f"i: {num}, soma: {soma}, med: {soma/5}")'''

#exercicio 5

'''num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    vn2 = num2
    num2 = num1
    num1 = vn2
i = num1
while i < num2:
    i += 1
    print(i)'''

#exercicio 6

'''user = input("Digite seu usuario: ")
senha_cadastrar = input("Digite sua senha: ")
tentativas = 1
while user == senha_cadastrar and tentativas < 3:
    print(f"Você não pode ter a senha igual ao User. Você tem mais {3 - tentativas} tentativas para criar uma senha")
    user = input("Digite seu usuario: ")
    senha_cadastrar = input("Digite sua senha: ")
    tentativas += 1
if user != senha_cadastrar:
    print("Senha Cadastrada, pode logar.")
else:
    print(f"Você não pode ter a senha igual ao User. Você não tem mais tentativas")'''

#exercicio 7


'''num = int(input("Digite um numero entre 1 e 10: " ))
print(f"Tabuada do {num}")
i = 1
mult = 0
while i<11:
    print(f"Tabuada do {num} x {i} = {num*i}")
    i +=1'''

#exercicio 8

'''num = int(input("Digite um numero: "))
i = 1
numero = 1'''

#exercicio 9

# faça um programa que peça 10 numeros inteiros, calcule e peça a quantidade de numeros impares e pares

'''rep = 0
pares = 0
while rep < 10:
    num = int(input("Digite um número: "))
    if (num % 2) == 0:
        pares += 1
    rep += 1
impares = 10 - pares
print(f"tem {pares} numeros pares e {impares} numeros impares")'''

#exercicio 10

'''num = int(input("Digite um número: "))
i = 1
fat = i
while i < num:
    i += 1
    fat = fat * fat * i
print(f"o numero fatorial {num} é {fat}")
'''

#exercicio 11

'''num = int(input("Digite um número"))'''


#exercicio 12

'''tentativas = 0
soma = 0
while tentativas < 5:
    notas = int(input("Digite uma nota: "))
    tentativas += 1
    soma += notas
media = soma/tentativas
print(f"A média de notas é: {media}")'''

#exercicio 13

anos = 0
salario_inicial = 1000
aumento_inicial = 0.015


anos = int(input("Digite quantos anos se passaram a partir de 1995: "))
anos += 0
ano_atual = 1995 + anos
aumento_anual = 0.015 * 2 * anos
print(f"O ano é {ano_atual} e a pessoa ganha {salario_inicial + salario_inicial * aumento_anual}")
# print(f"1996 - aumento de {salario_inicial} para {salario_inicial + salario_inicial * aumento_inicial}")
# print(f"1997 - aumento de {salario_inicial} para {salario_inicial + salario_inicial * aumento_anual}")










