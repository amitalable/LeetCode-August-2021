# https://www.techiedelight.com/find-shortest-path-in-maze/
import sys


class Solution:
    def __init__(self) -> None:
        self.row = [-1, 0, 1, 0]
        self.col = [0, -1, 0, 1]

    def isSafe(self, arr, visited, r, c):
        return visited[r][c] == 0 and arr[r][c] == 1

    def isValid(self, r, c, n):
        return n > r >= 0 and n > c >= 0

    def findShortestPathInMaze(self, arr, visited, n, i, j, x, y, min_dist, dist):
        '''
            i : Current row position
            j : Current col position
            x : Final row position
            y : Final col position

        '''
        if i == x and j == y:
            return min(dist, min_dist)

        visited[i][j] = 1
        for k in range(4):
            new_row = i+self.row[k]
            new_col = j + self.col[k]
            if self.isValid(new_row, new_col, n) and \
                    self.isSafe(arr, visited, new_row, new_col):

                min_dist = self.findShortestPathInMaze(
                    arr, visited, n, new_row, new_col, x, y, min_dist, dist+1)
        visited[i][j] = 0
        return min_dist


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

min_dist = obj.findShortestPathInMaze(
    mat, visited, 10, 0, 0, 7, 5, sys.maxsize, 0)

if min_dist != sys.maxsize:
    print("The shortest path from source to destination has length", min_dist)
else:
    print("Destination can't be reached from source")
