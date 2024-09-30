class BinarySearchTree:
    class __Node:
        def __init__(self, val, left = None, right = None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val
        
        def setVal(self, newVal):
            self.val = newVal

        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right 
        
        def setLeft(self, newleft):
            self.left = newleft

        def setRight(self, newright):
            self.right = newright

    # This method deserves a little explanation. It does an inorder traversal
    # of the nodes of the tree yielding all the values. In this way, we get
    # the values in ascending order.

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right != None:
                for elem in self.right:
                    yield elem

    # Below are the methods of the BinarySearchTree class
    def __init__(self):
        self.root = None

    def insert(self, val):
        # The __insert function is recursive and is not a passed a self parameter. It is a
        # static function (not a method of the class) but is hidden inside the insert
        # function so users of the class will not know it exists.
        def __insert(root, val):
            if root == None:
                return BinarySearchTree.__Node(val)
            if val < root.getVal():
                root.setLeft(BinarySearchTree.__insert(root.getLeft(), val))
            else:
                root.setRight(BinarySearchTree.__insert(root.getright(), val))
            
            return root
        
        self.root = __insert(self.root,val)

    def __iter__(self):
        if self.roof != None:
            return self.root.__iter__()
        else:
            return ().__iter__()
        
def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(float(x))

    for x in tree:
        print(x)

if __name__ == "__main__":
    main()