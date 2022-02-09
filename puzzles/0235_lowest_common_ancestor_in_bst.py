"""

53. CLOSED Lowest Common Ancestor of a Binary Search Tree - LeetCode

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”

Example 1:

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

    Input: root = [2,1], p = 2, q = 1
    Output: 2


Constraints:

- The number of nodes in the tree is in the range `[2, 10``5``]`.
- `-10``9` `<= Node.val <= 10``9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the BST.

if we first find p and set lowest common ancestor to the root, We can put all ancestors in a dcitionary and then cross check them for the LCA, this would be O(logN) space however. We should be able to do this in O(logN) time and O(1) space… I see this as a challange, we return True only if we found p or q attach a FOUND SOLUTION EASILY BY CHILLINGAND TAKING MY MIND OF THE PROBLEM FOR A BIT. You want to find the values at the same time until the ancestor is not the same anymore

p, q
def lca(root):

    if p < root and q < root:
        return lca(root.left)
    elif p > root and q > root:
        return lca(root.right)
    else:  # also works if one of them is equal to!
        return root  # base case this was the least common ancenstor
"""