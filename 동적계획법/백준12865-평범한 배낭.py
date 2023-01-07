import sys
input = lambda: sys.stdin.readline().rstrip()

def one_zero_knapsack(capacity, cargo):
    n = len(cargo)
    pack = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        v, w = cargo[i - 1]
        for c in range(1, capacity + 1):
            prev = pack[i - 1][c]
            if w <= c:
                pack[i][c] = max(prev, v + pack[i - 1][c - w])
                continue
            pack[i][c] = prev
    return pack[n][capacity]


cargo = []
N, capacity = map(int, input().split())
for _ in range(N):
    w, v = map(int, input().split())
    cargo.append((v, w))

print(one_zero_knapsack(capacity, cargo))