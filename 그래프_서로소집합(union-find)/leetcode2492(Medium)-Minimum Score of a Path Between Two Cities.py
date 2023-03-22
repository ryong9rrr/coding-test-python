# 별로 좋은 문제는 아닌 것 같다. (문제의 설명이 애매하고 예시도 부족함)
# 유니온파인드 : 1618ms(93.96%), 58.6MB(96.31%)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    x, y = find_parent(parent, a), find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [v for v in range(n + 1)]
        for v, w, distance in roads:
            union_parent(parent, v, w)

        ans = int(1e9)
        for v, w, distance in roads:
            if find_parent(parent, 1) == find_parent(parent, v):
                ans = min(ans, distance)

        return ans