#!/usr/local/bin/python3.9

# Declaro o Objectivo de ter argumentos em forma de letra maicuscla para comandar a Lista
#           [A] Adiciona Directorio,        [E] Eliminar Directorio,   [R] Renomear Directorio,
#           [L] Lista Directorios,          [S] Sair do programa,


#Importar as Livrarias Python necessarias
import os, os.path                       # Sistema Operativo
import sys                               # Mexer no Sys
path = '.'



## Funçoes de MENU ##

def menu():
    print('''
    Menu:
    [A] Adicionar Directorio,           [E] Eliminar Directorio,     [R] Renomear Directorio,
    [L] Lista Directorios,              [S] Sair do programa,
    ''')
  
def ler_letra():
    option = input ("Escolher a LETRA: ").upper() # upper é para transformar tudo em Maisculas
    while option not in "AERLS":
        print ("Erro: LETRA Invalida. ")
        option = input ("Escolher Novamente: ").upper() # upper é para transformar tudo em Maisculas
    return option



## Funçoes de Trabalho por LETRA ##

# L
def li_dir ():
    print (os.listdir(path))
    main()
    
# A
def ad_dir ():
    print ("Adicionar Directorio")
    nome = input ("Nome do Directorio > ")
    while nome in os.listdir(path):
        print ("Erro: Directorio já exite")
        main ()
    else:
        print ("Directorio Adicionado")
        os.mkdir(nome)
        main()

# E
def rd_dir ():
    print ("Eliminar Directorio")
    nome = input ("Nome de Directorio > ")
    while nome not in os.listdir(path):
        print ("Erro: Directorio não exite")
        main ()
    else:
        print ("Directorio Eliminado\n")
        os.removedirs(nome)
        main()

# R
def re_dir ():
    print("Renomear o Directorio ")
    nome = input ("Nome do Directorio > ")
    while nome in os.listdir(path):
        nome2 = input ("Novo Nome > ")
        os.rename(nome, nome2)
        print ("Directorio Alterado\n")
        main ()
    else:
        print ("Directorio não existente")
        main()



#_____________MAIN__________________________
def main():

    #MENU
    print('''
    Menu:
    [A] Adicionar Directorio,           [E] Eliminar Directorio,     [R] Renomear Directorio,
    [L] Lista todos Directorios,        [S] Sair do programa,
    ''') 
    
    #Escolha da LETRA do MENU
    option = ler_letra()
    while option != 'S':

        if option == 'L':
            print("......................... Lista Directorios:\n")
            li_dir()
        
        elif option == 'A':
            print("......................... Adicionar Directorio\n")
            ad_dir()

        elif option == 'E':
            print("......................... Eliminar Directorio\n")
            rd_dir()
        
        elif option == 'R':
            print("......................... Renomear Directorio\n")
            re_dir()
    else:
        print("\nADEUS e Volte Sempre!\n")
        exit()

main()
