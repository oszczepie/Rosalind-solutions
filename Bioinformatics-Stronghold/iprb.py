data = open("rosalind_iprb.txt", "r")
nums = data.read()
values = nums.split()

k = int(values[0]) #number of dominant homozygotes
m = int(values[1]) #number of heterozygotes
n = int(values[2]) #number of recessive homozygotes

total1 = k + m + n
total2 = total1-1

pk = k/total1 * ((k-1)/total2 + m/total2             + n/total2)
pm = m/total1 * (k/total2     + ((m-1)/total2 * 3/4) + (n/total2 * 2/4))
pn =  n/total1 * (k/total2     + (m/total2 * 2/4)    + ((n-1)/total2 * 0))

P = pk + pm + pn
print(P)
