#시간초과
N = int(input())

def check(queens, row):
    for i in range(row):
        if queens[i] == queens[row] or abs(queens[i] - queens[row]) == abs(i - row):
            return False
    return True

def search(queens, row):
    count = 0
    if N == row:
        return 1
    for col in range(N):
        queens[row] = col
        if check(queens, row):
            count += search(queens, row + 1)
    return count

queens = [-1] * N
print(search(queens, 0))


#시간초과
N = int(input())

check_cols = [False] * N
check_d1 = [False] * N * 2
check_d2 = [False] * N * 2

def search(row):
    count = 0
    if row == N:
        return 1
    for i in range(N):
        d1 = row + i
        d2 = row - i + N
        if check_cols[i] == False and check_d1[d1] == False and check_d2[d2] == False:
            check_cols[i] = True
            check_d1[d1] = True
            check_d2[d2] = True
            count += search(row + 1)
            check_cols[i] = False
            check_d1[d1] = False
            check_d2[d2] = False
    return count

print(search(0))