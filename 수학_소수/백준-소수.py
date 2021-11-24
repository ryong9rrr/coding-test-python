import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

sosu = [True] * (n+1)

sosu[0:2] = [False, False]

for num in range(2, int(n**0.5) + 1) :
    if sosu[num] :
        for i in range(num*num, n+1, num) :
            sosu[i] = False

result = [x for x in range(m, n+1) if sosu[x] == True]

if len(result) != 0 :
    print( sum(result) )
    print( min(result) )

else :
    print("-1")