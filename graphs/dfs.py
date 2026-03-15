# Algorithm: Depth First Search (DFS)
# Time Complexity: O(V + E)
# Space Complexity: O(V)

def dfs(graph, node, visited):

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


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
    graph[v].append(u)  # remove for directed graph


start = input("Enter starting node: ")

visited = set()

print("DFS traversal:")
dfs(graph, start, visited)
