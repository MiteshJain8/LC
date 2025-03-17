class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hmap = Counter(nums)
        for val in hmap.values():
            if val & 1:
                return False
        return True