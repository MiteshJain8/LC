class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate, votes, n = -1, 0, len(nums)
        for i in range(n):
            if (votes == 0):
                candidate = nums[i]
                votes = 1
            else:
                if (nums[i] == candidate):
                    votes += 1
                else:
                    votes -= 1

        votes = 0
        for j in range(n):
            if nums[j] == candidate:
                votes += 1
                if 2*votes > j+1:
                    return j if 2*nums[j+1:].count(candidate) > n-j-1 else -1
        return -1