class NQueen:
    def __init__(self, N):
        self.board = [[0 for i in range(N)] for j in range(N)]
        self.n = N
        self.res = []

    def solve(self, r):
        if r == self.n:
            self.res.append([[self.board[i][j]
                              for i in range(self.n)] for j in range(self.n)])
            return
        for i in range(self.n):
            if self.isValid(r, i):
                self.board[r][i] = 1
                self.solve(r+1)
                self.board[r][i] = 0

    def isValid(self, row, col):
        if self.board[row][col]:
            return False

        for i in range(row):
            if self.board[i][col]:
                return False
        (i, j) = (row, col)
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1
        (i, j) = (row, col)
        while i >= 0 and j < self.n:
            if self.board[i][j]:
                return False
            i -= 1
            j += 1
        return True


N = 4
obj = NQueen(N)
obj.solve(0)
print(obj.res)
