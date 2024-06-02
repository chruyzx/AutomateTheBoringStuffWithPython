grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def print_grid(grid):
  """Prints the image represented by the grid."""
  for j in range(len(grid[0])):  # Loop through columns
    for i in range(len(grid)):  # Loop through rows within each column
      print(grid[i][j], end='')  # Print the character without a newline
    print()  # Print a newline after each column


print_grid(grid)