class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n < 3:
            return n
        t1, t2 = fruits[0], fruits[1]
        end1, end2 = 0, 1
        k = 2
        while k < n and t1 == t2:
            t2 = fruits[k]
            end1 = k - 1
            end2 = k
            k += 1
        # print(k)
        if k == n:
            return n
        l = 0
        res = cur = k
        for r in range(k, n):
            if fruits[r] == t1:
                end1 = r
                cur += 1
            elif fruits[r] == t2:
                end2 = r
                cur += 1
            else:
                print(r, t1, t2, l)
                if fruits[l] == t1 and fruits[r-1] == t2:
                    l = end1 + 1
                    t1 = fruits[r]
                    end1 = r
                elif fruits[l] == t2 and fruits[r-1] == t1:
                    l = end2 + 1
                    t2 = fruits[r]
                    end2 = r
                else:
                    if fruits[r-1] == t1:
                        l = end2 + 1
                        t2 = fruits[r]
                        end2 = r
                    else:
                        l = end1 + 1
                        t1 = fruits[r]
                        end1 = r
                cur = r - l + 1
            print(cur)

            res = max(res, cur)

        return res
