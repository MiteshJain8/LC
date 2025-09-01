class Solution:
    def maxAverageRatio(self, c: List[List[int]], e: int) -> float:
        heap = []
        i = 0
        for p,t in c:
            heappush(heap, (-((p+1)/(t+1) - p/t), i))
            i += 1
        for _ in range(e):
            a, i = heappop(heap)
            c[i][0] += 1
            c[i][1] += 1
            heappush(heap, (-((c[i][0]+1)/(c[i][1]+1) - (c[i][0])/(c[i][1])), i))
        Sum = 0
        for p,t in c:
            Sum += p/t
        return Sum/len(c)