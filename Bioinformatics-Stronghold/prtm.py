import re
import pyperclip
import timeit

mass_table = open('monoisotopicmasstable.txt', "r")
table = mass_table.read()

def firstway():
    aas = re.findall("[A-Z]", table)
    mass = re.findall("\d+\.\d+", table)
    trans = {}
    for i in range(len(aas)):
        trans[aas[i]] = mass[i]
#firstway()

def secondway():
    whole =  table.split()
    trans = dict(zip(whole[0::2],
                     map(float, whole[1::2])))
    return trans
trans = secondway()

#print(timeit.timeit(firstway, number=100000))
#print(timeit.timeit(secondway, number=100000))

protein_seq = open('rosalind_prtm.txt', 'r')
protein = protein_seq.read()[:-1]

themass = 0
for a in protein:
    themass += trans[a]

pyperclip.copy(themass)

