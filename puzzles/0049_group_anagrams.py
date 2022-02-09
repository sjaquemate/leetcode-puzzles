"""

13. CLOSED Group Anagrams - LeetCode

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

SOLUTION ATTEMPT:
This seems doable with a dictionary and comparing the dictionaries in the end, this will be a solution of order O(N*klogk), k is length of words N is number of elements. The key will be a tuple indicating the

get_anagram_hash(string):

    letters = {}
    for s in string:  # O(k)
        if s not in letters:
            anagram[s] = 1
        else:
            anagram[s] += 1


    sorted_letters = sorted(letters.keys())  # O(k log k)
    hash = ( (s, letters[s]) for s in sorted_letters)

anagrams = {}
for string in strs:

    hash = get_anagram_hash(string)
    if hash not in anagram:
        anagrams[hash] = [string]
    else:
        anagrams[hash].append(string)

print(anagrams.values)
"""