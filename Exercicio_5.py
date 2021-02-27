#!/usr/local/bin/python3.9.1
# Programa solicita duas letras por ordem alfabetica e retorna ai utilizador a letra do meio se não for impar


# Importar as Livrarias Python necessarias
import random, string                   # Importar para criar numeros aleatorios e trabalhar com strings              
import pyfiglet                         #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo


ascii_banner = pyfiglet.figlet_format("Pinto 5") 
print (ascii_banner) 
print ('')



 
 


######  Inicio do Exercico   ###### 

# Colocar todos os carectares em Letras maiculas para ter só uma fonte.
caracteres = string.ascii_uppercase 

# Pedimos ao utilizador duas leras e colocamos nas variaveis
l1 = input("Qual a sua primeira Letra? \n").upper()
l2 = input("Qual a segunda Letra? \n").upper()

# Damos feedback ao utilizador
print ("As letras escolhidas são: ", l1," ",l2 )

# Onde fazemos o cauculo da posição da letra
posi1 = caracteres.find(l1) 
posi2 = caracteres.find(l2) 

encontraLetra = (posi1 + posi2)/2 

# Usamos o if para caso seja Par (maior que um) ou impar e damos informação ao utilizaodr
if posi1 > posi2:
 encontraLetra = encontraLetra + 0.5
 print ("A letra que fica mais a meio da primeira e segunda letra é: ", caracteres[int(encontraLetra)])
else:
 print ("A letra que fica mais a meio da primeira e segunda letra é: ", caracteres[int(encontraLetra)])

