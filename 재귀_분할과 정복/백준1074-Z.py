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

##########################################################################

### 나의 방법

##########################################################################


#분할정복 다른 방법 // 하지만 역시나 사실상 완전탐색이므로 시간초과
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())
count = 0
def divide(n, i, j):
    global result, count
    if n == 2:
        for x in range(2):
            for y in range(2):
                #print(i + x, j + y)
                if i + x == r and j + y == c:
                    print(count)
                    return
                count += 1
        return
    else:
        mid = n // 2
        divide(mid, i, j)
        divide(mid, i, j + mid)
        divide(mid, i + mid, j)
        divide(mid, i + mid, j + mid)

divide(2 ** n, 0, 0)

# 위 방법에서 최적화로 풀이 성공!!
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())
count = 0
def divide(n, i, j):
    global count
    if n == 2:
        for x in range(2):
            for y in range(2):
                #print(i + x, j + y)
                if i + x == r and j + y == c:
                    print(count)
                    return
                count += 1
        return
    else:
        mid = n // 2
        jump = mid ** 2
        # 필요한 부분만 재귀호출 합니다.
        # a 탐색
        if r < i + mid and c < j + mid:
            #print("a", i, j)
            divide(mid, i, j)
        # b 탐색
        elif r < i + mid and c >= j + mid:
            #print("b", i, j + mid)
            count += jump
            divide(mid, i, j + mid)
        # c 탐색
        elif r >= i + mid and c < j + mid:
            #print("c", i + mid, j)
            count += jump * 2
            divide(mid, i + mid, j)
        # d 탐색
        elif r >= i + mid and c >= j + mid:
            #print("d", i + mid, j + mid)
            count += jump * 3
            divide(mid, i + mid, j + mid)

divide(2 ** n, 0, 0)