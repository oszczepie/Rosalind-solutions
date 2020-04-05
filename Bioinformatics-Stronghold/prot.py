import re
import pyperclip

"""preparing dictionary for translation"""
codon_table = open('prot_table.txt', "r")
tab = codon_table.read()

codons = re.findall('[AUGC]{3}', tab)

aas = re.findall('\s\w\s|Stop', tab)


def cleaning(x):
    x = x.replace(" ", "")
    x = x.replace("\n", "")
    return x
caas = list(map(cleaning, aas))


trans = {}
for i in range(len(codons)):
    trans[str(codons[i])] = caas[i]

"""translation"""
seq = open("rosalind_prot.txt", "r")
s = seq.read()

cods = re.findall(".{3}", s)

translation = ""
for cod in cods:
    if trans[cod] == "Stop":
        break
    else:
        translation += trans[cod]
print(translation)
pyperclip.copy(translation)
    
