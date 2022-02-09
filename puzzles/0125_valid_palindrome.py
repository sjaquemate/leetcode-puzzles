"""


32. CLOSED Valid Palindrome - LeetCode

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

alphabet = [“abcdefghijklmnopqrstuvwxyz”]
def preprocess(string):

    string = string.lower()
    valid_chars = [s for s in string if s in alphabet]
    return ‘’.join(valid_chars)

def is_palindrome(string):


    if len(string) <= 1:  # base case
        return True
    return string[0]==string[-1] and is_palindrome(string[1:-1])  # recursion
"""