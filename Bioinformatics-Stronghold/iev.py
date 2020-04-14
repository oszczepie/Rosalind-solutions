with open('rosalind_iev.txt') as f:
    pairs = [int(x) for x in f.read().split()]

"""Probabilities of the offspring of each pair to present dominant phenotype:"""
probs = [1, 1, 1, 0.75, 0.5, 0]

print(2 * sum([a * b for a, b in zip(pairs, probs)]))
