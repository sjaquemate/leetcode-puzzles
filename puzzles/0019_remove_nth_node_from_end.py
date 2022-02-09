"""

6. CLOSED Remove Nth Node From End of List - LeetCode


Given the `head` of a (forwardly) linked list, remove the `n``th` node from the end of the list and return its head. E.g: Input: head = [1,2,3,4,5], n = 2

    Output: [1,2,3,5]

Let's attempt the solution immediately
[n1, n2, n3, n4] n=2
index  | nth_last
0           None
1            None
2           n1
3           n2

now link n2 to n4

def remove_nth_last_node(head, n):  # n is nth last node: 1 is last node


    nth_last_node = None
    index = 0

    node = head
    while node.next is not None:
        if index == n:
            nth_last_node = head
        if index > n:
            nth_last_node = nth_last_node.next
        index += 1

    if nth_last_node is None
        raise Error(f“{n} is bigger than length of linkedlist”)
    if nth_last_node == head:
        return head.next  # new head


    nth_last_node.next = nth_last_node.next.next  # remove the link
    return head 
"""