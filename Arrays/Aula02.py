# -> Identificar produto que tem o preço maior
# -> Inverter listas
# -> Funções
# -> Par ou impar
# -> Vogal ou não


def exemplo_carros():

    carros = ['Up', 'Gol', 'Celtinha', 'Kombi', 'Uno'] #vai cair no cp
    preco = [130,220,12000,1225,1235]
    maior = preco[0]
    indice_maior = 0
    maior = preco[indice_maior]
    for i in range(len(preco)):
        print(f"Vou testar se {preco[i]} > {maior}")
        if preco[i] > maior:
            print(f"Deu certo, então vou trocar {maior} por {preco[i]}")
            maior = preco[i]
            indice_maior = i

    print(f"\n-> {carros[indice_maior]}", f"\n-> R$ {preco[indice_maior]:.2f}")


def ultimo_elemento():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]                        
    ultimo = len(lista) - 1
    print(f"Lista Inicial -> {lista}\n")
    for i in range(len(lista) // 2):
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
        i += 1
    print(f"Lista Invertida -> {lista}")

    # i = 0
    # aux = lista[i]
    # lista[i] = lista[ultimo - i]
    # lista[ultimo - i] = aux
    # i += 1
    # print(lista)
    # aux = lista[1]
    # lista[i] = lista[ultimo - i]
    # lista[ultimo - i] = aux
    # print(lista)


def printar_oi(frase):
    print(frase)

    return


def verificar_par(num):
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
    return


def vogal_ou_nao(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if letra in vogais:
        print(f"{letra} é uma vogal")
    else:
        print(f"{letra} é consoante")
    return

def somar_lista(lista):
    soma = 0
    for i in range (len(lista)):
        soma += lista[i]
    print(f"A soma é {soma}")
    return



def media_lista(lista):
    soma = 0
    for i in range (len(lista)):
        soma += lista[i]
        div = soma / len(lista)
    print(f"A soma é {soma}")
    print(f"A média é {div}")
    return




def contar_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogal = 0
    for i in range (len(string)):
        if string[i] in vogais:
            vogal += 1
    print(f"A quantidade de vogais em {string} é {vogal}")


def verificar_par_lista(lista):
    for i in range (len(lista)):
        if lista[i] % 2 == 0:
            print(f"O número {lista[i]} : é par")
    return

def verifica_vinhos(msg):

    lista_vinhos = ['Vinho1','Vinho2','Vinho3']
    escolha = input(msg)
    opcoes = ''
    for opcao in lista_vinhos:
        opcoes += f"\n{opcao}"
    if escolha in lista_vinhos:
        print(f"Você escolheu o vinho: {escolha}")
    while escolha not in lista_vinhos:
        escolha = input(msg)
    return escolha

    

vinho = verifica_vinhos("Escolha o Vinho que deseja escolher: ")



# somar_lista([1,2,3,4,5])
# verificar_par_lista([1,2,3,4,5])
# contar_vogais('matheus')
# media_lista([1,2,3,4,5])
# vogal_ou_nao('y')
# printar_oi([1, 2, 3, 'teste'])
# verificar_par(7)
# ultimo_elemento()
# exemplo_carros()

