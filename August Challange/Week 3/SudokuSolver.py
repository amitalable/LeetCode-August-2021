# https://leetcode.com/problems/sudoku-solver
from collections import defaultdict
from itertools import product


class Solution:
    def solveSudoku(self, board):
        def dfs(board, empty, rows, cols, boxes):
            if not empty:
                return True
            r, c = empty[-1]
            for k in set("123456789") - (rows[r] | cols[c] | boxes[3*(r//3)+c//3]):
                board[r][c] = k
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.add(k)
                if dfs(board, empty[:-1], rows, cols, boxes):
                    return True
                board[r][c] = '.'
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.remove(k)

            return False

        cols, rows, boxes, empty = defaultdict(
            set), defaultdict(set), defaultdict(set), []
        for r, c in product(range(9), range(9)):
            if board[r][c] == ".":
                empty.append((r, c))
            else:
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.add(board[r][c])

        dfs(board, empty, rows, cols, boxes)
