import sys
input = sys.stdin.readline

x, y = map(int, input().split())

sosu = [True] * (y+1)
sosu[0:2] = [False, False]

for num in range(2, int(y**0.5)+1) :
    if sosu[num] :
        for i in range(num*num, y+1, num) :
            sosu[i] = False

for result in range(x, y+1) :
    if sosu[result] :
        print( result )