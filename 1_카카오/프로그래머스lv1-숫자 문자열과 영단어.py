def solution(s):
    NUMBER_TABLE = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    result = s
    
    for index, number_str in enumerate(NUMBER_TABLE):
        result = result.replace(number_str, str(index))
    
    return int(result)

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (3.10ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
"""