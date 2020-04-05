data = open("rosalind_fib.txt", "r")
nums = data.read()
values = nums.split()

n = int(values[0]) #number of months
k = int(values[1]) #number of pairs produced by every pair

def fib(n=n, k=k, a=0, b=1):
    return a if n ==0 else fib(n-1, k, a+b, a*k)

total = fib()
print(total)
