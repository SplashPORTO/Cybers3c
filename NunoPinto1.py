#!/usr/local/bin/python3.9

#Declaro Variaveis que vou usar
a = 1
b = 2


# Cumprimento ao Professor
print ("\nOlá Professor \n Fabio\n")


#Numero do Exercico de aula
print("Exercicios da aula n.1")

#Operação Aritmética entre 2 variáveis tipo integer
print("Aritmética entre 2 variáveis: ")
print ('a = 1 \nb = 2 \n(a + b) =',(a + b))
print ('\n')


#Operação Relacional entre 2 variáveis tipo integer
print ("Relacional entre 2 variáveis: ")
print ('a = 1 \nb = 2 \n(a < b) =',(a < b))
print ('\n')

#Operação binaria entre 2 variáveis tipo integer
print ("Binario entre 2 variáveis do tipo inteiro: ")
c = (bin(a) + bin(b))
print ("a = 1 \nb = 2 \nBinario de (a + b) = ",(c))
print ("Binario de a and b = ", (bin(a|b)))
print ("Binario de 1 = ", (bin(1)))
print ("Binario de 2 = ", (bin(2)))
print ("Binario de 3 = ", (bin(3)))
print ('\n')

#Operação relacional 2 variáveis tipo integer
print ("Relacional entre a > b : ")
m = (a > b)
print (m)
print ('\n')

#Operação associação entre 2 variáveis
print ("Operacao associacao entre variaveis para retornar Verdadeiro ou Falso")
print ("\nValor guardados na lista")
lista = [10,20,30,40,50,60,70,80,90,100]
print (lista)
print ("\nValor escolhido 50 que tera retorno Verdadeiro")
ln = 50 in lista
print (ln)
print( "\nValor escolhido 200 que tera retorno Falso")
ln = 200 in lista
print (ln)
print ("\n")

