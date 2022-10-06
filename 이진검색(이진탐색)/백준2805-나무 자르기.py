# 파라메트릭 서치 기초문제
# python으로는 시간초과, PyPy3로 제출. 262760KB	516ms
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if mid < tree:
            total += (tree - mid)
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    #print(total, mid)

print(result)