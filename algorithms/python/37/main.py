from collections import deque
import sys

sys.setrecursionlimit(int(1e6))


class Solution:
    def __init__(self):
        self.blanks = []
        self.blanks_len = 0
        self.board = []
        self.blank_info = defaultdict(set)

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    self.blanks.append((i, j))

        self.blanks_len = len(self.blanks)
        if not self.blanks_len:
            return
        self.solve(0)

    def solve(self, idx):
        if idx == self.blanks_len:
            (row_res, row_set), (col_res, col_set) = self.line_valid(*(self.blanks[idx - 1]))
            (box_res, box_set) = self.box_valid(*(self.blanks[idx - 1]))
            if row_res and col_res and box_res:
                print(self.board)
                return True
        (row_res, row_set), (col_res, col_set) = self.line_valid(*(self.blanks[idx]))
        (box_res, box_set) = self.box_valid(*(self.blanks[idx]))
        if row_res and col_res and box_res:
            selection = list(row_set & col_set & box_set)
            y, x = self.blanks[idx]
            for sel in selection:
                self.board[y][x] = str(sel)
                if self.solve(idx + 1):
                    return True
            self.board[y][x] = "."
        else:
            return False

    def line_valid(self, i=None, j=None):
        row_set, col_set = set(range(1, 10)), set(range(1, 10))
        row_res, col_res = True, True
        for k in range(9):
            if i is not None and self.board[i][k].isalnum():
                if int(self.board[i][k]) in row_set:
                    row_set.remove(int(self.board[i][k]))
                else:
                    row_res = False
            if j is not None and self.board[k][j].isalnum():
                if int(self.board[k][j]) in col_set:
                    col_set.remove(int(self.board[k][j]))
                else:
                    col_res = False
        return (row_res, row_set), (col_res, col_set)

    def box_valid(self, i, j):
        i, j = i - i % 3, j - j % 3
        contain = set(range(1, 10))
        res = True
        for y in range(i, i + 3):
            for x in range(j, j + 3):
                if self.board[y][x].isalnum():
                    if int(self.board[y][x]) in contain:
                        contain.remove(int(self.board[y][x]))
                    else:
                        res = False
        return (res, contain)