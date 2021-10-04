import sys
input = sys.stdin.readline
cnt = 0

N = int(input())

for _ in range(N) :
    word = input().rstrip()
    temp = [word.index(i) for i in word]
    if temp == sorted(temp) :
        cnt += 1

print(cnt)