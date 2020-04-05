sample = open('rosalind_revc.txt', 'r')
s = sample.read()
compl = s.maketrans('ACGT', 'TGCA')
print(s.translate(compl)[::-1])

