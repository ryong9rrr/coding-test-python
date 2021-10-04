import sys
input = sys.stdin.readline

def check_type(num):
    if num - int(num) == 0 :
        return int(num)
    else :
        return 99999;

n = int(input())

all_arr = []

if n < 3 :
    print("error")

a=0

while 3*a <= n :
    b = (n-3*a)/5
    all_arr.append([a, b])
    a+=1

cases =  list(map(lambda arr : sum(arr), all_arr))
result = list(map(lambda num : check_type(num) , cases ))

if min(result) == 99999 :
    print("-1")
else :
    print(min(result))