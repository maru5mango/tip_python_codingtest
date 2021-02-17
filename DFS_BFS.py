# BFS
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    dq = deque([root])

    while dq:
        n = dq.popleft()
        if n not in visited:
            visited.append(n)
            dq.extend(graph[n])
    return visited

# DFS
def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit
