"""

13. CLOSED Maximum Subarray - LeetCode

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

SOLUTION ATTEMPT:
first sort, e.g: [4, 8, -5] → [-5, 4, 8], and its argsort: [2, 0, 1] → and its sorted argsort, then look for the largest by 1 increasing, and their sum, we cannot do this with a bigger sliding window, but we can at least do it in O(N^2) time, by changing the window every time… this is worst case O(N^2). Do I think we can do better? — Yes. Because we could have done this from the start!
By one run over the sorted arguments I can find the start + end of all,
Look from highest to lowest in argsorted by steps of one, use a cur_max.
If total increases we have a fixed start........…

[-1, 2, -1, 2, -2] → calculate cumsum [-1, 1, 0, 2, 0], the sum between some numbers can then be found as: cumsum[j] - cumsum[i], j > i, so the largest sum can be found by max(cumsum) - min(cumsum), where argmax(cumsum) > argmin(cumsum). So just try to find:

imax = argmax(cumsum)
imin_b4_imax = argmin(cumsum[:argmax(cumsum)])
print(imin_b4_imax, imax)
total = cumsum(imax)-cumsum(imin)

This would be an O(N) solution:
CODED AND VERIFIED in python:


    def argmax(arr):  # must select the latest
        return max( range(len(arr)), key=lambda i: arr[i])


    def argmin(arr):
        return min( range(len(arr)), key=lambda i: arr[i])


    def running_sum(arr):
        cursum = 0
        runsum = []
        for a in arr:
            cursum += a
            runsum.append(cursum)
        return runsum

    def find_maximum_subarray(nums):
        runsum = running_sum(nums)
        print('runsum', runsum)
        imax = argmax(runsum)
        imin_b4_imax = argmin(runsum[:imax])
        print(imin_b4_imax, imax)
        return nums[imin_b4_imax+1:imax+1]

"""