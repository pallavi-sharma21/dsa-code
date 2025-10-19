class TrieNode:
    def _init_(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def _init_(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()
words = ["apple", "banana", "cherry"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: False
print(trie.starts_with("app"))  # Output: True
