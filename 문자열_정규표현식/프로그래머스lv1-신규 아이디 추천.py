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
    #1. 모든 대문자를 소문자로 치환한다.
    new_id = new_id.lower()

    #2. 알파벳 소문자, 숫자, -, _, .를 제외한 문자를 없앤다.
    new_id = re.sub("[^a-z0-9\-_.]", "", new_id)

    #3. 마침표가 반복되면 하나의 마침표로 치환한다.
    new_id = re.sub("\.+", ".", new_id)

    #4. 처음이나 끝에 위치한 마침표는 없앤다.
    new_id = re.sub("^\.||\.$", "", new_id)

    #5. 문자가 없다면 a를 대입한다.
    if not new_id:
        new_id = "a"

    #6-1. 길이가 16자 이상이면 첫 15개의 문자만 남긴다.
    if len(new_id) >= 16:
        new_id = new_id[:15]

    #6-2. 끝에 마침표가 위치하면 없앤다.
    new_id = re.sub("\.$", "", new_id)

    #7. 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복한다.
    if new_id and len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id
"""
정확성 테스트
테스트 1 〉 통과 (0.20ms, 10.2MB)
테스트 2 〉 통과 (0.31ms, 10.2MB)
테스트 3 〉 통과 (0.35ms, 10.2MB)
테스트 4 〉 통과 (0.22ms, 10.2MB)
테스트 5 〉 통과 (0.30ms, 10.4MB)
테스트 6 〉 통과 (0.31ms, 10.3MB)
테스트 7 〉 통과 (0.31ms, 10MB)
테스트 8 〉 통과 (0.27ms, 10.2MB)
테스트 9 〉 통과 (0.33ms, 10.2MB)
테스트 10 〉 통과 (0.23ms, 10.1MB)
테스트 11 〉 통과 (0.32ms, 10.2MB)
테스트 12 〉 통과 (0.31ms, 10.2MB)
테스트 13 〉 통과 (0.32ms, 10.1MB)
테스트 14 〉 통과 (0.31ms, 10.2MB)
테스트 15 〉 통과 (0.21ms, 10.2MB)
테스트 16 〉 통과 (0.22ms, 10.3MB)
테스트 17 〉 통과 (0.41ms, 10.3MB)
테스트 18 〉 통과 (0.51ms, 10.2MB)
테스트 19 〉 통과 (0.61ms, 10.1MB)
테스트 20 〉 통과 (0.51ms, 10.2MB)
테스트 21 〉 통과 (0.51ms, 10.2MB)
테스트 22 〉 통과 (0.42ms, 10MB)
테스트 23 〉 통과 (0.21ms, 10.2MB)
테스트 24 〉 통과 (0.64ms, 10.3MB)
테스트 25 〉 통과 (0.24ms, 10.1MB)
테스트 26 〉 통과 (0.21ms, 10.3MB)
"""