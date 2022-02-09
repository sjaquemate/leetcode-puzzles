"""


37. CLOSED Reorder List - LeetCode

You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:

![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

SOLUTION ATTEMPT
simple is O(N^2) solution (inplace), Also simple is O(N) time and O(N) space. If it has to be inplace Im not sure where to begin… x1, x2, x3, x4, x5 → x1, x5, x2, x4, x3.
I can inplace get x1 x3 x2 x4 x5

Knowing first_node, second_node, end_node
first_node.next = end_node
end_node.next = second_node

now same routine with (second_node, second_node.next, end_node.previous)!
end_node.previous is tricky, but probably we can find it from recursion? yes, let's try it:

n1 n2 n3 n4 n5 n6 None
n1 n6 n2 n3 n4 n5 None
n1 n6 n2 n5 n3 n4 None
n1 n6 n2 n5 n3 n4 None

    [1,2,3,4,5,None]
    Output: [1,5,2,4,3,None]

def reorder_3(first, second, last):

    first.next = last
    last.next = second
    return last

n1 n2 n3
1, 2, 3 done
= 3

n1 n2 n3 n4 n5
1, 2, …
n-3 n-2 n-1
n-2 n-1 n
n-1 n None
4, 5, return 5
def reorder_linked(start_node, last_node=None)

    if start_node.next is None: # base case
        return start_node  # this is now the last node

    reorder_3(start_node, start_node.next,
                  reorder_3(start_node.next, start_node.next.next) if last_node is None else last_node)
    return



This works from begin to end and then collapses sequentially… We however, want to collapse from outside to the inside. That is why THE FOLLOWING IS THE BETTER IDEA:

first = node
second = node.next
def reorder_list(node)

    if node.next is None:
        reorder_3(first, second, node)
        first = first.next
        second = second.next
    reorder_list(first, second, node)

    reorder_list(node.next)

    reorder_3(start_node, start_node.next,
                  reorder_3(start_node.next, start_node.next.next) if last_node is None else last_node)
    return


def reorder_3(last_node):

    first.next = last_node
    last_node.next = second
    first = second
    second = second.next


first = node
second = node.next

def reorder_list(node)

    if node.next is None:
        return


    reorder_list(node)
    reorder_3(node)

"""