"""
5
3 2 1 1 9
-> 8
"""
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
array = list(map(int, input().split()))
array.sort()

target = 1
for num in array:
    if target < num:
        break
    target += num

print(target)