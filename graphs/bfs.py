# Algorithm: Breadth First Search (BFS)
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# User input
edges = int(input("Enter number of edges: "))

graph = {}

for _ in range(edges):
    u, v = input("Enter edge (u v): ").split()

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)   # remove this line for directed graph


start = input("Enter starting node: ")

print("BFS traversal:")

bfs(graph, start)
