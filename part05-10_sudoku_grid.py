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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    # Directly modify the sudoku list
    sudoku[row_no][column_no] = number


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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
