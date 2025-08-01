class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]for _ in range(numRows)]
        
        if numRows > 1:
            res[1] = [1,1]
            
        for i in range(2, numRows):
            prev = res[i-1]
            for j in range(1, len(prev)):
                res[i].append(prev[j-1] + prev[j])
            res[i].append(1)

        return res