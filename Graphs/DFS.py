def graphcis(G, start, goal):
    # G =(V,E) is the graph with vertices, V and edges, E.
    V, E = G
    stack = stack()
    visited = set()
    stack.push(start)

    while not stack.any():
        # A vertex is popped from the stack. This is called the current vertex.
        current = stack.pop()
        # The current vertex is added to the visited set
        visited.add(current)

        # if the current vertex is the goal vertex, then we discontinue the
        # search reporting that we found the goal.
        if current == goal:
            return True
        
        # Otherwise, for every adjacent vertex, V, to the current 
        # vertex in the graph, v is pushed on the stack of vertices yet
        # to search unless v is already in the visited set in which case
        # the edge leading to v is ignored.
        for v in [v for u, v in E if u == current] + [u for u, v in E if v == current]:
            if not v in visited:
                stack.push(v)
            
    return 0 