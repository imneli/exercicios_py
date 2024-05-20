def printar_msg(msg):
    print(msg)
    return

def meu_in(lista,buscar):
    print(lista)
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return True
    return False

def forca_opcao(msg, lista_opcoes, msg_erro):
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao

def verifica_numero(msg, msg_erro):
    numero = input(msg)
    while not numero.isnumeric():
        print(msg_erro)
        numero = input(msg)
    numero = int(numero)
    return numero

def soma_lista(lista_numeros):
    soma = 0
    for i in range(len(lista_numeros)):
        soma += lista_numeros[i]
    return soma

def acha_maior(lista_numeros):
    indice_maior = 0
    maior = lista_numeros[indice_maior]
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > maior:
            maior = lista_numeros[i]
            indice_maior = i
    return indice_maior

vinhos = ['Pergola', 'Chapinha', 'Sangue de boi']
precos = [15, 20, 40]
estoque = [17, 20, 34]
valor_total = 0
opcoes = ""
for i in range (len(vinhos)):
    opcoes += f"\n-> {vinhos[i]}"

ano = verifica_numero("Qual sua Idade:","Deve ser um numero")
if ano >= 18:
    print("Acesso Liberado")
    escolha = forca_opcao(f"Qual vinho voce quer?\n{opcoes}\n\n->",vinhos, "Opção Invalida")
    qtd = verifica_numero(f"Diga a quantidade de garrafas de Vinho {escolha} você quer:","A quantidade deve ser um numero!")
    total_escolha = qtd * precos
    print(total_escolha)
else:
    print("Acesso Negado")










