class Solution:
    def maxTotalFruits(self,fruits, startPos, k):
        n=len(fruits)
        left=0
        total=0
        ans=0

        for right in range(n):
            total+=fruits[right][1]
            while left<=right:
                l=fruits[left][0]
                r=fruits[right][0]
                dist=min(abs(startPos-l)+(r-l), abs(startPos-r)+(r-l))
                if dist>k:
                    total-=fruits[left][1]
                    left+=1
                else:
                    break

            ans=max(ans, total)

        return ans