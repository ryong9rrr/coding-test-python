def solution(dartResult):
    array = []
    # 점수, 스타상(*), 아차상(#) 을 배열에 담습니다.
    for x in dartResult.replace("10", "k"):
        if x == "k":
            array.append(10)
        if x.isdigit():
        #if ord("0") <= ord(x) <= ord("9"):
            array.append(int(x))
        if x == "D":
            array[-1] **= 2
        if x == "T":
            array[-1] **= 3
        if x == "*" or x == "#":
            array.append(x)
    
    result = []
    for x in array:
        if type(x) == int:
            result.append(x)
        if x == "*":
            if len(result) >= 2:
                result[-1] *= 2
                result[-2] *= 2
            else:
                result[-1] *= 2
        if x == "#":
            result[-1] *= (-1)
            
    return sum(result)

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.5MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.4MB)
테스트 14 〉	통과 (0.02ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.4MB)
테스트 17 〉	통과 (0.03ms, 10.5MB)
테스트 18 〉	통과 (0.03ms, 10.4MB)
테스트 19 〉	통과 (0.02ms, 10.4MB)
테스트 20 〉	통과 (0.03ms, 10.4MB)
테스트 21 〉	통과 (0.03ms, 10.4MB)
테스트 22 〉	통과 (0.03ms, 10.4MB)
테스트 23 〉	통과 (0.02ms, 10.4MB)
테스트 24 〉	통과 (0.02ms, 10.4MB)
테스트 25 〉	통과 (0.02ms, 10.4MB)
테스트 26 〉	통과 (0.02ms, 10.4MB)
테스트 27 〉	통과 (0.02ms, 10.4MB)
테스트 28 〉	통과 (0.02ms, 10.4MB)
테스트 29 〉	통과 (0.02ms, 10.4MB)
테스트 30 〉	통과 (0.03ms, 10.5MB)
테스트 31 〉	통과 (0.02ms, 10.4MB)
테스트 32 〉	통과 (0.02ms, 10.4MB)
"""