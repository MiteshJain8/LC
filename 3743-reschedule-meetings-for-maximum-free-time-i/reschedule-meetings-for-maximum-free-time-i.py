class Solution:
    def maxFreeTime(self, eventTime: int, k: int, start: List[int], end: List[int]) -> int:
        start=start+[eventTime]
        end=[0]+end
        n=len(start)
        gaps=[0]*n

        for i in range(n):
            gaps[i]=start[i]-end[i]
    
        left=curr=maxGap=0
        for right in range(n):
            curr+=gaps[right]
            if right-left+1>k+1:
                curr-=gaps[left]
                left+=1
            maxGap=max(maxGap,curr)

        return maxGap