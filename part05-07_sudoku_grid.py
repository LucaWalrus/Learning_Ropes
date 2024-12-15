# Write your solution here

#sudoku rows
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True

#sudoku columns
def column_correct(sudoku: list, column_no: int):
    numbers2 = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers2:
            return False
        numbers2.append(number) 
    return True

#sudoku squares
def block_correct(sudoku: list, row_num: int, column_num: int):
    numbers3 = []
    for r in range(row_num, row_num+3):
        for s in range(column_num, column_num+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers3:
                return False
            numbers3.append(number)
    return True

def all_blocks_correct(sudoku: list):
    tuple_check = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for row_cnt, colum_cnt in tuple_check:
        if not block_correct(sudoku, row_cnt, colum_cnt):
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    # Check all rows
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False
    # Check all columns
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False
    # Check all blocks
    if not all_blocks_correct(sudoku):
        return False
    # If all checks pass, the grid is valid
    return True

if __name__ == "__main__":
    sudoku = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
        ]
    print(sudoku_grid_correct(sudoku))
