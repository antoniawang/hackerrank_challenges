# Enter your code here. Read input from STDIN. Print output to STDOUT
def fib(a,b,n):
    lst = [a, b]
    i = 3
    while i <= n:
        c = lst[0]
        d = lst[1]
        tot = c+d**2
        lst.append(tot)
        lst = lst[1:]
        i+=1
    return tot

ilist = raw_input().split()
A=int(ilist[0])
B=int(ilist[1])
N=int(ilist[2])

print fib(A,B,N)