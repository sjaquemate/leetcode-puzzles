"""


51. LOSED Invert Binary Tree - LeetCode

Given the `root` of a binary tree, invert the tree, and return its root.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:

    Input: root = []
    Output: []

SOLUTION ATTEMPT:
set all left to rights and vice versa for each recursive step

def invert_btree(root):

    if root is None
        return


    left_tmp = root.left
    root.left = root.right
    root.right = left_tmp


    invert_btree(root.left)
    invert_btree(root.right)

O(N)
"""