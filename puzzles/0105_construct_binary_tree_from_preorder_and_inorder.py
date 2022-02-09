"""


29. CLOSED Construct Binary Tree from Preorder and Inorder Traversal - LeetCode

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

Example 2:

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]


Constraints:

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of the tree.
- `inorder` is guaranteed to be the inorder traversal of the tree.

SOLUTION ATTEMPT:
Note that preorder # root left right gives us the root immediately, inorder # left root right, gives us the most left node and most right node immediately. Preorder gives us no sense of horizontal direction, whereas inorder gives us no sense of vertical directions.

1st ASSUMPTION: all subtrees are fully filled….

In both cases, the last node is the lowest rightmost node. We could start from there… and construct the first subtree from inorder: […., left, root, right], we then pop this from the inorder subtree. We also pop the three last of preorder. BETTER YET: pop only the children of that subtree (left, right), then the inorer and preorder subtrees are nicely intact.

example:

def construct_bt(preorder, inorder, prev_parent=None):


    if len(preorder) == 1:
        pass


    left = Node(preorder[-2])
    right = Node(preorder[-1]) if prev_parent is None else prev_parent
    parent = Node(preorder[-3], left=left, right=right)


    preorder.pop([-1, -2])
    inorder.pop([-1, -3]


    construct(preorder, inorder, prev_parent=parent)
"""