# 리스트 슬라이싱 + sum()
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
for i in range(1, n + 1):
    # i번째 까지의 합을 구한 후
    _sum = sum(data[:i])
    # 결과에 더한다.
    result += _sum

print(result)

#####################################################

# 수학적인 공식 접근
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
for i in range(n):
    # i번 사람은 n - i번 등장한다.
    # 1번 사람 : 5 - 0 = 5번
    # 2번 사람 : 5 - 1 = 4번 ...
    result += data[i] * (n - i)

print(result)

