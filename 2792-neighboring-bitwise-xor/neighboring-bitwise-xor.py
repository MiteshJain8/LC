class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not reduce(lambda x, y: x ^ y, derived)