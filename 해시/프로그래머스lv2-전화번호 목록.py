# 데이터의 개수가 백만개이기 때문에 n^2으로는 통과할 수 없음
def solution(phone_book):
    phone_book = sorted(phone_book)
    n = len(phone_book)
    for i in range(n):
        m = len(phone_book[i])
        for j in range(i + 1, m):
            if phone_book[i] == phone_book[j][:m]:
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

# 정렬을 시켰으니 바로 다음꺼랑만 비교하면 된다는 귀납법적인 추론
# 따라서 위 풀이를 O(n)으로 개선
def solution(phone_book):
    phone_book = sorted(phone_book)
    n = len(phone_book)
    for i in range(n - 1):
        m = len(phone_book[i])
        if phone_book[i] == phone_book[i + 1][:m]:
            return False
    return True
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.40ms, 10.4MB)
테스트 15 〉	통과 (0.50ms, 10.4MB)
테스트 16 〉	통과 (0.57ms, 10.3MB)
테스트 17 〉	통과 (0.66ms, 10.4MB)
테스트 18 〉	통과 (1.36ms, 10.3MB)
테스트 19 〉	통과 (0.64ms, 10.4MB)
테스트 20 〉	통과 (1.38ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (3.43ms, 10.8MB)
테스트 2 〉	통과 (3.03ms, 10.8MB)
테스트 3 〉	통과 (115.64ms, 30.8MB)
테스트 4 〉	통과 (100.28ms, 28.1MB)
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

# startswith + zip()
def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.32ms, 10.2MB)
테스트 15 〉	통과 (0.39ms, 10.3MB)
테스트 16 〉	통과 (0.45ms, 10.3MB)
테스트 17 〉	통과 (0.53ms, 10.4MB)
테스트 18 〉	통과 (0.77ms, 10.4MB)
테스트 19 〉	통과 (0.66ms, 10.4MB)
테스트 20 〉	통과 (1.57ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (2.83ms, 10.7MB)
테스트 2 〉	통과 (3.18ms, 10.9MB)
테스트 3 〉	통과 (97.68ms, 30.8MB)
테스트 4 〉	통과 (76.87ms, 28MB)
"""