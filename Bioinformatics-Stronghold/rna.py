sample = open('rosalind_rna.txt', 'r')
t = sample.read()

sc = t.replace('T', 'U')
print(sc)

import re
us = re.compile('T')
u2 = us.sub('U', t)
print(u2)


