"""

20. CLOSED Climbing Stairs - LeetCode

You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step


Constraints:

- `1 <= n <= 45`

SOLUTION ATTEMPT: mathematically — x1 + 2y = n, we can see this as the same problem. So the upper bound is n nCr n/2… but whatever.
With the same level of recursion we can calculate this:

n = 42

def step(total=0, num_paths=0):  # we can also save the exact paths if we use an intermediate list

    if total > n:
        return num_paths

    if total == n:
        return num_paths + 1

    num_paths = step(total+1, num_paths)
    num_paths = step(total+2, num_paths)

Can we calculate this mathematically? More effiently: we can calculate x * 1 + y * 2 = n, we can check x in a for loop, and check if y is divisible by 2, like so:

n = 42
num_paths = 0
for x in range(0, n):

    remaining = n - x
    if remaining % 2:
        num_paths += 1,

However, the other code is more flexible because this O(N) code cannot handle multiple stepsizes

"""