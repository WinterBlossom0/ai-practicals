def depth_limited_dfs(graph, current, goal, depth_limit, visited=None, path=None):
    """
    Depth-Limited DFS implementation
    
    Args:
        graph: 2D adjacency matrix
        current: Current vertex
        goal: Goal vertex to find
        depth_limit: Maximum depth to search
        visited: Set of visited vertices
        path: Current path being explored
    
    Returns:
        Tuple (found, path) where found is boolean and path is the path to goal
    """
    # Initialize visited and path if this is the first call
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    # Add current vertex to path and visited
    path.append(current)
    visited.add(current)
    
    # Check if we found the goal
    if current == goal:
        return True, path
    
    # If depth limit reached, backtrack
    if depth_limit <= 0:
        path.pop()
        visited.remove(current)
        return False, path
    
    # Explore neighbors within depth limit
    for neighbor in range(len(graph)):
        if graph[current][neighbor] != 0 and neighbor not in visited:
            found, new_path = depth_limited_dfs(
                graph, neighbor, goal, depth_limit - 1, 
                visited.copy(), path.copy()
            )
            if found:
                return True, new_path
    
    # Goal not found in this path, backtrack
    return False, path

def iddfs(graph, start, goal, max_depth=float('inf')):
    """
    Iterative Deepening Depth-First Search
    
    Args:
        graph: 2D adjacency matrix
        start: Starting vertex
        goal: Goal vertex to find
        max_depth: Maximum depth to search
    
    Returns:
        Path to goal if found, None otherwise
    """
    for depth in range(max_depth + 1):
        print(f"\n--- Searching with depth limit: {depth} ---")
        found, path = depth_limited_dfs(graph, start, goal, depth)
        
        if found:
            return path
            
    return None  # Goal not found within max_depth

if __name__ == "__main__":
    # Example adjacency matrix from DFS
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
    
    # Visualize the graph
    print("Graph structure:")
    print("0 -- 1 -- 3")
    print("|    |    |")
    print("2 -- 4 -- 5 -- 6")
    
    # Get user input for start and goal vertices
    try:
        start_vertex = int(input("\nEnter start vertex (0-6): "))
        goal_vertex = int(input("Enter goal vertex (0-6): "))
        
        if not (0 <= start_vertex < len(graph) and 0 <= goal_vertex < len(graph)):
            raise ValueError("Vertices must be between 0 and 6")
        
        print(f"\nFinding path from vertex {start_vertex} to vertex {goal_vertex} using IDDFS...")
        path = iddfs(graph, start_vertex, goal_vertex, len(graph))
        
        if path:
            print(f"\nPath found: {' -> '.join(map(str, path))}")
            print(f"Path length: {len(path) - 1}")
        else:
            print(f"\nNo path exists from vertex {start_vertex} to vertex {goal_vertex}")
            
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example with predefined start and goal (comment out if using user input)
    # start_vertex = 0
    # goal_vertex = 6
    # print(f"\nFinding path from vertex {start_vertex} to vertex {goal_vertex} using IDDFS...")
    # path = iddfs(graph, start_vertex, goal_vertex, len(graph))
    # if path:
    #     print(f"\nPath found: {' -> '.join(map(str, path))}")
    # else:
    #     print(f"\nNo path exists from vertex {start_vertex} to vertex {goal_vertex}")