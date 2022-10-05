#1) functools를 사용한 방법, 하지만 느리다. 60696KB 944ms
import sys
import functools
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
table = []
for _ in range(N):
    row = input().split()
    for i in range(1, 4):
        row[i] = int(row[i])
    table.append(row)

def compare(a, b):
    if a[1] != b[1]:
        return b[1] - a[1]
    else:
        if a[2] != b[2]:
            return a[2] - b[2]
        else:
            return b[3] - a[3]

# 마지막에는 이름 순으로 정렬해야해서 일단 정렬
table.sort()

result = sorted(table, key=functools.cmp_to_key(compare))

for name in [x[0] for x in result]:
    print(name)

#2. 그냥 sort 함수를 잘 쓰기, 69808KB	532ms
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
table = []
for _ in range(N):
    row = input().split()
    for i in range(1, 4):
        row[i] = int(row[i])
    table.append(row)

# 1. 값을 -로 주면 역정렬시킴
# 2. 같은 값일 경우 다음 조건으로 넘어감
result = sorted(table, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name in [x[0] for x in result]:
    print(name)