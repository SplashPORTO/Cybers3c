#!/usr/local/bin/python3.9

#Importar as Livrarias Python necessarias
import os                       # Sistema Operativo
import sys                      # Mexer no sistema
import socket                   # Socket de Rede
import threading                # Thread
from datetime import datetime   # Para contagem do tempo


#_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo
import pyfiglet








#__________________MAIN_____________________

# Uso o tipo de font para escrever Port Scanner no ecra
ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print (ascii_banner) 

# Programer
print ("By: Pinto\n")  
print ('') 
#
#  Pedir o IP da maquina destino fazer scanner
destino = input('[+] Qual o IP da maquina> ')

  
# Damos feedback ao user do input
print ('')
print ("-" * 50) 
print ("Scanning ao  TCP/IP: " + destino) 
print ("Scanning a iniciar : " + str(datetime.now())) 
print ("-" * 50)
print ('')



# Definimos a maquina a inspecionar
def portscanner (destino,porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #Criar aligação via socket
        Resultado = sock.connect_ex (destino, porta)                    #Conectar o socket ao destino
        t0 = datetime.datetime.now()
        for porta in range (1,1025):
            thread = threading.Thread(target = portscanner, args=(destino,porta))
            thread.start()
            thread.join()
            t1 = datetime.datetime.now () -t0
            print ('Demorou' +str(t1)+ "segundos")

        if Resultado == 0:
            print ("Porta " +str(porta) + "Está Aberta")                #Validar se a porta esta aberta
        else:
            print ("Porta " +str(porta) + "Está Fechada")               #Apresentar o Resultado
            sock.close()

    #Saidas do programa         
    except KeyboardInterrupt: 
        print ("\n Saiu do Programa | Scanner!!!!") 
        sys.exit() 
    except socket.error: 
        print ("\n Maquina não activa !!!!") 
        sys.exit()
