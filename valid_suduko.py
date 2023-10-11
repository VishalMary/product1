'''Valid suduko-leetcode(36)'''
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        col=collections.defaultdict(set)
        boxes=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in rows[i] or board[i][j] in col[j] or board[i][j] in boxes[(i//3,j//3)]:
                        return False
                    rows[i].add(board[i][j])
                    col[j].add(board[i][j])
                    boxes[(i//3,j//3)].add(board[i][j])
        return True
