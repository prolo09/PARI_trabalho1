#!/usr/bin/env python

""" trabalho PARI 2020/2021 Grupo 2 """

import  argparse


def escolhaModo():

    # escolha do MODO DE TESTE

    global modo # variavel para saber em que modo de jogo estou

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
        print(tes)
        modo = True # modo -true significa que o modo do teste e por tempo limite
        print ("PARI Typing Test, Grupo 2, Outober 2020")  # ?????falta por pari em cor vermelho
        print ("test running up to " + str(args_list['max_value']) + " seconds.")
        return (args_list['max_value'])  # tempo maximo

    else:
        modo= False # modo false quer dizer que o modo do teste e por imputs limite
        print (tes)
        print ("PARI Typing Test, Grupo 2, Outober 2020")  # ????? falta por a cor no pari
        print ("test running up to " + str(args_list['max_value']) + " inputs")
        return (args_list['max_value'])  # imputs maximo














def main():
    escolhaModo()
    print (modo)









if __name__ == '__main__':
    main()










