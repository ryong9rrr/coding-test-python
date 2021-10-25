import sys
input = lambda : sys.stdin.readline().rstrip()

test_case = int(input())

while test_case:
    array = []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        array.append((a, b))

    s_arr = sorted(array, key= lambda x:x[0])
    count = 0
    min = 100001
    for i in range(n):
        if min > s_arr[i][1] :
            min = s_arr[i][1]
            count += 1
    print(count)
    test_case -= 1