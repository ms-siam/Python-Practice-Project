def printTable(table):
    # Determine the column widths
    colWidths = [max(len(item) for item in column) for column in table]

    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(colWidths[col]), end= ' ')
        print()


# Test the function with the given data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
