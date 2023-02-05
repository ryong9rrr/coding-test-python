# leetcode 567 문제와 동일한 문제임
# 딕셔너리 해시테이블 풀이 : 333ms(40.9%), 15.2MB(74.41%)
class Solution:
    def lower_alphabets(self):
        return [chr(i) for i in range(97, 123)]

    def is_matched(self, a_map, b_map):
        for key in self.lower_alphabets():
            if a_map[key] != b_map[key]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        s_map = collections.defaultdict(int)
        p_map = collections.defaultdict(int)

        for i in range(len(p)):
            s_map[s[i]] += 1
            p_map[p[i]] += 1

        result = []
        for i in range(len(s) - len(p)):
            if self.is_matched(s_map, p_map):
                result.append(i)
            s_map[s[i]] -= 1
            s_map[s[i + len(p)]] += 1

        if self.is_matched(s_map, p_map):
            result.append(len(s) - len(p))

        return result