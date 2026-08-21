class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            num_counter = [0] * 10
            for col in range(9):
                if board[row][col] != ".":
                    if num_counter[int(board[row][col])] == 1:
                        return False
                    num_counter[int(board[row][col])] += 1

        for col in range(9):
            num_counter = [0] * 10
            for row in range(9):
                if board[row][col] != ".":
                    if num_counter[int(board[row][col])] == 1:
                        return False
                    num_counter[int(board[row][col])] += 1

        for i in range(3):
            for j in range(3):
                num_counter = [0] * 10
                for row in range(3):
                    for col in range(3):
                        if board[3 * i + row][3 * j + col] != ".": 
                            if num_counter[int(board[3 * i + row][3 * j + col])] == 1:
                                return False
                            num_counter[int(board[3 * i + row][3 * j + col])] += 1

        return True

