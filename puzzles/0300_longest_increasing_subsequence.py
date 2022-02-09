"""
OPEN (1) Longest Increasing Subsequence - LeetCode

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.

Example 1:

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:

    Input: nums = [7,7,7,7,7,7,7]
    Output: 1


Constraints:

- `1 <= nums.length <= 2500`
- `-10``4` `<= nums[i] <= 10``4`


Follow up: Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

SOLUTION ATTEMPT

(N^2) solution is super straightforward and also not interesting


    [0,1,0,3,2,3]


You are looking for the

I have thought of a sort of list of lists:…
Make a new list if none of these smaller than current, else append to all of those list to which it is bigger:

SubSequenceCount:

    count: int = 0
    last_num = last_num


subsequences = []  # or faster dict with start_index, count and last_num

for num in nums:

    fits_in_sub = False
    for subsequence in subsequences:
        if subsequence.last_num < num:
            fits_in_sub = True
            subsequence.count += 1
            subsequence.last_num = num
    if not fits_in_sub:
        subsequences.append(SubSequenceCount(last_num=num)

return max(sub.last_num for sub in subseqeuences)

This is  worst case O(N) in space and (1+2+3+.. N=N^2) time complexity
Worst case: [10, 9, 8, 7, 6] OR [7,7,7,7,7]. so this is not faster at all..


    [0, 1, 6, 2, 4]
    [0, 1, 2, 4, 6]
    [0, 1, 2, 2, 4]
    If numbers are next to eacother in sorted and...
    We are essentially looking for the longest increasing subarray in argsorted! Example


    [10,9,2,5,3,7,101,18]
    [2,3,5,7,9,10,18,101] sorted
    [2,4,3,5,1,0,7,6]  argsorted

    ....
"""