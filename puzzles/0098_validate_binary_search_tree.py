"""


25. CLOSED Validate Binary Search Tree - LeetCode

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.


Example 1:

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

    Input: root = [2,1,3]
    Output: true

Example 2:

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

validate_bst(root):


    is_valid_left = True if root.left is None
                      else root.left.value < root.value and validate_bst(root.left)  # this line is where the recursive boolean multiplication comes in :0
    is_valid_right = True if root.right is None
                      else root.right.value > root.value and validate_bst(root.right)
    return is_valid_left and is_valid_right

honestly pretty slick code ;)

TESTED PYTHON CODE


    class Node:

        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def validate_bst(root):
        is_valid_left = True if root.left is None else root.left.value < root.value and validate_bst(root.left)
        is_valid_right = True if root.right is None else root.right.value > root.value and validate_bst(root.right)
        return is_valid_left and is_valid_right

    def main():
        n3 = Node(3)
        n7 = Node(7)
        n6 = Node(6, right=n7)
        n4 = Node(4, n3, n6)
        n1 = Node(1)
        n5 = Node(5, n1, n4)

        print(validate_bst(n5))

"""