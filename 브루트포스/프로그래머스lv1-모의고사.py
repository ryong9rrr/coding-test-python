def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    a_i = 0
    b_i = 0
    c_i = 0
    for i, answer in enumerate(answers):
        if answer == a[a_i]:
            score[0] += 1
        if answer == b[b_i]:
            score[1] += 1
        if answer == c[c_i]:
            score[2] += 1
        
        a_i += 1
        b_i += 1
        c_i += 1
            
        if a_i == 5:
            a_i = 0
        if b_i == 8:
            b_i = 0
        if c_i == 10:
            c_i = 0
        
    _max = max(score)
    result = []
    for i in range(3):
        if score[i] == _max:
            result.append(i + 1)
    
    return result

"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (1.61ms, 10.3MB)
테스트 8 〉	통과 (0.45ms, 10.2MB)
테스트 9 〉	통과 (2.32ms, 10.3MB)
테스트 10 〉	통과 (1.10ms, 10.3MB)
테스트 11 〉	통과 (2.45ms, 10.4MB)
테스트 12 〉	통과 (2.55ms, 10.3MB)
테스트 13 〉	통과 (0.14ms, 10.3MB)
테스트 14 〉	통과 (2.49ms, 10.3MB)
"""

# 조금 더 smart한 방법 1 -> 딕셔너리
def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    counts = {
        1: 0,
        2: 0,
        3: 0
    }
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            counts[1] += 1
        if answers[i] == b[i % len(b)]:
            counts[2] += 1
        if answers[i] == c[i % len(c)]:
            counts[3] += 1
    
    _max = max(counts.values())
    result = [x[0] for x in counts.items() if x[1] == _max]
    # sorted(result)를 안해도 무방
    return result

# 조금 더 smart한 방법 1 -> 배열
def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    counts = [0] * 3
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            counts[0] += 1
        if answers[i] == b[i % len(b)]:
            counts[1] += 1
        if answers[i] == c[i % len(c)]:
            counts[2] += 1

    _max = max(counts)
    result = []
    for i in range(3):
        if counts[i] == _max:
            result.append(i + 1)
    # sorted(result) 를 생략해도 무방
    return result

"""
두 결과 모두 비슷하다.

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (1.09ms, 10.4MB)
테스트 8 〉	통과 (0.35ms, 10.2MB)
테스트 9 〉	통과 (2.00ms, 10.3MB)
테스트 10 〉	통과 (0.90ms, 10.3MB)
테스트 11 〉	통과 (2.17ms, 10.3MB)
테스트 12 〉	통과 (1.77ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (2.38ms, 10.3MB)
"""

# 2022년 7월 풀이
# 위 풀이들처럼 하나하나 인덱스로 접근하면 당연히 시간복잡도를 줄일 수 있다.
# 문제와는 관련이 없지만 학생들이 많아질 경우 저렇게 코드를 짤 수는 없음. 따라서 어쩔 수없이 2중 루프를 선택해야 할 것이다.
def solution(answers):
    N = 3
    table = [
        [],
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    result = [0] * (N + 1)

    for i, answer in enumerate(answers):
        for j in range(1, N + 1):
            x = table[j]
            if x[i % len(x)] == answer:
                result[j] += 1
    
    most_value = max(result)

    return sorted([i for i in range(1, N + 1) if result[i] == most_value])
"""
정확성 테스트
테스트 1 〉 통과 (0.01ms, 10.2MB)
테스트 2 〉 통과 (0.01ms, 10.3MB)
테스트 3 〉 통과 (0.01ms, 10.1MB)
테스트 4 〉 통과 (0.01ms, 10.3MB)
테스트 5 〉 통과 (0.04ms, 10.1MB)
테스트 6 〉 통과 (0.05ms, 10.2MB)
테스트 7 〉 통과 (2.98ms, 10.1MB)
테스트 8 〉 통과 (0.94ms, 10.2MB)
테스트 9 〉 통과 (6.12ms, 10MB)
테스트 10 〉 통과 (2.33ms, 10.4MB)
테스트 11 〉 통과 (9.23ms, 10.4MB)
테스트 12 〉 통과 (5.34ms, 10.4MB)
테스트 13 〉 통과 (0.29ms, 10.1MB)
테스트 14 〉 통과 (5.63ms, 10.4MB)
"""