"""

46. CLOSED Implement Trie (Prefix Tree) - LeetCode

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.


Example 1:

    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]

    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True


Constraints:

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10``4` calls in total will be made to `insert`, `search`, and `startsWith`.

We can use hashmap to input and get O(1) lookup, but cannot do anything useful with prefixes. Most logical is to have a 26-tree:

Trie():

    self.root = Node(children={})


    def get_child(node, char):
        if char in node.children:
            return node.children[char]
        return None


    def search(word):
        return starts_with(word)

    def starts_with(prefix):
        node = self.root
        for char in prefix:
            node = get_child(node, char)
            if node is None:
                return False
        return True

    def insert(word):
        node = self.root
        for char in word:
            node = add_char(char, node)

    def add_char(char, node):
        ""” adds and returns added node ""”
        if char not in node.children:
             node.children[car] = Node(children={})
        return node.children[char]

This does not use recursion, but is in itself pretty elegant. O(N) lookup and insertions.
"""