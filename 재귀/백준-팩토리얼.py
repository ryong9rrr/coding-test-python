import sys
input = sys.stdin.readline

def fac(n) :
    return 1 if n<=1 else n*fac(n-1)

n = int(input())

print( fac(n) )