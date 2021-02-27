#!/usr/local/bin/python3.9.1
# Encontrar o numero positivo mais pequeno que é uniformamnete divisivel por todos os números de 1 até 20


# Importar as Livrarias Python necessarias
from math import gcd                # Importar a bibiliteca para funcionalidades Matematicas              
import pyfiglet                     #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo


ascii_banner = pyfiglet.figlet_format("Pinto 3") 
print (ascii_banner) 
print ('')



 
 


######  Inicio do Exercico   ###### 

# Range pedido mais pequeno de 1 até 20 e dar o feedback ao user
numero = range(1,21)

# Encontrar o numero positivo 
def uni(numero):
    x =  1
    for n in numero:
        x = x * n // gcd(x, n)
    return x

# Informação ao utilizador
print ("O numero mais pequeno que é divisivel por todos os números de 1 até 20 é o", uni(numero))

#Realizar calculo com range escolhido
print ('')
print ('---------------------------------------')
print ("Quer escolher os seu proprios valores? ")
print ('---------------------------------------')

# Pedir os valores ao utilizador e guardalos nas variaveis
val_1 = int(input ("Qual o seu 1º Mutiplo? > "))
val_2 = int(input ("Qual o seu 2º Mutiplo? > "))
val_3 = range(val_1,val_2)

#Realizar o calculo com range escolhido
print (" O Range escolhido é:", val_3)
print ('')

def uni(val_3):
    x =  1
    for n in val_3:
        x = x * n // gcd(x, n)
    return x

# Informação ao utilizador
print ("O numero mais pequeno que é divisivel por todos os números escolhidos é", uni(val_3))
