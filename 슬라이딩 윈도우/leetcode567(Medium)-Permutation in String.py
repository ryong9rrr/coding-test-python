# 나의 풀이(최적화 되지 않은 정직한 슬라이딩 윈도우, 리트코드 오피셜 "Approach 2: Using sorting" 접근과 비슷)
# : 3997ms(12.63%), 14.1MB(28.54%)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = "".join(sorted(s1))

        windows_size = len(s1)

        for i in range(len(s2) - windows_size + 1):
            windows = "".join(sorted(s2[i : i + windows_size]))
            if target == windows:
                return True

        return False
    
# 1단계 개선된 슬라이딩 윈도우(리스트 형태의 테이블 이용) : 71ms(81.14%), 14MB(64.59%)
class Solution:
    def is_matched(self, s1map, s2map):
        for i in range(26):
            if s1map[i] != s2map[i]:
                return False
        return True

    def index(self, char):
        return ord(char) - 97

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        s2map = [0] * 26
        for i in range(len(s1)):
            s1map[self.index(s1[i])] += 1
            s2map[self.index(s2[i])] += 1

        WINDOW_SIZE = len(s1)
        for i in range(len(s2) - WINDOW_SIZE):
            if self.is_matched(s1map, s2map):
                return True
            s2map[self.index(s2[i])] -= 1
            s2map[self.index(s2[i + WINDOW_SIZE])] += 1

        return self.is_matched(s1map, s2map)
    

# 26개의 배열을 순회하지 않도록 더 개선된 슬라이딩 윈도우(근데 파이썬이라 그런지 속도면에서는 별 차이가 없었음)
# 73ms(78.34%), 14MB(28.54%)
class Solution:
    def index(self, char):
        return ord(char) - 97

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        s2map = [0] * 26
        for i in range(len(s1)):
            s1map[self.index(s1[i])] += 1
            s2map[self.index(s2[i])] += 1

        count = sum([1 if s1map[i] == s2map[i] else 0 for i in range(26)])
        WINDOW_SIZE = len(s1)
        for i in range(len(s2) - WINDOW_SIZE):
            if count == 26:
                return True

            prev_index = self.index(s2[i])
            next_index = self.index(s2[i + WINDOW_SIZE])
            
            s2map[next_index] += 1
            if s2map[next_index] == s1map[next_index]:
                count += 1
            elif s2map[next_index] == s1map[next_index] + 1:
                count -= 1
            
            s2map[prev_index] -= 1
            if s2map[prev_index] == s1map[prev_index]:
                count += 1
            elif s2map[prev_index] == s1map[prev_index] - 1:
                count -= 1

        return count == 26