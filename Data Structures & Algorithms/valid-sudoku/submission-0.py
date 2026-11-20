class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)

        rows = len(board)
        cols = len(board[0])

        rSet = defaultdict(set)
        cSet = defaultdict(set)
        rcSet = defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rSet[r] or board[r][c] in cSet[c] or board[r][c] in rcSet[r//3,c//3]:
                    return False
                rSet[r].add(board[r][c])
                cSet[c].add(board[r][c])
                rcSet[r//3, c//3].add(board[r][c])
        return True
        