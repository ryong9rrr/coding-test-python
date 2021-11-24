import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

sum = 0

for number in numbers :
    if(number > 1) :
        sosu = []
        i=1
        while(i <= number**0.5) :
            if(number % i == 0) :
                sosu.append(i)
            if(len(sosu) > 1) :
                break
            i+=1
        if(len(sosu) == 1) :
            sum += 1
    
print(sum)