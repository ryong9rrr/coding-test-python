from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
number = input()

stack = deque()
i = 0
while i != len(number):
    while K != 0 and stack and stack[-1] < number[i]:
        stack.pop()
        K -= 1
    stack.append(number[i])
    i += 1

while K:
    stack.pop()
    K -= 1

print("".join(stack))