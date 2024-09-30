from AVL_Trees import AVLTree

class AVLNode:
    def __init__(self, item, height =1, left= None, right = None):
        self.item = item
        self.height = height
        self.left = left
        right = right

    def balance(self):
        return AVLTree.height(self.right) - AVLTree.height(self.left)    