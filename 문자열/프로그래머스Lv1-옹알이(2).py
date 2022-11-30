def can_pronounce(target_word):
    BABY_WORDS = ["aya", "ye", "woo", "ma"]
    for i, BABY_WORD in enumerate(BABY_WORDS):
        target_word = target_word.replace(BABY_WORD, str(i))
        if target_word.find(str(i) * 2) > -1:
            return False
    return target_word.isdigit()

def solution(babbling):
    result = 0
    for word in babbling:
        if can_pronounce(word):
            result += 1
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.26ms, 10.3MB)
테스트 13 〉	통과 (0.22ms, 10.2MB)
테스트 14 〉	통과 (0.21ms, 10.2MB)
테스트 15 〉	통과 (0.15ms, 10.2MB)
테스트 16 〉	통과 (0.21ms, 10.4MB)
테스트 17 〉	통과 (0.19ms, 10.3MB)
테스트 18 〉	통과 (0.18ms, 10.2MB)
테스트 19 〉	통과 (0.06ms, 10.2MB)
테스트 20 〉	통과 (0.14ms, 10.2MB)
"""