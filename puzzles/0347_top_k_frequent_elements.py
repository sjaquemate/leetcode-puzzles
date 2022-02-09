"""

68. CLOSED (1) Top K Frequent Elements - LeetCode

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:

    Input: nums = [1], k = 1
    Output: [1]


Constraints:

- `1 <= nums.length <= 10``5`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

SOLUTION ATTEMPT

let’s use the array itself and a queue?



let's use a dictionary:

counts  = {int =0}
for num in nums:

    counts[num] += 1

# numbers = {v: k for k,v in counts.items()}  # beware, can contain clashes!

counts_arr = counts.values() # or make this named tuples with

Now keep a heap of length k, insertion now is log k, So this would be worst case Nlogk
"""