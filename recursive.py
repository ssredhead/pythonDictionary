#a bit of recursion practice with python

N = int(input())

def factorial(x):
    if x==0:
        return 1
    return x * factorial(x - 1)

print factorial(N)
