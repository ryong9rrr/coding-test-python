# 나의 풀이, 리트코드 솔루션과 거의 동일 : 42ms(55.42%), 13.9MB(31.27%)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        freq = collections.defaultdict(int)

        # 우선순위 value(i)가 작을수록 우선순위가 높은 것
        for i, char in enumerate(order):
            freq[char] = i

        for i in range(len(words) - 1):
            cur_word = words[i]
            next_word = words[i + 1]
            min_length = min(len(cur_word), len(next_word))
            
            for j in range(min_length):
                cur_char = cur_word[j]
                next_char = next_word[j]
                # 다음 문자의 우선순위 value가 크다면 다음 문자의 우선순위가 더 작다는 것(현재 문자의 우선순위가 더 크다는 것)
                # 이므로 더 확인할 필요가 없음
                if freq[cur_char] < freq[next_char]:
                    break
                # 현재 문자의 우선순위가 더 작다면
                if freq[cur_char] > freq[next_char]:
                    return False
                # 마지막 문자를 확인하고, 두 단어의 길이를 체크한다.
                # 현재 문자의 길이가 더 길다면 다음 문자의 뒤에 나와야하는 것이므로 정렬되어있지 않은 상태임
                if j == min_length - 1 and len(cur_word) > len(next_word):
                    return False

        return True