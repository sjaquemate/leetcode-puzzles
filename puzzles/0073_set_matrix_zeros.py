"""

 OPEN Set Matrix Zeroes - LeetCode
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s, and return the matrix.
You must do it in place.

Example 1:

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2``31` `<= matrix[i][j] <= 2``31` `- 1`


Follow up:

- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space solution?

SOLUTION ATTEMPT
matrix[i, j] of size nxm
NAIVE SOLUTION: loop over matrix,

    when we encounter a 0 at (i, j), set all matrix[i, :] = 0 # row zero, matrix[:, j] = 0 # column zero
    OR: to-be zeros, to_be_zeros = [(i, j), (i+1, j)] etc.

This would be a O(NM) space solution.

We can just save all the elements in a list or dictionary that are columns & rows that are to be zerod: this would be a O(M + N) space solution.
Can we do a constant space solution?

Constant space solution is probably iterating over the matrix in a start way, as to hit first only the columns, or certain row, column combinations . Or set them to NULL and at the end set all to .

If you find a zero in a row, the whole row has to be set to zero, and we can continue to the next row
"""