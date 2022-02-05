# 테이블을 중심으로 탐색
def solution(s):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, num in enumerate(nums):
        if num in s:
            s = s.replace(num, str(i))
            
    return int(s)

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
"""

# 문자열을 중심으로 탐색
def solution(s):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = ""
    temp = ""
    for char in s:
        if char.isalpha():
            temp += char
        else:
            result += char
            
        if temp in nums:
            result += str(nums.index(temp))
            temp = ""
    
    return int(result)

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
"""