"""


47. CLOSED Design Add and Search Words Data Structure - LeetCode

Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.


Example:

    Input
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
    [null,null,null,null,false,true,true,true]

    Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True


Constraints:

- `1 <= word.length <= 500`
- `word` in `addWord` consists lower-case English letters.
- `word` in `search` consist of  `'.'` or lower-case English letters.
- At most `50000` calls will be made to `addWord` and `search`.

SOLUTION ATTEMPT
Much like previous exercise, add_word works the same as insert.
Now search is different, But this could be a very big lookup in the tree, therefore i propose the following: For every insertion we create a new letter ‘.’  However, this would make the tree w! bigger. We could lay the problem at the search, but the search would be somewhat inefficient that way, but okay, this seems to make the most sense for now:
so:

We would need recursion for this:

def search(word, node=self.root):

    if len(word) == 0:
        return node.next is None


    char = word[0]
    word = word[1:]
    for child in node.children:
        if char == ‘.’ or char in child:
            if seach(word, node=child):
                return True:


    return False

Without the ‘.’, a dictionary would be the fastest solution,.. VERY INTERESTED IN FSATEST ANSWER!!!

"""