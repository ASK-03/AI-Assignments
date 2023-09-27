# Define a heuristic function that estimates the cost from current position to goal position.
def heuristic(current_pos, goal_pos):
    terrain_cost = {'G': 1, 'D': 2, 'R': 5, 'F': 0, 'S': 0}  # Define terrain traversal costs
    return abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1]) * terrain_cost[terrain[current_pos[0]][current_pos[1]]]

# Define A* Search algorithm.
def a_star_search(start, goal):
    open_list = [(start, 0)]        # Initialize open list with starting position and cost so far
    closed_set = set()              # Initialize closed set (visited nodes)

    while open_list:
        current, cost_so_far = min(open_list, key=lambda x: x[1])       # Get the node with minimum cost from open list
        open_list.remove((current, cost_so_far))                        # Remove the current node from open list

        if current == goal:                                             # If current node is the goal, return the total cost
            return cost_so_far

        closed_set.add(current)                                         # Add current node to closed set

        for neighbor in get_neighbors(current):                         # Explore neighbors of current node
            if neighbor not in closed_set:
                new_cost = cost_so_far + terrain_cost[terrain[neighbor[0]][neighbor[1]]]        # Calculate new cost
                open_list.append((neighbor, new_cost))                                          # Add neighbor and new cost to open list

    return float('inf')             # Return infinity if no path found

# Define Weighted A* Search algorithm.
def weighted_a_star_search(start, goal, weight):
    open_list = [(start, 0)]        # Initialize open list with starting position and cost so far
    closed_set = set()              # Initialize closed set (visited nodes)

    while open_list:
        current, cost_so_far = min(open_list, key=lambda x: x[1] + weight * heuristic(x[0], goal))  # Get node with minimum cost + heuristic
        open_list.remove((current, cost_so_far))            # Remove current node from open list

        if current == goal:                                 # If current node is the goal, return the total cost
            return cost_so_far

        closed_set.add(current)                             # Add current node to closed set

        for neighbor in get_neighbors(current):             # Explore neighbors of current node
            if neighbor not in closed_set:
                new_cost = cost_so_far + terrain_cost[terrain[neighbor[0]][neighbor[1]]]        # Calculate new cost
                open_list.append((neighbor, new_cost))                                          # Add neighbor and new cost to open list

    return float('inf')             # Return infinity if no path found

# Define function to get valid neighboring cells.
def get_neighbors(pos):
    neighbors = []
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:         # Define possible movements (up, down, left, right)
        new_pos = (pos[0] + move[0], pos[1] + move[1])      # Calculate new position
        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m and terrain[new_pos[0]][new_pos[1]] != 'R':      # Check if new position is valid
            neighbors.append(new_pos)                       # Add valid neighbor to list
    return neighbors

print('Enter input dimensions (2 single spaced integers)')
# Read input dimensions
n, m = map(int, input().split(' '))
print(f'Enter {n} rows of the maze each having {m} characters without any spaces, representing the cell terrain.')
# Read terrain grid
terrain = [list(input()) for _ in range(n)]

start = None
goal = None

# Find start and goal positions
for i in range(n):
    for j in range(m):
        if terrain[i][j] == 'S':
            start = (i, j)
        elif terrain[i][j] == 'F':
            goal = (i, j)

# Define terrain traversal costs
terrain_cost = {'G': 1, 'D': 2, 'R': 5, 'F': 0, 'S': 0}

# Run A* Search
min_cost_a_star = a_star_search(start, goal)
print('A* search result =',min_cost_a_star)

# Run Weighted A* Search (with weight = 5 for example)
weight = 5
min_cost_weighted_a_star = weighted_a_star_search(start, goal, weight)
print(f'Weighted A* search result (with weight : {weight}) = {min_cost_weighted_a_star}')