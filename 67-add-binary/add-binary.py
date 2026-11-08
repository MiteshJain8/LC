class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p, q = 0, 0
        for c in a:
            p *= 2
            p += int(c)
        for c in b:
            q *= 2
            q += int(c)
        return bin(p+q)[2:]
