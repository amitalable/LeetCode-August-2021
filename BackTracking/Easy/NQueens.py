class Solution:
    def __init__(self) -> None:
        self.final_list = []

    def NQueens(self, arr, r, n):
        if r == n:
            x = [[arr[i][j] for i in range(n)] for j in range(n)]
            self.final_list.append(x)
            return

        for i in range(n):
            if self.isSafe(arr, r, i, n):
                arr[r][i] = 'Q'
                self.NQueens(arr, r+1, n)
                arr[r][i] = '-'

    def isSafe(self, arr, r, c, n):
        for i in range(r):
            # upper
            if arr[i][c] == 'Q':
                return False

        (i, j) = (r, c)
        while i >= 0 and j >= 0:
            # upper left diagonal
            if arr[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        (i, j) = (r, c)
        while i >= 0 and j < n:
            # upper right diagonal
            if arr[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True


x = 4
arr = [['-' for i in range(x)] for i in range(x)]
obj = Solution()
obj.NQueens(arr, 0, x)
for i in obj.final_list:
    print(i)
