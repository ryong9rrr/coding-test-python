# 그냥 큐를 사용하기
from collections import deque
def solution(A, B):
    q = deque(A)
    i = 0
    while i < len(A):
        x = "".join(q)
        if x == B:
            return i
        q.rotate(1)
        i += 1
    return -1

# find 메서드 사용하기
def solution(A, B):
    index = (A + A).find(B)
    if index > 0:
        index = len(A) - index
    return index

# 반대로 생각하기
def solution(A, B):
    return (B + B).find(A)