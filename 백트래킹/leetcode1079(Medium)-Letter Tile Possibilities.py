# 순열로 완전탐색 : 95ms, 16.8MB
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = 0
        for i in range(1, len(tiles) + 1):
            permus = list(itertools.permutations(tiles, i))
            pick = set(["".join(list(x)) for x in permus])
            result += len(pick)
        return result

# 백트래킹 : 72ms, 13.9MB (Counter 사용 시 100ms)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # 백트래킹
        def dfs(table):
            if sum(table.values()) <= 0:
                return 0

            result = 0
            for tile in table.keys():
                if table[tile] <= 0:
                    continue
                table[tile] -= 1
                result += dfs(table) + 1
                table[tile] += 1
            return result

        return dfs(collections.Counter(tiles))