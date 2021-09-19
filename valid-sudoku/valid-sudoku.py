class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen={}
            for cell in row:
                if cell.isnumeric():
                    if cell in seen:
                        return False
                    else:
                        seen[cell]=True
        for r in range(len(board)):
            seen={}
            for c in range(len(board[0])):
                cell=board[c][r]
                if cell.isnumeric():
                    if cell in seen:
                        return False
                    else:
                        seen[cell]=True

        square = [dict() for _ in range(9)]

        for row in range(0,3):
            for col in range(0,3):
                #check each board
                """
                square 1 add nothing
                square 2 add 3 to row
                square 3 add 6 to row
                square 4 add 3 to col
                square 5 add 3 to col & 3 to row
                """
                cell=board[row][col]
                if cell.isnumeric():
                    if cell in square[0]:
                        return False
                    else:
                        square[0][cell]=True

                cell=board[row+3][col]
                if cell.isnumeric():
                    if cell in square[1]:
                        return False
                    else:
                        square[1][cell]=True

                cell=board[row+6][col]
                if cell.isnumeric():
                    if cell in square[2]:
                        return False
                    else:
                        square[2][cell]=True

                cell=board[row][col+3]
                if cell.isnumeric():
                    if cell in square[3]:
                        return False
                    else:
                        square[3][cell]=True


                cell=board[row+3][col+3]
                if cell.isnumeric():
                    if cell in square[4]:
                        return False
                    else:
                        square[4][cell]=True

                cell=board[row+6][col+3]
                if cell.isnumeric():
                    if cell in square[5]:
                        return False
                    else:
                        square[5][cell]=True

                cell=board[row+0][col+6]
                if cell.isnumeric():
                    if cell in square[6]:
                        return False
                    else:
                        square[6][cell]=True

                        
                cell=board[row+3][col+6]
                if cell.isnumeric():
                    if cell in square[7]:
                        return False
                    else:
                        square[7][cell]=True

                cell=board[row+6][col+6]
                if cell.isnumeric():
                    if cell in square[8]:
                        return False
                    else:
                        square[8][cell]=True

        return True