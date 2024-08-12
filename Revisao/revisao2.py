def password():

    db_pass = '1234'
    passw = input("type your pass\n-> ")
    while passw != db_pass:
        print("wrong pass!")
        passw = input("type your pass\n-> ")
    if db_pass == passw:
        print("nice")
    else:
        print("fuck u")

def wines():
    wine1 = 'sangue de boi'
    wine2 = 'pergola'
    wine3 = 'chapinha'

    chose = input("search your prefer wine\n->")
    while not chose != wine1 or chose != wine2 or chose != wine3:
        print("wrong option")
        chose = input("search your prefer wine\n->")

    if chose == wine1:
        price = 10
    elif chose == wine2:
        price = 20
    else:
        price = 30

# def fibonacci():
#     a = 1
#     b = 1
#     i = 0

#     while i < qtd:
#         c = a + b
#         a = b
#         print(c, end = " ")
#         b = c
#         i += 1


# 


def ex_01():
    list_grades = [6,7,8,9,10]
    grade = int(input("put your grade\n-> "))

    while grade > 10 or grade < 0:
        print("type a valid grade")
        grade = int(input("put your grade\n-> "))

        if grade in list_grades:
            print("nice")
        if grade < 6:
            print("rec")
# ex_01()

def ex_02():
    name = input("write your name\n-> ")

    while len(str(name)) < 3:
        print("write a valid name!")
        name = input("write your name\n-> ")

        if len(str(name)) > 3:
            pass


    age = int(input("write your age\n-> "))

    while age > 150 or age < 0:
        print("invalid age! type your real name")
        age = int(input("write your age\n-> "))

        if age > 0 or age < 150:
            print("thanks!")
            pass


    salary = int(input("type your salary\n-> "))

    while salary < 0: 
        print("invalid salary! type your salary.")
        salary = int(input("type your salary\n-> "))

        if salary > 0:
            pass

    gender = input("type your gender (f/m) \n-> ")
    list_gender = ['f','m']

    while gender not in list_gender:
        print("type a valid gender!")
        gender = input("type your gender (f/m) \n-> ")

        if gender in list_gender:
            print("tks")
            pass

    marital_status = input("type your marital status (s,c,v,d)\n-> ")
    ms_list = ['s','c','v','d']

    while marital_status not in ms_list:
        print("type your marital status..")
        marital_status = input("type your marital status (s,c,v,d)\n-> ")

        if marital_status in ms_list:
            print("tks")
            pass

# ex_02()

def ex_03():
    a = 80000
    b = 200000
    tax_a = 0.03
    tax_b = 0.015
    counter = 0

    while a < b:
        a *= tax_a
        b *= tax_b
        counter += 1

    print(counter)

# ex_03()

def ex_04():
    alvo = 1
    

    while alvo < 11:
        print(f"Tabuada do {alvo}:")
        i = 1
        while i < 11:
            print(f"{alvo} x {i} = {alvo*i}")
            i += 1
        alvo += 1

ex_04()
