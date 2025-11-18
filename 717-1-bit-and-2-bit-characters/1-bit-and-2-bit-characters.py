class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        flag = True
        while i < n:
            if bits[i] == 0:
                i += 1
                flag = True
            else:
                i += 2
                flag = False
        return flag