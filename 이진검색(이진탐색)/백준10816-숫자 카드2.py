# 이분탐색
# 112328KB	4484ms
# 같은 값을 가지는 숫자들이 여러 개인 상황에서 갯수를 세려면
# 가장 낮은 인덱스, 가장 높은 인덱스를 찾는 함수 2개를 구현해야한다.
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

def lower(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if target <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def upper(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if target < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

for target in targets:
    lo = lower(numbers, target)
    hi = upper(numbers, target)
    print(hi - lo, end=" ")


##############################################################################
# bisect 모듈 사용
# 114356KB	1740ms
import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right

N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    lo = bisect_left(numbers, target)
    hi = bisect_right(numbers, target)
    print(hi - lo, end=" ")