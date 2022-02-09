"""


26. CLOSED Same Tree - LeetCode

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

    Input: p = [1,2,1], q = [1,1,2]
    Output: false


SOLUTION ATTEMPT:

If we have a method “traverse_tree” we are already halfway there…

traverse_tree(root):

    left_traversed = True if root.left is None else traverse_tree(root.left)
    right_traversed = True if root.right is None else traverse_tree(root.right)
    return left_traversed and right_traversed

Now we can write a method “same_tree” that checks

same_tree(root_a, root_b):


    is_same = False if root_a is None or root_b is None else root_a.value == root_b.value

    left_same = True if root.left is None and root_b is None else  # same ending
                    is_same and same_tree(root_a.left, root_b.left)

    right_same = True if root.right is None and root_b.right is None else  # same ending
                    is_same and same_tree(root_a.right, root_b.right)


    return left_same and right_same
    
"""