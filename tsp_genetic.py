import numpy as np
import random

# Sample adjacency matrix representing distances between cities
# Each value represents the distance between city i and city j
distances = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 15],
    [25, 30, 5, 15, 0]
])

def initialize_population(pop_size, num_cities):
    """
    Creates an initial population of random routes
    Example: For 5 cities, might generate route [0,2,1,4,3]
    """
    population = []
    for _ in range(pop_size):
        # Create a random permutation of cities (excluding the first city)
        route = list(range(1, num_cities))
        random.shuffle(route)
        # Add starting city (0) at beginning and end to complete the tour
        route = [0] + route + [0]
        population.append(route)
    return population

def calculate_fitness(route, distances):
    """
    Calculate fitness as inverse of total distance (shorter distance = higher fitness)
    Example: For route [0,1,2,3,4,0] calculates distance 0→1→2→3→4→0
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i], route[i + 1]]
    
    # We want to maximize fitness, so we use inverse of distance
    if total_distance == 0:
        return float('inf')  # Avoid division by zero
    return 1 / total_distance

def tournament_selection(population, fitness_values, tournament_size=3):
    """
    Tournament selection - selects the best individual from a random sample
    Example: From 3 random individuals with fitness [0.1, 0.3, 0.2], selects the one with 0.3
    """
    # Select random tournament contestants
    tournament_indices = random.sample(range(len(population)), tournament_size)
    
    # Find the best contestant
    best_idx = tournament_indices[0]
    for idx in tournament_indices:
        if fitness_values[idx] > fitness_values[best_idx]:
            best_idx = idx
            
    return population[best_idx].copy()

def crossover(parent1, parent2):
    """
    Ordered crossover (OX) for TSP
    Example: parent1 = [0,1,2,3,4,0], parent2 = [0,4,1,3,2,0]
    might produce child = [0,1,3,2,4,0]
    """
    # We exclude first and last city (fixed as 0)
    size = len(parent1) - 2
    
    # Choose two crossover points
    start, end = sorted(random.sample(range(size), 2))
    
    # Create child with parent1's values between crossover points
    child = [None] * (size + 2)
    child[0] = 0  # Start city
    child[-1] = 0  # End city
    
    # Copy segment from parent1
    for i in range(start+1, end+1):
        child[i] = parent1[i]
    
    # Fill remaining positions with cities from parent2, maintaining order
    # But skipping cities already in the child
    parent2_idx = 1
    for i in range(1, size+1):
        if child[i] is None:
            while parent2[parent2_idx] in child:
                parent2_idx += 1
                if parent2_idx >= len(parent2) - 1:  # Skip the last city (0)
                    parent2_idx = 1
            child[i] = parent2[parent2_idx]
    
    return child

def mutate(route, mutation_rate):
    """
    Swap mutation - randomly swaps two cities in the route
    Example: [0,1,2,3,4,0] might become [0,1,4,3,2,0]
    """
    if random.random() < mutation_rate:
        # Select two positions to swap (excluding first and last)
        idx1, idx2 = random.sample(range(1, len(route)-1), 2)
        # Swap the cities
        route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

def genetic_algorithm(distances, pop_size=50, generations=100, mutation_rate=0.1):
    """
    Main genetic algorithm for TSP with tournament selection
    """
    num_cities = distances.shape[0]
    population = initialize_population(pop_size, num_cities)
    
    # Track best route
    best_distance = float('inf')
    best_route = None
    
    # Track progress
    progress = []
    
    for gen in range(generations):
        # Calculate fitness for each individual
        fitness_values = [calculate_fitness(route, distances) for route in population]
        
        # Find best route in current generation
        best_idx = np.argmax(fitness_values)
        current_best_route = population[best_idx]
        current_best_distance = 1 / fitness_values[best_idx]
        
        # Update overall best
        if current_best_distance < best_distance:
            best_distance = current_best_distance
            best_route = current_best_route.copy()
            print(f"Generation {gen}: New best route: {best_route} with distance: {best_distance:.2f}")
        
        progress.append(best_distance)
        
        # Create next generation
        new_population = []
        
        # Elitism: Keep the best individual
        new_population.append(current_best_route)
        
        # Create rest of the new population
        while len(new_population) < pop_size:
            # Tournament selection
            parent1 = tournament_selection(population, fitness_values)
            parent2 = tournament_selection(population, fitness_values)
            
            # Crossover
            child = crossover(parent1, parent2)
            
            # Mutation
            child = mutate(child, mutation_rate)
            
            new_population.append(child)
        
        # Replace old population
        population = new_population
    
    return best_route, best_distance

# Run the genetic algorithm
best_route, best_distance = genetic_algorithm(distances, pop_size=50, generations=100, mutation_rate=0.1)

print("\nFinal Results:")
print(f"Best route found: {best_route}")
print(f"Total distance: {best_distance:.2f}")

print("\nCity-by-city path:")
for i in range(len(best_route)-1):
    print(f"City {best_route[i]} → City {best_route[i+1]}: Distance = {distances[best_route[i]][best_route[i+1]]}")