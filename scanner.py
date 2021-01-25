#!/usr/local/bin/python3.9

#Importar as Livrarias Python necessarias
import os                       # Sistema Operativo
import sys                      # Mexer no sistema
import socket                   # Socket de Rede
import threading                # multiThreading
import datetime                 # Para contagem do tempo ao segundo
import pyfiglet                 #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo





ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print (ascii_banner) 
print ("By: Pinto\n")  
print ('')

#  Pedir o IP da maquina destino fazer scanner
ip = input('[+] Qual o IP da maquina> ')



# Damos feedback ao user do input
print ('')
print ("-" * 50) 
print ("Scanning ao  TCP/IP: " + ip) 
print ("Scanning a iniciar : " + str(datetime.datetime.now())) 
print ("-" * 50)
print ('')

def portScanner (ip,port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                   #Criar aligação via socket
            pp = s.connect_ex((ip, port))
            if pp == 0:
                print ("Porta " +str(port) + "  ::::: Está Aberta")                #Validar se a porta esta Aberta
            else:
                print ("Porta " +str(port) + "  ::::: Está Fechada")               #Validar se a porta esta Fecahda
                s.close()

        #Saidas do programa        
        except socket.gaierror: 
            print ("\n Não foi identificado o IP da Maquina !!!") 
        except socket.error: 
            print ("\n MOcorreu um erro de Comunicaçao !!!")
        except KeyboardInterrupt: 
            print ("\n Saiu do Programa | Scanner !!!")
        except:
            print ("Ocorreu um erro !!!")
    





# #__________________MAIN_____________________
def main():
    t0 = datetime.datetime.now()
    for port in range(80, 111):
        portScanner(ip,port)
        t1 = datetime.datetime.now() -t0 
        print ('Demorou' +str(t1)+ "segundos\n") 
    
main()
