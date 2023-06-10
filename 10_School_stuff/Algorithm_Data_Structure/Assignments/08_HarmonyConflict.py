# this is a graph coloring exercise, where each vertex is colored either as 0 or 1
# edge between two vertices is labeled as 0 or 1
# if two vertices are connected by an edge labeled 0, they must be colored the same
# if two vertices are connected by an edge labeled 1, they must be colored differently
# if the graph can satisfy above conditions, return 1, otherwise return 0

import sys

def graph_coloring(n, m, edges):
    graph = [[] for _ in range(n)]
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))
    colors = [-1] * n
    for i in range(n):
        if colors[i] == -1:
            if not dfs(i, 0, colors, graph):
                return 0
    return 1

def dfs(start, color, colors, graph):
    stack = [(start, color)]
    while stack:
        u, c = stack.pop()
        colors[u] = c
        for v, e in graph[u]:
            if colors[v] == -1:
                stack.append((v, 1 - c) if e else (v, c))
            elif colors[v] != 1 - c and e:
                return False
    return True

sys.setrecursionlimit(10**6) # set the maximum recursion depth to 10^6
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(graph_coloring(n, m, edges))

# Here, we first create a graph using the given edges and then perform a depth-first search (DFS) on the graph to check if it can be colored as per the given conditions. We maintain a colors array to store the color of each vertex, which is initially set to -1 to indicate that it has not been colored yet. In the DFS function, we start with a vertex and a color and color all its neighbors accordingly. If we encounter an already colored vertex, we check if it has the correct color as per the given edge label. If not, we return False, indicating that the graph cannot be colored as per the given conditions. Finally, if all vertices are colored correctly, we return True, indicating that the graph can be colored as per the given conditions.
# In this updated code, we use a stack to simulate the recursive calls in the DFS function. The stack contains tuples of the form (u, c), where u is the current vertex and c is its color. We pop the top element from the stack and color the current vertex, and then iterate over its neighbors. For each neighbor, we check if it has been colored already. If not, we push it onto the stack with the opposite color if the edge label is 1, or the same color if the edge label is 0. If the neighbor has already been colored and its color is not compatible with the current vertex, we return False. Finally, if all vertices are colored correctly, we return True.
