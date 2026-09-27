"""A simple two-player Tic-Tac-Toe game for the terminal."""

WINNING_LINES = (
	(0, 1, 2),
	(3, 4, 5),
	(6, 7, 8),
	(0, 3, 6),
	(1, 4, 7),
	(2, 5, 8),
	(0, 4, 8),
	(2, 4, 6),
)


def display_board(board):
	"""Print the board with numbered empty squares."""
	print()
	for row in range(3):
		start = row * 3
		print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
		if row < 2:
			print("---+---+---")
	print()


def has_won(board, player):
	"""Return True when player occupies a complete winning line."""
	return any(all(board[index] == player for index in line) for line in WINNING_LINES)


def get_move(board, player):
	"""Ask for an available square and return its number from 1 to 9."""
	while True:
		choice = input(f"Player {player}, choose a square (1-9): ").strip()
		if not choice.isdigit() or not 1 <= int(choice) <= 9:
			print("Enter a number from 1 to 9.")
			continue

		move = int(choice)
		if board[move - 1] in ("X", "O"):
			print("That square is taken. Choose an empty square.")
			continue
		return move


def play_game():
	"""Play one round, returning when it ends."""
	board = [str(number) for number in range(1, 10)]
	player = "X"

	while True:
		display_board(board)
		move = get_move(board, player)
		board[move - 1] = player

		if has_won(board, player):
			display_board(board)
			print(f"Player {player} wins!")
			return

		if all(square in ("X", "O") for square in board):
			display_board(board)
			print("It's a draw!")
			return

		player = "O" if player == "X" else "X"


def main():
	print("Welcome to Tic-Tac-Toe!")
	try:
		while True:
			play_game()
			answer = input("Play again? (y/n): ").strip().lower()
			while answer not in ("y", "n"):
				answer = input("Please enter y or n: ").strip().lower()
			if answer == "n":
				break
	except (EOFError, KeyboardInterrupt):
		print()
	print("Thanks for playing!")


if __name__ == "__main__":
	main()
