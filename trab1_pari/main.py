#!/usr/bin/env python

""" trabalho PARI 2020/2021 Grupo 2 """

import  argparse
import string
import readchar
import random
from time import time
from collections import namedtuple
from colorama import Fore

input = namedtuple('Input', ['requested', 'received','duration']) # t tempo ls letra aleatoria lr letra introduzida

def escolhaModo():

    # escolha do MODO DE TESTE

    global modo # variavel para saber em que modo de jogo estou
    global timeInput # variavel que guarda os tempo ou o input

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
        timeInput= (args_list['max_value'])  # tempo maximo

    else:
        modo= False # modo false quer dizer que o modo do teste e por imputs limite
        print (tes)
        print ("PARI Typing Test, Grupo 2, Outober 2020")  # ????? falta por a cor no pari
        print ("test running up to " + str(args_list['max_value']) + " inputs")
        timeInput= (args_list['max_value'])  # imputs maximo










def letter_time_counter():

    '''?????fazer com que o programa so aceite letras '''


    letter = random.choice(string.ascii_letters) # gera letras em maiusculas e minusculas
    letter = letter.lower() # converte para minusculas
    print('type letter: ' + letter)
    Start=time() # tempo inicio


    while True:  # serve para so premitir que seja inseridas letras e nao carateres
        ins_letter = readchar.readchar() # pede para inserir uma letra
        asrletter=ord(ins_letter)
        if (asrletter >97) and (asrletter<122):
            break


    Stop= time() # tempo final

    if letter == ins_letter:
        print('you typed letter: ' + Fore.GREEN + ins_letter + Fore.RESET)
    else:
        print('you typed letter: ' + Fore.RED + ins_letter + Fore.RESET)


    time_elapsed = Stop-Start # tempo de insersao da letra


    return input( requested=letter,received=ins_letter,duration=time_elapsed)




def ModoTime(Time):
    # modo de teste limitado pelo tempo

    list=[]

    for x in range(1,3):




            list.append(letter_time_counter())



    print (list[1].duration)






    timeinicio=time()
    timeduracao=int(timeinicio)+int(Time)


   # while True:
    #    timeinicio=time()
     #   if timeinicio!=timeduracao:

      #      print
       # else:
        #    break









def ModoInput(input):
    # modo de teste limitado pelos inputs
    list = []

    for x in range(0, int(input)):
        list.append(letter_time_counter())













def main():

    escolhaModo()
    print ("Press any key to start the test")
    readchar.readchar() # para imprimir uma tecla qualquer para continuar o teste




    if modo:
      ModoTime(timeInput)
    else:
      ModoInput(timeInput)







if __name__ == '__main__':
    main()


