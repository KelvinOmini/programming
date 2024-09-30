class Trie:
    def __insert(node,item):
        # This is the recursive insert function 
        pass
    def __contains(node, item):
        # This is the recursive membership test
        pass

    class TrieNode:
        def __init__(self, item, next = None, follows = None ):
            self.item = item
            self.next = next
            self.follows = follows

    def __init__(self):
        self.start = None

    def insert(self, item):
        self.start = Trie.__insert(self.start, item)

    def __contains__(self, item):
        return Trie.__contains(self.start, item)
    
    
        
        