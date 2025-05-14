from collections import deque

def bfs(graph, start_vertex):
    """
    Breadth-First Search implementation using adjacency matrix
    
    Args:
        graph: 2D adjacency matrix where graph[i][j] represents edge from i to j
        start_vertex: Starting vertex for BFS
    
    Returns:
        List containing the BFS traversal path
    """
    n = len(graph)
    visited = set()
    queue = deque([start_vertex])  # Use a queue for BFS
    path = []
    
    while queue:
        # Dequeue a vertex from queue
        current = queue.popleft()
        
        # Skip if already visited
        if current in visited:
            continue
        
        # Mark as visited and add to path
        visited.add(current)
        path.append(current)
        print(f"Visiting vertex {current}")
        
        # Add all unvisited neighbors to queue
        for neighbor in range(n):
            if graph[current][neighbor] != 0 and neighbor not in visited:
                queue.append(neighbor)
    
    return path

if __name__ == "__main__":
    # Example adjacency matrix (same as DFS)
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
    
    print("BFS traversal starting from vertex 0:")
    bfs_path = bfs(graph, 0)
    print(f"BFS Path: {bfs_path}")
    
    # Try BFS from a different starting point
    print("\nBFS traversal starting from vertex 3:")
    bfs_path = bfs(graph, 3)
    print(f"BFS Path: {bfs_path}")
    
    # Visualize the graph (text-based)
    print("\nGraph structure:")
    print("0 -- 1 -- 3")
    print("|    |    |")
    print("2 -- 4 -- 5 -- 6")