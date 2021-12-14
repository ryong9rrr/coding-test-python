cargo = []
n, k = map(int, input().split())
for _ in range(n):
    w, v = map(int, input().split())
    cargo.append((v, w))

def zero_one_knapsack(cargo, _max):
    capacity = _max
    pack = []
    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])
    return pack

result = zero_one_knapsack(cargo, k)

print(result[-1][-1])