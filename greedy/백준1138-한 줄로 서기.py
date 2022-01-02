import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
counts = [0] + list(map(int, input().split()))

result = [0] * (n + 1)

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        # 현재 count가 i번 사람 앞에 있는 사람 수와 같고
        # 자리가 비어있으면
        if count == counts[i] and result[j] == 0:
            result[j] = i
            # 자리를 찾았다면 바로 반복 중단
            break
        # 아직 비어있는 자리가 있다면 i보다 큰 사람이 있다는 자리이므로 +1
        if result[j] == 0:
            count += 1

print(*result[1:])