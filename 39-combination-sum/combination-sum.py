class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(curList):
            curSum = sum(curList)
            if curSum == target:
                curList.sort()
                if curList not in res:
                    res.append(curList)
                return
                
            for c in candidates:
                if curSum + c <= target:
                    backtrack(curList + [c])
                else:
                    break
            return

        res = []
        candidates.sort()
        backtrack([])
        return res