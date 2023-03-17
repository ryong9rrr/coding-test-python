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
        self.count = 0
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            node.count += 1

    def startsWithCount(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

def solution(words, queries):
    trie_table = defaultdict(Trie)
    trie_table2 = defaultdict(Trie)
    counter = defaultdict(int)
    
    for word in words:
        key = len(word)
        trie_table[key].insert(word)
        trie_table2[key].insert(word[::-1])
        counter[key] += 1
        
    result = []
    for query in queries:
        key = len(query)
        if not counter[key]:
            result.append(0)
            continue
            
        q = query.replace("?", "")
        if not q:
            result.append(counter[key])
            continue
        
        if query[0] == "?":
            count = trie_table2[key].startsWithCount(q[::-1])
            result.append(count)
            continue
        
        count = trie_table[key].startsWithCount(q)
        result.append(count)
        
    return result
"""
정확성  테스트
테스트 1 〉	통과 (1.07ms, 10.4MB)
테스트 2 〉	통과 (0.32ms, 10.1MB)
테스트 3 〉	통과 (0.46ms, 10.4MB)
테스트 4 〉	통과 (0.44ms, 10.3MB)
테스트 5 〉	통과 (0.28ms, 10.4MB)
테스트 6 〉	통과 (0.52ms, 10.4MB)
테스트 7 〉	통과 (7.99ms, 12.8MB)
테스트 8 〉	통과 (3.23ms, 11MB)
테스트 9 〉	통과 (7.28ms, 12.5MB)
테스트 10 〉	통과 (12.97ms, 12.7MB)
테스트 11 〉	통과 (3.06ms, 10.8MB)
테스트 12 〉	통과 (7.77ms, 12.8MB)
테스트 13 〉	통과 (43.49ms, 22.3MB)
테스트 14 〉	통과 (16.47ms, 15.3MB)
테스트 15 〉	통과 (45.23ms, 21.9MB)
테스트 16 〉	통과 (46.14ms, 23MB)
테스트 17 〉	통과 (15.69ms, 15MB)
테스트 18 〉	통과 (60.17ms, 21.6MB)
효율성  테스트
테스트 1 〉	통과 (1470.07ms, 206MB)
테스트 2 〉	통과 (3340.63ms, 389MB)
테스트 3 〉	통과 (2983.81ms, 367MB)
테스트 4 〉	통과 (3037.03ms, 434MB)
테스트 5 〉	통과 (7031.52ms, 818MB)
"""