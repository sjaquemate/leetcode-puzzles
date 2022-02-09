"""


54. CLOSED Lowest Common Ancestor of a Binary Tree - LeetCode

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”

Example 1:

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

    Input: root = [1,2], p = 1, q = 2
    Output: 1


Constraints:

- The number of nodes in the tree is in the range `[2, 10``5``]`.
- `-10``9` `<= Node.val <= 10``9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the tree.

SOLUTION ATTEMPT
First we need to find where p and q are themselves, this is O(N), storing the ancestors is then O(logN) in space. But what if we want O(1) in space?

p_found = False
q_found = False
p_found_twice = False
q_found_twice = False
lca = None
def lca(node):

    if node is None or (p_found and q_found): # no need for further recursion
        return

    if node == p:
        p_found = True
    if node == q:
        q_found = True


    lca(node.left)
    lca(node.right)


    # you get here first if p and q are found for the first time
    if p_found_twice and q_found_twice:
        lca = node
        return

    if node == p:
        p_found_twice = True
    if node == q:
        q_found_twice = True


This code is ugly, and should be rewriten somehow… probably by returning somehing, i think or how about returning and passing p_anc=None, q_anc = None, if p_anc is not None and  q_anc is not None…
"""