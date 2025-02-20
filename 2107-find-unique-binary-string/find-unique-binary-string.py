class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = set()
        for num in nums:
            num = int(num)
            p, q = 0, 0
            while num:
                p += (2 ** q) * (num%10)
                q += 1
                num //= 10
            res.add(p)
        for i in range(2 ** len(nums)-1,-1,-1):
            if i not in res:
                ans  = bin(i)[2:]
                zeros = len(nums[0]) - len(ans)
                return "0" * zeros + ans