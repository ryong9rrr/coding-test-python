# 정규표현식을 쓰지 않고 풀었을 때
def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    new_id = [c for c in new_id if 97<=ord(c)<=122 or 48<=ord(c)<=57 or 45<=ord(c)<=46 or ord(c)==95 ]
    #3
    for dot in range(len(new_id)-1) :
        if new_id[dot] == "." and new_id[dot+1] == "." :
            new_id[dot] = ""
    new_id = list("".join(new_id))
    #4
    for dot in range(-1, 1) :
        if new_id[dot] == "." :
            new_id[dot] = ""
    
    new_id = list("".join(new_id))
            
    #5
    if len(new_id) == 0 :
        new_id.append("a")
        
    #6
    if len(new_id) >= 16 :
        new_id = new_id[0:15]
    if new_id[-1] == "." :
        new_id.pop()
        
    #7
    if len(new_id) <= 2 :
        while len(new_id) < 3 :
            new_id.append(new_id[-1])
        
    return "".join(new_id)

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.06ms, 10.3MB)
테스트 17 〉	통과 (0.15ms, 10.2MB)
테스트 18 〉	통과 (0.25ms, 10.3MB)
테스트 19 〉	통과 (0.47ms, 10.3MB)
테스트 20 〉	통과 (0.45ms, 10.4MB)
테스트 21 〉	통과 (0.45ms, 10.3MB)
테스트 22 〉	통과 (0.40ms, 10.3MB)
테스트 23 〉	통과 (0.50ms, 10.3MB)
테스트 24 〉	통과 (0.42ms, 10.2MB)
테스트 25 〉	통과 (0.53ms, 10.2MB)
테스트 26 〉	통과 (0.54ms, 10.3MB)
"""


# 정규표현식을 사용하며 풀었을 때
import re
def solution(new_id):
    #1 모든 대문자를 소문자로
    new_id = new_id.lower()
    #2 알파벳소문자, 숫자, -, _, . 를 제외한 문자를 제거
    new_id = re.sub("[^a-z0-9\-_.]", "", new_id)
    #3 마침표가 2번이상 연속된다면 마침표를 하나만 남길 것
    new_id = re.sub("\.+", ".", new_id)
    #4 문자열 처음이나 끝에 마침표가 있다면 제거
    new_id = re.sub("^\.||\.$", "", new_id)
    print(new_id)
    #5 빈 문자열이라면 "a"를 대입
    if len(new_id) == 0:
        new_id += "a"
    #6 길이가 16이상이라면 첫 15개의 문자만 남길것, 제거 후 마침표가 끝에 위치한다면 제거할것
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = re.sub("\.$", "", new_id)
    #7 길이가 2 이하라면 마지막문자를 길이가 3이 될 때까지 끝에 붙일 것
    if len(new_id) <= 2:
        new_id = new_id + (new_id[-1] * (3 - len(new_id)))
        
    return new_id
"""
정확성  테스트
테스트 1 〉	통과 (0.35ms, 10.3MB)
테스트 2 〉	통과 (0.23ms, 10.3MB)
테스트 3 〉	통과 (0.22ms, 10.3MB)
테스트 4 〉	통과 (0.31ms, 10.2MB)
테스트 5 〉	통과 (0.28ms, 10.3MB)
테스트 6 〉	통과 (0.36ms, 10.3MB)
테스트 7 〉	통과 (0.31ms, 10.3MB)
테스트 8 〉	통과 (0.34ms, 10.2MB)
테스트 9 〉	통과 (0.21ms, 10.3MB)
테스트 10 〉	통과 (0.20ms, 10.3MB)
테스트 11 〉	통과 (0.31ms, 10.3MB)
테스트 12 〉	통과 (0.21ms, 10.3MB)
테스트 13 〉	통과 (0.22ms, 10.3MB)
테스트 14 〉	통과 (0.22ms, 10.2MB)
테스트 15 〉	통과 (0.30ms, 10.2MB)
테스트 16 〉	통과 (0.22ms, 10.3MB)
테스트 17 〉	통과 (0.33ms, 10.3MB)
테스트 18 〉	통과 (0.29ms, 10.2MB)
테스트 19 〉	통과 (0.37ms, 10.3MB)
테스트 20 〉	통과 (0.37ms, 10.2MB)
테스트 21 〉	통과 (0.28ms, 10.3MB)
테스트 22 〉	통과 (0.30ms, 10.3MB)
테스트 23 〉	통과 (0.21ms, 10.2MB)
테스트 24 〉	통과 (0.67ms, 10.4MB)
테스트 25 〉	통과 (0.24ms, 10.3MB)
테스트 26 〉	통과 (0.21ms, 10.2MB)
"""