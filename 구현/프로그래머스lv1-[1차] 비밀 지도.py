def solution(n, arr1, arr2):
    result = []
    
    for i in range(0, n) :
        r = bin(arr1[i] | arr2[i])[2::]
        
        zero = n-len(r)
        r = "0"*zero + r
        
        temp = ""
        for j in range(0, len(r)) :
            if r[j]=="1" :
                temp += "#"
            else :
                temp += " "
            
        result.append(temp)
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
"""

def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        b = bin(arr1[i] | arr2[i])[2:]
        if len(b) < n:
            b = b.zfill(n)
            # b = "0" * (n - len(b)) + b
        b = b.replace("1", "#")
        b = b.replace("0", " ")
        result.append(b)
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
"""