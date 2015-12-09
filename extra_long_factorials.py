# Enter your code here. Read input from STDIN. Print output to STDOUT
def fac(n):
    prod = n
    while n > 2:
        prod = prod * (n-1)
        n = n - 1
    return prod

N = int(raw_input())
print fac(N)