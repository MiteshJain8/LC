class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for perm in itertools.permutations(str(n)):
            if perm[0] == "0":
                continue

            val = int("".join(perm))
            if (val & (val - 1)) == 0:
                return True

        return False