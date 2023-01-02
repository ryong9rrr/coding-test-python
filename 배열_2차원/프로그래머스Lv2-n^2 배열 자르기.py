def judge_value(index, n):
    a, b = divmod(index, n)
    if a < b:
        return b + 1
    return a + 1

def solution(n, left, right):
    sliced_index_arr = [x for x in range(left, right + 1)]
    return [judge_value(x, n) for x in sliced_index_arr]

"""
정확성  테스트
테스트 1 〉	통과 (19.70ms, 16.2MB)
테스트 2 〉	통과 (24.15ms, 19.2MB)
테스트 3 〉	통과 (23.20ms, 19.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (22.35ms, 18.4MB)
테스트 7 〉	통과 (24.09ms, 19MB)
테스트 8 〉	통과 (20.64ms, 17.5MB)
테스트 9 〉	통과 (23.50ms, 18.9MB)
테스트 10 〉	통과 (24.47ms, 18.4MB)
테스트 11 〉	통과 (31.21ms, 18.5MB)
테스트 12 〉	통과 (21.00ms, 17.9MB)
테스트 13 〉	통과 (23.40ms, 18.2MB)
테스트 14 〉	통과 (23.29ms, 18.1MB)
테스트 15 〉	통과 (21.19ms, 17.9MB)
테스트 16 〉	통과 (22.75ms, 18.5MB)
테스트 17 〉	통과 (25.90ms, 18.5MB)
테스트 18 〉	통과 (25.37ms, 19.2MB)
테스트 19 〉	통과 (24.90ms, 18.6MB)
테스트 20 〉	통과 (22.12ms, 18MB)
"""