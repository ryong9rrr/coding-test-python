import sys, math
input = sys.stdin.readline

case = int(input())

for _ in range(case) :
    x, y = map(int, input().split())
    distance = y-x
    i = math.ceil( distance**0.5 )

    if(i**2 - (i-1) > distance) : 
        print(2*i-2)
    else :
        print(2*i-1)