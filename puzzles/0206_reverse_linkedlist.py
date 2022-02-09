"""


44. CLOSED Reverse Linked List - LeetCode

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

Example 1:

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

    Input: head = [1,2]
    Output: [2,1]

Example 3:

    Input: head = []
    Output: []


Constraints:

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Let's do it recursively:

SOLUTION ATTEMPT:

def reverse_list(node, prev_node=None):

    if node is None:
        return


    next_node = node.next  # 2
    node.next = prev_node  # link 1 to previuos (or None)


    reverse_list(next_node, next)

"""