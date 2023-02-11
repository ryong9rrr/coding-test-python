def convert_file(file):
    N = len(file)
    HEAD = ""
    NUMBER = "0"
    HEAD_OK = NUMBER_OK = False
    for i, s in enumerate(file):
        if HEAD_OK and NUMBER_OK:
            break
        if not HEAD_OK:
            HEAD += s
            if i < N - 1 and file[i + 1].isdigit():
                HEAD_OK = True
            continue
        NUMBER += s
        if i < N - 1 and not file[i + 1].isdigit():
            NUMBER_OK = True
    return [HEAD, NUMBER]

def solution(files):
    converted = []
    for i, file in enumerate(files):
        HEAD, STRING_NUMBER = convert_file(file.lower())
        converted.append([HEAD, int(STRING_NUMBER), i])
    
    return [files[x[2]] for x in sorted(converted)]
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (2.77ms, 10.4MB)
테스트 4 〉	통과 (2.86ms, 10.5MB)
테스트 5 〉	통과 (2.70ms, 10.6MB)
테스트 6 〉	통과 (2.74ms, 10.4MB)
테스트 7 〉	통과 (2.78ms, 10.5MB)
테스트 8 〉	통과 (2.42ms, 10.4MB)
테스트 9 〉	통과 (2.53ms, 10.5MB)
테스트 10 〉	통과 (4.78ms, 10.5MB)
테스트 11 〉	통과 (4.55ms, 10.3MB)
테스트 12 〉	통과 (2.77ms, 10.5MB)
테스트 13 〉	통과 (2.33ms, 10.6MB)
테스트 14 〉	통과 (4.70ms, 10.6MB)
테스트 15 〉	통과 (3.11ms, 10.5MB)
테스트 16 〉	통과 (2.51ms, 10.4MB)
테스트 17 〉	통과 (2.13ms, 10.5MB)
테스트 18 〉	통과 (4.35ms, 10.5MB)
테스트 19 〉	통과 (2.54ms, 10.4MB)
테스트 20 〉	통과 (2.50ms, 10.6MB)
"""

# 정규식 사용
import re
def solution(files):
    regexp = re.compile(r"(^\D+)(\d{1,5})", re.I)
    
    converted = []
    for i, file in enumerate(files):
        HEAD, STRING_NUMBER = regexp.match(file).groups()
        converted.append([HEAD.lower(), int(STRING_NUMBER), i])
    
    return [files[x[2]] for x in sorted(converted)]
"""
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.2MB)
테스트 2 〉	통과 (0.17ms, 10.2MB)
테스트 3 〉	통과 (1.38ms, 10.5MB)
테스트 4 〉	통과 (2.46ms, 10.5MB)
테스트 5 〉	통과 (2.11ms, 10.4MB)
테스트 6 〉	통과 (1.51ms, 10.3MB)
테스트 7 〉	통과 (2.44ms, 10.4MB)
테스트 8 〉	통과 (1.88ms, 10.5MB)
테스트 9 〉	통과 (1.34ms, 10.4MB)
테스트 10 〉	통과 (2.26ms, 10.3MB)
테스트 11 〉	통과 (1.94ms, 10.5MB)
테스트 12 〉	통과 (1.66ms, 10.4MB)
테스트 13 〉	통과 (1.02ms, 10.4MB)
테스트 14 〉	통과 (2.97ms, 10.7MB)
테스트 15 〉	통과 (1.65ms, 10.6MB)
테스트 16 〉	통과 (1.32ms, 10.4MB)
테스트 17 〉	통과 (1.39ms, 10.5MB)
테스트 18 〉	통과 (1.26ms, 10.4MB)
테스트 19 〉	통과 (1.45ms, 10.3MB)
테스트 20 〉	통과 (2.10ms, 10.3MB)
"""