"""

https://leetcode.com/problems/longest-substring-without-repeating-characters/
2.  CLOSED Longest Substring Without Repeating Characters - LeetCode

Hint: use sliding window and a dictionary last_index: Dict[str, int]. Combine this with the fact that once we have a longest substring, we only have to keep looking for substrings of that same long length, hence the sliding, increasing, window.

def find_longest_substring(string):


    last_index: Dict[str, int] = {}
    max_len = 0


    start_index = 0
    for i, s in enumerate(string):


        if s in last_index:
            start_index = max(start_index, last_index[s] + 1)  # ?


        max_len = max(max_len, i - start_index + 1)


        last_index[s] = i

return string[start_index:start_index + max_len]

O(d) in space, d: length of dictionary
O(N) in time

"""