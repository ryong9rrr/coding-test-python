# 정렬 + bisect 이분탐색
from collections import defaultdict
from bisect import bisect_left, bisect_right

def search(array, target):
    lo = bisect_left(array, target.replace("?", "a"))
    hi = bisect_right(array, target.replace("?", "z"))
    if (hi - lo) < 0:
        return 0
    return hi - lo
    

def solution(words, queries):
    table = defaultdict(list)
    reverse_table = defaultdict(list)
    for word in words:
        key = len(word)
        table[key].append(word)
        reverse_table[key].append(word[::-1])
    
    for key in table:
        table[key].sort()
        reverse_table[key].sort()
    
    result = []
    for query in queries:
        key = len(query)
        if not table[key]:
            result.append(0)
            continue
        if query[-1] == "?":
            count = search(table[key], query)
            result.append(count)
        elif query[0] == "?":
            count = search(reverse_table[key], query[::-1])
            result.append(count)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.32ms, 10.3MB)
테스트 8 〉	통과 (0.39ms, 10.2MB)
테스트 9 〉	통과 (0.74ms, 10.2MB)
테스트 10 〉	통과 (0.27ms, 10.4MB)
테스트 11 〉	통과 (0.28ms, 10.3MB)
테스트 12 〉	통과 (0.34ms, 10.3MB)
테스트 13 〉	통과 (1.60ms, 10.4MB)
테스트 14 〉	통과 (1.50ms, 10.4MB)
테스트 15 〉	통과 (1.56ms, 10.4MB)
테스트 16 〉	통과 (2.84ms, 10.3MB)
테스트 17 〉	통과 (1.51ms, 10.4MB)
테스트 18 〉	통과 (1.57ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (96.47ms, 22.6MB)
테스트 2 〉	통과 (130.26ms, 25.2MB)
테스트 3 〉	통과 (117.78ms, 26.2MB)
테스트 4 〉	통과 (3.63ms, 13.8MB)
테스트 5 〉	통과 (2.93ms, 13.6MB)
"""

########################## 정렬 + 이분탐색 ############################
from collections import defaultdict
from bisect import bisect_left, bisect_right

def search(arr, target):
    def lower(arr, target):
        target = target.replace("?", "a")
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if target <= arr[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def upper(arr, target):
        target = target.replace("?", "z")
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if target < arr[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    lo = lower(arr, target)
    hi = upper(arr, target)
    return hi - lo if hi - lo >= 0 else 0
    

def solution(words, queries):
    table = defaultdict(list)
    reverse_table = defaultdict(list)
    for word in words:
        key = len(word)
        table[key].append(word)
        reverse_table[key].append(word[::-1])
    
    for key in table:
        table[key].sort()
        reverse_table[key].sort()
    
    result = []
    for query in queries:
        key = len(query)
        if not table[key]:
            result.append(0)
            continue
        if query[-1] == "?":
            count = search(table[key], query)
            result.append(count)
        elif query[0] == "?":
            count = search(reverse_table[key], query[::-1])
            result.append(count)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.82ms, 10.5MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (0.07ms, 10.4MB)
테스트 7 〉	통과 (0.56ms, 10.3MB)
테스트 8 〉	통과 (0.68ms, 10.2MB)
테스트 9 〉	통과 (0.71ms, 10.3MB)
테스트 10 〉	통과 (0.44ms, 10.4MB)
테스트 11 〉	통과 (0.49ms, 10.3MB)
테스트 12 〉	통과 (0.52ms, 10.4MB)
테스트 13 〉	통과 (2.95ms, 10.4MB)
테스트 14 〉	통과 (2.88ms, 10.4MB)
테스트 15 〉	통과 (2.93ms, 10.4MB)
테스트 16 〉	통과 (2.94ms, 10.2MB)
테스트 17 〉	통과 (2.90ms, 10.3MB)
테스트 18 〉	통과 (2.91ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (246.19ms, 22.7MB)
테스트 2 〉	통과 (317.60ms, 25.3MB)
테스트 3 〉	통과 (287.90ms, 26.2MB)
테스트 4 〉	통과 (3.53ms, 13.4MB)
테스트 5 〉	통과 (3.33ms, 13.7MB)
"""

################################# Trie 풀이 ##################################
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word:str)->None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.count += 1
        node.word = True
    
    # 해당 문자열로 시작하는 단어가 몇 개인지
    def startsWithCount(self, prefix:str)->bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

def solution(words, queries):
    table = defaultdict(Trie)
    reverse_table = defaultdict(Trie)
    counter = defaultdict(int)
    
    for word in words:
        key = len(word)
        table[key].insert(word)
        reverse_table[key].insert(word[::-1])
        counter[key] += 1
        
    result = []
    for query in queries:
        key = len(query)
        if key not in table:
            result.append(0)
            continue
        t_query = query.replace("?", "")
        if not t_query:
            result.append(counter[key])
            continue
        if query[-1] == "?":
            count = table[key].startsWithCount(t_query)
            result.append(count)
        else:
            count = reverse_table[key].startsWithCount(t_query[::-1])
            result.append(count)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (1.11ms, 10.6MB)
테스트 2 〉	통과 (0.27ms, 10.3MB)
테스트 3 〉	통과 (0.49ms, 10.3MB)
테스트 4 〉	통과 (0.44ms, 10.4MB)
테스트 5 〉	통과 (0.49ms, 10.4MB)
테스트 6 〉	통과 (0.78ms, 10.3MB)
테스트 7 〉	통과 (8.64ms, 13MB)
테스트 8 〉	통과 (3.46ms, 11MB)
테스트 9 〉	통과 (10.33ms, 12.6MB)
테스트 10 〉	통과 (13.73ms, 12.8MB)
테스트 11 〉	통과 (3.77ms, 10.9MB)
테스트 12 〉	통과 (11.40ms, 12.8MB)
테스트 13 〉	통과 (48.16ms, 22.3MB)
테스트 14 〉	통과 (17.98ms, 15.3MB)
테스트 15 〉	통과 (46.65ms, 22.1MB)
테스트 16 〉	통과 (49.61ms, 23MB)
테스트 17 〉	통과 (16.20ms, 15MB)
테스트 18 〉	통과 (43.83ms, 21.8MB)
효율성  테스트
테스트 1 〉	통과 (1452.53ms, 206MB)
테스트 2 〉	통과 (3350.32ms, 389MB)
테스트 3 〉	통과 (3047.68ms, 367MB)
테스트 4 〉	통과 (2944.32ms, 434MB)
테스트 5 〉	통과 (6893.49ms, 818MB)
"""