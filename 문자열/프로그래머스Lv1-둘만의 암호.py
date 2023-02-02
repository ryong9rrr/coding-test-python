def get_next_char(cur_char, interval, skip_set):
        next_chars = []
        n = ord(cur_char)
        while len(next_chars) < interval:
            n += 1
            if n > 122:
                n = 97
            if chr(n) not in skip_set:
                next_chars.append(chr(n))
        return next_chars[-1]

def solution(s, skip, index):
    return "".join([get_next_char(char, index, set(skip)) for char in s])

"""
정확성  테스트
테스트 1 〉	통과 (0.15ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.49ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10MB)
테스트 5 〉	통과 (0.10ms, 10.2MB)
테스트 6 〉	통과 (0.13ms, 10.2MB)
테스트 7 〉	통과 (0.21ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.18ms, 10.2MB)
테스트 12 〉	통과 (0.09ms, 10.2MB)
테스트 13 〉	통과 (0.19ms, 10.3MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.3MB)
테스트 16 〉	통과 (0.07ms, 10MB)
테스트 17 〉	통과 (0.15ms, 10.2MB)
테스트 18 〉	통과 (0.19ms, 10.1MB)
테스트 19 〉	통과 (0.24ms, 10.1MB)
"""