"""
접근 : 유니온파인드 + 수학(약간의 수학적 규칙)
- 시간복잡도 : 노드의 개수가 N, 간선의 개수가 E 일 때 O(N + E)
- 공간복잡도 : O(N)
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    x, y = find_parent(parent, a), find_parent(parent, b)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 유니온파인드
        parent = [x for x in range(n)]
        for v, w in edges:
            union_parent(parent, v, w)

        # parent를 한번 더 갱신해주면서 카운트
        groups = collections.Counter([find_parent(parent, x) for x in parent])
        ans = 0
        for count in groups.values():
            ans += (count * (n - count))
            n -= count
        
        return ans