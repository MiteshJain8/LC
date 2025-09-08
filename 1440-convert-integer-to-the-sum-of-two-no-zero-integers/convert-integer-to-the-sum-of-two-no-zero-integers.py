class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(num):
            if '0' in str(num):
                return True
            return False

        a, b = 1, n-1
        while True:
            if has_zero(a) or has_zero(b):
                a += 1
                b -= 1
            else:
                return [a, b]