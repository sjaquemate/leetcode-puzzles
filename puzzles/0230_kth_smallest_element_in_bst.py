"""

52. OPEN Kth Smallest Element in a BST - LeetCode

Given the `root` of a binary search tree, and an integer `k`, return the `k``th` smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

    Input: root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3


Constraints:

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10``4`
- `0 <= Node.val <= 10``4`


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

SOLUTION ATTEMPT
if we first go left and then go right, we are traversing the bstree exactly in order, once we hit the lowest number we want to start to count, and when the count is k we want to return that node.
If there are only lefts:

0 → 1 → 2 → None
0 | count=
1 | count = 1 sets k_smallest returns=1
2 | returns =0
k= 2

k_smallest = None
def get_k_smallest(root, parent=None):


    if node is None:
        return 0


    count = get_k_smallest(root) + 1
    if count == k:
        k_smallest = root

    return count


This is how we traverse in order AND ALSO GIVES US THE SOLUTION!

count = 0
k_smallest = None
def traverse(node):

    if node is None:
        return


    traverse(node.left)

    # the first time this is executed is on the the most left node
    count += 1
    if k == count:
        k_smallest = node

    traverse(node.right)



    This is O(N), CONCLUSION OF BST, execute code between left and right recursion
"""