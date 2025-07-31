class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        for i in range(n-1):
            l, r = i-1, i+1
            cur_max = deque([s[i]])
            if s[r] == s[i]:
                cur_max.append(s[r])
                r += 1
                while 0 <= l and r < n and s[l] == s[r]:
                    cur_max.append(s[r])
                    cur_max.appendleft(s[l])
                    l -= 1
                    r += 1
            if len(cur_max) > len(ans):
                ans = "".join(cur_max)
            cur_max = deque([s[i]])
            l, r = i-1, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                cur_max.append(s[r])
                cur_max.appendleft(s[l])
                l -= 1
                r += 1
            if len(cur_max) > len(ans):
                ans = "".join(cur_max)

        return ans