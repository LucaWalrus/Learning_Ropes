# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    check_list = []
    seen = []
    for i in range(3):  # Iterate over rows in the block
        for j in range(3):  # Iterate over columns in the block
            check_list.append(sudoku[row_no + i][column_no + j])
    print(check_list)
    for num in check_list:
        if num != 0:
            if num in seen:
                result = False              
            else:
                result = True
            seen.append(num)
    print(seen)
    return result
    
if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
