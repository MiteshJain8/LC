class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        cur_sum = k = 0
        diff = [0] * (n+1)

        for idx in range(n):
            while cur_sum + diff[idx] < nums[idx]:
                k += 1
                if k > q:
                    return -1

                left, right, val = queries[k-1]
                
                if right >= idx:
                    diff[max(left, idx)] += val
                    diff[right+1] -= val

            cur_sum += diff[idx]

        return k
