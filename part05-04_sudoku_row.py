# Write your solution here

def row_correct(sudoku: list, row_no: int):
    check_list = []
    duplos = set()
    seen = set()
    for i in sudoku[row_no]:
        check_list.append(i)
    for item in check_list:
        if item in seen:
            duplos.add(item)
        else:
            seen.add(item)
    if duplos == {0}:
        result = True
    else:
        result = False
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
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
