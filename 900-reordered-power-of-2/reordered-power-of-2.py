class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ctr = sorted(str(n))
        return any(sorted(str(1<<i)) == ctr for i in range(32))