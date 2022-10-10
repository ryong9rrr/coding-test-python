"""
<사용된 문제>
- 프로그래머스 Lv4 - 카카오 : 가사 검색
"""
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

    # 단어가 존재하는지
    def search(self, word:str)->bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    # 해당 문자열로 시작하는 단어가 존재하는지
    def startsWith(self, prefix:str)->bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    # 해당 문자열로 시작하는 단어가 몇 개인지
    def startsWithCount(self, prefix:str)->bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count