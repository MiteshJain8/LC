class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        total = l = cur_sum = 0
        hset = set()
        for r in range(len(nums)):
            if nums[r] in hset:
                while nums[r] in hset:
                    cur_sum -= nums[l]
                    hset.remove(nums[l])
                    l += 1
            hset.add(nums[r])
            cur_sum += nums[r]
            total = max(total, cur_sum)

        return total
