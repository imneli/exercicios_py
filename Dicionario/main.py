"""res = input("Qual time vc torce?\n-> ")

times = {
        'São Paulo': 'O maior do mundo bb',
        'Corinthians': 'Chora',
        'Palmeiras': 'i o dudu'
        }

if res != times:
    print("no")
else:
    print(times[res])"""



"""dic = {}
dic['pares'] = 2
print(dic)

dic['pares'] = [dic['pares']]
dic['pares'].append(4) 

print(dic)"""


"""times = {
    'sp': 3,
    'pal': 0,
    'cor': 1,
    'santos': 2,
    'inter': 1
}

for key in times.keys():
    if times[key] == 1:
        print(f'o {key} tem {times[key]} mundial')
    else:
        print(f'o {key} tem {times[key]} mundiais')"""

def calc_poligono(n):
    dic = {
        3: 'triangulo',
        4: 'quadrado',
        5: 'pentagono',
        6: 'hexagono',
        7: 'heptagono',
        8: 'octagono'
    }

    for key in dic.keys():
        if key == n:
            output = dic[key]
    return output

print(calc_poligono(8))

dic = {
    'zero': '0',
    'um': '1',
    'dois': '2',
    'três': '3',
    'quatro': '4',
    'cinco': '5',
    'seis': '6',
    'sete': '7',
    'oito': '8',
    'nove': '9'
}

"""numero = ''
i = 0

while i < 9:
    res = input("digite o numero por extenso\n-> ")
    numero += dic[res]
    i += 1

print(f"seu numero é {numero}")"""

emocoes = {
    'feliz': '😁',
    'triste': '😢',
    'bravo': '😡',
    'surpreso': '😲',
    'confuso': '😕',
    'amor': '❤️',
    'medo': '😨',
    'ansioso': '😰',
    'envergonhado': '😳',
}

res = input("digite como vc esta\n-> ")

palavras = res.split(" ")


for palavra in palavras:
    for key in emocoes.keys():
        if palavra == key:
            print(f'voce esta {emocoes[palavra]}')