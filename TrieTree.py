from Node import *

class TrieTree:
    
    def __init__(self):
        
        self.root = Node("")
        self.nodeCount = 1
        
    def insert(self, word):
        
        currNode = self.root
        for c in word:
            if c in currNode.childNodes:
                # go to child node
                currNode = currNode.childNodes[c]
            else:
                # make new node
                self.nodeCount += 1
                insertNode = Node(c)
                currNode.childNodes[c] = insertNode
                currNode = insertNode
                
                
    def query(self, word):
        
        currNode = self.root
        queryArr = []
        for c in word:
            if c in currNode.childNodes:
                queryArr.append(currNode.childNodes[c].char)
                currNode = currNode.childNodes[c]
            else:
                # word not found
                print("{} was NOT found in the Trie Tree".format(word))
                
        print("Successful search for {}".format(word))
        print(queryArr)
        
        
        
        


words = ["apple", "apply", "application"]
trie = TrieTree()

for word in words:
    trie.insert(word)
    
trie.query("application")
print("Number of nodes: {}".format(trie.nodeCount))

            
                