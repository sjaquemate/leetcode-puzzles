"""


50. CLOSED Contains Duplicate - LeetCode

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

Example 1:

    Input: nums = [1,2,3,1]
    Output: true

Example 2:

    Input: nums = [1,2,3,4]
    Output: false

Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

SOLUTION ATTEMPT
Just use a set:

def contains_duplicates(nums):

    return len(list(set(nums)) == len(nums)

or more explicitly:
def contains_duplicates(nums):

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
"""