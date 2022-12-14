import ipaddress

class Node():
    def __init__(self, end=False, str=""):
        self.str = str #value stored in the node
        self.children = {} #store the associated children nodes
        self.end = end  #indicates if terminating at this path means its been inserted already

    #inserts a child into the trie
    def insertChild(self, value, isEnd=False):
        self.children[value] = Node(str=value, end=isEnd) 

    #allows child node to be set to an ending node
    def isEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end

    def getValue(self):
        return self.str

    def getChild(self, child):
        #return the node corresponding to the child being looked for
        if child in self.children:
            return self.children[child]
        else:
            return None

class RadixTrie():
    
    #initalize with empty root node
    def __init__(self):
        self.root = Node()
        self.name = 'radix_trie'
        self.nodeCount = 0

     #convert ip address to binary representation
    def ip2bin(self, addr):
        return bin(int(addr.network_address)) #convert to bits

    #checks if a node's children shares a prefix with the remainig portion of the search string
    def comparePrefix(self, prefix, remStr):
        if len(prefix) == 0 or len(remStr) == 0: return False
        return True if prefix[0] == remStr[0] else False
    
    #returns index of where the prefix and string overlap
    def overlap(self, prefix, remStr):
        i, n, m = 0, len(prefix), len(remStr)
        while i < n and i < m and prefix[i] == remStr[i]:
            i +=1
        return i
    
    #trim the protion of the remiaing string that matches the child
    def trimPrefix(self, prefix, remStr):
        i, n, m = 0, len(prefix), len(remStr)
        while i < n and i < m and prefix[i] == remStr[i]: 
            i +=1
        return remStr[i: m]
    
    
    def queryHelper(self, node, str, currStr, remStr):
        searchNode = None # holds the node that needs to be searched next
        currStr += node.getValue() #add this to the found string

        #string exists inside the trie
        if node.isEnd() and str == currStr:
            return True

        #if no children, string will not be in the tree
        elif len(node.children) == 0 or remStr == "":
            return False
        
        #keep exploring the tree
        else:
            #loop over all the children nodes
            for prefix, childNode in node.children.items():
                if self.comparePrefix(prefix, remStr):
                    searchNode = childNode
                    remStr = self.trimPrefix(prefix, remStr)
                    break 

            #prefix match not found
            if searchNode is None:
                return False
            
            else:
                return self.queryHelper(searchNode, str, currStr, remStr)

    #check if string exists 
    def query(self, str):
        if str.__contains__("."):
            arr = str.split(",")
            str = self.ip2bin(ipaddress.ip_network(arr[1]))
            str = str[2:len(str)]
            res = "0b" + self.queryIPHelper(self.root,str, "",str)
            return ipaddress.ip_network(int(res, 2))

        return self.queryHelper(self.root, str, "", str)
    
    def insertHelper(self, node, word):
        searchNode = None #node that we need to recurse to

        #no more word to be found
        if word == "":
            return

        #node has no children so we can insert the rest of the new word
        if len(node.children.values()) == 0:
            node.insertChild(word, isEnd=True)
            return

        #check if a prefix already exists
        for prefix, childNode in node.children.items():
            #prefix exists
            if self.comparePrefix(prefix, word):
                searchNode = childNode #found node to search
                
        #prefix does not exists so we create a new node
        if searchNode is None:
            newNode = Node(str=word, end=True)
            node.children[word] = newNode
            return

        #prefix exists in the tree, potential need for splitting nodes
        else:
            currPrefix = searchNode.str #prefix that was stored as a child
            matchedPrefix = word[0: self.overlap(word, currPrefix)] #portion of prefix thats the same for node value and new insert
            remStr = self.trimPrefix(word, currPrefix) #remainig string
            word = self.trimPrefix(currPrefix, word)

            #prefixes matches with entire node value, insert 
            if currPrefix == matchedPrefix:
                if word == "":
                    self.nodeCount -=1 #discount value
                    #print("Word is already inserted")
                    searchNode.setEnd(True) #indicated that child node is now an end to a word
                    return
                else:
                    self.insertHelper(searchNode, word) #insert remaining string
                    return
            
            #prefix does not match and needs to be split
            else:
                newNode = None
                searchNode.str = matchedPrefix #matched prefix becomes the new node value
                newNode = Node(end=searchNode.isEnd(), str=remStr) #remaining string becomes a new node
                toPop = []
                for prefix, childNode in searchNode.children.items():
                    newNode.children[prefix] = childNode #add to new node
                    toPop.append(prefix) 

                #pop old prefix values form updated node
                for popVal in toPop:
                    searchNode.children.pop(popVal)
                    
                searchNode.children[newNode.str] = newNode #insert old prefixes to new node
                searchNode.insertChild(word, isEnd=True) #insert new node
                node.children.pop(currPrefix)
                searchNode.setEnd(False)
                node.children[matchedPrefix] = searchNode
                self.nodeCount +=1


    def queryIPHelper(self, node, str, currStr, remStr):
        searchNode = None # holds the node that needs to be searched next
        currStr += node.getValue() #add this to the found string

        #string exists inside the trie
        if node.isEnd() and str == currStr:
            return currStr

        #if no children, string will not be in the tree
        elif len(node.children) == 0 or remStr == "":
            #for i in range(len(remStr)): currStr += "0"
            return currStr
        
        #keep exploring the tree
        else:
            #loop over all the children nodes
            for prefix, childNode in node.children.items():
                if self.comparePrefix(prefix, remStr):
                    searchNode = childNode
                    remStr = self.trimPrefix(prefix, remStr)
                    break 

            #prefix match not found
            if searchNode is None:
                print("in")
                for i in range(len(remStr)): currStr += "0"
                return currStr
            
            else:
                return self.queryIPHelper(searchNode, str, currStr, remStr)
        

    def insert(self, word):
        if word.__contains__("."):
            arr = word.split(",")
            word = self.ip2bin(ipaddress.ip_network(arr[1]))
            word = word[2:len(word)]

        self.nodeCount +=1
        self.insertHelper(self.root, word)

    def printTrieHelper(self, tmpNode, i):
        print(f"Level {i}: {tmpNode.str}, End: {tmpNode.isEnd()}")
        print("Children: ")
        for key, _ in tmpNode.children.items():
            print(f"{key}\n")

        for _, node in tmpNode.children.items():
            self.printTrieHelper(node, i+1)

    #prints Trie layer by layer    
    def printTrie(self):
       self.printTrieHelper(self.root, 1)


#tree = RadixTrie()
#tree.insert('CHAPTER')
#tree.insert('I')
#tree.insert('CHAPTER')
#tree.insert('II')

#tree = RadixTrie()
#tree.insert("01111001.01000010.10111101.11110010,121.66.189.242")
#tree.printTrie()
#print(tree.query("01111001.01000010.10111101.11110010,121.0.0.0"))
# tree = RadixTrie()
# tree.insert("bac")
# #tree.printTrie()
# tree.insert("abc")
# #tree.printTrie()
# tree.insert("abd")
# #tree.printTrie()
# tree.insert("abdf")
# tree.insert("ab")
# tree.printTrie()
# assert(tree.lookup("abdf") == True)
# assert(tree.lookup("ab") == True)
# assert(tree.lookup("bac") == True)
# assert(tree.lookup("abc") == True)

            



        

