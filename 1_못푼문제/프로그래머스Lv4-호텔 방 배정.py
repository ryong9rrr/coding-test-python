def solution(k, room_number):
    table = {}
    result = []
    
    for i, room in enumerate(room_number):
        if room not in table:
            table[room] = i + 1
            result.append(room)
            continue
        next_room = room + 1
        while next_room in table:
            next_room += 1
        table[next_room] = i + 1
        result.append(next_room)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.19ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.4MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.04ms, 10.2MB)
테스트 17 〉	통과 (0.03ms, 10.3MB)
테스트 18 〉	통과 (0.09ms, 10.2MB)
테스트 19 〉	통과 (0.19ms, 10.3MB)
테스트 20 〉	통과 (0.26ms, 10.3MB)
테스트 21 〉	통과 (0.85ms, 10.4MB)
테스트 22 〉	통과 (0.68ms, 10.5MB)
테스트 23 〉	통과 (0.30ms, 10.5MB)
테스트 24 〉	통과 (0.71ms, 10.4MB)
테스트 25 〉	통과 (0.01ms, 10.1MB)
테스트 26 〉	통과 (0.05ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
"""