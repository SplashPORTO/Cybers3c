#!/usr/bin/python3

# Este segundo exercico abre um ficheiro para poder escrever o resultado de uma busca na lista

#Declarar Variavei
# Variavel (os) em forma de Lista, com Sistemas Operativos
os = ["MacOS", "LinuX", "Windows", "Solaris", "Android", "iOS"]


# Cumprimento ao Professor antes de abrir o ficheiro
print ("\nOlá Professor \n Fabio\n")

# Abre o ficheiro com o o nome Busca.txt e escreve la dentro
file = open("Busca.txt", "w")
file.write("Lista de Sistemas Operativos usando o (for)\n")

 
# Retirar o nome Solaris da lista e escreve os restantes
for L in os:
    if L != "Solaris":
        print(L)
        file.write(str(L)+"\n")
print("\n \n")

#Escreve o resultado no ficheiro
print ("Aguarde, a escrever no ficeiro")
file.write("\n")


# Lista e escreve os a Lista usando LooP
print ("Vamos usar um (Loop - while)" "\n" ) 
file.write("\n" + "Listagem usado um (Loop - while)" + "\n")

x = 0
while x < len(os):
    if os[x] != "Solaris":
        print (os[x])
        file.write(str(os[x]) + "\n")
    x += 1

 # Fecha o ficheiro para ficar disponivel
file.close()
