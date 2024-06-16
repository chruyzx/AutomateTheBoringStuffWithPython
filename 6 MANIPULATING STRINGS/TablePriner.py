def printTable(tableData):
  """
  Prints a table of strings, right-justified.

  Args:
    tableData: A list of lists of strings, where each inner list represents a column.
  """

  # Calculate the width of each column
  colWidths = [0] * len(tableData)
  for i in range(len(tableData)):
    for j in range(len(tableData[i])):
      if len(tableData[i][j]) > colWidths[i]:
        colWidths[i] = len(tableData[i][j])

  # Print the table
  for row in range(len(tableData[0])):
    for col in range(len(tableData)):
      print(tableData[col][row].rjust(colWidths[col]), end=' ')
    print()

# Example usage
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)