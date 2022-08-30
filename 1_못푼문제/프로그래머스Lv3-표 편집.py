import copy
def solution(n, k, cmd):
    table = [i for i in range(n)]
    snapshots = [copy.copy(table)]

    for x in cmd:
        commands = x.split(" ")
        command = commands[0]
        if command == "U" or command == "D":
            shift = int(commands[1])
            if command == "U":
                k -= shift
                if k <= 0:
                    k = 0
            else:
                k += shift
                if k >= n - 1:
                    k = n - 1

        elif command == "C":
            snapshots.append(copy.copy(table))
            del table[k]
            last_idx = len(table) - 1
            if k > last_idx:
                k = last_idx

        elif command == "Z":
            snapshot = snapshots.pop()
            if table[k] != snapshot[k]:
                k += 1
            table = snapshot
        
    result = ""

    for i in range(n):
        if i in table:
            result += "O"
        else:
            result += "X"

    return result

"""
시간초과가 나는 이유는 아마 del 사용(O(N)이 추가), 마지막에 결과를 구하는 과정에서 O(N^2)이 발생했기 때문같다.
정확성 테스트
테스트 1 〉 통과 (0.04ms, 10.4MB)
테스트 2 〉 통과 (0.03ms, 10.4MB)
테스트 3 〉 통과 (0.04ms, 10.4MB)
테스트 4 〉 통과 (0.03ms, 10.4MB)
테스트 5 〉 통과 (0.12ms, 10.3MB)
테스트 6 〉 통과 (0.13ms, 10.5MB)
테스트 7 〉 통과 (0.12ms, 10.4MB)
테스트 8 〉 통과 (0.15ms, 10.4MB)
테스트 9 〉 통과 (0.13ms, 10.4MB)
테스트 10 〉 통과 (0.12ms, 10.4MB)
테스트 11 〉 통과 (1.60ms, 10.4MB)
테스트 12 〉 통과 (1.56ms, 10.6MB)
테스트 13 〉 통과 (1.57ms, 10.5MB)
테스트 14 〉 통과 (1.58ms, 10.4MB)
테스트 15 〉 통과 (1.62ms, 10.6MB)
테스트 16 〉 통과 (1.60ms, 10.7MB)
테스트 17 〉 통과 (5.63ms, 10.6MB)
테스트 18 〉 통과 (5.79ms, 10.5MB)
테스트 19 〉 통과 (5.83ms, 10.4MB)
테스트 20 〉 통과 (6.32ms, 10.7MB)
테스트 21 〉 통과 (6.33ms, 10.9MB)
테스트 22 〉 통과 (6.80ms, 11MB)
테스트 23 〉 통과 (0.03ms, 10.4MB)
테스트 24 〉 통과 (0.03ms, 10.6MB)
테스트 25 〉 통과 (0.03ms, 10.4MB)
테스트 26 〉 통과 (0.03ms, 10.4MB)
테스트 27 〉 통과 (0.04ms, 10.4MB)
테스트 28 〉 통과 (0.04ms, 10.4MB)
테스트 29 〉 통과 (0.06ms, 10.4MB)
테스트 30 〉 통과 (0.05ms, 10.4MB)
효율성 테스트
테스트 1 〉 실패 (시간 초과)
테스트 2 〉 실패 (시간 초과)
테스트 3 〉 실패 (시간 초과)
테스트 4 〉 실패 (시간 초과)
테스트 5 〉 실패 (시간 초과)
테스트 6 〉 실패 (시간 초과)
테스트 7 〉 실패 (시간 초과)
테스트 8 〉 실패 (시간 초과)
테스트 9 〉 실패 (시간 초과)
테스트 10 〉 실패 (시간 초과)
"""

# 링크드리스트 풀이