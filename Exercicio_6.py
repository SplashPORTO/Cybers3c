#!/usr/local/bin/python3.9.1
# Programa para apresentar a soma de todos os mutiplos de 3 e 5 abaixo de 1000


# Importar as Livrarias Python necessarias
import pyfiglet                    #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo


ascii_banner = pyfiglet.figlet_format("Pinto 6") 
print (ascii_banner) 
print ('')



 
 



######  Inicio do Exercico   ###### 


# Realizar o calculo do operador sum dentro do range predefenido
def mutiplos(limite):
    return sum([n for n in range(limite) if n%3 == 0 or n%5 == 0])

print ('')
print( "A soma de todos os múltiplos de 3 e 5 abaixo de 1000 é:", mutiplos(1000))
print ('')


#Realizar o calculo do operador sum dentro do range escolhido
print ('---------------------------------------')
print ("Quer escolher os seu proprios valores? ")
print ('---------------------------------------')

# Pedir os valores ao utilizador e guardalos nas variaveis
val_1 = int(input ("Qual o seu 1º Mutiplo? > "))
val_2 = int(input ("Qual o seu 2º Mutiplo? > "))
val_3 = int(input ("Qual o valor maximo da procura? > "))

#Realizar o calculo do operador sum dentro do range escolhido
def mutiplos2(limites):
    return sum([n for n in range(limites) if n%val_1 == 0 or n%val_2 == 0])
print( "A soma de todos os múltiplos de", val_1,"e", val_2,"abaixo de", val_3," é: ", mutiplos2(val_3))
