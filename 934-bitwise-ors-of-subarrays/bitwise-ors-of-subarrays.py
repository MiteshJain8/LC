class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res, prev = set(), set()
        for num in arr:
            cur = set()
            for k in prev:
                cur.add(num | k)
                res.add(num | k)
            cur.add(num)
            res.add(num)
            prev = cur

        return len(res)