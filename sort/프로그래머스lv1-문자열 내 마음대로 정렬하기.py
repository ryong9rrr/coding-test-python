def solution(strings, n):
    return sorted(sorted(strings), key = lambda x : x[n])

# 또는
def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))