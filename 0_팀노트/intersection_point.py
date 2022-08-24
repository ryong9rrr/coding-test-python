# 두 직선 A, B의 교점 (Px, Py)를 구하는 함수
# A = B = [number, number, number]
# 직선이 평행하거나 일치한다면 None을 리턴한다.
def intersection_point(A, B):
    a1, b1, c1 = A
    a2, b2, c2 = B
    numerator = (b1 * c2) - (b2 * c1)
    denominator = (a1 * b2) - (a2 * b1)
    if denominator == 0:
        return None
    Px = numerator / denominator
    Py = ((-1 * (a1 / b1)) * Px) - (c1 / b1)
    return [Px, Py]