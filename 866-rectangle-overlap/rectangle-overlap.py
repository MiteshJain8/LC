class Solution:
    def isRectangleOverlap(self, rect1: List[int], rect2: List[int]) -> bool:
        # bottom left of r2 above r1
        if rect2[0] >= rect1[2] or rect2[1] >= rect1[3]:
            return False
        # top right of r2 below r1
        if rect2[2] <= rect1[0] or rect2[3] <= rect1[1]:
            return False
        return True