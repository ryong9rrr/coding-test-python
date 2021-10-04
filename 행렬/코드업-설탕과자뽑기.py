import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

mtx = [[0]*M for _ in range(N)]

num = int(input().rstrip())
for _ in range(num):
    l, a, n, m = map(int, input().rstrip().split())
    if a == 0:
        for i in range(l) :
            if m-1+i <= M:
                mtx[n-1][m-1+i] = 1
    else:
        for i in range(l):
            if n-1+i <= N:
                mtx[n-1+i][m-1] = 1

for i in range(N):
    for j in range(M):
        print(mtx[i][j], end=" ")
    print()