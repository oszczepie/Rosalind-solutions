with open("rosalind_ini.txt", "r") as f:
    seq = f.read()

counts = [str(seq.count(n)) for n in "ACGT"]
print(' '.join(counts))

