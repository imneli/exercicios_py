# salario = int(input("Diga seu salario \n->"))

# if salario < 1903.98:
#     aliquota = 0
#     desconto = aliquota * salario
#     salario = salario - desconto
#     print(f"O desconto foi de {desconto} e seu salario será \n-> {salario}")
    
# if salario > 1903.98 and salario <= 2826.66:
#     aliquota = 0.075
#     desconto = aliquota * salario
#     salario = salario - desconto
#     print(f"O desconto foi de {desconto} e seu salario será \n-> {salario}")

# if salario > 2826.66 and salario <= 3751.05:
#     aliquota = 0.15
#     desconto = aliquota * salario
#     salario = salario - desconto
#     print(f"O desconto foi de {desconto} e seu salario será \n-> {salario}")

# if salario > 3751.05 and salario <= 4664.68:
#     aliquota = 0.225
#     desconto = aliquota * salario
#     salario = salario - desconto
#     print(f"O desconto foi de {desconto} e seu salario será \n-> {salario}")

# if salario > 4664.68:
#     aliquota = 0.275
#     desconto = aliquota * salario
#     salario = salario - desconto
#     print(f"O desconto foi de {desconto} e seu salario será \n-> {salario}")


# def salarys(salary):
#     descount = salary * aliquota
#     res = print(f"O descount foi de {descount} e seu salary será \n-> {salary}")

#     if salary < 1903.98: 
#         aliquota = 0
#         return res
#     sal = int(input("input your salary \n->"))
#     if salary <= 1903.98: 
#         aliquota = 0.075
#         return res
#     if salary >= 3751.05: 
#         aliquota = 0.255
#         return res
#     if salary > 4664.68: 
#         aliquota = 0.275
#         return res
# salarys(2700)


# def valores(valor1, valor2):
#     if valor1 > valor2:
#         print(f"o maior é o {valor1}")
#     else:
#         print(f"o maior é o {valor2}")
# valores(2, 5)

# 123

# def password():
#     while True: 
#         senha = int(input("digite sua senha \n->"))
#         if senha == 1234:
#             print("ok pode ir papito")
#             break
#         else: 
#             print("errou. tenta denovo")
# password()

print("é ouro vadia.")


    

# a = int(input("digite um numero: "))
# b = int(input("digite um numero: "))
# c = int(input("digite um numero: "))

# if a > b and a > c: 
#     aux = a
#     a = c
#     c = aux

# elif b > c: 
#     aux = b
#     b = c
#     c = aux

# if a > b:
#     aux = a
#     a = b
#     b = aux
# print(a,b,c)

# i = 0
# pares = 0

# while i < 10:
#     num = int(input(f"{i+1} | Digite um numero.."))
#     if num % 2 == 0:
#         pares  += 1
#     else: 
#         pares += 1
# print(f"vc digitou {pares} pares\nvc digitou {i - pares} impares")

senha = '1234'

while senha != password:
    password = input("input your pass")
    if senha != password:
        print("senha incorreta")
        password = input("input your pass")
    else:
        print("acesso liberado")





        
    
    
    


    
