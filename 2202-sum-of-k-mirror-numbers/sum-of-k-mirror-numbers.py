class Solution:
    def kMirror(self, k: int, n: int) -> int:
        current = [str(i) for i in range(1, k)]
        ans = 0
        odd = True
        half_len = 1
        while n:
            next = []
            for c in current:
                a = int(c, k)
                b = str(a)
                if b == b[::-1]:
                    ans += a
                    n -= 1
                    if n == 0:
                        return ans
                if odd:
                    next.append(c[:half_len] + c[half_len-1] + c[half_len:])
                else:
                    for i in range(k):
                        next.append(c[:half_len] + str(i) + c[half_len:])
            current = next
            odd = not odd
            if odd:
                half_len += 1