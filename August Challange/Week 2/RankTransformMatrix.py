# https://leetcode.com/problems/rank-transform-of-a-matrix/
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        self.parent.setdefault(u, u)
        self.parent.setdefault(v, v)
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        self.parent[pu] = pv

    def getGroups(self):
        groups = defaultdict(list)
        for i in self.parent.keys():
            groups[self.find(i)].append(i)
        return groups


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        d = defaultdict(list)

        for r in range(m):
            for c in range(n):
                d[matrix[r][c]].append([r, c])

        # rank[i] is the largest rank of the row or column so far.
        rank = [0] * (m + n)
        for a in sorted(d):
            uf = UnionFind()

            for r, c in d[a]:
                # Union row `r` with column `c` (column +m to separate with r)
                uf.union(r, c + m)

            for group in uf.getGroups().values():
                maxRank = max(rank[i] for i in group)
                for i in group:
                    rank[i] = maxRank + 1
            for r, c in d[a]:
                matrix[r][c] = rank[r]

        return matrix
