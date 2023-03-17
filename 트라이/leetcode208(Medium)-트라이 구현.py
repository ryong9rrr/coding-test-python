class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def searchPrefixNode(self, word: str) -> TrieNode:
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefixNode(word)
        return node.isWord if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefixNode(prefix)
        return True if node else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)