# https://leetcode.com/problems/remove-boxes

from collections import namedtuple
from functools import cache
from itertools import groupby
from typing import List

BoxRun = namedtuple("BoxRun", ("color", "count"))


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def best_score(boxes, same_as_first_around):
            color = boxes[0].color
            # Try to grab all same colored boxes from both sides
            if len(boxes) > 1 and boxes[-1].color == color:
                same_as_first_around += boxes[0].count + boxes[-1].count
                boxes = boxes[1:-1]
            else:
                # Or at least from the left
                same_as_first_around += boxes[0].count
                boxes = boxes[1:]
            score = same_as_first_around ** 2
            if boxes:  # Oh there are more boxes left, have to focus on them first
                # Start assuming there are no same-color boxes left
                score += best_score(boxes, 0)
                # Then verify by looking for the same colored boxes
                # Sure first and last groups of the rest are different color
                for mid in range(1, len(boxes) - 1):
                    if boxes[mid].color == color:
                        # Check if removing boxes to the left first improves the score
                        score_for_removed = best_score(boxes[:mid], 0)
                        score_for_joined = best_score(
                            boxes[mid:], same_as_first_around)
                        score = max(score, score_for_removed +
                                    score_for_joined)
            return score

        box_runs = tuple(BoxRun(color, len(list(run)))
                         for color, run in groupby(boxes))
        return best_score(box_runs, 0)
