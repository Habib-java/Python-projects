# I Built a Tiny Tic-Tac-Toe Game for the Terminal

*A beginner-friendly Python project to play with friends and family.*

**Publication:** DEV Community  
**Tags:** `python`, `beginners`, `cli`, `games`

Sometimes a good first project is a familiar game with just enough logic to make you think. I built a two-player Tic-Tac-Toe game that runs right in the terminal, with no extra packages to install.

## How to play

You and a friend share the keyboard and take turns entering the number of the square you want. X goes first. The game checks for a win or a draw, and then offers a rematch.

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player X, choose a square (1-9):
```

Save or open `main.py`, then start a terminal in the project folder and run:

```bash
python main.py
```

On some systems, use `python3 main.py` instead.

## What I practiced

The project uses a list of nine squares to represent the board. A tuple of eight winning lines covers the rows, columns, and diagonals, so one small function can check every possible win. Input validation prevents out-of-range numbers and moves on occupied squares; the round loop handles turns, wins, and draws.

Keeping the game in the terminal made it easy to focus on the rules and the flow of a complete little program: show the board, accept a move, update the state, and decide what happens next. The replay prompt means friends and family can keep playing without restarting the script.

## Give it a try

Play a round with someone nearby, then see if you can add a feature: a single-player mode, a move counter, or a scoreboard that lasts across rematches. The simplest projects are often the best place to start experimenting.
