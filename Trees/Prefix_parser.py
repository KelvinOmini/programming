from AST import PlusNode, TimesNode, NumNode
from AST_Traversal import PlusNode, TimesNode, NumNode
from postfix_parser import prefix_to_postfix 

import queue

def E(q):
    if q.empty():
        raise ValueError("Invalid Prefix Expression")
    
    token = q.get()
    if token == "+":
        return PlusNode(E(q), E(q))
    
    if token == "*":
        return TimesNode(E(q), E(q))
    
    return NumNode(float(token))

def main():
    x = input("Please enter a prefix expression: ")

    postfix_form = prefix_to_postfix(x)
    
    lst = x.split()
    q = queue.Queue()
    for token in lst:
        q.put(token)

    root = E(q)

    print("The infix from is: " + root.inorder())
    print(f"The postfix form is: {postfix_form}" )
    print(root.eval())

if __name__ == "__main__":
    main()
    