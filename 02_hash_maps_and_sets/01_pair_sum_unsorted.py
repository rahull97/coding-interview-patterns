from typing import List


def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for idx, el in enumerate(nums):
        complement = target - el
        if complement in hash_map:
            return [hash_map[complement], idx]
        else:
            hash_map[el] = idx
    return []
