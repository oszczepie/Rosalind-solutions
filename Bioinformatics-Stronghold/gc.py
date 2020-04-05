import re

sample = open("rosalind_gc.txt", "r")
seqs = sample.read()
#print(seqs)

seqReg = re.compile(r'''
                     >(.*)\n
                     (
                     [ATGC$\n]+
                     )
                     ''', re.VERBOSE)

full = dict(seqReg.findall(seqs))
#print(full)

for key, value in full.items():
    full[key] = value.replace('\n', '')
#print(full)

for key, value in full.items():
    full[key] = (value.count('G')+value.count('C'))/len(value)*100
#print(full)

final = sorted(full.values(), reverse=True)
#print(final)

finalkey = [key for (key, value) in full.items() if value == final[0]]
print(finalkey[0], "\n", final[0])
