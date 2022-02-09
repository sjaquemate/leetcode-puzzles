"""

77. OPEN (1) Find the Duplicate Number - LeetCode

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
There is only one repeated number in `nums`, return this repeated number.
You must solve the problem without modifying the array `nums` and uses only constant extra space.

Example 1:

    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:

    Input: nums = [3,1,3,4,2]
    Output: 3


Constraints:

- `1 <= n <= 10``5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times.


Follow up:

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?

solution attempt

we know [1, 2, 3, 4, 4,4] containing n=4 integers has a sum of (n+1)n/2=10,

know if we have any duplicate sum(nums) = (n+1)n/2 + x*duplicate
at least one duplicate number must exit in nums if sums(nums) > (n+1)n/2

So
thus known = x * duplicate, this could be 2 * 2 or 1 * 4

BUT CAN ALSO BE
[1, 2, 2, 2, 4, 5],
or [5, 5, 5, 5, 5]
"""