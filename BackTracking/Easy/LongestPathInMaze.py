# https://www.techiedelight.com/find-longest-possible-route-matrix/

class Solution:
    def __init__(self) -> None:
        self.row = [-1, 0, 1, 0]
        self.col = [0, -1, 0, 1]

    def isSafe(self, arr, visited, r, c):
        return visited[r][c] == 0 and arr[r][c] == 1

    def isValid(self, r, c, n):
        return n > r >= 0 and n > c >= 0

    def findLongestPathInMaze(self, arr, visited, n, i, j, x, y, max_dist, dist):
        '''
            i : Current row position
            j : Current col position
            x : Final row position
            y : Final col position

        '''
        if i == x and j == y:
            return max(dist, max_dist)

        visited[i][j] = 1
        for k in range(4):
            new_row = i+self.row[k]
            new_col = j + self.col[k]
            if self.isValid(new_row, new_col, n) and \
                    self.isSafe(arr, visited, new_row, new_col):

                max_dist = self.findLongestPathInMaze(
                    arr, visited, n, new_row, new_col, x, y, max_dist, dist+1)
        visited[i][j] = 0
        return max_dist


obj = Solution()
mat = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

M = N = 10

# construct a matrix to keep track of visited cells
visited = [[0 for x in range(N)] for y in range(M)]

max_dist = obj.findLongestPathInMaze(
    mat, visited, 10, 0, 0, 7, 5, 0, 0)

if max_dist != 0:
    print("The longest path from source to destination has length", max_dist)
else:
    print("Destination can't be reached from source")
