# <2022 8월 프로그래머스 모의테스트 1회 1번문제>
# 집합을 사용하지 않으면 시간초과
from collections import defaultdict
def solution(X, Y):
    table_x = defaultdict(int)
    table_y = defaultdict(int)

    for n in X:
        table_x[n] += 1

    for n in Y:
        table_y[n] += 1

    intersection = set(table_x.keys()) & set(table_y.keys())

    strings = ""
    for n in list(intersection):
        count = min(table_x[n], table_y[n])
        strings += n * count

    result = sorted(strings, reverse = True)

    if not result:
        return "-1"

    if result[0] == "0":
        return "0"

    return "".join(result)