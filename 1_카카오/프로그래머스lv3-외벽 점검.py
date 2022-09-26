from itertools import permutations
def solution(n, weak, dist):
    W_LENGTH = len(weak)
    PEOPLE_LENGTH = len(dist)
    # 취약지점을 2배 늘려준다.
    weaks = weak[:]
    for w in weak:
        weaks.append(w + n)
        
    # 사람들의 순서를 순열로 만든다.
    permus = list(permutations(dist, PEOPLE_LENGTH))
    
    result = 999
    
    for i in range(W_LENGTH):
        for people in permus:
            count = 1
            # 맨 처음 첫번째 사람이 갈 수 있는 거리
            distance = weaks[i] + people[count - 1]
            # 사람을 보내면서 그 다음 사람을 투입
            for j in range(i, i + W_LENGTH):
                if distance < weaks[j]:
                    count += 1
                    if count > PEOPLE_LENGTH:
                        break
                    distance = weaks[j] + people[count - 1]
            result = min(result, count)
    
    return -1 if result > PEOPLE_LENGTH else result

"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (752.53ms, 14.8MB)
테스트 4 〉	통과 (608.83ms, 14.7MB)
테스트 5 〉	통과 (1.62ms, 10.2MB)
테스트 6 〉	통과 (110.42ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.49ms, 10.2MB)
테스트 9 〉	통과 (0.23ms, 10.3MB)
테스트 10 〉	통과 (1429.66ms, 14.7MB)
테스트 11 〉	통과 (1100.83ms, 14.8MB)
테스트 12 〉	통과 (1138.58ms, 14.7MB)
테스트 13 〉	통과 (973.18ms, 14.7MB)
테스트 14 〉	통과 (1369.85ms, 14.7MB)
테스트 15 〉	통과 (1328.90ms, 14.8MB)
테스트 16 〉	통과 (1126.87ms, 14.8MB)
테스트 17 〉	통과 (1355.81ms, 14.9MB)
테스트 18 〉	통과 (1178.38ms, 14.7MB)
테스트 19 〉	통과 (1160.65ms, 14.8MB)
테스트 20 〉	통과 (1116.99ms, 14.7MB)
테스트 21 〉	통과 (1082.40ms, 14.8MB)
테스트 22 〉	통과 (0.26ms, 10.1MB)
테스트 23 〉	통과 (0.42ms, 10.2MB)
테스트 24 〉	통과 (0.51ms, 10.2MB)
테스트 25 〉	통과 (323.11ms, 14.7MB)
"""