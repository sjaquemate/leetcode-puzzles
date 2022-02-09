"""

55. CLOSED Product of Array Except Self - LeetCode

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in `O(n)` time and without using the division operation.

Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]


Constraints:

- `2 <= nums.length <= 10``5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in `O(1)` extra space complexity? (The output array does not count as extra space for space complexity analysis.)

prod_cumsum = n1 * n2 * n3 * n4= 10, n2 * n3 * n4, n1 * n3 * n4, n1 * n2 * n4, n1 * n2 * n3,
n1 n2 (n3 + n4) n5 n6
all contain n3*n4, except last two: all contain num[i] * num[i+1], except i and i+1, we can also do first the half i<center_index//2

output= [1, 1, 1, 1… , 1]
output[:center] *= nums[n-1]*nums[n-2]*…*nums[center]  O(N/2)
output[center:] *= nums[0] * nums[center-1]   O(N/2)
output[…
However, this solution is O(NlogN), but O(1) in space
def multiply(index=0):



HINT SOLUTION:
create  left_prod_cumsum and right_prod_cumsum, then product without itself is just left_prod_cumsum[i] * right_prod_cumsum[i], reasoning:
answer[i] = nums[:i] * nums[i+1:], anyways, this costs O(N) of space. Now to do away with the space complexity and go to O(1), we can use a prev_product, ie.g:

output = [1]*len(nums)

[1, 2, 3, 4]
[1, 1, 2, 6]
[24, 12, 8, 6]
product = 1
for i, num in enumerate(nums):

    output[i] *= product
    product *= num

product = 1
for i, num for reversed(list(enumerate(nums))): # from len(nums) -1 to 0

    output[i] *= product
    product *= num
"""