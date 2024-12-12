from s_q import Queue

def get_overflow_list(grid):
	# Implement total rows and cols of the grid
	rows = len(grid)
	cols = len(grid[0]) if rows > 0 else 0
	tuplesList = []

	# Iteratate the row and col with requirement of the overflow
	for row in range(rows):
		for col in range(cols):
			# Calculate the neighbor, 2 neighbors with 2 'if' matches, 3 neighbots with 3 'if' matches and so on
			neighbors = 0
			if row > 0: 
				neighbors += 1
			if row < rows - 1: 
				neighbors += 1
			if col > 0:  
				neighbors += 1
			if col < cols - 1: 
				neighbors += 1
			# If the absolute value of the cell is greater than or equal to its neighbors, mark it as an overflow cell
			if neighbors > 0 and abs(grid[row][col]) >= neighbors:
				tuplesList.append((row, col))
	
	return tuplesList if tuplesList else None


def overflow(grid, a_queue):
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Check if all values in the grid are positive or negative
    all_positive = all(all(cell >= 0 for cell in row) for row in grid)
    all_negative = all(all(cell <= 0 for cell in row) for row in grid)

    # If the grid is all positive or all negative, enqueue the grid and return 1
    if all_positive or all_negative:
        return 0

    count = 0

    # Get the list of cells that need to overflow by calling back the function
    overflow_cells = get_overflow_list(grid)
    if not overflow_cells:
        return count

    # Process each overflow cell
    for row, col in overflow_cells:
        sign = 1 if grid[row][col] > 0 else -1
        
        # Store the absolute value of the current cell (magnitude of overflow)
        current_cell_value = abs(grid[row][col])
        grid[row][col] = 0

        # Overflow to the right cell, if within bounds
        if col < num_cols - 1:
            next_cell_value = abs(grid[row][col + 1])
            # Check if right neighbor has the same value and is also an overflow cell
            if current_cell_value == next_cell_value and (row, col + 1) in overflow_cells:
                # Handle special overflow condition
                grid[row][col] = sign
                grid[row][col + 1] = sign
                # Overflow to cells two steps away, if within bounds
                if col + 2 < num_cols - 1:
                    grid[row][col + 2] = (abs(grid[row][col + 2]) + 1) * sign
                    if row + 1 < num_rows:
                        grid[row + 1][col + 1] = (abs(grid[row + 1][col + 1]) + 1) * sign
                overflow_cells.remove((row, col))
            else:
                # Overflow normally to the right neighbor
                grid[row][col + 1] = (abs(grid[row][col + 1]) + 1) * sign

        # Overflow to the left, top, or bottom cell, if within bounds
        if col > 0:
            grid[row][col - 1] = (abs(grid[row][col - 1]) + 1) * sign
        if row > 0:
            grid[row - 1][col] = (abs(grid[row - 1][col]) + 1) * sign
        if row < num_rows - 1:
            grid[row + 1][col] = (abs(grid[row + 1][col]) + 1) * sign

    # Save the current state of the grid after handling overflows
    a_queue.enqueue([row[:] for row in grid])

    # Recursively call overflow to handle further cascades and increase count
    count += overflow(grid, a_queue) + 1

    return count
