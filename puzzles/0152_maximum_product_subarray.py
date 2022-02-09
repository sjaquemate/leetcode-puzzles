"""

38. CLOSED Maximum Product Subarray - LeetCode

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:

    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:

    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

- `1 <= nums.length <= 2 * 10``4`
- `-10 <= nums[i] <= 10`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

[2, 3, -2, 4]
cur_sum = 0
max_sum = float(“-inf”)
for i, num for enumerate(nums):

    cur_sum = max(cur_sum + num, num)
    max_sum = max(max_sum, cur_sum)

This works fine… what if we multiply:

[2, 3, -2, 4]
[2|2, 6|6, -2|6, -8|6]
[-2, 0, -1]
[-2|-2, 0|0, 0|0]
THIS SEEMS TO WORK:
cur_product = 1
max_product = float(“-inf”)
for i, num in enumerate(nums):

    cur_prod = max(cur_prod * num, num)
    max_prod = max(max_prod, cur_prod)

"""