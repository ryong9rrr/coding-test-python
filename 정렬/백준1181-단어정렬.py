import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

arr.sort(key= lambda x:(len(x), x))

for i in range(n):
    if i > 0 and arr[i] == arr[i - 1]:
        continue
    print(arr[i])