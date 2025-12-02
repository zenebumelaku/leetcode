
class Solution(object):
    def heightChecker(self, heights):
        y = 0
        x = sorted(heights)  # sorted copy of heights
        for a, b in zip(heights, x):  # compare element by element
            if a != b:
                y += 1
        return y
