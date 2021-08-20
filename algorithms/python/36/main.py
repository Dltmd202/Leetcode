from collections import defaultdict


class Solution:
    def __init(self):
        self.board = []
        self.res = True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if not self.is_tri_valid(i, j):
                    return False
        for i in range(0, 9):
            if not self.is_vertical_valid(i) or \
                    not self.is_horizontal_valid(i):
                return False
        return True

    def is_tri_valid(self, y, x):
        consist = defaultdict(bool)
        print(y, x)
        for i in range(y, y + 3):
            for j in range(x, x + 3):
                print(consist)
                print(self.board[i][j])
                if self.board[i][j].isalnum() and \
                        not consist[self.board[i][j]]:
                    consist[self.board[i][j]] = True
                elif self.board[i][j].isalnum():
                    return False
        return True

    def is_vertical_valid(self, i):
        consist = defaultdict(bool)
        for j in range(9):
            print(consist)
            if self.board[i][j].isalnum() and \
                    not consist[self.board[i][j]]:
                consist[self.board[i][j]] = True
            elif self.board[i][j].isalnum():
                return False
        return True

    def is_horizontal_valid(self, j):
        consist = defaultdict(bool)
        for i in range(9):
            print(consist)
            if self.board[i][j].isalnum() and \
                    not consist[self.board[i][j]]:
                consist[self.board[i][j]] = True
            elif self.board[i][j].isalnum():
                return False
        return True