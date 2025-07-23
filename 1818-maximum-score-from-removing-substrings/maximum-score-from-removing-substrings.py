class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def one_pass(cur, p, q, val):
            nonlocal res
            stack = []
            for i in range(len(cur)):
                if cur[i] == q and stack and stack[-1] == p:
                    stack.pop()
                    res += val
                else:
                    stack.append(cur[i])

            return "".join(stack)

        res = 0
        if x < y:
            remaining_s = one_pass(s, 'b', 'a', y)
            one_pass(remaining_s, 'a', 'b', x)
        else:
            remaining_s = one_pass(s, 'a', 'b', x)
            one_pass(remaining_s, 'b', 'a', y)
        return res