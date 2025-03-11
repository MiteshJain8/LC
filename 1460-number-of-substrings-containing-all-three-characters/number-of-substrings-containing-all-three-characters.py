class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_count = {}
        start = 0
        valid_substrings = 0

        for end in range(len(s)):
            char_count[s[end]] = char_count.get(s[end], 0) + 1

            while len(char_count) == 3:
                valid_substrings += len(s) - end
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    del char_count[s[start]]
                start += 1

        return valid_substrings