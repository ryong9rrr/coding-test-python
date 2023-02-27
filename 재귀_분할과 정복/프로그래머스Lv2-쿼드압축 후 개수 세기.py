def divide(n, i, j, arr):
    if n <= 1:
        return str(arr[i][j])

    mid = n // 2
    
    a = divide(mid, i, j, arr)
    b = divide(mid, i, j + mid, arr)
    c = divide(mid, i + mid, j, arr)
    d = divide(mid, i + mid, j + mid, arr)

    if len(a) == 1 and a == b == c == d:
        return a
    
    return f"({a + b + c + d})"

def solution(arr):
    result = divide(len(arr), 0, 0, arr)
    return [result.count("0"), result.count("1")]