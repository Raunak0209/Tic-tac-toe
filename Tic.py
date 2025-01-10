class TicTacToe3x3:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        print("\n   0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i}  {' | '.join(row)}")
            if i < 2:
                print("  ---+---+---")

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("Cell already occupied! Try again.")
            return False

    def check_win(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):  # Row
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):  # Column
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)):  # Diagonal \
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):  # Diagonal /
            return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_full(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def play_game(self):
        print("Welcome to 3x3 Tic Tac Toe!")
        self.display_board()
        while True:
            try:
                print(f"\nPlayer {self.current_player}'s turn:")
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if 0 <= row < 3 and 0 <= col < 3:
                    if self.make_move(row, col):
                        self.display_board()
                        if self.check_win():
                            print(f"Player {self.current_player} wins!")
                            break
                        if self.is_full():
                            print("It's a draw!")
                            break
                        self.switch_player()
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

if __name__ == "__main__":
    game = TicTacToe3x3()
    game.play_game()
