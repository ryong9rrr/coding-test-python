"""
이 코드는 실패한 풀이임...

DFS나 위상정렬로 접근한 리트코드 2360(Hard) 문제인데 코사라주 알고리즘으로 풀려하다가 테스트케이스 상에서 2개 이상의 그래프가 나올 수 있는 경우가 존재했기 때문에 실패... 아래 코사라주 알고리즘은 나중에 다시 써먹어보자.

참고한 블로그 : https://storyofvector7.tistory.com/32
참고(타잔 알고리즘) : https://storyofvector7.tistory.com/44 (타잔 알고리즘도 나중에 다시 보면 좋을 듯)
"""

```python
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        # 1. 정방향 그래프와 역방향 그래프 생성
        graph = collections.defaultdict(list)
        rev_graph = collections.defaultdict(list)
        for v, w in enumerate(edges):
            graph[v].append(w)
            rev_graph[w].append(v)

        # 2. 정방향 DFS 수행
        finished = []
        visited = [False] * n
        def dfs(v):
            visited[v] = True
            for w in graph[v]:
                if not visited[w]:
                    visited[w] = True
                    dfs(w)
            finished.append(v)

        for v in range(n):
            if not visited[v]:
                visited[v] = True
                dfs(v)

        # 3. 마지막에 탐색이 완료된 순으로 역방향 DFS 수행
        visited = [False] * n # 방문기록 초기화
        def rev_dfs(v, elements):
            elements.append(v)
            for w in rev_graph[v]:
                if not visited[w]:
                    visited[w] = True
                    rev_dfs(w, elements)

        scc_groups = []
        while finished:
            v = finished.pop()
            if not visited[v]:
                scc = []
                visited[v] = True
                rev_dfs(v, scc)
                scc_groups.append(scc)

        print(scc_groups)

        # 가장 긴 그룹의 길이가 1이라면 scc가 없는 상황
        result = 1
        for scc in scc_groups:
            result = max(result, len(scc))
        return -1 if result == 1 else result
```
