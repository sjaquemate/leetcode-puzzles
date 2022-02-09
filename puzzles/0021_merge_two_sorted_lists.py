"""


8. CLOSED Merge Two Sorted Lists - LeetCode

You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Use two finger method again:
odo: refactor → refactored in next question!

def merge_sorted_linkedlists(n1, n2):  # input heads

    merged = None
    merged_head = None
    while n1 is not None or n2 is not None:
        if merged is None:
            if n1.val < n2.val:  # new head
                merged_head= n1
                merged = merged_head
                n1 = n1.next
            else:
                merged_head = n2
                merged = merged_head
                n2 = n2.next
        elif n2 is None:  # keep adding from n1
            merged.next = n1
            n1 = n1.next
        elif n1 is None:  # keep adding from n2
            merged.next = n2
            n2 = n2.next
        else:
            if n1.val < n2.val:
                merged.next = n1
                merged = merged.next
                n1 = n1.next
            else:
                merged.next = n2
                merged = merged.next
                n2 = n2.next

space complexity: O(1), time complexity O(N)

"""