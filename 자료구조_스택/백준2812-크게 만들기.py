from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
number = input()

stack = deque()

for i in range(n):
    while k and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])
    
# 아직 더 빼야할 숫자가 있다면 pop()
while k:
    stack.pop()
    k -= 1

print("".join(stack))