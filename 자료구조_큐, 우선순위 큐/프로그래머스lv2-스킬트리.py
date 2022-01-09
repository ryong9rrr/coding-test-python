from collections import deque, defaultdict
def check_skill(key:str, target:str)->int:
    dic = defaultdict(int)
    for i, v in enumerate(key):
        dic[v] = i + 1
    visited = [True] + [False] * 26
    q = deque()
    for a in target:
        q.append(a)
    
    while q:
        x = q.popleft()
        if dic[x]:
            if visited[dic[x] - 1]:
                visited[dic[x]] = True
            else:
                return 0
    if not q:
        return 1


def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        result += check_skill(skill, skill_tree)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
"""

# 가독성도 좋고 로직 자체도 더 좋은 풀이
# 위 풀이에서는 굳이 알파벳들의 배열을 선언했고,
# 딕셔너리로 선행스킬을 담았는데, 굳이 그럴필요없고
# 둘 다 큐로 선언해서 앞에서 부터 빼주면 됨

from collections import deque

def check_skill(skill, skill_tree):
    # 선행스킬목록을 큐에 담음
    skill_q = deque()
    for s in skill:
        skill_q.append(s)
    
    # 제시된 스킬트리 중 선행스킬목록에 있는 스킬만 큐에 담음
    q = deque()
    for s in skill_tree:
        if s in skill:
            q.append(s)
    
    # 제시된 스킬트리 중 선행스킬목록에 있는 스킬만 담은 큐가 비었다? 
    # -> 아무거나 막찍어도 가능한 스킬트리임 -> return 1
    # 그런데 이 코드는 없어도 됨 (while skill_q and q 이므로)
    if not q:
        return 1
    
    while skill_q and q:
        if skill_q.popleft() != q.popleft():
            return 0
    return 1

def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        result += check_skill(skill, skill_tree)
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
"""