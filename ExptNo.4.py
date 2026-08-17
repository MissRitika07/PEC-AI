import heapq

def best_first_search(graph, heuristics, start, goal):
   
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start, [start]))
    
    # Set to keep track of visited nodes (CLOSED list)
    closed_list = set()
    
    while open_list:
        # Extract the node with the lowest heuristic value
        current_heuristic, current_node, path = heapq.heappop(open_list)
        
        # Check if we reached our target
        if current_node == goal:
            return path
            
        # If the node has not been visited yet, expand it
        if current_node not in closed_list:
            closed_list.add(current_node)
            
            # Explore neighbors
            for neighbor in graph.get(current_node, []):
                if neighbor not in closed_list:
                    # Calculate neighbor's heuristic value and push to priority queue
                    h_val = heuristics.get(neighbor, float('inf'))
                    heapq.heappush(open_list, (h_val, neighbor, path + [neighbor]))
                    
    return None  # Path not found

# --- Example Usage ---
if __name__ == "__main__":
    # Define a sample graph using an adjacency list
    example_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': ['H'],
        'F': [],
        'G': ['H'],
        'H': []
    }
    
    # Define heuristic values (Estimated straight-line distance to goal 'H')
    heuristic_values = {
        'A': 10,
        'B': 8,
        'C': 7,
        'D': 12,
        'E': 3,
        'F': 6,
        'G': 4,
        'H': 0  # Heuristic of goal node is always 0
    }
    
    start_node = 'A'
    goal_node = 'H'
    
    # Run the algorithm
    result_path = best_first_search(example_graph, heuristic_values, start_node, goal_node)
    
    # Output the result
    if result_path:
        print(f"Path found: {' -> '.join(result_path)}")
    else:
        print("No path could be found to the goal node.")