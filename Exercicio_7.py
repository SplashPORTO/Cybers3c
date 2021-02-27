#!/usr/local/bin/python3.9.1
# Criação de password seguras de 8 a 32 caratectres


# Importar as Livrarias Python necessarias
import random, string                   # Importar para numeros aleatorios e strings            
import pyfiglet                         #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo


ascii_banner = pyfiglet.figlet_format("Pinto 7") 
print (ascii_banner) 
print ('')



 



######  Inicio do Exercico   ###### 

tamanho = 0 
password = "" 
caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 

# Abrir o ficheiro para guardar as passwords geradas
file = open("pass_geradas.txt","a") 

# Criação da password
while tamanho < 8 or tamanho > 32:

    print ('------------------------------------------------')
    tamanho = int(input("Escolha de 8 a 32 para criar sua password?\n >"))
    print ('')

    # Testar se o numero escolhido esta no range se sim criar a password
    if tamanho < 8 or tamanho > 32:
        print ("Numero escolhido fora do range!")
    else: 
        print ("A criar uma password aleatoria de", tamanho,"Caracteres")
        print ('')
        for x in range (tamanho):
            password += random.choice(caracteres)
        print ('                  ---------------------------------')
        print ("A sua password é: ", password, sep="" ) 
        print ('                  ---------------------------------')
        print ('')
        file.write( password + "\n")


file.close()