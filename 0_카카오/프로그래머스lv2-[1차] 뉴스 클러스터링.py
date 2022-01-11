# 아이디어, 집합, KAKAO

# 처음 푼 풀이... 굳이 문자열을 나눌 때 재귀를 사용할 필요도 없고 정규표현식을 사용할 필요도 없었음.
import sys
sys.setrecursionlimit(10**6)
import re
from collections import defaultdict

a = []
b = []
# 재귀적으로 문자열을 분할하는 함수(index 1만큼)
def recurse(start, end, s, arr):
    if end  >= len(s) + 1:
        return
    recurse(start + 1, end + 1, s, arr)
    result = s[start:end]
    arr.append(result)
    
# 문자열을 원소로 가지고 있는 target_list 에서 정규표현식과 매칭되는 원소를 모아 리스트로 반환
def match_string(target_list:list, regex:str)->list:
    result = []
    for i in target_list:
        p = re.compile(regex)
        m = p.match(i)
        # 매칭이 안되면 None을 반환하기 때문에
        if m :
            s = m.group()
            if s and len(s) > 1: # len(s) > 1은 문제의 조건
                result.append(s)
    return result            
    

def solution(str1, str2):
    global a
    global b
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 재귀로 문자열을 분할합니다.
    recurse(0, 2, str1, a)
    recurse(0, 2, str2, b)
    a = a[::-1]
    b = b[::-1]
    
    # 문자열을 정규표현식을 이용하여 추출합니다.
    filter_a = match_string(a, "[a-z]+")
    filter_b = match_string(b, "[a-z]+")
    
    # 중복 값을 포함하기위해 집합 논리연산을 사용하지않고 딕셔너리사용
    dic_a = defaultdict(int)
    dic_b = defaultdict(int)
    for i in filter_a :
        dic_a[i] += 1
    for i in filter_b :
        dic_b[i] += 1
    
    all_key = set(dic_a.keys()) | set(dic_b.keys())
    union = 0
    intersection = 0
    
    if len(all_key) == 0:
        return 65536
    
    for key in all_key:
        x = dic_a[key]
        y = dic_b[key]
        if x and y:
            # 둘다 존재한다면 더 큰값이 union, 작은 값이 intersection
            if x > y:
                x, y = y, x
            intersection += x
            union += y
        else:
            union += x + y
            
    return int((intersection / union) * 65536)

"""
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.11ms, 10.3MB)
테스트 3 〉	통과 (0.11ms, 10.4MB)
테스트 4 〉	통과 (3.49ms, 11MB)
테스트 5 〉	통과 (0.17ms, 10.4MB)
테스트 6 〉	통과 (0.09ms, 10.3MB)
테스트 7 〉	통과 (0.28ms, 10.3MB)
테스트 8 〉	통과 (0.17ms, 10.3MB)
테스트 9 〉	통과 (0.27ms, 10.3MB)
테스트 10 〉	통과 (0.59ms, 10.3MB)
테스트 11 〉	통과 (0.87ms, 10.4MB)
테스트 12 〉	통과 (0.14ms, 10.3MB)
테스트 13 〉	통과 (0.33ms, 10.3MB)
"""


# 220111 풀이^^ 실력이 많이 늘었다.
from collections import defaultdict

def make_set(strings):
    result = defaultdict(int)
    for i in range(len(strings) - 1):
        x = strings[i: i + 2]
        if x.isalpha():
            result[x.upper()] += 1
    return result

def solution(str1, str2):
    a, b = make_set(str1), make_set(str2)
    
    if not a and not b:
        return 65536
    
    all_keys = set(a.keys()) | set(b.keys())
    intersection = 0
    union = 0
    for key in all_keys:
        if key in a and key in b:
            intersection += min(a[key], b[key])
        union += max(a[key], b[key])
    
    return int((intersection / union) * 65536)

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.66ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.16ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.14ms, 10.3MB)
테스트 11 〉	통과 (0.22ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
"""