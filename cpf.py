# exercicios python

import os
import time

def main():
    print("""
    █▀▀ █░█ █▀█ █▀ █▀█
    █▄▄ █▄█ █▀▄ ▄█ █▄█
        
    Olá! Seja vem-vindo ao curso, por favor digite os 11 digitos do seu CPF abaixo""")
main()


def pedir_cpf():
    time.sleep(3)
    os.system('clear')
    while True:
        cpf = input("Digite o CPF: ")
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido! Por favor, digite apenas os 11 dígitos do CPF.")
            continue
        else:
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            print(f"O CPF é válido e seu formato é: {cpf_formatado}")
            return

pedir_cpf()
