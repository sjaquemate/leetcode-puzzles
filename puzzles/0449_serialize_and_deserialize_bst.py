"""

73. CLOSED (1) Serialize and Deserialize BST - LeetCode

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.

Example 1:

    Input: root = [2,1,3]
    Output: [2,1,3]

Example 2:

    Input: root = []
    Output: []


Constraints:

- The number of nodes in the tree is in the range `[0, 10``4``]`.
- `0 <= Node.val <= 10``4`
- The input tree is guaranteed to be a binary search tree.

SOLUTION ATTEMPT

it is easy if we can get the list version: just ‘#’.join(tree_as_list)

But how do we make the tree as a list?
Lets write it in pre-order notation: root, left, right

to_preorder_list()
preorder_list = []
def traverse_tree(root):

    if root is None
        return


    preorder_list.append(root)

    traverse_tree(root.left)
    traverse_tree(root.right)

return preorder_list

serialize = ‘#’.join([node.val for node in to_preorder_list(root)])


preorders = …etc

index = -1
recurse(parent_val=float(‘inf’)):

    index += 1
    val = preorder[index]
    node = Node(val = val)



    if index >= len(preorders) - 1:
        return Node

    if preorder[index+1] < val:
        node.left = recurse(val)
    if preorder[index+1] > val and preorder[index+1] < parent_val
        node.right = recurse(val)

    return node


THIS WORKS I THINK.

"""