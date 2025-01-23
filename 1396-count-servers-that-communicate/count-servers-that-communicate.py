class Solution:
    def countServers(self, grid):
        m,n=len(grid),len(grid[0])
        rows,cols=[0]*m,[0]*n
        arr=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rows[i]+=1
                    cols[j]+=1
                    arr.append([i,j])
        cnt=0
        for i,j in arr:
            if rows[i]>1 or cols[j]>1:
                cnt+=1
        return cnt