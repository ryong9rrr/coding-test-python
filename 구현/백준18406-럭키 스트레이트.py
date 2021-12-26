import sys
input = lambda : sys.stdin.readline().rstrip()

n = input()
mid = len(n) // 2
left = sum(map(int, n[:mid]))
right = sum(map(int, n[mid:]))

print("LUCKY") if left == right else print("READY")