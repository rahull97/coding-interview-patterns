from typing import List


def largest_container(heights: List[int]) -> int:
    max_water = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, area)
        if heights[left] < heights[right]:
            left = left + 1
        elif heights[left] > heights[right]:
            right = right - 1
        else:
            left = left + 1
            right = right -1
    return max_water
