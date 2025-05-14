def dfs(graph, start_vertex, visited=None, path=None):
    """
    Recursive Depth-First Search implementation using adjacency matrix
    
    Args:
        graph: 2D adjacency matrix where graph[i][j] represents edge from i to j
        start_vertex: Starting vertex for DFS
        visited: Set of visited vertices (for recursive calls)
        path: List to track DFS traversal path (for recursive calls)
    
    Returns:
        List containing the DFS traversal path
    """
    # Initialize visited set and path list on first call
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    # Mark current vertex as visited and add to path
    visited.add(start_vertex)
    path.append(start_vertex)
    print(f"Visiting vertex {start_vertex}")
    
    # Get all adjacent vertices
    n = len(graph)
    for neighbor in range(n):
        # Check if there's an edge and if neighbor is not visited
        if graph[start_vertex][neighbor] != 0 and neighbor not in visited:
            # Recursive call for the neighbor
            dfs(graph, neighbor, visited, path)
    
    return path

if __name__ == "__main__":
    # Example adjacency matrix
    # 0 represents no edge, non-zero represents an edge
    graph = [
        #0  1  2  3  4  5  6
        [0, 1, 1, 0, 0, 0, 0],  # 0
        [1, 0, 0, 1, 1, 0, 0],  # 1
        [1, 0, 0, 0, 1, 0, 0],  # 2
        [0, 1, 0, 0, 0, 1, 0],  # 3
        [0, 1, 1, 0, 0, 1, 0],  # 4
        [0, 0, 0, 1, 1, 0, 1],  # 5
        [0, 0, 0, 0, 0, 1, 0]   # 6
    ]
    
    print("DFS traversal starting from vertex 0:")
    dfs_path = dfs(graph, 0)
    print(f"DFS Path: {dfs_path}")
    
    # Try DFS from a different starting point
    print("\nDFS traversal starting from vertex 3:")
    dfs_path = dfs(graph, 3)
    print(f"DFS Path: {dfs_path}")
    
    # Visualize the graph (text-based)
    print("\nGraph structure:")
    print("0 -- 1 -- 3")
    print("|    |    |")
    print("2 -- 4 -- 5 -- 6")