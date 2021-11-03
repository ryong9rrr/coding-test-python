import re
from collections import defaultdict
def solution(record):
    dic = defaultdict(str)
    temp = []
    for rec in record:
        r = rec.split(" ")
        command = r[0]
        _id = r[1]
        if command == "Leave":
            temp.append(f"{_id}님이 나갔습니다.")
        else:
            nickname = r[2]
            if command == "Enter":
                dic[_id] = nickname
                temp.append(f"{_id}님이 들어왔습니다.")
            elif command == "Change":
                dic[_id] = nickname
    
    result = []
    for command in temp:
        _id = re.sub("님이 들어왔습니다.||님이 나갔습니다.", "", command)
        command = re.sub(f"{_id}", dic[_id], command)
        result.append(command)
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.20ms, 10.3MB)
테스트 2 〉	통과 (0.22ms, 10.3MB)
테스트 3 〉	통과 (0.43ms, 10.3MB)
테스트 4 〉	통과 (0.46ms, 10.3MB)
테스트 5 〉	통과 (4.85ms, 10.6MB)
테스트 6 〉	통과 (4.64ms, 10.6MB)
테스트 7 〉	통과 (2.36ms, 10.4MB)
테스트 8 〉	통과 (5.14ms, 10.7MB)
테스트 9 〉	통과 (18.58ms, 10.9MB)
테스트 10 〉	통과 (4.89ms, 10.6MB)
테스트 11 〉	통과 (13.53ms, 10.6MB)
테스트 12 〉	통과 (13.58ms, 10.7MB)
테스트 13 〉	통과 (5.42ms, 10.6MB)
테스트 14 〉	통과 (27.61ms, 11.1MB)
테스트 15 〉	통과 (0.27ms, 10.3MB)
테스트 16 〉	통과 (0.36ms, 10.3MB)
테스트 17 〉	통과 (0.86ms, 10.3MB)
테스트 18 〉	통과 (0.87ms, 10.3MB)
테스트 19 〉	통과 (8.42ms, 10.6MB)
테스트 20 〉	통과 (5.01ms, 10.4MB)
테스트 21 〉	통과 (2.82ms, 10.5MB)
테스트 22 〉	통과 (5.40ms, 10.4MB)
테스트 23 〉	통과 (4.08ms, 10.7MB)
테스트 24 〉	통과 (4.40ms, 10.7MB)
테스트 25 〉	통과 (2226.40ms, 49.1MB)
테스트 26 〉	통과 (2764.03ms, 53.8MB)
테스트 27 〉	통과 (2582.37ms, 59.7MB)
테스트 28 〉	통과 (2734.91ms, 61.9MB)
테스트 29 〉	통과 (2837.71ms, 61.6MB)
테스트 30 〉	통과 (2822.88ms, 50.1MB)
테스트 31 〉	통과 (2902.19ms, 61.6MB)
테스트 32 〉	통과 (2828.33ms, 53.6MB)
"""