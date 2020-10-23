#!/usr/bin/env python

""" trabalho PARI 2020/2021 Grupo 2 """

import  argparse
import string
import readchar
import random


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












def ModoTime(time):
    # modo de teste limitado pelo tempo



    e = random.choice(string.ascii_letters)
    e.lower()



def ModoInput(input):
    # modo de teste limitado pelos inputs











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









