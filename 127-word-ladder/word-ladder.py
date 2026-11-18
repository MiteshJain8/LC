class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        w = len(endWord)
        for word in wordList:
            for i in range(w):
                key = word[:i] + "*" + word[i+1:]
                adj[key].append(word)
        dq = deque([beginWord])
        res = 1
        while dq:
            res += 1
            for _ in range(len(dq)):
                word = dq.popleft()
                for i in range(w):
                    key = word[:i] + "*" + word[i+1:]
                    for nei in adj[key]:
                        if nei in wordList:
                            if nei == endWord:
                                return res
                            wordList.remove(nei)
                            dq.append(nei)
        return 0