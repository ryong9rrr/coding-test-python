"""
첫째줄에 떡의 개수, 요청한 떡의 길이
둘째줄에 떡들의 길이
요청한 떡의길이를 만들기 위해 절단할 수 있는 떡의 최대길이는?
4 6
19 15 10 17
-> 15

전형적인 이진탐색문제
parametric search 유형 문제
- 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
"""
n, target = 4, 6
data = [19, 15, 10, 17]

start = 0
end = max(data)

result = 0
# 파라메트릭 서치유형은 재귀보다는 반복문이 더 간단할 수 있음.
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in data:
        #중간길이로 떡을 잘랐을 때 남는 떡의 길이 합
        if mid < x:
            total += x - mid
    if total < target:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result) # 15