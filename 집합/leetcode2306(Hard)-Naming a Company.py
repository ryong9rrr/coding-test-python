# 이건 사실 "집합"문제인데, 떠올리기가 매우 어려운 아이디어임.
# 541ms(96.74%), 28.6MB(43.48%)
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        sets = collections.defaultdict(set)
        for idea in ideas:
            suffix = idea[0]
            sets[suffix].add(idea[1:])

        suffixes = list(sets.keys())
        n = len(suffixes)
        answer = 0
        for i in range(n - 1):
            for j in range(i, n):
                set_a = sets[suffixes[i]]
                set_b = sets[suffixes[j]]
                intersection_length = len(set_a & set_b)
                answer += 2 * (len(set_a) - intersection_length) * (len(set_b) - intersection_length)

        return answer