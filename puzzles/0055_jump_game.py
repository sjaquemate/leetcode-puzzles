"""
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return `true` if you can reach the last index, or `false` otherwise.

Example 1:

    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Can we reach the last index? Ordering the array will be larger than O(N), we need to check all those element in any case… I think… 0 < nums < … so jumping to right is always guaranteed
NAIVE SOLUTION

index = 0
while nums[index] != 0 and index < len(nums)-1:

    index += nums[index]

return index == len(nums)-1

Is there anything better than this? This would be worst case O(N) complexity — arrays full of ones… I think we can do no better than this…
"""