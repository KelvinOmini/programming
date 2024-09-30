class Edge:
    def __init__(self, v1, v2, weight = 0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight 

    def __it__(self, other):
        return self.weight < other.weight 
