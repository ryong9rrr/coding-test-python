# 구현, 정규표현식, 카카오

# 정규표현식으로 푼 풀이... 너무 느림
import re
from collections import defaultdict
def solution(record):
    users = defaultdict(str)
    temp = []
    for commands in record:
        commands = commands.split()
        command = commands[0]
        userId = commands[1]
        if command == "Leave":
            temp.append(f"{userId}님이 나갔습니다.")
        else:
            nickname = commands[2]
            if command == "Enter":
                users[userId] = nickname
                temp.append(f"{userId}님이 들어왔습니다.")
            elif command == "Change":
                users[userId] = nickname
    
    result = []
    for command in temp:
        userId = re.sub("님이 들어왔습니다.||님이 나갔습니다.", "", command)
        command = re.sub(f"{userId}", users[userId], command)
        result.append(command)
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.31ms, 10.3MB)
테스트 2 〉	통과 (0.34ms, 10.3MB)
테스트 3 〉	통과 (0.68ms, 10.3MB)
테스트 4 〉	통과 (0.77ms, 10.3MB)
테스트 5 〉	통과 (2.64ms, 10.6MB)
테스트 6 〉	통과 (5.13ms, 10.7MB)
테스트 7 〉	통과 (2.52ms, 10.6MB)
테스트 8 〉	통과 (6.32ms, 10.7MB)
테스트 9 〉	통과 (17.46ms, 10.8MB)
테스트 10 〉	통과 (4.87ms, 10.5MB)
테스트 11 〉	통과 (9.65ms, 10.7MB)
테스트 12 〉	통과 (9.22ms, 10.6MB)
테스트 13 〉	통과 (4.87ms, 10.7MB)
테스트 14 〉	통과 (17.20ms, 10.9MB)
테스트 15 〉	통과 (0.38ms, 10.3MB)
테스트 16 〉	통과 (0.26ms, 10.3MB)
테스트 17 〉	통과 (0.87ms, 10.3MB)
테스트 18 〉	통과 (0.96ms, 10.3MB)
테스트 19 〉	통과 (4.99ms, 10.7MB)
테스트 20 〉	통과 (2.84ms, 10.4MB)
테스트 21 〉	통과 (3.83ms, 10.6MB)
테스트 22 〉	통과 (3.03ms, 10.4MB)
테스트 23 〉	통과 (6.14ms, 10.7MB)
테스트 24 〉	통과 (4.68ms, 10.7MB)
테스트 25 〉	통과 (2128.95ms, 49.4MB)
테스트 26 〉	통과 (2497.87ms, 53.9MB)
테스트 27 〉	통과 (2370.09ms, 59.6MB)
테스트 28 〉	통과 (2466.23ms, 61.9MB)
테스트 29 〉	통과 (2562.16ms, 61.5MB)
테스트 30 〉	통과 (2174.50ms, 50MB)
테스트 31 〉	통과 (2619.91ms, 61.6MB)
테스트 32 〉	통과 (2578.44ms, 53.5MB)
"""

#정규표현식 폴더에서는 정규표현식을 썼었지만... 로직자체가 너무 비효율적이었음.
# 딱히 다른점은 많이 없긴하지만 시간을 엄청 개선시킨방법
from collections import defaultdict
def solution(record):
    # (key: value => userId: userName)
    users = defaultdict(str)
    for commands in record:
        commands = commands.split()
        if commands[0] != "Leave":
            _, userId, nickName = commands
            users[userId] = nickName
            
    result = []
    for commands in record:
        commands = commands.split()
        userId = commands[1]
        if commands[0] == "Leave":
            result.append(f"{users[userId]}님이 나갔습니다.")
        elif commands[0] == "Enter":
            result.append(f"{users[userId]}님이 들어왔습니다.")
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.97ms, 10.4MB)
테스트 6 〉	통과 (1.31ms, 10.4MB)
테스트 7 〉	통과 (0.86ms, 10.4MB)
테스트 8 〉	통과 (1.12ms, 10.4MB)
테스트 9 〉	통과 (0.83ms, 10.5MB)
테스트 10 〉	통과 (1.83ms, 10.4MB)
테스트 11 〉	통과 (0.64ms, 10.3MB)
테스트 12 〉	통과 (0.61ms, 10.3MB)
테스트 13 〉	통과 (1.33ms, 10.4MB)
테스트 14 〉	통과 (2.28ms, 10.6MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.07ms, 10.3MB)
테스트 18 〉	통과 (0.10ms, 10.3MB)
테스트 19 〉	통과 (0.95ms, 10.6MB)
테스트 20 〉	통과 (0.98ms, 10.3MB)
테스트 21 〉	통과 (0.64ms, 10.4MB)
테스트 22 〉	통과 (0.59ms, 10.3MB)
테스트 23 〉	통과 (1.18ms, 10.7MB)
테스트 24 〉	통과 (0.68ms, 10.7MB)
테스트 25 〉	통과 (101.70ms, 47.5MB)
테스트 26 〉	통과 (79.57ms, 50MB)
테스트 27 〉	통과 (89.59ms, 50.1MB)
테스트 28 〉	통과 (93.68ms, 51.6MB)
테스트 29 〉	통과 (117.83ms, 51.5MB)
테스트 30 〉	통과 (94.03ms, 44.6MB)
테스트 31 〉	통과 (75.01ms, 52.1MB)
테스트 32 〉	통과 (60.79ms, 47.5MB)
"""

from collections import defaultdict
def solution(record):
    # (key: value => "userId": "nickName")
    users = defaultdict(str)
    temp_records = []
    
    for commands in record:
        commands = commands.split()
        command = commands[0]
        if command == "Enter" or command == "Change":
            userId, nickName = commands[1], commands[2]
            users[userId] = nickName
            if command == "Enter":
                temp_records.append(("Enter", userId))
        elif command == "Leave":
            userId = commands[1]
            temp_records.append(("Leave", userId))
    
    result = []
    for command, userId in temp_records:
        if command == "Enter":
            result.append(f"{users[userId]}님이 들어왔습니다.")
        elif command == "Leave":
            result.append(f"{users[userId]}님이 나갔습니다.")
    
    return result
            
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.99ms, 10.6MB)
테스트 6 〉	통과 (0.71ms, 10.4MB)
테스트 7 〉	통과 (0.52ms, 10.4MB)
테스트 8 〉	통과 (0.63ms, 10.6MB)
테스트 9 〉	통과 (1.18ms, 10.7MB)
테스트 10 〉	통과 (0.65ms, 10.4MB)
테스트 11 〉	통과 (0.33ms, 10.5MB)
테스트 12 〉	통과 (0.53ms, 10.5MB)
테스트 13 〉	통과 (0.60ms, 10.6MB)
테스트 14 〉	통과 (1.11ms, 10.7MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.07ms, 10.3MB)
테스트 18 〉	통과 (0.09ms, 10.3MB)
테스트 19 〉	통과 (1.15ms, 10.7MB)
테스트 20 〉	통과 (0.68ms, 10.4MB)
테스트 21 〉	통과 (0.48ms, 10.5MB)
테스트 22 〉	통과 (0.48ms, 10.5MB)
테스트 23 〉	통과 (0.83ms, 10.7MB)
테스트 24 〉	통과 (0.74ms, 10.7MB)
테스트 25 〉	통과 (82.78ms, 54.7MB)
테스트 26 〉	통과 (124.39ms, 61.8MB)
테스트 27 〉	통과 (122.20ms, 63.3MB)
테스트 28 〉	통과 (155.12ms, 66.4MB)
테스트 29 〉	통과 (99.71ms, 66.3MB)
테스트 30 〉	통과 (106.07ms, 49.6MB)
테스트 31 〉	통과 (105.84ms, 56.9MB)
테스트 32 〉	통과 (77.19ms, 52.8MB)
"""


# 22년 7월 풀이 // 코드가 더 나아진듯 하다
from collections import defaultdict

MESSAGE_MAP = {
    "Enter": "님이 들어왔습니다.",
    "Leave": "님이 나갔습니다."
}

def solution(record):
    user_table = defaultdict(str)
    user_log = []
    
    for command in record:
        commands = command.split(" ")
        action, user_id = commands[0], commands[1]
        if action == "Enter" or action == "Change":
            username = commands[2]
            user_table[user_id] = username
        if not action == "Change":
            user_log.append([action, user_id])
    
    return [f"{user_table[user_id]}{MESSAGE_MAP[action]}"
            for action, user_id
            in user_log]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.95MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.59ms, 10.3MB)
테스트 6 〉	통과 (0.64ms, 10.5MB)
테스트 7 〉	통과 (0.54ms, 10.2MB)
테스트 8 〉	통과 (1.15ms, 10.3MB)
테스트 9 〉	통과 (0.75ms, 10.3MB)
테스트 10 〉	통과 (0.64ms, 10.3MB)
테스트 11 〉	통과 (0.38ms, 10.1MB)
테스트 12 〉	통과 (0.39ms, 10.1MB)
테스트 13 〉	통과 (1.05ms, 10.3MB)
테스트 14 〉	통과 (0.72ms, 10.4MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10MB)
테스트 17 〉	통과 (0.07ms, 10MB)
테스트 18 〉	통과 (0.10ms, 10.1MB)
테스트 19 〉	통과 (0.92ms, 10.4MB)
테스트 20 〉	통과 (0.51ms, 10.1MB)
테스트 21 〉	통과 (0.53ms, 10MB)
테스트 22 〉	통과 (0.50ms, 10.1MB)
테스트 23 〉	통과 (0.67ms, 10.4MB)
테스트 24 〉	통과 (0.75ms, 10.2MB)
테스트 25 〉	통과 (99.57ms, 45MB)
테스트 26 〉	통과 (148.61ms, 49MB)
테스트 27 〉	통과 (108.84ms, 52.8MB)
테스트 28 〉	통과 (131.95ms, 54.8MB)
테스트 29 〉	통과 (125.66ms, 54.7MB)
테스트 30 〉	통과 (93.15ms, 44.6MB)
테스트 31 〉	통과 (102.91ms, 52.5MB)
테스트 32 〉	통과 (82.28ms, 47.5MB)

"""