# Algorithm: Topological Sort 
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import defaultdict, deque

def topological_sort(vertices, edges):

    graph = defaultdict(list)
    indegree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()

    for i in range(vertices):
        if indegree[i] == 0:
            queue.append(i)

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != vertices:
        print("Graph has a cycle")
    else:
        print("Topological Order:", topo_order)


# User input
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []

for _ in range(E):
    u, v = map(int, input("Enter edge (u v): ").split())
    edges.append((u, v))

topological_sort(V, edges)
