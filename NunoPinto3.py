#!/usr/bin/python3

# Este Terceiro exercico abre dois ficheiros uma para ips e outra para portas

# Declarar variaveis
ipLista = []
portLista = []
mynet = "100.100.100."

# Cumprimento ao Professor antes de abrir o ficheiro
print ("\nOlá Professor \n Fabio\n")
print ("\nVisualizar as duas listas, uma com Ip´s e outra com Portas: \n")


# Criar ficheiros e gravar
ipFile = open("ips.txt", "w")
portFile = open("ports.txt", "w")

#Cirar a lista dos ips e escrever no ficheiro
for ip in range(1, 256):
    ipLista.append(mynet+str(ip))
    ipFile.write(mynet + str(ip) + '\n')

#Cirar a lista dos Portos e escrever no ficheiro
for port in range(1, 1025):
    portLista.append(str(port))
    portFile.write(str(port) + '\n')


# Fechar os ficheiros abertos.
ipFile.close()
portFile.close()

# Visualizar as listas criadas no Terminal
print(ipLista)
print(portLista)



