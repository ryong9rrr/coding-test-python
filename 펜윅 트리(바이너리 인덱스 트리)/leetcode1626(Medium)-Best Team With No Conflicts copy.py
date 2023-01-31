# 동적계획법 풀이 : O(N^2), 1736ms(73.76%), 14.2MB(83.69%)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        
        # [age, score][]
        pair = []
        for i in range(N):
            pair.append([ages[i], scores[i]])
        # 나이순대로 정렬
        pair.sort()

        # 처음에는 정렬된 배열의 점수로 초기화
        dp = [score for age, score in pair]
        
        for i in range(N):
            cur_score = pair[i][1]
            for j in range(i - 1, -1, -1):
                prev_score = pair[j][1]
                # (이미 나이 순대로 정렬했으므로 나이는 비교하지 않음, 무조건 뒷 사람이 더 나이가 같거나 많은 사람)
                # 뒷 사람(cur)의 점수가 더 클 경우에만 갱신
                if cur_score >= prev_score:
                    dp[i] = max(dp[i], cur_score + dp[j])

        return max(dp)
    

"""
인덱스 트리(Fenwick Tree) : 232ms(98.58%), 14.1MB(83.69%)

플레이어의 수가 N, 가장 많은 나이가 K일 때,
- 시간복잡도 : NlogN + NlogK
- 공간복잡도 : N + K
"""
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        def query_tree(tree, age):
            max_value = float('-inf')
            i = age
            while i > 0:
                max_value = max(max_value, tree[i])
                i -= (i & -i)
            return max_value

        def update_tree(tree, age, current_best):
            i = age
            while i < len(tree):
                tree[i] = max(tree[i], current_best)
                i += (i & -i)

        N = len(scores)
        
        # [score, age]
        pair = []
        for i in range(N):
            pair.append([scores[i], ages[i]])
        pair.sort()

        highest_age = max(ages)
        tree = [0] * (highest_age + 1)

        answer = float('-inf')
        for score, age in pair:
            current_best = score + query_tree(tree, age)
            
            update_tree(tree, age, current_best)
            
            answer = max(answer, current_best)

        # return max(tree)
        return answer