# 9283ms(72.19%), 80.4MB(12.52%)

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word :
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.match(self.root, 0, word)

    # DFS
    def match(self, node: TrieNode, index: int, word: str) -> bool:
        if index == len(word):
            return node.isWord
        
        char = word[index]
        if char == ".":
            for nextChar in node.children.keys():
                if self.match(node.children[nextChar], index + 1, word):
                    return True
            return False
        
        return char in node.children and self.match(node.children[char], index + 1, word)