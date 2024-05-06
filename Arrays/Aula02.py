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



# exemplo_carros()


def ultimo_elemento():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ultimo = len(lista) - 1
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
    print(f"Lista Inicial -> {lista}\n")
    for i in range(len(lista) // 2):
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
        i += 1
    print(f"Lista Invertida -> {lista}")


ultimo_elemento()