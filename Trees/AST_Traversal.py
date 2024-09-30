class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()
    
    def inorder(self):
        return "(" + self.left.inorder() + " * " + self.right.inorder() + ")"
    
class PlusNode:
    def __init__(self, left, rigth):
        self.left = left
        self.right = rigth

    def eval(self):
        return self.left.eval() + self.right.eval()
    
    def eval(self):
        return self.left.eval() + self.right.eval()
    
    def inorder(self):
        return "(" + self.left.inorder() + " + " + self.right.inorder() + ")"
    
class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num
    
    def eval(self):
        return self.num
    
    def inorder(self):
        return str(self.num)
    
    

        