

class Node:
    "Node representation for TrieTree"
    def __init__(self, char):
        
        self.char = char
        # key = char, value = Node
        self.childNodes = {}