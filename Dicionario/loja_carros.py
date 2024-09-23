import pandas as pd

carros = {
    'modelo' : ['Opala','Marea','Kombi','Celtinha','Uno','Monza','Corcel'],
    'potência (cv)' : [172,130,250,140,100,120,150],
    'consumo (km/l)' : [1,3,8,7,15,2,1.5],
    'cor' : ['laranja','verde','branca','preto','prata','preto','azul'],
    'ano' : ['1972','2004','1985','2014','2001','1980','1975'],
    'estoque' : [5,6,7,8,9,10,11],
    'preço(R$)' : [50,10,2.50,1000000,100,200,999999]
}

indices = {}

sim_ou_nao = ['yes', 'no']


def comprar():
    while True:
        escolha = forca_opcao("Qual carro lhe interessa?", carros['modelo'])
        indice_escolha = indices[escolha]

        for key in carros.keys():
            print(f"{key} : {carros[key][indice_escolha]}")

        comprar = forca_opcao(f"Você vai comprar o {escolha}?", sim_ou_nao)
        if comprar == sim_ou_nao[0]:
            qtd = checa_numero(f"Quantas unidades de {escolha} você deseja comprar?\n->")

            show_stock = carros['estoque'][indice_escolha]

            if qtd > carros['estoque'][indice_escolha]:
                print(f"Não há quantidade suficiente de carros. Temos {show_stock} carros.")
                continue
            else:
                carros['estoque'][indice_escolha] -= qtd
                if escolha not in carrinho['carros'].keys():
                    carrinho['carros'][escolha] = qtd
                else:
                    carrinho['carros'][escolha] += qtd

            encerrar = forca_opcao("Você deseja encerrar a compra?", sim_ou_nao)
            if encerrar == sim_ou_nao[0]:
                if carrinho['Valor total (R$)'] != 0:
                    for key in  carrinho['Endereço'].keys():
                        info = input(f"Diga o {key}: ")
                        carrinho['Endereço'][key] = info
                print(carrinho)
                break
        else:
            print("tchau")
            break

    return

for i in range(len(carros['modelo'])):
    nome = carros['modelo'][i]
    indices[nome] = i

print(pd.DataFrame(carros))

def forca_opcao(msg, conjunto_opcoes, msg_erro = "Invalido"):
    opcoes = '\n'.join(conjunto_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in conjunto_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n->")

    return escolha

def remover():
    forca_opcao("Qual carro você deseja remover?", carros['modelo'])
    nome = carros['modelo'][i]
    indices[nome] = carros['modelo'].pop()


def checa_numero(msg, err = 'Invalido'):
    num = input(msg)
    while not num.isnumeric():
        print(err)
        num = input(msg)
    return int(num)

carrinho = {
    'carros': {},
    'Valor total (R$)': 0,
    'Endereço': {
        'Rua': '',
        'Número': '',
        'Complemento': '',
        'CEP': ''
    }
}

usuario = ['cliente', 'funcionário']
tipo_usuario = forca_opcao("O que você é?", usuario)
if tipo_usuario == usuario[0]:
    comprar()
else:
    pass
    remover()

print(pd.DataFrame(carros))
