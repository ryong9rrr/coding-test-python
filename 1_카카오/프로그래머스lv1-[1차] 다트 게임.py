# 내가 푼 풀이
def solution(dartResult):
    dart = []
    for x in dartResult.replace("10", "k") :
        if x == "k" :
            dart.append(10)
        elif x.isdigit() :
            dart.append(int(x))
        else :
            dart.append(x)
    
    result = []
    for i in range(0, len(dart)) :
        if dart[i] == "S" :
            result.append(dart[i-1] ** 1)
        elif dart[i] == "D" :
            result.append(dart[i-1] ** 2)
        elif dart[i] == "T" :
            result.append(dart[i-1] ** 3)
        elif dart[i] == "#" :
            result[-1] = result[-1] * (-1)
        elif dart[i] == "*" :
            if len(result) > 1 :
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
            else :
                result[-1] = result[-1] * 2
    
    return sum(result)

"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.5MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.5MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.5MB)
테스트 11 〉	통과 (0.03ms, 10.5MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.4MB)
테스트 17 〉	통과 (0.03ms, 10.5MB)
테스트 18 〉	통과 (0.03ms, 10.5MB)
테스트 19 〉	통과 (0.03ms, 10.4MB)
테스트 20 〉	통과 (0.03ms, 10.4MB)
테스트 21 〉	통과 (0.02ms, 10.4MB)
테스트 22 〉	통과 (0.04ms, 10.5MB)
테스트 23 〉	통과 (0.03ms, 10.4MB)
테스트 24 〉	통과 (0.03ms, 10.4MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.02ms, 10.4MB)
테스트 27 〉	통과 (0.02ms, 10.4MB)
테스트 28 〉	통과 (0.02ms, 10.4MB)
테스트 29 〉	통과 (0.02ms, 10.4MB)
테스트 30 〉	통과 (0.02ms, 10.4MB)
테스트 31 〉	통과 (0.02ms, 10.4MB)
테스트 32 〉	통과 (0.02ms, 10.4MB)
"""

# 스택 pop을 사용하면 통과하지 못한다... 왜일까?
def pow_score(_type, score):
    if _type == "S":
        return score
    if _type == "D":
        return score ** 2
    if _type == "T":
        return score ** 3
    raise Exception("유효한 타입이 아닙니다.")

def solution(dartResult):
    # 10점에 대한 마킹
    dartResult = dartResult.replace("10", "A")
    darts = []
    # darts에 점수, *, # 만 담는다.
    for s in dartResult:
        if s == "A":
            darts.append(10)
        elif s.isdigit():
            darts.append(int(s))
        elif s == "S" or s == "D" or s == "T":
            if type(darts[-1]) is not int:
                raise Exception("에러")
            darts.append(pow_score(s, darts.pop()))
        else:
            darts.append(s)
    
    # 점수계산
    scores = []
    for dart in darts:
        if type(dart) is int:
            scores.append(dart)
        elif dart == "*":
            if len(scores) >= 2:
                scores[-1] *= 2
                scores[-2] *= 2
            elif len(scores) == 1:
                scores[-1] *= 2
            else:
                raise Exception("에러")
        else:
            scores[-1] *= -1
    
    return sum(scores)
        
        

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.5MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.5MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.6MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.04ms, 10.5MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.6MB)
테스트 14 〉	통과 (0.03ms, 10.5MB)
테스트 15 〉	통과 (0.03ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.5MB)
테스트 17 〉	통과 (0.02ms, 10.4MB)
테스트 18 〉	통과 (0.03ms, 10.4MB)
테스트 19 〉	통과 (0.03ms, 10.4MB)
테스트 20 〉	통과 (0.03ms, 10.5MB)
테스트 21 〉	통과 (0.03ms, 10.5MB)
테스트 22 〉	통과 (0.03ms, 10.4MB)
테스트 23 〉	통과 (0.02ms, 10.4MB)
테스트 24 〉	통과 (0.02ms, 10.4MB)
테스트 25 〉	통과 (0.03ms, 10.6MB)
테스트 26 〉	통과 (0.03ms, 10.5MB)
테스트 27 〉	통과 (0.02ms, 10.4MB)
테스트 28 〉	통과 (0.02ms, 10.4MB)
테스트 29 〉	통과 (0.02ms, 10.5MB)
테스트 30 〉	통과 (0.03ms, 10.4MB)
테스트 31 〉	통과 (0.03ms, 10.4MB)
테스트 32 〉	통과 (0.03ms, 10.4MB)
"""