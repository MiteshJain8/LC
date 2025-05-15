class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        start = groups[0]
        res = [words[0]]
        for w,g in zip(words,groups):
            if g == start:
                continue
            start = 1 - start
            res.append(w)
        return res