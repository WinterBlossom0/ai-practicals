import numpy as np

def minimax(node_index, depth, is_maximizing, game_tree):
    """
    Minimax algorithm with DFS on a game tree represented as a matrix
    
    Parameters:
    - node_index: Current position (i,j) in the game tree matrix
    - depth: Current depth in the tree
    - is_maximizing: Boolean indicating if current player is maximizing
    - game_tree: Matrix representation of the game tree
    
    Returns:
    - best_value: The optimal value for the current player
    """
    i, j = node_index
    
    # Base case: If leaf node (last row of the matrix)
    if i == len(game_tree) - 1:
        return game_tree[i][j]
    
    # Find child indices (in the next row)
    left_child = (i + 1, j * 2)
    right_child = (i + 1, j * 2 + 1)
    
    # Ensure children are within bounds
    children = []
    if left_child[1] < len(game_tree[i+1]):
        children.append(left_child)
    if right_child[1] < len(game_tree[i+1]):
        children.append(right_child)
    
    if is_maximizing:
        best_value = float('-inf')
        for child in children:
            value = minimax(child, depth + 1, False, game_tree)
            best_value = max(best_value, value)
            print(f"MAX node {node_index} evaluating child {child}: value={value}, best={best_value}")
        return best_value
    else:
        best_value = float('inf')
        for child in children:
            value = minimax(child, depth + 1, True, game_tree)
            best_value = min(best_value, value)
            print(f"MIN node {node_index} evaluating child {child}: value={value}, best={best_value}")
        return best_value

# Define the game tree as a matrix
# Each row represents a level in the tree
# Only leaf nodes have actual values, internal nodes have None
game_tree = [
    [None],             # Root (MAX) - Level 0
    [None, None, None], # Level 1 (MIN)
    [3, 5, 2, 9, 12, 8] # Level 2 (leaf nodes)
]

print("Game Tree Matrix:")
for i, level in enumerate(game_tree):
    print(f"Level {i}: {level}")

# Run the minimax algorithm starting at the root (0,0)
print("\nRunning Minimax with DFS:")
optimal_value = minimax((0, 0), 0, True, game_tree)
print(f"\nOptimal value for the root node: {optimal_value}")

# Visualize the game tree (text representation)
print("\nGame Tree Visualization:")
print("       MAX       ")
print("        |        ")
print("    MIN     MIN  ")
print("    / \\     / \\ ")
print("   3   5   2   9 ")