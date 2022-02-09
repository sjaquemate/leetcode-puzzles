"""

74. CLOSED (1) Subtree of Another Tree - LeetCode

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.
A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

Example 1:

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

Example 2:

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false


Constraints:

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10``4` `<= root.val <= 10``4`
- `-10``4` `<= subRoot.val <= 10``4`

Just recurse downwards:

is_subtree = True
def traverse(main_node, sub_node, in_subtree=False):


    if in_subtree:
        is_subtree *= main_node.val==sub_node.val:

    if not in_subtree and node is None:
        return
    ..etc.


    travserse(node.left, in_subtree, sub_node.left if in_subtree)
    traverse(node.right, in_subtree, sub_node.right)

Otherwise we can just find the root of the subtree in the maintree and do is_same_tree(node, node)
"""