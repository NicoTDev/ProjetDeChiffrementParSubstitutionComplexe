import random
import linecache
from Info import alphabet_list
def chiffrer_un_message(messageFile,keyFile,boxFile):
    messageFile = open(messageFile,"r")

    if len(boxFile) == 0:
        boxFile = open("FinalTextFile.txt", "a")
    else:
        boxFile = open(boxFile, "a")
        boxFile.truncate(0)
    number_of_keyFile_line = len(open(keyFile,"r").readlines())
    message_chiffree = ""
    #prendre toutes les lettres une à une
    for line in messageFile:
        for word in line:
            for letter in word:

                #faire les opérations sur chaque lettre
                        #trouver une ligne aléatoire
                index_of_chose_line = random.randint(1, number_of_keyFile_line)
                line = linecache.getline(keyFile, index_of_chose_line)
                        #trouver l'index de la lettre dans l'ordre alphabétique
                        #trouver la lettre correspondant avec la position alphabétique dans la ligne choisie
                message_chiffree += f"{line[alphabet_list.index(letter.upper())]}{index_of_chose_line}"
    boxFile.write(message_chiffree)


                #print(index_of_chose_line)