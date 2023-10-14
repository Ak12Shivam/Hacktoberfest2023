# Recursive Depth-First Search (DFS)
def recursive_dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')  # Visit the current node
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                recursive_dfs(graph, neighbor, visited)

# Iterative Depth-First Search (DFS)
def iterative_dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')  # Visit the current node
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recursive DFS:")
visited_recursive = set()
recursive_dfs(graph, 'A', visited_recursive)  # Start from node 'A'
print()

print("\nIterative DFS:")
visited_iterative = set()
iterative_dfs(graph, 'A')  # Start from node 'A'
