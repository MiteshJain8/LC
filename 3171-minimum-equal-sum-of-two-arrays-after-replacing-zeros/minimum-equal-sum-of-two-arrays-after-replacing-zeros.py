class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = z2 = s1 = s2 = 0
        for num in nums1:
            if num:
                s1 += num
            else:
                z1 += 1
        for num in nums2:
            if num:
                s2 += num
            else:
                z2 += 1
        if z1 == z2 and s1 == s2:
            return s1 + z1
        elif z2 == 0 and s2 < s1 + z1:
            return -1
        elif z1 == 0 and s1 < s2 + z2:
            return -1
        else:
            return max(s1+z1, s2+z2) 
            