import collections

'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

'''

class TrieNode:

    def __init__(self, isWord=False):
        self.word = None
        self.isWord = isWord
        self.children = collections.defaultdict(TrieNode)

    def __str__(self):
        res = ""
        res += self.word
        for k, v in self.children.items():            
            res += str(v)
        return res

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        if not word:
            return
        current = self.root
        for char in word:
            current = current.children[char]
        current.isWord = True
        current.word = word
    
    def search(self, word):
        current = self.root
        return self.search_helper(current, word, 0)

    def search_helper(self, node, word, index):
        if index < len(word):
            char = word[index]
            if char == '.':
                return any(self.search_helper(n, word, index+1) for n in node.children.values())
            elif char not in node.children:
                return False
            else:
                return self.search_helper(node.children[char], word, index+1)
        return True


t = Trie()
t.addWord("bad")
t.addWord("dad")
t.addWord("mad")
print(t.search("pad") == False)
print(t.search("bad") == True)
print(t.search(".ad") == True)
print(t.search("b..") == True)
print(t.search("b.d") == True)