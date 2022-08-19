from random import sample
from Info import alphabet_list
def Make_patern(number_of_patern=10, file:str= "patern_file"):
    f = open(file, "a")
    f.truncate(0)
    for _ in range(number_of_patern):
        f.write("".join(sample(alphabet_list, len(alphabet_list))))
        f.write("\n")
    f.close()