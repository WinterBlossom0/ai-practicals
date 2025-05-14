def ida_star_search(graph, start_node, goal_node, heuristic_costs):
    """
    Iterative Deepening A* Search using adjacency matrix representation
    
    Args:
        graph: 2D array where graph[i][j] is the cost from node i to node j (inf if no edge)
        start_node: Index of the starting node
        goal_node: Index of the goal node
        heuristic_costs: List of heuristic costs from each node to goal
    
    Returns:
        path: List of node indices representing the optimal path
        total_cost: Total cost of the path
    """
    # Initial threshold is the heuristic cost from start to goal
    threshold = heuristic_costs[start_node]
    
    iteration = 1
    
    while True:
        print(f"\n==== ITERATION {iteration}: Threshold = {threshold} ====")
        # Track minimum f_cost that exceeds threshold for next iteration
        next_threshold = float('inf')
        # Initialize search path and visited nodes
        path = []
        visited = set()
        exploration_paths = []  # List to track all paths explored
        
        # Initial call to recursive search function
        result, cost, new_threshold, exploration_paths = search(
            graph, start_node, goal_node, 0, threshold, 
            heuristic_costs, path, visited, exploration_paths, "", 0
        )
        
        # Print exploration paths for this threshold
        print(f"\nPaths explored at threshold {threshold}:")
        if not exploration_paths:
            print("No paths explored at this threshold.")
        else:
            for i, (p, f, status) in enumerate(exploration_paths):
                print(f"{i+1}. Path: {p} (f-cost: {f}) - {status}")
        
        # Path found
        if result:
            print(f"\nSolution found at threshold: {threshold}")
            return path, cost
            
        # No solution exists
        if new_threshold == float('inf'):
            print("No solution exists.")
            return None, float('inf')
            
        # Update threshold and try again
        print(f"Increasing threshold from {threshold} to {new_threshold}")
        threshold = new_threshold
        iteration += 1
        
        # For safety - if we somehow get stuck
        if threshold > 1000:  # Arbitrary large number
            print("Threshold too high, likely no solution")
            return None, float('inf')

def search(graph, current, goal, g_cost, threshold, heuristic, path, visited, 
          exploration_paths, path_str, depth):
    """
    Recursive search function for IDA*
    
    Args:
        graph: Adjacency matrix
        current: Current node index
        goal: Goal node index
        g_cost: Cost from start to current
        threshold: Current f-cost threshold
        heuristic: List of heuristic values to goal
        path: Current path (will be modified)
        visited: Set of visited nodes
        exploration_paths: List to track paths explored
        path_str: String representation of current path
        depth: Current depth in search tree
    
    Returns:
        Tuple of (found_path, path_cost, next_threshold, exploration_paths)
    """
    # Add current node to path
    path.append(current)
    visited.add(current)
    
    # Update path string
    curr_path_str = path_str + (str(current) if path_str == "" else f" -> {current}")
    
    # Calculate f_cost (g + h)
    f_cost = g_cost + heuristic[current]
    
    # If f_cost exceeds threshold, return minimum f_cost for next iteration
    if f_cost > threshold:
        path.pop()
        visited.remove(current)
        status = f"PRUNED (f-cost {f_cost} exceeds threshold {threshold})"
        exploration_paths.append((curr_path_str, f_cost, status))
        return False, 0, f_cost, exploration_paths
    
    # Goal found
    if current == goal:
        status = "GOAL REACHED"
        exploration_paths.append((curr_path_str, f_cost, status))
        return True, g_cost, threshold, exploration_paths
    
    # Add current path to exploration paths
    status = f"EXPLORED (depth {depth}, f-cost {f_cost})"
    exploration_paths.append((curr_path_str, f_cost, status))
    
    # Track minimum f_cost exceeding threshold for next iteration
    min_threshold = float('inf')
    
    # Explore neighbors
    for neighbor in range(len(graph)):
        # Skip if no edge or already visited
        if graph[current][neighbor] == float('inf') or neighbor in visited:
            continue
        
        # Calculate cost to neighbor
        new_g_cost = g_cost + graph[current][neighbor]
        
        # Recursive search from neighbor
        found, cost, new_threshold, exploration_paths = search(
            graph, neighbor, goal, new_g_cost, threshold, 
            heuristic, path, visited, exploration_paths, curr_path_str, depth + 1
        )
        
        # If path found, return success
        if found:
            return True, cost, new_threshold, exploration_paths
        
        # Update minimum threshold
        min_threshold = min(min_threshold, new_threshold)
    
    # Backtrack
    path.pop()
    visited.remove(current)
    
    # No path found with current threshold
    return False, 0, min_threshold, exploration_paths

if __name__ == "__main__":
    # Define a simple graph with 7 nodes (0-6)
    # Using adjacency matrix representation
    inf = float('inf')
    graph = [
        #0    1    2    3    4    5    6
        [0,   2,   4,   inf, inf, inf, inf], # 0
        [2,   0,   1,   7,   inf, inf, inf], # 1
        [4,   1,   0,   inf, 3,   inf, inf], # 2
        [inf, 7,   inf, 0,   2,   1,   inf], # 3
        [inf, inf, 3,   2,   0,   5,   2],   # 4
        [inf, inf, inf, 1,   5,   0,   3],   # 5
        [inf, inf, inf, inf, 2,   3,   0]    # 6
    ]
    
    # Heuristic costs to goal node (node 6)
    # These are estimated costs from each node to the goal
    heuristic_costs = [
        7,  # node 0 -> goal
        6,  # node 1 -> goal
        5,  # node 2 -> goal
        3,  # node 3 -> goal
        2,  # node 4 -> goal
        1,  # node 5 -> goal
        0   # node 6 -> goal (goal itself)
    ]
    
    # Find path from node 0 to node 6
    start_node = 0
    goal_node = 6
    
    path, cost = ida_star_search(graph, start_node, goal_node, heuristic_costs)
    
    print("\n=== FINAL IDA* SEARCH RESULTS ===")
    if path:
        print(f"Optimal path found: {' -> '.join(str(node) for node in path)}")
        print(f"Total cost: {cost}")
        
        # Print each step of the path with its cost
        print("\nDetailed path:")
        for i in range(len(path)-1):
            current = path[i]
            next_node = path[i+1]
            step_cost = graph[current][next_node]
            print(f"Vertex {current} -> Vertex {next_node}: Cost = {step_cost}")
    else:
        print("No path found!")