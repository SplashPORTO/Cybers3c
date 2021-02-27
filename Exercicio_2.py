#!/usr/local/bin/python3.9.1
# Criar um programa para Ler quatro valores inteiros e indica quantos são diferentes, quantos são pares e ímpares


# Importar as Livrarias Python necessarias
import collections                  # Para contagem do tempo ao segundo para Dias e hora                
import pyfiglet                     #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo


ascii_banner = pyfiglet.figlet_format("Pinto 2") 
print (ascii_banner) 
print ('')







######  Inicio do Exercico   ###### 


#Declarar Variaveis a ser em usadas
val_1 = int
val_2 = int
val_3 = int
val_4 = int


# Pedir os valores ao utilizador e guardalos nas variaveis
val_1 = input ("Qual o seu 1º valor? > ")
val_2 = input ("Qual o seu 2º valor? > ")
val_3 = input ("Qual o seu 3º valor? > ")
val_4 = input ("Qual o seu 4º valor? > ")

# Guadar valores em lista
Lista = [val_1, val_2, val_3, val_4]
nPar = 0
nInpar = 0

# Fazer analise dos valores entre pares e impares
for v in Lista:
    if v % 2 == 0:
        nPar += 1
    else:
        nInpar += 1


# Contagem de cada um e Diferentes
diferente = collections.Counter(Lista).items()

# Output para o User
print ("Diferentes = ", len(diferente), ("\n Pares = "), len(nPar), ("\n Ímpares = "), len(nInpar) )
