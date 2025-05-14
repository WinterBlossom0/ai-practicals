import numpy as np
import random

# Same distance matrix as in the genetic algorithm
distances = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 15],
    [25, 30, 5, 15, 0]
])

def calculate_total_distance(route, distances):
    """Calculate the total distance of a route"""
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i], route[i + 1]]
    return total

def generate_neighbors(route):
    """Generate all neighbors by swapping pairs of cities (excluding first and last)"""
    neighbors = []
    # We don't swap the first and last cities (fixed as 0)
    for i in range(1, len(route) - 1):
        for j in range(i + 1, len(route) - 1):
            # Create a new neighbor by swapping cities at positions i and j
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def steepest_hill_climbing(distances, max_iterations=100):
    """Steepest ascent hill climbing algorithm for TSP"""
    num_cities = distances.shape[0]
    
    # Create initial random solution (starting and ending at city 0)
    current_route = [0] + random.sample(range(1, num_cities), num_cities - 1) + [0]
    current_distance = calculate_total_distance(current_route, distances)
    
    print(f"Initial route: {current_route}")
    print(f"Initial distance: {current_distance}")
    
    iteration = 0
    improved = True
    
    while improved and iteration < max_iterations:
        improved = False
        
        # Generate all neighbors by swapping cities
        neighbors = generate_neighbors(current_route)
        
        # Find the best neighbor
        best_neighbor = None
        best_distance = current_distance
        
        for neighbor in neighbors:
            distance = calculate_total_distance(neighbor, distances)
            if distance < best_distance:
                best_distance = distance
                best_neighbor = neighbor
        
        # If we found a better neighbor, move to it
        if best_distance < current_distance:
            current_route = best_neighbor
            current_distance = best_distance
            improved = True
            print(f"Iteration {iteration+1}: Found better route with distance {current_distance}")
        
        iteration += 1
    
    if not improved:
        print(f"Local optimum reached after {iteration} iterations")
    
    return current_route, current_distance

# Run the algorithm
best_route, best_distance = steepest_hill_climbing(distances)

print("\nFinal Results:")
print(f"Best route found: {best_route}")
print(f"Total distance: {best_distance}")

print("\nCity-by-city path:")
for i in range(len(best_route)-1):
    print(f"City {best_route[i]} → City {best_route[i+1]}: Distance = {distances[best_route[i]][best_route[i+1]]}")