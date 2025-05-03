from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        lst = [[set(), set(), set()] for _ in range(6)]
        
        for i in range(len(tops)):
            lst[tops[i]-1][0].add(i)
            lst[bottoms[i]-1][0].add(i)
            lst[tops[i]-1][1].add(i)
            lst[bottoms[i]-1][2].add(i)
        
        ans, curr, flag = float('inf'), float('inf'), 0
        for i in range (len(lst)):
            if len(lst[i][0]) == len(tops):
                curr = len(tops) - max(len(lst[i][1]), len(lst[i][2]))
                flag = 1
            ans = min(ans, curr)
        
        if flag == 0:
            return -1
        else:
            return ans


