class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_ele = max(nums)
        cur_cnt = j = res = 0
        n = len(nums)
        while j < n and cur_cnt < k:
            if nums[j] == max_ele:
                    cur_cnt += 1
            j += 1
        if cur_cnt == k:
            res = (n-j+1)
        else:
            return 0
        for i in range(n):
            if nums[i] == max_ele:
                cur_cnt -= 1
            while j < n and cur_cnt < k:
                if nums[j] == max_ele:
                    cur_cnt += 1
                j += 1
            if cur_cnt == k:
                res += (n-j+1)
            else:
                return res
        return res