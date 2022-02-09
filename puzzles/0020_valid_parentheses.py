"""


7. CLOSED Valid Parentheses - LeetCode

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.


    Input: s = "()[]{}"
    Output: true


    Input: s = "(]"
    Output: false

We can rewrite somehow: -1, 1, -3, 3, 5, -5… this doesnt seem to lead somehwere.
We observe that all openings can be made no matter what, closing is the problem. It seems easy:


openers = {‘(‘: ‘)’, ‘{‘: ‘}’, ‘[‘: ‘]’}
closers = {v: k for k,v in closers.items()}

def validate_parentheses(string):

    unclosed_openers = []  # forwardly linked list
    for s in string:
        if s in openers:
            unclosed_openers.add_end(s)
        elif s in closers:
            if len(unclosed_openers) == 0:
                return False

            last_opener = unclosed_openers.get_last()
            if last_opener == closers[s]:
                unclosed_linkedlist.remove_last()
            else:
                return False
        else:
            raise CharError
    return len(unclosed_openers) == 0

worst case space complexity O(N), time complexity O(N)
"""