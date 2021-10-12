import sys
input = sys.stdin.readline

array = []

n = int(input())
for _ in range(n):
    s = input().rstrip()
    array.append(s)

def getSum(string:str)->int:
    sum = 0
    for s in string:
        if ord("0") <= ord(s) <= ord("9"):
            sum += int(s)
    return sum

result = sorted(array, key = lambda x: (len(x), getSum(x), x))

for i in result:
    print(i)