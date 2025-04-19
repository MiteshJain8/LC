class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def count_pairs(bound):
            cnt, l, r = 0, 0, len(nums)-1
            while l < r:
                while l < r and nums[l] + nums[r] > bound:
                    r -= 1
                cnt += r - l
                l += 1
            return cnt
            
        nums.sort()
        return count_pairs(upper) - count_pairs(lower-1)