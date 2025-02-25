class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n, res = len(arr), 0
        cur_sum, odd_cnt, even_cnt = 0, 0, 0
        for num in arr:
            cur_sum += num
            if cur_sum & 1:
                res += 1 + even_cnt
                odd_cnt += 1
            else:
                res += odd_cnt
                even_cnt += 1
        return res % (10**9 + 7)
