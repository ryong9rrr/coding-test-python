# 분기를 이용하여 탐색
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())

ans = 0
y = 2 ** (n - 1)
x = y
while n:
    distance = 2 ** (n - 2)
    jump = 4 ** (n - 1)
    if r < x and c < y:
        x -= distance
        y -= distance
    elif r < x and c >= y:
        x -= distance
        y += distance
        ans += jump
    elif r >= x and c < y:
        x += distance
        y -= distance
        ans += jump * 2
    elif r >= x and c >= y:
        x += distance
        y += distance
        ans += jump * 3
    n -= 1

print(ans)

# 모든 부분을 탐색.. -> 시간초과
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N, R, C = map(int, input().split())

ans = 0
def solve(n:int, r:int, c:int):
    global ans
    if n == 2:
        if r == R and c == C:
            print(ans)
            return
        ans += 1
        if r+1 == R and c == C:
            print(ans)
            return
        ans += 1
        if r == R and c+1 == C:
            print(ans)
            return
        ans += 1
        if r+1 == R and c+1 == C:
            print(ans)
            return
        ans += 1
        return
    solve(n // 2, r, c)
    solve(n // 2, r + n // 2, c)
    solve(n // 2, r, c + n // 2)
    solve(n // 2, r + n // 2, c + n // 2)

solve(2**N, 0, 0)