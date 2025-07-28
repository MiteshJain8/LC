class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = Trie()
            cur = cur.children[word[i]]

        cur.isEnd = True
        
    def search(self, word: str) -> bool:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)