#시간초과
def solution(n):
    def check(queens, row):
        for i in range(row):
            if queens[i] == queens[row] or abs(queens[i] - queens[row]) == abs(i - row):
                return False
        return True

    def search(queens, row):
        count = 0
        if n == row:
            return 1
        for col in range(n):
            queens[row] = col
            if check(queens, row):
                count += search(queens, row + 1)
        return count
    
    queens = [0] * n
    return search(queens, 0)
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 9.97MB)
테스트 4 〉	통과 (0.15ms, 10.3MB)
테스트 5 〉	통과 (0.60ms, 10.1MB)
테스트 6 〉	통과 (2.40ms, 10.1MB)
테스트 7 〉	통과 (11.46ms, 10.3MB)
테스트 8 〉	통과 (73.52ms, 10.2MB)
테스트 9 〉	통과 (319.70ms, 10.2MB)
테스트 10 〉	통과 (1814.47ms, 10.2MB)
테스트 11 〉	실패 (시간 초과)
"""

#백준에서는 통과못함
def solution(n):
    global count
    count = 0
    check_x = [False] * n
    check_d1 = [False] * n * 2
    check_d2 = [False] * n * 2

    def search(row):
        global count
        if row == n:
            count += 1
            return
        
        for x in range(n):
            d1 = row + x
            d2 = row - x + n
            if check_x[x] or check_d1[d1] or check_d2[d2]:
                continue
            check_x[x] = True
            check_d1[d1] = True
            check_d2[d2] = True

            search(row + 1)
            check_x[x] = False
            check_d1[d1] = False
            check_d2[d2] = False
    
    search(0)
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.19ms, 10.2MB)
테스트 6 〉	통과 (0.96ms, 10.2MB)
테스트 7 〉	통과 (2.48ms, 10.2MB)
테스트 8 〉	통과 (15.95ms, 10.1MB)
테스트 9 〉	통과 (54.42ms, 10.4MB)
테스트 10 〉	통과 (232.22ms, 10.3MB)
테스트 11 〉	통과 (1442.20ms, 10.2MB)
"""