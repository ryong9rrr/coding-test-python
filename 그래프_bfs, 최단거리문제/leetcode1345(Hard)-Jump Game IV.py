# (내가 푼 풀이) DP식 BFS : 619ms(99.19%), 27.3Mb(97.7%)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = collections.defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)

        q = collections.deque()
        dist = [-1] * n

        q.append(n - 1)
        dist[n - 1] = 0

        while q:
            index = q.popleft()
            num = arr[index]
            for i in graph[num]:
                if dist[i] == -1:
                    dist[i] = dist[index] + 1
                    q.append(i)

            graph[num] = [] # clear

            if index + 1 < n and dist[index + 1] == -1:
                dist[index + 1] = dist[index] + 1
                q.append(index + 1)

            if index - 1 >= 0 and dist[index - 1] == -1:
                dist[index - 1] = dist[index] + 1
                q.append(index - 1)
            
            if dist[0] != -1:
                break

        return dist[0]


# 리트코드 솔루션 1 (BFS) : 773ms(75.94%), 28.4MB(84.72%)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1




# 리트코드 솔루션 2 (양방향 BFS) : 645ms(97.4%), 27.8MB(90.57%)
class Solution:
    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])  # store layers from start
        visited = {0, n-1}
        step = 0

        other = set([n-1]) # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1