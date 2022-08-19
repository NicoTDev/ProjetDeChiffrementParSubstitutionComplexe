import linecache
from Info import alphabet_list
def dechiffre_message(messageFile,keyFile,FinalFile):

    #set-up default setting
    if len(FinalFile) == 0:
        boxFile = open("FinalTextFile.txt", "a")
    else:
        boxFile = open(FinalFile, "a")

    messageFile_inst = open(messageFile,"r")
    boxFile.truncate(0)
    message_dechiffree = ""
    list_of_code = []
    current_index = -1
    #séparer tous les éléments en groupe
    for element in messageFile_inst.read():
        try:
            element = int(element)
            list_of_code[current_index] += str(element)
        except:
            current_index += 1
            list_of_code.append(str(element))

    #trouver toutes les index associés au lettre
    for code in list_of_code:
        #trouver le numéro du pattern
        numero_patern = int(code[1:])
        #aller à la ligne
        line = linecache.getline(keyFile, numero_patern)
        #trouver le caractère correspondant
        current_try = 0
        for letter in line:
            if str(letter) == code[0]:
                message_dechiffree += f"{alphabet_list[current_try]}"
            else:
                current_try += 1
    boxFile.write(message_dechiffree)

