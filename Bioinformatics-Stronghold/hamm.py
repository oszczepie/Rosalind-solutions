#sample1 = open('rosalind_dna.txt', 'r')
#s = sample1.read()[:50]

#sample2 = open('rosalind_rna.txt', 'r')
#t = sample2.read()[:50]



def hamm_dist(s, t):
    return sum(a != b for a, b in zip(s, t))

answer = hamm_dist('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
print(answer)
