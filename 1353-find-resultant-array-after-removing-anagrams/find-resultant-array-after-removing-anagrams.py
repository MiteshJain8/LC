class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        temp = [""] * n
        for i in range(n):
            temp[i] = sorted(words[i])
        res = [words[0]]
        for i in range(1, n):
            if temp[i-1] != temp[i]:
                res.append(words[i])

        return res