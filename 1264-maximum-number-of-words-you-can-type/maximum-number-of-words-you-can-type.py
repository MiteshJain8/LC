class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = list(text.split())
        res = 0
        for word in text:
            for c in brokenLetters:
                if c in word:
                    break
            else:
                res += 1

        return res