class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_heap = []
        for idx,rect in enumerate(dimensions):
            heappush(max_heap, (-(rect[0] ** 2 + rect[1] ** 2), idx))
            max_diag = max_heap[0][0]
            max_area = 0
        while max_heap:
            ele_daig, ele_idx = heappop(max_heap)
            if ele_daig == max_diag:
                max_area = max(max_area, dimensions[ele_idx][0] * dimensions[ele_idx][1])
            else:
                break
        return max_area
