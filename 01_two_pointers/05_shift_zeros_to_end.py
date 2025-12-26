from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
    left = 0
    right = 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right + 1
        elif nums[right] == 0:
            right = right + 1
