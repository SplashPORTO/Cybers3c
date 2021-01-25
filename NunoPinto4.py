#!/usr/local/bin/python3.9

# Declaro o Objectivo de ter argumentos em forma de letra maicuscla para comandar a Lista
#           [A] Adiciona Aluno,             [E] Editar Aluno,   [R] Remover Aluno,
#           [L] Lista todos os Alunos,      [S] Sair do programa,


#Importar as Livrarias Python necessarias
import os                       # Sistema Operativo
import sys                      # Mexer no sistema




#LISTA Inicial dos alunos já pre-defenida
Lista = ['Nuno','Joana','Silvana','Fabio','Manuel'] 



## Funçoes de MENU ##

def menu():
    print('''
    Menu:
    [A] Adicionar Aluno,           [E] Editar Aluno,     [R] Remover Aluno,
    [L] Lista todos Alunos,        [S] Sair do programa,
    ''')
  
def ler_letra():
    option = input ("Escolher a LETRA: ").upper() # upper é para transformar tudo em Maisculas
    while option not in "AERLS":
        print ("Erro: LETRA Invalida. ")
        option = input ("Escolher Novamente: ").upper() # upper é para transformar tudo em Maisculas
    return option



## Funçoes de Trabalho por LETRA ##

# L
def li_aluno (Lista):
    print(Lista)
    main()
    
# A
def ad_aluno (Lista):
    print ("Adicionar Aluno na Lista")
    nome = input ("Nome de aluno > ")
    while nome in Lista:
        print ("Erro: Aluno já exite na lista ")
        main ()
    else:
        print ("Aluno adicionado na lista ")
        Lista.append(nome)
        main()

# E
def ed_aluno (Lista):
    print("Aluno a editar na Lista")
    nome = input ("Nome de aluno > ")
    while nome in Lista:
        Lista.remove(nome)
        nome2 = input ("Novo Nome > ")
        Lista.append(nome2)
        print ("Aluno modificado na lista\n")
        main ()
    else:
        print ("Aluno não existente na lista")
        main()

# R
def re_aluno (Lista):
    print ("Aluno a remover na Lista")
    nome = input ("Nome de aluno > ")
    while nome not in Lista:
        print ("Erro: Aluno não exite na lista ")
        main ()
    else:
        print ("Aluno retirado da lista\n")
        Lista.remove(nome)
        main()
  



#_____________MAIN__________________________
def main():

    #MENU
    print('''
    Menu:
    [A] Adicionar Aluno,           [E] Editar Aluno,     [R] Remover Aluno,
    [L] Lista todos Alunos,        [S] Sair do programa,
    ''') 
    
    #Escolha da LETRA do MENU
    option = ler_letra()
    while option != 'S':

        if option == 'L':
            print("......................... Alunos na Lista:\n")
            li_aluno(Lista)
        
        elif option == 'A':
            print("......................... Editar Aluno da Lista\n")
            ad_aluno(Lista)

        elif option == 'E':
            print("......................... Editar Aluno da Lista\n")
            ed_aluno(Lista)
        
        elif option == 'R':
            print("......................... Remover Aluno da Lista\n")
            re_aluno(Lista)
    else:
        print("\nADEUS e Volte Sempre!\n")
        exit()

main()
