"""

https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

So return all where the sum == 0. And not contain duplicate triplets! (in other order).
SLOW 3 for loops in (N ncr 3) style.
FAST some sort of sorting algorithm first, then binary search but smarter… In 2sum we could use the fact that we knew what we were looking for: TOTAL=0, so looking for TOTAL-num…, now we are looking for TOTAL-num1 = num2+num3… This doesnt help us. Unless you are happy with a O(N^2logN) solution.
We can probably do better… lets look at an example

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]




HINT:  start two index variables from two corners of the array and move them toward eachother to find the rest of the sum: i.e: use the two-finger method at opposite sides of the sorted array

SOLUTION ATTEMPT WITH HINT:

def find_3sums(nums):


    nums = sorted(nums)
    triplets = []
    for i in range(len(nums)-2):  # except the last two elements
        j = i+1  # first finger at start
        k = len(nums)-1  # second finger at end
        while j < k:
            three_elems = [nums[i], nums[j], nums[k]]
            total = sum(three_elems)
            if total == 0:
                triplets += three_elems
            elif total > 0: # move right finger to the left
                k -= 1
            else:  # move left finger to the right
                j += 1
"""