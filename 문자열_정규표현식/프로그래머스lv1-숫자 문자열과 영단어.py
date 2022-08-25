def solution(s):
    NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, NUMBER in enumerate(NUMBERS):
        s = s.replace(NUMBER, str(i))
    
    return int(s)
"""
정확성 테스트
테스트 1 〉 통과 (0.02ms, 10.4MB)
테스트 2 〉 통과 (0.02ms, 10.2MB)
테스트 3 〉 통과 (0.02ms, 10.3MB)
테스트 4 〉 통과 (0.02ms, 10.2MB)
테스트 5 〉 통과 (0.02ms, 10.3MB)
테스트 6 〉 통과 (0.02ms, 10.4MB)
테스트 7 〉 통과 (0.03ms, 10.2MB)
테스트 8 〉 통과 (0.02ms, 10.3MB)
테스트 9 〉 통과 (0.03ms, 10.3MB)
테스트 10 〉 통과 (0.02ms, 10.4MB)
"""