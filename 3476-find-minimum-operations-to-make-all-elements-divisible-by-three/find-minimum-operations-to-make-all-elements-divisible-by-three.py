class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            if i%3!=0:
                k+=1
        return k