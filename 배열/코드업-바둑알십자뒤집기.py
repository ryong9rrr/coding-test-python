import sys
input = sys.stdin.readline

state = []
for _ in range(19):
    n = list(map(int, input().rstrip().split()))
    state.append(n)

num = int(input().rstrip())
for _ in range(num):
    n, m = map(int, input().rstrip().split())
    for i in range(19):
        state[n-1][i] = 1 if state[n-1][i] == 0 else 0
    for i in range(19):
        state[i][m-1] = 0 if state[i][m-1] == 1 else 1

for i in range(19):
    for j in range(19):
        print(state[i][j], end=" ")
    print()
