# Use trie data structure to store Strings and search strings
# Implement insert() and search() function for TRIE data structure and search the given string A
# # Day 70/100

# Function to insert string into TRIE.
def insert(root, key):
    chars = list(key)
    if not root.children[charToIndex(chars[0])]:
        root.children[charToIndex(chars[0])] = set()
    root.children[charToIndex(chars[0])].add(key)


# Function to use TRIE data structure and search the given string.
def search(root, key):
    chars = list(key)

    if root.children[charToIndex(chars[0])]:
        if key in root.children[charToIndex(chars[0])]:
            return True
    return False



#  Driver Code Starts
class TrieNode:
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()


# use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch) - ord("a")


if __name__ == "__main__":
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = input().strip().split()
        strs = input()

        t = Trie()

        for s in arr:
            insert(t.root, s)

        if search(t.root, strs):
            print(1)
        else:
            print(0)
