# 잘못된 접근 - 단어는 무한대로 존재하기 때문에 순열로는 풀 수 없다.
from itertools import permutations
def solution(strs, t):
    N = len(strs)
    
    def search():
        result = int(1e9)
        for i in range(1, N + 1):
            for x in list(permutations(strs, i)):
                if "".join(x) == t:
                    return i
        return result
    
    print(search())