class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1
        for _ in range(t):
            z = count[25]
            for j in range(25, 0, -1):
                count[j] = count[j-1]
            count[0] = z
            count[1] += z

        return sum(count) % 1000000007