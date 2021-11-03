import itertools
def solution(numbers):
    n = int("".join(sorted(numbers, reverse=True)))
    # 만들 수 있는 모든 수
    p = set([])
    for i in range(1, len(numbers) + 1):
        for t in list(itertools.permutations(numbers, i)):
            x = "".join(list(t))
            p.add(int(x))
    
    # 소수 리스트
    sosu = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if sosu[i]:
            for j in range(i**2, n + 1, i):
                sosu[j] = False
    
    result = 0
    for n in p:
        n = int(n)
        if n > 1 and sosu[n]:
            result += 1
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.42ms, 10.5MB)
테스트 2 〉	통과 (59.34ms, 15.5MB)
테스트 3 〉	통과 (0.05ms, 10.5MB)
테스트 4 〉	통과 (24.97ms, 12.6MB)
테스트 5 〉	통과 (590.46ms, 36.6MB)
테스트 6 〉	통과 (0.05ms, 10.5MB)
테스트 7 〉	통과 (0.27ms, 10.4MB)
테스트 8 〉	통과 (923.99ms, 53.4MB)
테스트 9 〉	통과 (0.08ms, 10.5MB)
테스트 10 〉	통과 (121.45ms, 18.1MB)
테스트 11 〉	통과 (15.89ms, 11.1MB)
테스트 12 〉	통과 (7.95ms, 10.5MB)
"""