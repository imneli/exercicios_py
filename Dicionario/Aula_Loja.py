'''
#import pandas as pd
#import requests
def cadastrar_endereco():
    while True:
        cep = input("Diga seu cep: ")
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            printa_dics(response)
            confirmar = forca_opcao("As infos estão corretas?",sim_ou_nao)
            if confirmar == sim_ou_nao[0]:
                response['unidade'] = input("Diga o nº: ")
                response['complemento'] = input("Diga o complemento: ")
                carrinho['Endereço'] = response
                return
        else:
            print("Digitado incorretamente!")
def comprar():
    while True:
        escolha = forca_opcao("Qual carro lhe interessa?", carros['modelo'])
        indice_escolha = indices[escolha]
        for key in carros.keys():
            print(f"{key} : {carros[key][indice_escolha]}")
        comprar = forca_opcao(f"Você vai comprar o {escolha}?", sim_ou_nao)
        if comprar == sim_ou_nao[0]:
            qtd = checa_numero(f"Quantas unidades de {escolha}?\n->")
            if qtd > carros['estoque'][indice_escolha]:
                print("Não há quantidade suficiente!")
                continue
            else:
                carros['estoque'][indice_escolha] -= qtd
                if escolha not in carrinho['carros'].keys():
                    carrinho['carros'][escolha] = qtd
                else:
                    carrinho['carros'][escolha] += qtd
                carrinho['Valor total (R$)'] += qtd*carros['preço(R$)'][indice_escolha]

            encerrar = forca_opcao("Você deseja encerrar a compra?", sim_ou_nao)
            if encerrar == sim_ou_nao[0]:
                if carrinho['Valor total (R$)'] != 0:
                    cadastrar_endereco()
                    printa_dics(carrinho)
                break
        else:
            print('tchau 🤡🤡🤡')
            break
    return
def forca_opcao(msg,conjunto_opcoes,msg_erro = 'Inválido'):
    opcoes = '\n'.join(conjunto_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in conjunto_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha
def checa_numero(msg,msg_erro = 'Inválido'):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)
def remover():
    escolha = forca_opcao("Qual carro vc deseja remover?",carros['modelo'])
    indice_escolha = indices[escolha]
    for key in carros.keys():
        carros[key].pop(indice_escolha)
    return
def cria_indices():
    indices = {}
    for i in range(len(carros['modelo'])):
        nome = carros['modelo'][i]
        indices[nome] = i
    return indices
def cadastrar():
    for key in carros.keys():
        if types_dict[key] is float:
            while True:
                try:
                    info = float(input(f"Diga o novo {key}: "))
                    break
                except ValueError:
                    print("Deve ser um número. Se for quebrado, use '.' ao invés de ','.\n"
                          "Ex: 1234,5 -> 1234.5")
        elif types_dict[key] is int:
            while True:
                try:
                    info = int(input(f"Diga o novo {key}: "))
                    break
                except ValueError:
                    print("Deve ser um número. Se for quebrado, use '.' ao invés de ','.\n"
                          "Ex: 1234,5 -> 1234.5")
        else:
            info = input(f"Diga o novo {key}: ")
        carros[key].append(info)
    return
def atualizar():
    opcoes_atualizacao = ['Total','Específica']
    escolha = forca_opcao("Qual carro vc deseja atualizar?",carros['modelo'])
    indice_escolha = indices[escolha]
    tipo_atualizacao = forca_opcao("Que tipo de atualização?",opcoes_atualizacao)
    if tipo_atualizacao == opcoes_atualizacao[0]:
        for key in carros.keys():
            if types_dict[key] is float:
                while True:
                    try:
                        info = float(input(f"Diga o novo {key}: "))
                        break
                    except ValueError:
                        print("Deve ser um número. Se for quebrado, use '.' ao invés de ','.\n"
                              "Ex: 1234,5 -> 1234.5")
            elif types_dict[key] is int:
                while True:
                    try:
                        info = int(input(f"Diga o novo {key}: "))
                        break
                    except ValueError:
                        print("Deve ser um número. Se for quebrado, use '.' ao invés de ','.\n"
                              "Ex: 1234,5 -> 1234.5")
            else:
                info = input(f"Diga o novo {key}: ")

            carros[key][indice_escolha] = info
    else:
        caracteristica = forca_opcao("O que será alterado?",carros.keys())
        carros[caracteristica][indice_escolha] = input(f"Diga o novo {caracteristica}: ")
    return
def printa_dics(dic,qtd = 0):
    espacamento = qtd*'  '
    for key in dic.keys():
        if type(dic[key]) is not dict:
            print(f"{espacamento}{key} : {dic[key]}")
        else:
            print(key)
            if key in carrinho.keys():
                qtd = 1
            else:
                qtd += 1
            printa_dics(dic[key],qtd)
    return
carros = {
    'modelo' : ['opala','marea','kombi','celtinha brabo','uno','monza','corcel'],
    'potência (cv)' : [172,130,250,140,100,120,150],
    'consumo (km/l)' : [1,3,8,7,15,2,1.5],
    'cor' : ['laranja','verde','branca','preto','prata','preto','azul'],
    'ano' : ['1972','2004','1985','2014','2001','1980','1975'],
    'estoque' : [5,6,7,8,9,10,11],
    'preço(R$)' : [50,10,2.50,1000000,100,200,999999]
}
types_dict = {key : type(carros[key][0]) for key in carros.keys()}
indices = cria_indices()
carrinho = {
    'carros' : {},
    'Valor total (R$)' : 0,
    'Endereço' : {
        'Rua' : '',
        'Número' : '',
        'Complemento' : '',
        'CEP' : ''
    }
}
a = float(input("Diga um numero: "))
sim_ou_nao = ['sim','não']
opcoes_funcionario = ['Remover','Cadastrar','Atualizar','Sair']
usuario = ['cliente','funcionário']
tipo_usuario = forca_opcao("O que você é?",usuario)
if tipo_usuario == usuario[0]:
    comprar()
else:
    operacao = forca_opcao("Qual operação será realizada?",opcoes_funcionario)
    if operacao == opcoes_funcionario[0]:
        remover()
        indices = cria_indices()
    elif operacao == opcoes_funcionario[1]:
        cadastrar()
        indices = cria_indices()
    elif operacao == opcoes_funcionario[2]:
        atualizar()
    else:
        print('saindo...')
printa_dics(carros)

lista = [1,2,54,54,568,345,657,43,5568,6312]
while True:
    try:
        num = int(input("Diga um numero: "))
        print(lista[num])
    except ValueError:
        print("Você não digitou um número!")
    except IndexError:
        print(f"Só são válidos numeros entre 0 e {len(lista)-1}")
    except Exception as e:
        print(f"Isso não funcionou: {e}")
    else:
        print("BOM DIA")
        break

while True:
    try:
        num = input("Diga um numero: ")
        if ',' in num:
            raise ValueError("Teste")
        break
    except ValueError as e:
        print(e)
        print('Não pode ter ","! Números quebrados são: 1.2')

#Usando tratamento de exceções, escreva um código que peça uma chave ao usuario,
#peça um numero que fará papel de índice e printe na tela o elemento da lista
#correspondente
dic = {'chave' : ['valor1','valor2']}
while True:
    try:
        chave = input("Diga uma chave do dicionario: ")
        num = int(input("Diga um indice da lista: "))
        print(dic[chave][num])
    except KeyError:
        print(f"As chaves disponíveis são: {list(dic.keys())}")
    except ValueError:
        print("Deve ser um número inteiro!")
    except IndexError:
        print(f"Somente entre 0 e {len(dic['chave'])-1}")

dic = {'chave' : ['valor1','valor2']}
while True:
    try:
        chave = input("Diga uma chave do dicionario: ")
        if chave not in dic.keys():
            raise KeyError
    except KeyError:
        print(f"As chaves disponíveis são: {list(dic.keys())}")
    else:
        while True:
            try:
                num = int(input("Diga um indice da lista: "))
                print(dic[chave][num])
            except ValueError:
                print("Deve ser um número inteiro!")
            except IndexError:
                print(f"Somente entre 0 e {len(dic['chave'])-1}")
            else:
                break
    break

texto = 'Concluímos que chegamos à conclusão que não concluímos nada. Por isso, conclui-se que a conclusão será concluída quando todas tiverem concluído que já é tempo de concluir uma conclusão.'
dic_replace = {
    '.,:;!?': '',
    'ãáàâ' : 'a',
    'êé' : 'e',
    'íî' : 'i',
    'ôóõ' : 'o',
    'úü' : 'u'
}
for key in dic_replace.keys():
    for char in key:
        texto = texto.replace(char,dic_replace[key])
texto = texto.lower()
print(texto)
texto = texto.split(' ')
print(texto)
palavras = {}
for palavra in texto:
    if palavra in palavras.keys():
        palavras[palavra] += 1
    else:
        palavras[palavra] = 1
    print(palavras)
'''
import requests

url = "https://instagram-scraper-api3.p.rapidapi.com/highlight_media"

querystring = {"highlight_id":"18004653919636356"}

headers = {
	"x-rapidapi-key": "46a1b6e3a2msh3a0ee1c5e1f500dp15282ajsnd5e5a335c026",
	"x-rapidapi-host": "instagram-scraper-api3.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
