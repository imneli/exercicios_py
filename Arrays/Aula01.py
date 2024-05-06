def manipulando_lista():

    nomes = ['Allen', 'Lucas', 'Danilo', 'js', 'wellington', 'leandro', 'demetrius']
    for i in range (len(nomes)):
        if nomes[i] == 'Danilo':
            print(f"O {nomes[i]} tem um celta brabo")



def lista_profs():

    profs = ['Allen', 'Lucas', 
            'Danilo', 'wellington',
            'leandro', 'Demetrius']
    materias = ['Sw&TX', 'Web', 'Python & Calculo',
                'Front-end', 'Story Telling', 'Edge']
    for i in range(len(profs)):
        print(f"O {profs[i]} dá {materias[i]}")


def par_impar(): # com len
    impar = 0
    par = 0

    numeros = [1, 2, 3, 4, 5,
               6, 7, 8, 9, 10,
               11, 12, 13, 14, 15]

    for i in range (len(numeros)):
        if (numeros[i] % 2 == 0):
            par += 1
        else:
            impar += 1
        
    print(f"A qtd de numeros pares é {par} e impares é {impar} ")


def v_prof(): # sem len
    pares = 0
    numeros = [1, 2, 3, 4, 5,
               6, 7, 8, 9, 10,
               11, 12, 13, 14, 15]
    for num in numeros:
        if num % 2 == 0:
            pares += 1
    print(f"há {pares} pares e {len(numeros)-pares} impares")


    # par_impar()
    # v_prof()


def soma_num(): # sem len
    soma = 0
    numeros = [1, 2, 3, 4, 5,
               6, 7, 8, 9, 10,
               11, 12, 13, 14, 15]
    
    for i in range (len(numeros)):
        soma += numeros[i] # acessar lista e nao botar i
    print(f"A soma deu {soma} e a média deu {soma/len(numeros)}")

def add_lista():
    numeros = []
    for i in range(10):
        num = int(input("Diga um numero: "))
        num = int(num)
        numeros.append(num)
    print(f"\nLista -> {numeros}")



def achar_num():
    lista = [1, 23, 54, 64, 54,
             90, 123, 43, 12, 4, 1222]
    maior = lista[0] # definindo o maior como o primeiro da lista
    for i in range(len(lista)): #range lista
        if lista[i] > maior:
            maior = lista[i] # redefinindo o maior como o indice maior ao comprar
    print(f"O maior número é:\n-> {maior} e sua média é {maior/len(lista)}")


def carros_legais():
    carros = ['Celta', 'Up', 'Uno', 'Kwid', 'Kombi']
    precos = [1000000, 10000, 20000, 30000, 32000]
    # frase_erro = '\n'.join(carros) (juntar itens da lista)
    valor = precos[0]
    ind_carros = 0
    for i in range (len(precos)):
        if precos[i] > valor:
            valor = precos[i]
            ind_carros = i
    print(f"O carro mais caro é o {carros[ind_carros]} custando"
           f" R$ {precos[ind_carros]:.2f}")
    

def search_car():

    carros = ['Celta', 'Up', 'Uno', 'Kwid', 'Kombi']
    precos = [1000000, 10000, 20000, 30000, 32000]
    frase_erro = '\n'.join(carros)
    escolha = input("Digite qual carro você quer ver o preço: ")
    while escolha not in carros:
        print(f"Somente essas opções: \n{frase_erro}")
        escolha = input("Digite qual carro você quer ver o preço: ")

    for i in range (len(carros)):
        if escolha == carros[i]:
            print(f"O valor de {escolha} é R$ {precos[i]:.2f}")

# search_car()
# carros_legais()
# achar_num()
# add_lista()
# par_impar()
# v_prof()
# soma_num()


