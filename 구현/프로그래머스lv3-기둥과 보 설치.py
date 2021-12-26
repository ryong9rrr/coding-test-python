# 이코테 풀이
def solution(n, build_frame):
    def possible(answer:list)->bool:
        for x, y, a in answer:
            # 설치된 것이 기둥이라면
            if a == 0:
                # 바닥에 설치됐을 경우 or 기둥 위에 설치됐을 경우 or 보의 한쪽 끝에 설치됐을 경우(2가지)
                if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                    continue
                # 위에서 안걸러졌으면 설치 불가
                return False

            # 설치된 것이 보 라면
            elif a == 1:
                # 기둥 위에 설치됐을 경우(2가지) or 보 사이에 낑길 경우
                if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                    continue
                return False
        return True

    answer = []
    for x, y, a, b in build_frame:
        # 삭제할 경우
        if b == 0:
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        # 설치할 경우
        elif b == 1:
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])

    return sorted(answer)

"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.14ms, 10.3MB)
테스트 5 〉	통과 (0.15ms, 10.2MB)
테스트 6 〉	통과 (0.48ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.06ms, 10.3MB)
테스트 10 〉	통과 (283.14ms, 10.4MB)
테스트 11 〉	통과 (1864.44ms, 10.6MB)
테스트 12 〉	통과 (223.71ms, 10.4MB)
테스트 13 〉	통과 (1928.63ms, 10.6MB)
테스트 14 〉	통과 (213.56ms, 10.5MB)
테스트 15 〉	통과 (2143.81ms, 10.6MB)
테스트 16 〉	통과 (213.29ms, 10.4MB)
테스트 17 〉	통과 (1900.47ms, 10.6MB)
테스트 18 〉	통과 (1252.07ms, 10.4MB)
테스트 19 〉	통과 (1333.66ms, 10.6MB)
테스트 20 〉	통과 (1250.31ms, 10.5MB)
테스트 21 〉	통과 (1377.70ms, 10.5MB)
테스트 22 〉	통과 (978.95ms, 10.5MB)
테스트 23 〉	통과 (1344.02ms, 10.5MB)
"""