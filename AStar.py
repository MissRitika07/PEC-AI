import heapq

class Node:
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic (estimated cost from current to end)
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        # Define comparison for the priority queue based on f value
        return self.f < other.f

def astar(grid, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given grid"""

    # Create start and end nodes
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Initialize open and closed lists
    # open_list uses a heap for O(log n) pop operations
    open_list = []
    closed_set = set()

    # Heapify the open list and add the start node
    heapq.heappush(open_list, start_node)

    # Keep track of positions in the open list to prevent redundant checks
    open_positions = {start_node.position: start_node.g}

    # Loop until you find the end
    while open_list:

        # Get the current node (node with the lowest f value)
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position
        
        # Remove from open tracking
        if current_pos in open_positions:
            del open_positions[current_pos]

        # Add the current node to the closed set
        closed_set.add(current_pos)

        # Found the goal
        if current_pos == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children (Adjacent squares)
        (x, y) = current_pos
        # 4-movement directions (Up, Down, Left, Right). Add diagonals if needed.
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for next_pos in neighbors:
            
            # Make sure within range
            if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
                continue

            # Make sure walkable terrain (0 = walkable, 1 = obstacle)
            if grid[next_pos[0]][next_pos[1]] != 0:
                continue

            # If already evaluated, skip
            if next_pos in closed_set:
                continue

            # Create child node
            child = Node(current_node, next_pos)
            
            # Distance from start to child (assuming uniform weight of 1)
            child.g = current_node.g + 1 
            
            # Manhattan distance heuristic to end
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # Child is already in the open list with a lower or equal cost
            if next_pos in open_positions and child.g >= open_positions[next_pos]:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)
            open_positions[next_pos] = child.g

    return None # Return None if no path is found


# --- Example Usage ---
if __name__ == '__main__':
    # 0 = Walkable, 1 = Obstacle/Wall
    maze = [
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
    ]

    start_point = (0, 0)
    end_point = (4, 5)

    shortest_path = astar(maze, start_point, end_point)
    print("Path found:", shortest_path)
