class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [set() for _ in range(9)], [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == ".":
                    continue
                if ele in rows[i] or ele in cols[j] or ele in boxes[i//3][j//3]:
                    return False
                else:
                    rows[i].add(ele)
                    cols[j].add(ele)
                    boxes[i//3][j//3].add(ele)

        return True