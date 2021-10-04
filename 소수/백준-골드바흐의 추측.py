import sys
input = sys.stdin.readline

CASE = int(input())

for _ in range(CASE) :

    NUM = int(input())
    
    # 소수생성
    sosu = [True] * (NUM)
    
    for num in range(2, int(NUM**0.5)+1) :
        if sosu[num] :
            for i in range(num*num, NUM, num) :
                sosu[i] = False

    
    standard_num = int(NUM/2)
    x = [] # NUM/2 이하 소수 리스트
    y = [] # NUM/2 이상 소수 리스트

    for i in range(2, len(sosu)) :
        if sosu[i] :
            if i <= standard_num :
                x.append(i)
                if i == standard_num :
                    y.append(i)
            else :
                y.append(i)

    x.reverse()
    
    i = 0
    j = 0

    while( x[i]+y[j] != NUM ) :
        if x[i]+y[j] < NUM :
            j += 1
        elif x[i]+y[j] > NUM :
            j = 0
            i += 1

    print(f"{x[i]} {y[j]}")