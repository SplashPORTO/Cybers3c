#!/usr/local/bin/python3.9.1
# Criar programa para converter um valor em segundo em horas, minutos e segundos


# Importar as Livrarias Python necessarias
import datetime                     # Para contagem do tempo ao segundo para Dias e hora
import time                         # Para ler da maquian o actual ano e horas e minutos                  
import pyfiglet                     #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo

ascii_banner = pyfiglet.figlet_format("Pinto 1") 
print (ascii_banner) 
print ('')







######  Inicio do Exercico   ###### 


#  Pedir os segundos a serem calculados
Isec = float(input(' Quantos segundos deseja calcular? > '))

DIA = Isec // (24*3600)
Isec= Isec %(24*3600)

HORA = Isec // 3600
Isec%=3600

MINUTOS= Isec // 60
Isec%=60

SEC=Isec


# # # Damos feedback ao user do input Para a data de Hoje
print ('\n')
print ("-" * 40) 
print (" Seus segundos em regoligo são:")
print ('     %d:%d:%d:%d' %(DIA,HORA,MINUTOS,SEC))
print ("-" * 40)
print ('')


# Damos feedback ao user da data actual
print ('')
print (" A sua informação foi procecesada em:")
print ("-" * 40) 
relogio = time.ctime()
print(relogio)
print ("-" * 40)
print ('')