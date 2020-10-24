#!/usr/bin/env python

""" trabalho PARI 2020/2021 Grupo 2 """

import argparse
import string
import readchar
import random
from time import time
from collections import namedtuple
from colorama import Fore
from time import time, ctime


input = namedtuple('Input', ['requested', 'received', 'duration'])  # t tempo ls letra aleatoria lr letra introduz

def escolhaModo():
    # escolha do MODO DE TESTE

    global modo  # variavel para saber em que modo de jogo estou
    global timeInput  # variavel que guarda os tempo ou o input

    testModo = argparse.ArgumentParser(description="Defenicao do modo de teste")

    # ao usar o action = ''store_true'' quando o comando e chamado ele returna o valor true quando nao e chama o valor false
    testModo.add_argument('-utm', '--use_time_mode',
                          help='Max number of secs for time mode or maximum number of inputs for number of inputs mode',
                          action="store_true")
    testModo.add_argument('-mv', '--max_value',
                          help='Max number of secs for time mode or maximum number of inputs for number of inputs mode')

    tes = testModo.parse_args()

    ''' ???ainda nao pos para nao correr sem os argumentos '''

    args_list = vars(tes)  # NB: importante converte o mamespace em dicionario atraves do vars

    # excuta para teste em modo tempo (por isso o True e verdadeiro pois foi chamado no argomento) senao executa para modo imput

    if args_list['use_time_mode'] == True:
        modo = True  # modo -true significa que o modo do teste e por tempo limite
        print(tes)
        print ("PARI Typing Test, Grupo 2, Outober 2020")  # ?????falta por pari em cor vermelho
        print ("test running up to " + str(args_list['max_value']) + " seconds.")
        timeInput = (args_list['max_value'])  # tempo maximo

    else:
        modo = False  # modo false quer dizer que o modo do teste e por imputs limite
        print (tes)
        print ("PARI Typing Test, Grupo 2, Outober 2020")  # ????? falta por a cor no pari
        print ("test running up to " + str(args_list['max_value']) + " inputs")
        timeInput = (args_list['max_value'])  # imputs maximo




def letter_time_counter():

    letter = random.choice(string.ascii_letters)  # gera letras em maiusculas e minusculas
    letter = letter.lower()  # converte para minusculas
    print('type letter: ' + letter)
    Start = time()  # tempo inicio

    while True:  # serve para so premitir que seja inseridas letras e nao carateres e caso seja espaco interromper o programa
        ins_letter = readchar.readchar()  # pede para inserir uma letra
        asrletter = ord(ins_letter)
        if (asrletter > 97) and (
                asrletter < 122):  # so deixa de pedir letras quando insiro uma dentro dos parametros ascii pertendidid
            break
        elif asrletter == 32:  # caso clique no espaco devolve-me um tople de false
            return input(requested=False, received=False, duration=False)

    Stop = time()  # tempo final.



    if letter == ins_letter:

        print('you typed letter: ' + Fore.GREEN + ins_letter + Fore.RESET)


    else:
        print('you typed letter: ' + Fore.RED + ins_letter + Fore.RESET)

    time_elapsed = Stop - Start  # tempo de insersao da letra

    return input(requested=letter, received=ins_letter, duration=time_elapsed)


def ModoTime(Time):
    # modo de teste limitado pelo tempo


    listTime = []


    # print (list[1].duration)

    timeduracao = int(time()) + int(Time)

    while True:
        listTime.append(letter_time_counter())
        if time() >= timeduracao:
            break



def ModoInput(input):
    # modo de teste limitado pelos inputs
    list = []



    for x in range(0, int(input)):
        list.append(letter_time_counter())  # acresenta os varios nametuples numa lista
        if list[x][1] == False:  # caso ponha o espaco ele para de pedir os inputs
            del list[x]  # elemina o ultimo elemento da lista pois e um manetuple a false
            break

    print (list)


def main():
    escolhaModo()
    print ("Press any key to start the test")
    readchar.readchar()  # para imprimir uma tecla qualquer para continuar o teste

    Tempo_ini = time() #tempo inicial
    test_start = ctime() # data inicial

    if modo:
        ModoTime(timeInput)
    else:
        ModoInput(timeInput)

    Tempo_end = time() #tempo final
    test_end = ctime() #data final

    test_duration=Tempo_end - Tempo_ini
    print ( test_start )
if __name__ == '__main__':
    main()
