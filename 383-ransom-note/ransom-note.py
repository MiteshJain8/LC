class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = [0] * 26
        for c in magazine:
            hmap[ord(c)-97] += 1
        for c in ransomNote:
            if hmap[ord(c)-97]:
                hmap[ord(c)-97] -= 1
            else:
                return False
        return True
