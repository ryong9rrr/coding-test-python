import sys
input = sys.stdin.readline

mtx = []

for _ in range(10):
    N = list(map(int, input().rstrip().split()))
    mtx.append(N)
# start => move([1,1])
def move(state):
    [n, m] = state
    # if search food, stop
    if mtx[n][m] == 2:
        mtx[n][m] = 9
        return
    # if meet wall, stop
    elif mtx[n][m+1] == 1 and mtx[n+1][m] == 1:
        mtx[n][m] = 9
        return
    # move
    else:
        if mtx[n][m+1] == 1:
            mtx[n][m] = 9
            move([n+1, m])
        else:
            mtx[n][m] = 9
            move([n, m + 1])

move([1,1])

for i in range(10):
    for j in range(10):
        print(mtx[i][j], end=" ")
    print()