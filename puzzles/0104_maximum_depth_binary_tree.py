"""


28. CLOSED Maximum Depth of Binary Tree - LeetCode

Given the `root` of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:

    Input: root = [1,null,2]
    Output: 2

SOLUTION ATTEMPT:

find_max_depth(root, depth = 0, max_depth = 0):

    if root is None:
        return


    max_depth = max(max_depth, depth)

    find_max_depth(root.left, depth + 1, max_depth)
    find_max_depth(root.right, depth + 1, max_depth)


    return max_depth
"""