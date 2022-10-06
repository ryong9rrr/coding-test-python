#이진검색 - 46500KB	668ms
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
array = sorted(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

def binary_search(left, right, target_number):
    if left <= right:
        mid = (left + right) // 2
        if array[mid] < target_number:
            return binary_search(mid + 1, right, target_number)
        elif array[mid] > target_number:
            return binary_search(left, mid - 1, target_number)
        else:
            return True
    else:
        return False

for number in numbers:
    if binary_search(0, len(array) - 1, number):
        print(1)
    else:
        print(0)