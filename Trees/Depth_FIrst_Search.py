# ALGORITHM
'''
def dfs(current, goal):
    if current == goal:
        return (current)
    
    for next in adjacent(current):
        result = dfs(next)
        if result != None:
            return [current] + result
    return None
'''