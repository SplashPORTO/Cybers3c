#!/usr/local/bin/python3.9.1
# Tentar a tecnica de "Brute-Force" num ficheiro zipado com recurso a uma lista de passwords


# Importar as Livrarias Python necessarias
import string, sys, zipfile, os.path            # Importar as biblioteas para String, sistema, Ficeheiros compactados
from tqdm import tqdm                           #_ESPECIAL_  Importo para criar barra de progresso. Primeiro usei o pip3 para instalar este modulo
import pyfiglet                                 #_ESPECIAL_  Importo um tipo de letra. Primeiro usei o pip3 para instalar este modulo


ascii_banner = pyfiglet.figlet_format("Pinto 4") 
print (ascii_banner) 
print ('')
print ("Tem de usar com os seguintes argumentos: zipfile passfile")
print ('')

 
 

######  Inicio do Exercico   ###### 


if len(sys.argv) < 3:
    print ("Faltam argumentos ou nomes incorretos !")
    sys.exit(0)

# Atribuir os ficheiros zipado e de passwords do OS como argumentos 1 e 2
zip_file = sys.argv[1]
pass_file = sys.argv[2]

# Retornar erro se não existir algum dos dois ficheiros necessarios
if os.path.exists(zip_file) == False:
    print("\nFicheiro Zip " + zip_file + " não foi encontrado nesta pasta")
    sys.exit(0) 

if os.path.exists(pass_file) == False:
    print("\nFicheiro de Passwords " + pass_file + " não foi encontrado nesta pasta")
    sys.exit(0) 



# Abrir o ficheiro das password para ver o total de palavras
ficheiro_zipado = zipfile.ZipFile(zip_file)
passW = len(list(open(pass_file, "rb")))
print(" Este ficheiro tem passwords para testar no total:", passW)


# Exprimentar cada palavra do file com passwords no ficheiro zip e lidar com as excções, para sair do programa.
with open (pass_file, "rb") as passList:
    for word in tqdm(passList, total = passW, unit=" word "):
        word = word.strip()
        try:
            ficheiro_zipado.extractall(pwd=word)
        except zipfile.BadZipFile:
            print ("Erro a ler o ficheiro .ZIP")
            sys.exit(0)
        except zipfile.LargeZipFile:
            print ("Ficheiro .ZIP grande")
            sys.exit(0)
        except Exception as Erro:
            if "Password Errada!" in str(Erro):
                pass
            elif "Erro a descomprimir o ficheiro" in str(Erro):
                pass
            else:
                pass
        except KeyboardInterrupt:
                print("Saiu do Programa")
                sys.exit()
        else:
            print(" [OK] Macth de Password # A password é:", word.decode())
            sys.exit(0)

print("[!] SEM Macth de Password # Tente outro ficheiro de com passwords [!]")