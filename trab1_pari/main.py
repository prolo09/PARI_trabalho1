#!/usr/bin/env python

""" trabalho PARI 2020/2021 Grupo 2 """

import argparse
import string
import readchar
import random
from collections import namedtuple
from colorama import Fore
from time import time, ctime
from pprint import pprint


input = namedtuple('Input', ['requested', 'received', 'duration'])
list = []                                                           # lista - guarda os tuples de cada input

number_of_hits = 0                                                   # variavel de inputs corretos
number_of_types = 0                                                  # varivel input de carateres

def escolhaModo():
    # escolha do MODO DE TESTE

    global modo                                                     # variavel para saber em que modo de jogo estou
    global timeInput                                                # variavel que guarda os tempo ou o input

    testModo = argparse.ArgumentParser(description="Defenicao do modo de teste")

    # ao usar o action = ''store_true'' quando o comando e chamado ele retorna o valor true quando nao e chama o valor false
    testModo.add_argument('-utm', '--use_time_mode',
                          help='Max number of secs for time mode or maximum number of inputs for number of inputs mode',
                          action="store_true")
    testModo.add_argument('-mv', '--max_value',
                          help='Max number of secs for time mode or maximum number of inputs for number of inputs mode', required=True)

    args_list = vars(testModo.parse_args())                        # NB: importante converte o mamespace em dicionario atraves do vars

    # excuta para teste em modo tempo (por isso o True e verdadeiro pois foi chamado no argumento) senao executa para modo imput

    if args_list['use_time_mode']:
        modo = True                                                  # modo -true significa que o modo do teste e por tempo limitado
        print(args_list)
        print (Fore.RED + "PARI" + Fore.RESET + " Typing Test, Grupo 2, Outober 2020")
        print ("test running up to " + str(args_list['max_value']) + " seconds.")
        timeInput = (args_list['max_value'])                         # tempo maximo

    else:
        modo = False                                                 # modo false quer dizer que o modo do teste e por imputs limite
        print (args_list)
        print ("PARI Typing Test, Grupo 2, Outober 2020")  # ????? falta por a cor no pari
        print ("test running up to " + str(args_list['max_value']) + " inputs")
        timeInput = (args_list['max_value'])                         # imputs maximo


def letter_time_counter():
    # crai uma letra aliatoria
    letter = random.choice(string.ascii_letters)                     # gera letras em maiusculas e minusculas
    letter = letter.lower()                                          # converte para minusculas
    print('type letter: ' + letter)
    Start = time()                                                   # tempo inicio

    while True:                                                      # serve para so premitir que seja inseridas letras e nao carateres e caso seja espaco interromper o programa
        ins_letter = readchar.readchar()                             # pede para inserir uma letra
        asrletter = ord(ins_letter)
        if (asrletter >= 97) and (
                asrletter <= 122):                                   # so aceita letras entre 'a' e 'z' de acordo com a tabela ascii caso contrario continua a pedir
            break
        elif asrletter == 32:                                        # caso clique no espaco devolve-me um tuple de false
            return input(requested=False, received=False, duration=False)

    Stop = time()                                                    # tempo final.


    global number_of_hits
    global number_of_types

    number_of_types += 1
    if letter == ins_letter:
        print('you typed letter: ' + Fore.GREEN + ins_letter + Fore.RESET)
        number_of_hits += 1

    else:
        print('you typed letter: ' + Fore.RED + ins_letter + Fore.RESET)

    time_elapsed = Stop - Start                                     # tempo de insersao da letra

    return input(requested=letter, received=ins_letter, duration=time_elapsed)


def ModoTime(Time):
    # modo de teste limitado pelo tempo

    timeduracao = float(time()) + float(Time)                       # registo tempo limite do teste

    while True:
        list.append(letter_time_counter())                          # adiciona o namedtuple uma lista
        if time() >= timeduracao:                                   # compara o tempo atual com a previsao de fim de teste
            break
        elif not list[-1][1]:                                      # caso o ultimo elemento to da lista de tuples for falso
            del list[-1]                                           # elimina ultimo elemento da lista
            break



def ModoInput(input):
    # modo de teste limitado pelos inputs


    for x in range(0, int(input)):
        list.append(letter_time_counter())                       # acrecenta os varios namedtuples numa lista
        if not list[-1][1]:                                      # caso ponha o espaco ele para de pedir os inputs
            del list[-1]                                         # elimina o ultimo elemento da lista
            break


def dict_resultados(test_date_end, test_date_start, test_duration):
    # eleboracao das contas nececarias para os valres estatiticos e criacao do dicionario

    # para caso clique no espaco sem inserir nenhum caratere
    if number_of_types != 0:
        accuracy = float(number_of_hits) / number_of_types             # precentagem de respostas certas
    else:
        accuracy = 0

    # calculos para a media da duracao de cada input
    sumTime = 0                                                     # variavel para somar todos os valores de duracao


    if len(list) != 0:                                              # para caso clique no espaco ao inicio
        for z in range(0, len(list)):
            sumTime = list[z].duration+sumTime                      # variavel para somar todos os valores
        type_average_duration = sumTime/(len(list))                 # media dos valores
    else:
        type_average_duration = 0                                   # devolve a 0 caso cliquemps espaco no inicio
    # calculos para a media da duracao dos inputs corretos

    sumTimeEq = 0                                                   # variavel para somar os tempos certos
    sumTimeDef = 0                                                  # variavel para somar os tempos certos
    certa = 0                                                       # num de certas                                                   # nun de erradas
    errada = 0                                                      # num de erradas

# corre a vista compreta para destingir quais esta certas e erradas e faz a media consuante a certa ou errada
    for r in range(0, len(list)):
        if list[r].received == list[r].requested:
            sumTimeEq = list[r].duration+sumTimeEq                 # soma o tempo de duracao das  certas
            certa += 1                                             # contador de certas
        else:
            sumTimeDef = list[r].duration+sumTimeDef               # soma o tempo de duracao das erradas
            errada += 1                                            # contador erradas


# devolve '0' caso se acerte ou erre todas para que nao haja divisoes por '0'
    if certa != 0:
        type_hit_average_duration = sumTimeEq/certa
    else:
        type_hit_average_duration = 0

    if errada != 0:
        type_miss_average_duration = sumTimeDef/errada
    else:
        type_miss_average_duration = 0


# dicionario com os valores a imprimir
    resultdict = {'accuracy': accuracy,
                  'inputs': list,
                  'number_of_hits': number_of_hits,
                  'number_of_types': number_of_types,
                  'test_duration': test_duration,
                  'test_end': test_date_end,
                  'test_start': test_date_start,
                  'type_average_duration': type_average_duration,
                  'type_hit_average_duration': type_hit_average_duration,
                  'type_miss_average_duration': type_miss_average_duration}
    pprint(resultdict)

def main():
    escolhaModo()
    print ("Press any key to start the test")
    readchar.readchar()                                         # para imprimir uma tecla qualquer para continuar o teste

    Tempo_ini = time()                                          # tempo inicial para correr o teste
    test_date_start = ctime()                                   # data inicial do teste

    # aplica o modo consunte o escolhido ateriormente se for true corre o modo tempo se for false o modo input
    if modo:
        ModoTime(timeInput)
    else:
        ModoInput(timeInput)

    Tempo_end = time()                                     # tempo final para correr o teste
    test_date_end = ctime()                                 # data final do teste

    test_duration = Tempo_end - Tempo_ini                 # calculo para o tempo de duracao

    if modo:
        if float(test_duration) >= float(timeInput):
            print ("Current test duration (" + str(test_duration) + ") exceeds maximum of " + timeInput)
        else:
            print ("Current test duration (" + str(test_duration) + ") was less than " + timeInput)

    print (Fore.BLUE + "test finished" + Fore.RESET)

    dict_resultados(test_date_end, test_date_start, test_duration)    # Dicionario dados teste



if __name__ == '__main__':
    main()