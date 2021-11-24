import sys
input = sys.stdin.readline

q = int(input())

# 어렵게 풀기..
sosu = [True] * (q+1)
sosu[0:2] = [False, False]

for num in range(2, int(len(sosu)**0.5) +1) :
    if sosu[num] :
        for i in range(num*num, len(sosu), num) :
            sosu[i] = False

# print(sosu)

sosu_of_q = []

for t in range(2, len(sosu)) :
    if sosu[t] :
        sosu_of_q.append(t)

# print(sosu_of_q)

k = 0
while(k<len(sosu_of_q)) :
    if q%sosu_of_q[k] == 0 :
        print(sosu_of_q[k])
        q = q/sosu_of_q[k]
    elif q%sosu_of_q[k] != 0 :
        if k == len(sosu_of_q) - 1 and q != 1 :
            print(q)
        k += 1
