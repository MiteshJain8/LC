class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        a, b = nums[i], nums[j]
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for val in {a + b, a - b, a * b, b and a / b}:
                            if dfs(next_nums + [val]):
                                return True
            return False

        for perm in itertools.permutations(cards):
            if dfs(list(perm)):
                return True
        return False