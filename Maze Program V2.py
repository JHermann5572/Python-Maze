import random

def random_neighbor(tile, width):
    legal_choice = False
    while not legal_choice:
        directions = ["U", "D", "L", "R"]
        directions[0] = tile - width
        directions[1] = tile + width
        directions[2] = tile - 1
        directions[3] = tile + 1
        direction = random.choice(directions)

        if direction == directions[0] and (tile // width == 0):
            pass
        elif direction == directions[1] and (tile // width == (width - 1)):
            pass
        elif direction == directions[2] and (tile % width == 0):
            pass
        elif direction == directions[3] and (tile % width == (width - 1)):
            pass
        else:
            neighbor = direction
            legal_choice = True
    return neighbor

def random_walk(tile, width, stop_list):
    next_step = random_neighbor(tile, width)
    walk = []
    while next_step not in stop_list:
        walk.append(next_step)
        stop_list.append(next_step)
        tile = next_step
        next_step = random_neighbor(tile, width)
    result = walk[:]  # Assign result here
    return result

def printable_maze(walks, width):
    maze = [["#" for _ in range(2 * width + 1)] for _ in range(2 * width + 1)]
    for walk in walks:
        for tile in walk:
            # Calculate the row and col indices for the maze
            row = 2 * (tile // width) + 1
            col = 2 * (tile % width) + 1
            
            # Check if the calculated indices are within the maze bounds
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
                maze[row][col] = " "
            else:
                print(f"Index out of range: row={row}, col={col}")  # Debug output
    
    maze_str = "\n".join("".join(row) for row in maze)
    return maze_str

def wilsons(start, end, width):
    stop_list = [end]
    result = []
    print(f"Initial stop_list: {stop_list}")  # Debug output

    while len(set(stop_list)) < width ** 2:
        x = random_walk(start, width, stop_list)
        stop_list += x
        result.append(x)
        print(f"Updated stop_list: {stop_list}")  # Debug output
        print(f"Current result: {result}")  # Debug output
        start = random.randint(0, width ** 2 - 1)

    return result

name_of_file = input("What is the name of the file? ")
wide = int(input("What is the width of the maze? "))
start_tile = random.choice(list(range(wide)))
tile2 = random_neighbor(start_tile, wide)

# Debug output to check initial state
print(f"Start tile: {start_tile}")
print(f"Tile2: {tile2}")

walks = wilsons(start_tile, tile2, wide)
maze_str = printable_maze(walks, wide)

# Write the generated maze to a text file
with open(f"{name_of_file}.txt", "w") as the_file:
    the_file.write(maze_str)

print("DONE")
