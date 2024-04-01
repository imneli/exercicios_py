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




