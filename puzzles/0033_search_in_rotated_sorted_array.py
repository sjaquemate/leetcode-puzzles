"""

10. CLOSED Search in Rotated Sorted Array - LeetCode

There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.
Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.
You must write an algorithm with `O(log n)` runtime complexity.

Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

SOLUTION ATTEMPT:
An O(N) solution would be trivial, note nums has distinct integers. Now, we are required to find a logN solution, likely involving a binary search. However, in this binary search we are unsure where the pivot has taken place. However, it must have taken place somewhere. In that case we now that sublist[0] > sublist[-1] instead of the other way around. Interesting in any case is an logN algorithm to find the single pivot:

Tested solution in python:

    def do_pivot(nums, k):
        return nums[k:] + nums[:k]

    def find_pivot(nums, left=None, right=None):
        if left is None:
            left = 0
        if right is None:
            right = len(nums)-1

        length = right - left + 1
        print(f'{left = } {right = } {length = }')

        if length == 2:  # base case
            return len(nums) - right

        center = left + length//2
        left_contains_pivot = nums[left] > nums[center]
        right_contains_pivot = nums[center] > nums[right]

        if left_contains_pivot:  # branching
            return find_pivot(nums, left, center)
        elif right_contains_pivot:
            return find_pivot(nums, center, right)
        else:
            return -1
            # raise AssertionError(f"pivot should be between {left+1} and {right}") # contains no pivot


    def main():
        nums = list(range(10))
        nums_pivoted = do_pivot(nums, 5)
        print(f'{nums = }')
        print(f'{nums_pivoted = }')
        pivot = find_pivot(nums_pivoted)  # log N
        print(f'pivot found at {pivot = }')


        nums_multi_pivoted = (do_pivot(do_pivot(nums, 5), 3))
        print(f'{nums_multi_pivoted = }')
        sum_pivots_mod_length = find_pivot(nums_multi_pivoted)  # log N
        print(f'{sum_pivots_mod_length = }')

        # thus the effective pivot after a different rotations is
        # p1 + p2 + p3 + ... mod len(nums) !!!
"""