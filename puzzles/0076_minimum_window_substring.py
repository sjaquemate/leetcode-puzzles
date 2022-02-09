"""


22. CLOSED Minimum Window Substring - LeetCode

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.

Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

Follow up: Could you find an algorithm that runs in `O(m + n)` time?

SOLUTION ATTEMPT:
string s (length n) t (length m)

s = [“abanc”], t=[“bca”], solution = [“banc”]
sort(t)  # tlogt
remove s chars not in t
abaaaacab

start = 0
min_len = 0
latest_letters = {“a”: ([], 2 ( FIFO queue of length 2)}, .”b”: ([], 1), …}  # O(t) to create this
abac
for i, s in enumerate(string):  # O(N)

    if s in latest_letters:
        latest_letter[s].add_to_queue(i)


    if all(letter.queue_is_full() for letter in latest_letters):  # O(26)  number of characters
        cur_start = min(letter.queue.get_oldest_index() for letter in latest_letters)
        cur_end = max( … same … )
        cur_len = cur_end - cur_start
        if cur_len < min_len:
            min_len = cur_len
            start = cur_start


        PYTHON IMPLEMENTATION:
    import collections

    def minimal_window_substring(string, t):

        chars_counts = {}
        for char in t:  # O(t)
            if char not in chars_counts:
                chars_counts[char] = 1
            else:
                chars_counts[char] += 1

        latest_chars = {char: collections.deque([], maxlen=count) for char, count in chars_counts.items()}
        print(latest_chars)

        start = 0
        min_len = None
        for i, s in enumerate(string):  # O(N)

            if s in latest_chars:
                latest_chars[s].appendleft(i)

            queues = list(latest_chars.values())
            if all(len(qu) == qu.maxlen for qu in queues):  # O(26)  number of characters
                cur_start = min(qu[-1] for qu in queues)  # O(26)
                cur_end = max(qu[0] for qu in queues)  # O(26)

                cur_len = cur_end - cur_start
                if min_len is None or cur_len < min_len:
                    min_len = cur_len
                    start = cur_start

        return string[start:start+min_len+1]

    def main():
        sub = minimal_window_substring("adbaacabb", "aabbc")
        print(sub)
"""