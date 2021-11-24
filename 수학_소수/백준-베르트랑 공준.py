import sys
input = sys.stdin.readline

while(True) :
    n = int(input())
    
    if(n == 0) :
        break

    sosu = [True] * ((2*n) + 1)
    sosu_list = []

    for num in range(2, int(2*n**0.5)+1) :
        if sosu[num] :
            for i in range(num*num, (2*n)+1, num) :
                sosu[i] = False

    for i in range(n+1, (2*n)+1) :
        if sosu[i]==True :
            sosu_list.append(i)

    print(len(sosu_list))