"""
파라메트릭 서치 (30840KB	120ms)

- end값에 + 1을 해줘야함. 
- 그리고 이분탐색은 항상 등호를 잘 신경써줘야한다는 것이 헷갈린다..
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

start = 0
end = max(numbers) + 1

while start < end:
    count = 0
    mid = (start + end) // 2
    for number in numbers:
        count += (number // mid)
    if count < K:
        end = mid
    else:
        start = mid + 1

print(start - 1)