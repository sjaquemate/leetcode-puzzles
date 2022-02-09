"""

61. CLOSED [LeetCode] 269. Alien Dictionary (zhuhan0.blogspot.com)

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Example 1:
Given the following words in dictionary,

    [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt"
    ]

The correct order is: `"wertf"`.
Example 2:
Given the following words in dictionary,

    [
      "z",
      "x"
    ]

The correct order is: `"zx"`.
Example 3:
Given the following words in dictionary,

    [
      "z",
      "x",
      "z"
    ]

The order is invalid, so return `""`.
Note:

1. You may assume all letters are in lowercase.
2. You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
3. If the order is invalid, return an empty string.
4. There may be multiple valid order of letters, return any one of them is fine.

SOLUTION ATTEMPT

Establish a Node that has a dictionary of lower and higher Nodes, this is maximum O(26*26)  complexity, also create a dicationary like so:
{“a”: Node(char=”a”, lower={}, higher= {}), … extract order of letters from this dictionary: i.e: ‘w’, ‘r’, node[‘w’].add_higher(‘r’) and viceversa. Iterate over all letterpairs as such (except if they are the same). NVM: inconsistencies can thus be solved by checking if add_higher() checks if char not in lower.

example : 'a’, ‘b’, ‘c’, ‘a’  # inconsistency will be fixed later! (hopefully)

then select the one that has no lower, if not possible, it is inconsistent
then remove that one and continue, until done. This is O(chars) complexity, involves no sorting or anything else! (it makes a lot of sense to solve inconsistencies at a later step of the algorithm)

class Letter:

    lower = set()
    higher = set()


    add_lower(letter: Letter):
        lower.add(letter)


    add_higher(letter: Letter):
        higher.add(letter)

letters[‘a’] = Letter() etc.

order_pairs = []
def add_order_pairs(words):

    ordered_letters = [word[0] for word in words if words]
    if len(ordered_letters) < 2:
        return
    for char_a, char_b in ordered_letters:
        if char_a != char_b
            order_pairs.append(letter_a, letter_b)
    add_order_pairs([word[1:] for word in words]

for char_a, char_b in order_pairs:

    letters[char_a].add_higher(letters[char_b])
    letters[char_b].add_lower(letters[char_b])

Most likely only add_lower is needed, but we will see:

Then
order = []
def get_order():

    if len(letters) == 0;
        return

    for letter in letters:
        if len(letter.lower) == 0:
            order.append(letter)
            letters.remove(letter)
            break
    else:
        raise Inconsistent


    for other_letter in letters:
        other_lether.remove_lower(letter)


    get_order()


example : z x z  → z: lower=set{x}, x: lower={z}, this will give Inconsistent error
example : z x → x: lower=set(z), z: lower=set() → this will pop z out, remove z from x.lower and then pop x out. Seems good
example: ,

    "wrt"
    "wrf",
      "er",
      "ett",
      "rftt"

pairs = we, er, tf, rt. and that's it: so:
e: {w}, r: {e}, w: {}, t: {r}, f: {t} →
1 [‘w’], pop w →
e: {}, r: {e}, t: {r}, f: {t}
2 [w, e] , pop e ->
r: {}, t: {r}, f: {t}, pop
3 [w, e, r]
t: {}, f: {t}
final: w, e, r, t, f

SEEMS PERFECT AND IS VERY CLEAR
"""