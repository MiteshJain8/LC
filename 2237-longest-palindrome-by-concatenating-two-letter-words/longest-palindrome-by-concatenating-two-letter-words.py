class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        hmap = defaultdict(int)
        for word in words:
            if hmap[word[::-1]] > 0:
                res += 4
                hmap[word[::-1]] -= 1
            else:
                hmap[word] += 1
        for k,v in hmap.items():
            if k[0] == k[1] and v:
                res += 2
                break
        return res