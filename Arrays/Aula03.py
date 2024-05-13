def printa_msg(msg):
    print(msg)
    return

# printa_msg('Erro!')

def val_idade(idade):
    if idade >= 18:
        print("Acesso Liberado!")
    else:
        print("Acesso Negado")
    return

    idade = int(input("Qual sua idade?\n->"))
# val_idade(idade)


def sum_list(list):
    soma = 0
    for i in range (len(num)):
        soma += num[i]
    return soma


    num = [1,2,3,4,5]
    num_2 = [2,3,4,5,5]
    num_3 = [12,3,4,5,2,4,6,7,8]
    sum_num = sum_list(num_3)
    print(sum_num)




# def verify_num(msg):
#     year = input(msg)
#     while not year.isnumeric():
#         year = input(msg)
#         year = int(year)
            
#     return year
# verify_num("Diga sua idade\n->")
# qtd = verify_num("Digite a quantidade de garrafas\n->")

# search = 'Lucas'

# def my_in(lista, search):
#     for i in range (len(lista)):
#         elem = lista[i]
#         if elem == search:
#             return True
#     return False


# def force(msg, lista, msg_err):
#     opcao = input(msg)
#     while not my_in(search, lista):
#         opcao = input(msg)
#     return opcao
        
lista = ['Danilo', 'Allen', 'Lucas Vasquez', 'Lucas']
wines = ['pergola', 'chapinha', 'sangue de boi']
# asd = force("Diga um nome: ",lista, "Diga uma opção valida")

# qtd = input("digite a qtd de garrafas\n->")
# while not qtd.isnumeric():
#     qtd = input("digite a qtd de garrafas\n->")
# qtd = int(qtd)





def wine_stock(a_list, b_list, c_list):
    output = "Wine | Price | Stock\n\n"
    for i in range (len(a_list)):
        output += f"Wine: {a_list[i]} | Price: {b_list[i]} | Stock: {c_list[i]}\n"
    return output

print(wine_stock(['Wine0', 'Wine1', 'Wine2', 'Wine3', 'Wine4'],
                  [f'{40:.2f}', f'{20:.2f}', f'{32:.2f}', f'{65:.2f}', f'{78:.2f}'],
                    [100, 80, 23, 43, 53]))


def forcethis(ml_list):
    wine1 = ml_list[0]
    wine2 = ml_list[1]
    wine3 = ml_list[2]
    lista_2 = [wine1, wine2, wine3]
    output = input(f"Escolha o tamanho do vinho\n{ml_list}")

    if 
    print (wine1, wine2, wine3)
    return output
    


print(forcethis(['500ml', '700ml', '1L']))


def contar_num():
    lista = [1,0,1,0,0,1,0,1,0,1,0,1,1,1,0]
    sub_lista = [1,0,1]
    contagem = 0
    for i in range(len(lista) - len(sub_lista)):
        pivo = i
        qtd_corretos = 0
        for j in range(len(sub_lista)):
            if sub_lista[j] != lista [pivo+j]:
                break
            qtd_corretos += 1
        if qtd_corretos == 3:
            contagem += 1
    print(contagem)

contar_num()




        
        

