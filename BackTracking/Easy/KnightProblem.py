class Solution:
    def __init__(self, n) -> None:
        self.row = [2, 1, -1, -2, -2, -1, 1, 2]
        self.col = [1, 2, 2, 1, -1, -2, -2, -1]
        self.n = n
        self.final_list = []

    def isMoveValid(self, r, c):
        return not (r < 0 or c < 0 or r >= self.n or c >= self.n)

    def KnightTour(self, visited, r, c, pos):
        visited[r][c] = pos

        if pos >= self.n*self.n:
            self.final_list.append(
                [[visited[j][i] for i in range(self.n)] for j in range(self.n)])
            visited[r][c] = 0
            return

        for k in range(8):
            new_row = r + self.row[k]
            new_col = c + self.col[k]
            if self.isMoveValid(new_row, new_col) and visited[new_row][new_col] == 0:
                self.KnightTour(visited, new_row, new_col, pos+1)
        visited[r][c] = 0


x = 5
arr = [[0 for i in range(x)] for j in range(x)]
obj = Solution(x)
obj.KnightTour(arr, 0, 0, 1)
print(obj.final_list[0])
