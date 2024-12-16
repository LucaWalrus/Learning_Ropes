# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x > 2 or x < 0 or y > 2 or y < 0: #conditions can be improved #poorly written
        return False
    if x <= 2 or y <= 2:
        if game_board[y][x] != "":
            return False
        elif game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False

if __name__ == "__main__":
    game_board = [["X", "X", ""], ["", "", "o"], ["o", "", ""]]
    print(play_turn(game_board, 1, 1, "o"))
    print(game_board)
