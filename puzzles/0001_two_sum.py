from typing import List
import numpy as np
from algorithms.search import binary_search


def two_sum(nums: List[int], target: int):
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    sorted_nums = sorted(nums)
    argsorted_nums = np.argsort(nums)

    for index, value in enumerate(sorted_nums):
        second_index = binary_search(sorted_nums[index+1:], target - value) + index+1

        if second_index != -1:
            return (argsorted_nums[index], argsorted_nums[second_index])

    return (-1, -1)


def test_two_sum():
    assert two_sum([2, 7, 11, 15], target=9) == (0, 1)
    assert two_sum([3, 2, 4], target=6) == (1, 2)
    assert two_sum([3, 3], target=6) == (0, 1)
    assert two_sum([5, 5], target=0) != (0, 1)
