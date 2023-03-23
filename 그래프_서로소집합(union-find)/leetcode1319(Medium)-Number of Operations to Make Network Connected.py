# 유니온파인드 풀이 : 465ms(97.9%), 34MB(76.41%)

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = [x for x in range(n)]
        edges = n - 1
        for v, w in connections:
            if edges == 0:
                return 0
            if find_parent(parent, v) != find_parent(parent, w):
                union_parent(parent, v, w)
                edges -= 1

        return edges