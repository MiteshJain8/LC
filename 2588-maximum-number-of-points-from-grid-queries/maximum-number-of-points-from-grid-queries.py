class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_heap = []
        for i, query in enumerate(queries):
            heappush(query_heap, (query, i))
        
        grid_heap = [(grid[0][0], 0, 0)] 
        answer = [0] * len(queries)
        points = 0
        directions = [(-1, 0), (1, 0), (0,1), (0,-1)]
        for i in range(len(queries)):
            query_val, index = heappop(query_heap)

            while grid_heap and grid_heap[0][0] < query_val:
                grid_val, row, col = heappop(grid_heap)

                if not grid[row][col]:
                    continue

                points += 1
                grid[row][col] = 0

                for dr, dc in directions:
                    next_row, next_col = row + dr, col + dc
                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col]:
                        heappush(grid_heap, (grid[next_row][next_col], next_row, next_col))
            
            answer[index] = points
        
        return answer        