# https://leetcode.com/problems/rectangle-area-ii/
from typing import List, Tuple


class Solution:
    def getHeight(self, yPairs: List[Tuple[int, int]]) -> int:
        height = 0
        prevBottom = 0
        for y1, y2 in yPairs:
            bottom = max(y1, prevBottom)
            if y2 > bottom:
                height += y2 - bottom
                prevBottom = y2
        return height

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 's'))
            events.append((x2, y1, y2, 'e'))

        events.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        prevX = 0
        yPairs = []

        for currX, y1, y2, type in events:
            if currX > prevX:
                width = currX - prevX
                ans += width * self.getHeight(yPairs)
            if type == 's':
                yPairs.append((y1, y2))
                yPairs.sort()
            else:  # type == 'e'
                yPairs.remove((y1, y2))
            prevX = currX

        return ans % (10**9 + 7)
