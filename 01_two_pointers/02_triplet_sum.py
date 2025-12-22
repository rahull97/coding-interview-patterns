from typing import List


def pair_sum_sorted(nums: List[int], left: int, right: int, target: int) -> List[List[int]]:
    ans = []
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            ans.append([nums[left], nums[right]])
            left = left + 1
            while left < right and nums[left] == nums[left - 1]:
                left = left + 1
        elif total < target:
            left = left + 1
        elif total > target:
            right = right - 1
    return ans


def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    right = len(nums) - 1
    ans = set()
    for idx, el in enumerate(nums):
        if nums[idx] > 0:
            break
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue
        else:
            sum_pair = pair_sum_sorted(nums, idx + 1, right, -el)
            for pair in sum_pair:
                pair.append(el)
                ans.add(tuple(sorted(pair)))
    triplet = []
    for item in ans:
        triplet.append(list(item))
    return triplet


if __name__ == "__main__":
    print(triplet_sum([]))
    print(triplet_sum([0]))
    print(triplet_sum([1, -1]))
    print(triplet_sum([0, 0, 0]))
    print(triplet_sum([1, 0, 1]))
    print(triplet_sum([0, 0, 1, -1, 1, -1]))
