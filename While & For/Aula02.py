def nota():

    while True:
        nota = input("Digite sua nota: ")
        if not nota.isnumeric():
            print("Digite um numero.")
            continue
        nota = int(nota)
        if nota > 10 or nota < 0:
            print("Nota invalida, digite novamente")
            continue


def matheus_char():
    for char in 'matheus':
        print(char, end = ' ')
        char = 1
        print(char)


def dois():
    for i in range(1,10,2): #start,end,stop
        print(i)

def numeros_100():
    num_som = 0
    for i in range(101):
        num_som += i
        print(num_som)


def password():
    correct_pass = '1234'
    for i in range(3):
        pass_input = input("type your pass: ")
        if pass_input == correct_pass:
            print("Correct Pass")
        if pass_input != correct_pass:
             print("Incorret")
             continue




def teste_num():
    qtd = 10
    soma = 0
    for i in range(qtd):
        num = input(f"Diga o {i+1}º numero: ")
        while True:
            if num.isnumeric():
                break
        num = int(num)
        soma += num

    print(f"A soma é {soma} e a média é {soma/qtd}")


def tabuada():
    for i in range(1,11):
        print(f"Tabuada do {i}: ")
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")
        print()


def fibonacci():
    a = 1
    b = 0
    input_num = int(input("type a num: "))

    for i in range(input_num):
        c = a + b
        a = b
        b = c
        print(c)

def idade():
    idd = int(input("Digite sua idade: "))
    if idd < 18:
        print("Nao tem idade")
    else:
        print("ok")
        

# idade()
# nota()
# matheus_char()
# numeros_100()
# password()
# teste_num()
# tabuada()
# fibonacci()
