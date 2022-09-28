def check(brackets):
    stack = []
    for s in brackets:
        if s == ")":
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(s)
    return True

def divide(brackets):
    count = 0
    for i, s in enumerate(brackets):
        if s == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
    return len(brackets) - 1

def rev(brackets):
    result = ""
    for s in brackets:
        if s == "(":
            result += ")"
        else:
            result += "("
    return result

def solution(p):
    if not p or check(p):
        return p
    
    index = divide(p)
    u, v = p[:index + 1], p[index + 1:]
    
    if check(u):
        return u + solution(v)
    
    temp = "("
    temp += solution(v)
    temp += ")"

    return temp + rev(u[1:-1])
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.4MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.1MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.11ms, 10.2MB)
테스트 15 〉	통과 (0.08ms, 10.2MB)
테스트 16 〉	통과 (0.27ms, 10.2MB)
테스트 17 〉	통과 (0.31ms, 10.1MB)
테스트 18 〉	통과 (0.53ms, 10.2MB)
테스트 19 〉	통과 (0.27ms, 10.4MB)
테스트 20 〉	통과 (0.53ms, 10.3MB)
테스트 21 〉	통과 (0.25ms, 10.2MB)
테스트 22 〉	통과 (0.11ms, 10.2MB)
테스트 23 〉	통과 (0.35ms, 10.4MB)
테스트 24 〉	통과 (0.06ms, 10.1MB)
테스트 25 〉	통과 (0.23ms, 10.4MB)
"""