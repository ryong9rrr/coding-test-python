# 일반적 이분매칭 알고리즘, input 정보를 바탕으로 graph를 구현하는 것이 관건이었음.
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

def dfs(x):
    for node in graph[x]:
        if c[node]:
            continue
        c[node] = True
        if d[node] == 0 or dfs(d[node]):
            d[node] = x
            return True
    return False

graph = defaultdict(list)
stat = defaultdict(list)
n = int(input())
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for s in info:
        stat[i].append(s)

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        # 스탯이 모두 동일한 경우
        if stat[i][0] == stat[j][0] and stat[i][1] == stat[j][1] and stat[i][2] == stat[j][2]:
            graph[i].append(j)
        elif stat[i][0] >= stat[j][0] and stat[i][1] >= stat[j][1] and stat[i][2] >= stat[j][2]:
            graph[i].append(j)
        elif stat[i][0] <= stat[j][0] and stat[i][1] <= stat[j][1] and stat[i][2] <= stat[j][2]:
            graph[j].append(i)
d = [0] * (n + 1)
count = 0
for k in range(2):
    for i in range(1, n + 1):
        c = [False] * (n + 1)
        if dfs(i):
            count += 1

print(n - count)