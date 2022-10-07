#파라메트릭 서치
"""
두 가지 풀이가 있는데, 전체적인 로직은 동일하지만 풀이에 따라 등호를 설정해야하는 부분이 다르다.
등호만 다른 것일뿐, 로직은 동일해서 시간은 같음.
"""

"""
<인덱스만으로 값을 판별하는 풀이 - 40044KB	544ms>
1. 처음 상한에 +1을 하고
2. 마지막에 하한에 -1을 한다.
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

left = 1
right = houses[-1] - houses[0] + 1

def install(distance):
    installed = [] #공유기가 설치된 집
    house = houses[0] #첫번째 집은 무조건 공유기를 설치하겠다고 가정
    installed.append(house)
    for i in range(1, N):
        #공유기를 설치할 수 있다면 설치하고 가장 최근에 설치한 집으로 갱신
        if houses[i] >= house + distance:
            installed.append(houses[i])
            house = houses[i]
    return len(installed)

while left < right:
    mid = (left + right) // 2
    #공유기를 설치한 집이 C보다 적다면 거리를 좁힌다.
    if install(mid) < C:
        right = mid
    #그렇지 않다면 거리를 늘린다.
    else:
        left = mid + 1

print(left - 1)


"""
<매번 result를 갱신하는 풀이 - 40044KB	544ms>
상한과 하한에 +1, -1을 하지않고 최적해를 매번 갱신
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

left = 1
right = houses[-1] - houses[0]

def install(distance):
    installed = [] #공유기가 설치된 집
    house = houses[0] #첫번째 집은 무조건 공유기를 설치하겠다고 가정
    installed.append(house)
    for i in range(1, N):
        #공유기를 설치할 수 있다면 설치하고 가장 최근에 설치한 집으로 갱신
        if houses[i] >= house + distance:
            installed.append(houses[i])
            house = houses[i]
    return len(installed)

result = 0

while left <= right:
    mid = (left + right) // 2
    #공유기를 설치한 집이 C보다 적다면 거리를 좁힌다.
    if install(mid) < C:
        right = mid - 1
    #그렇지 않다면 거리를 늘리고, 최적해를 갱신한다.
    else:
        left = mid + 1
        result = mid

print(result)