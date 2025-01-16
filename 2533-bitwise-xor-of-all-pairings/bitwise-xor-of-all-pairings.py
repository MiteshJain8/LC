class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1, x2 = 0, 0
        if len(nums1) & 1:
            x2 = reduce(lambda x, y: x ^ y, nums2)
        if len(nums2) & 1:
            x1 = reduce(lambda x, y: x ^ y, nums1)
        return x1 ^ x2