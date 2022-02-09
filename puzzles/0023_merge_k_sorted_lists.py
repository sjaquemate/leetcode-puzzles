"""

9. CLOSEDMerge k Sorted Lists - LeetCode

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

Same problem as before, we now however need to use something like:

- smallest_node = min(nodes, lambda node: node.val)
- smallest_node_idx = argmin(nodes, lambda node: node.val)

In this case we get:

def merge_sorted(nodes):

    merged_head = None
    merged_node = None
    while not all([node is None for node in nodes]):
        smallest_node = min(nodes, lambda node: node.val if node is not None else inf)
        smallest_node_idx = argmin(nodes, lambda node: node.val if node is not None else inf)
        # note: native argmin is same as return min(range(len(a)), key=lambda x: a[x])


        if merged_head is None:
            merged_head = smallest_node
            merged_node = merged_head
        else:
            merged_node.next = smallest_node
            merged_node = merged_node.next


        # increase smallest node
        nodes[smallest_node_idx] = nodes[smallest_node_idx].next

"""