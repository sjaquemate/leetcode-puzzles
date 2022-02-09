"""

19. CLOSED Unique Paths - LeetCode

There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.
Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to `2 * 10``9`.

Example 1:

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

    Input: m = 3, n = 7
    Output: 28

Example 2:

    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

Answer: O(1) there are a total of (m-1)+(n-1) moves to be made, of that, (n-1) are to the right. So the number of unique paths = (n+m-2) nCr (n-1) ( this is the same as (n+m-2) nCr (m-1)

Programmatically: we can write this using recursion & backtracking:

num_paths = 0



def step(pos, dx=0, dy=0):

    pos.x += dx
    pos.y += dy

    if pos == (n-1, m-1):  # base case: reach the corner
        num_paths += 1
        return

    if pos.x == m or pos.y == n:
        return

    step(pos, dx=1)
    pos.x -= 1
    step(pos, dy=1)
    return

TESTED IN PYTHON:


    def step(x=0, y=0, num_paths=0):

        if x == m-1 and y == n-1:
            return num_paths + 1

        if x == m or y == n:
            return num_paths

        num_paths = step(x+1, y, num_paths)
        num_paths = step(x, y+1, num_paths)
        return num_paths

    m = 7
    n = 3
    print(step())

O(N+M ncr N)
"""