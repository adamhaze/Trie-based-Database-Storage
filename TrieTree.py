import ipaddress

class TrieNode:
    "Node representation for TrieTree"
    def __init__(self, char):
        
        self.char = char
        # key = char, value = Node
        self.childNodes = {}

class TrieTree:
    
    def __init__(self):
        
        self.root = TrieNode("")
        self.nodeCount = 1
        self.name = 'basic_trie'

    #convert ip address to binary representation
    def ip2bin(self, addr):
        return bin(int(addr.network_address)) #convert to bits
    
    def bin2ip(self, addr):
        return int(addr)
        
    def insert(self, word):
        
        currNode = self.root
        for c in word:
            if c in currNode.childNodes:
                # go to child node
                currNode = currNode.childNodes[c]
            else:
                # make new node
                self.nodeCount += 1
                insertNode = TrieNode(c)
                currNode.childNodes[c] = insertNode
                currNode = insertNode
    
                
    def queryIPHelper(self, node, addr):
        searchNode = node
        longestMatch = "0b"
        bits = self.ip2bin(addr)
        for i, bit in enumerate(bits):

            if i > 1:
                #matched with child  node
                if int(bit)  in searchNode.childNodes:
                    longestMatch += bit
                    searchNode = searchNode.childNodes[int(bit)]

                else:    
                    for _ in range(i, 34): longestMatch += "0"   
                    break
        
            
        # print(longestMatch)
        return ipaddress.ip_network(int(longestMatch, 2))
        
                
    def queryHelper(self, word):
        
        currNode = self.root
        queryArr = []
        for c in word:
            if c in currNode.childNodes:
                queryArr.append(currNode.childNodes[c].char)
                currNode = currNode.childNodes[c]
            else:
                # word not found
                print("{} was NOT found in the Trie Tree".format(word))
        # return queryArr


    def query(self, word):
        if word.__contains__("."):
            arr = word.split(",")
            # print(arr)
            addr = arr[1]
            return self.queryIPHelper(self.root, ipaddress.ip_network(addr))
        
        else:
            self.queryHelper(word)
                
        # print("Successful search for {}".format(word))
        # print(queryArr)
        
            