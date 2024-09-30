class Vertex:
    def __init__(self, vertexId, x, y, label):
        self.vertexId = vertexId
        self.x = x
        self.y = y
        self.label = label
        self.adjacent = []
        self.previous = None


        
    