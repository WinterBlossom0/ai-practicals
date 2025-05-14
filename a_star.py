import heapq

def a_star_search(graph, start_node, goal_node, heuristic_costs):
    """
    A* Search Algorithm using adjacency matrix representation
    
    Args:
        graph: 2D array where graph[i][j] is the cost from node i to node j (inf if no edge)
        start_node: Index of the starting node
        goal_node: Index of the goal node
        heuristic_costs: List of heuristic costs from each node to goal
    
    Returns:
        path: List of node indices representing the optimal path
        total_cost: Total cost of the path
    """
    # Number of nodes in the graph
    num_nodes = len(graph)
    
    # Priority queue for open nodes: (f_cost, node_index, path, g_cost)
    open_list = [(heuristic_costs[start_node], start_node, [start_node], 0)]
    
    # Set to track visited nodes
    closed_set = set()
    
    while open_list:
        # Get node with lowest f_cost
        f_cost, current, path, g_cost = heapq.heappop(open_list)
        
        # If we reached the goal, return the path and cost
        if current == goal_node:
            return path, g_cost
        
        # Skip if we've already visited this node
        if current in closed_set:
            continue
        
        # Mark current node as visited
        closed_set.add(current)
        
        # Check all neighbors of current node
        for neighbor in range(num_nodes):
            # Skip if there's no edge or if neighbor is already visited
            if graph[current][neighbor] == float('inf') or neighbor in closed_set:
                continue
                
            # Calculate costs
            edge_cost = graph[current][neighbor]
            new_g_cost = g_cost + edge_cost
            new_f_cost = new_g_cost + heuristic_costs[neighbor]
            
            # Add to open list
            new_path = path + [neighbor]
            heapq.heappush(open_list, (new_f_cost, neighbor, new_path, new_g_cost))
    
    # No path found
    return None, float('inf')

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
    
    path, cost = a_star_search(graph, start_node, goal_node, heuristic_costs)
    
    print("A* Search Results:")
    if path:
        print(f"Path found: {' -> '.join(str(node) for node in path)}")
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
    
    # Another example with different start node
    start_node = 1
    path, cost = a_star_search(graph, start_node, goal_node, heuristic_costs)
    
    print("\nA* Search from Vertex 1 to Vertex 6:")
    if path:
        print(f"Path found: {' -> '.join(str(node) for node in path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found!")