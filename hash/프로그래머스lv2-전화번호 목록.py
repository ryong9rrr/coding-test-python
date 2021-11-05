# 데이터의 개수가 백만개이기 때문에 n^2으로는 통과할 수 없음
def solution(phone_book):
    phone_book = sorted(phone_book)
    n = len(phone_book)
    for i in range(0, n):
        c = phone_book[i]
        l = len(c)
        for j in range(i + 1, n):
            if c == phone_book[j][:l]:
                return False
    return True

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (56.25ms, 10.3MB)
테스트 15 〉	통과 (82.75ms, 10.4MB)
테스트 16 〉	통과 (129.24ms, 10.3MB)
테스트 17 〉	통과 (194.27ms, 10.3MB)
테스트 18 〉	통과 (262.76ms, 10.4MB)
테스트 19 〉	통과 (70.34ms, 10.4MB)
테스트 20 〉	통과 (435.80ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (3.29ms, 10.8MB)
테스트 2 〉	통과 (3.32ms, 10.8MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
"""
# 시간초과..
# 해시를 이용한 문자열매칭 -> 라빈카프
# pattern이 parent에 매칭되는지를 판단합니다, 매칭되면 True 아니면 False
def Rabin_karf(pattern:str, parent:str)->bool:
    parent_size = len(parent)
    pattern_size = len(pattern)
    parent_hash = 0
    pattern_hash = 0
    power = 1
    for i in range(0, parent_size - pattern_size + 1):
        if i == 0:
            for j in range(0, pattern_size):
                parent_hash += hash(parent[pattern_size - 1 - j]) * power
                pattern_hash += hash(pattern[pattern_size - 1 - j]) * power
                if j < pattern_size - 1:
                    power *= 2
        else:
            parent_hash = 2 * (parent_hash - ord(parent[i-1]) * power) + ord(parent[pattern_size - 1 + i])
        if parent_hash == pattern_hash:
            found = True
            for j in range(0, pattern_size):
                if parent[i + j] != pattern[j]:
                    found = False
                    return False
            if found:
                return True
    return False


def solution(phone_book):
    n = len(phone_book)
    phone_book = sorted(phone_book, key = lambda x : len(x))
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            a = phone_book[i]
            b = phone_book[j]
            result = Rabin_karf(a, b)
            if result:
                return False
            else:
                continue
    return True

"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (2357.32ms, 10.4MB)
테스트 15 〉	통과 (3787.50ms, 10.3MB)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	실패 (시간 초과)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	실패 (시간 초과)
효율성  테스트
테스트 1 〉	통과 (1.97ms, 11.1MB)
테스트 2 〉	통과 (1.68ms, 11MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
"""

from collections import defaultdict
def solution(phone_book):
    book = defaultdict(str)
    # 길이로 비교를 할 것이므로
    phone_book = sorted(phone_book, key = lambda x: len(x))
    
    # 길이를 일종의 key로 사용한다.
    lengs = [len(phone_book[0])]
    for number in phone_book:
        for leng in lengs:
            # 같은 길이라면 바로 해싱(문제조건:중복된 번호 없음)
            if leng == len(number):
                book[hash(number)] = number
            # 길이가 더 길다면 한번 찾아봐야함
            if leng < len(number):
                x = number[0:leng]
                if book[hash(x)]:
                    return False
        # 확인을 해봤는데 완전 새로운 문자열임
        if lengs[-1] < len(number):
            lengs.append(len(number))
            book[hash(number)] = number
    return True

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (3.31ms, 10.8MB)
테스트 15 〉	통과 (3.63ms, 10.8MB)
테스트 16 〉	통과 (0.76ms, 10.4MB)
테스트 17 〉	통과 (0.89ms, 10.4MB)
테스트 18 〉	통과 (3.14ms, 11MB)
테스트 19 〉	통과 (1.45ms, 10.6MB)
테스트 20 〉	통과 (3.91ms, 11MB)
효율성  테스트
테스트 1 〉	통과 (1.86ms, 11MB)
테스트 2 〉	통과 (1.63ms, 11MB)
테스트 3 〉	통과 (103.07ms, 55.9MB)
테스트 4 〉	통과 (85.34ms, 40.3MB)
"""