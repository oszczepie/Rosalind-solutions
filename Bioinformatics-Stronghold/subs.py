import pyperclip

with open('rosalind_subs.txt') as s:
    lines = s.read().splitlines()
seq, motif = lines[0], lines[1]

finds = [str(n+1) for n in range(len(seq)) if seq.startswith(motif, n)]

pyperclip.copy(" ".join(finds))
