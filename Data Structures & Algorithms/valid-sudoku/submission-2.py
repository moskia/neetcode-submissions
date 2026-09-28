class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])

        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for k in range(0, 3):
                    for l in range(0, 3):
                        print(k, l, i)
                        if board[k+i][l+j] in seen:
                            return False
                        if board[k+i][l+j] != ".":
                            seen.add(board[k+i][l+j])

        return True