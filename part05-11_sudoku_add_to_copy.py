# Write your solution here

def print_sudoku(sudoku: list):
    for row in range(9):
        row_str = ""
        for col in range(9):
            # If the cell is 0 (empty), print '_', otherwise print the number
            if sudoku[row][col] == 0:
                row_str += "_ "
            else:
                row_str += str(sudoku[row][col]) + " "
            # Add a double space after the 3rd and 6th column
            if col == 2 or col == 5:
                row_str += " "  # Adding an extra space after the 3rd and 6th column
        print(row_str.strip())  # Strip the trailing space at the end of the row
        # Add a blank line after every 3 rows to separate the blocks
        if (row + 1) % 3 == 0 and row != 8:
            print()


def copy_and_add(sudoku: list, row: int, col: int, number:int):
    duplicate_list = [r[:] for r in sudoku]
    duplicate_list[row][col] = number
    return duplicate_list

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
