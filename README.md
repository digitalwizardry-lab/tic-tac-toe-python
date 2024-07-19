# Tic-Tac-Toe Python

A simple Tic-Tac-Toe game implemented in Python, supporting dynamic board sizes and featuring a clear console-based interface.

## Features

- Supports different board sizes (e.g., 3x3, 4x4, 5x5, etc.)
- Clear and centered console display
- Dynamic cell width calculation for proper alignment
- Move validation to ensure valid moves
- Checks for win conditions and draw
- Clear screen before displaying the board for better user experience

## How to Play

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/digitalwizardry-lab/tic-tac-toe-python.git
    cd tic-tac-toe-python
    ```

2. **Run the Game**:
    ```bash
    python tic_tac_toe.py
    ```

3. **Instructions**:
    - At the start, you will be prompted to enter the board size.
    - Players take turns entering their moves by specifying the cell number.
    - The game checks for a win or draw after each move.
    - The game ends when a player wins or when the board is full (draw).

## Example Game Play

```
Enter the board size (e.g., 3 for a 3x3 board): 3

Turn 1, Player X
┏━━━┳━━━┳━━━┓
┃ 1 ┃ 2 ┃ 3 ┃
┣━━━╋━━━╋━━━┫
┃ 4 ┃ 5 ┃ 6 ┃
┣━━━╋━━━╋━━━┫
┃ 7 ┃ 8 ┃ 9 ┃
┗━━━┻━━━┻━━━┛

Enter your move (1-9): 5

Turn 2, Player O
┏━━━┳━━━┳━━━┓
┃ 1 ┃ 2 ┃ 3 ┃
┣━━━╋━━━╋━━━┫
┃ 4 ┃ X ┃ 6 ┃
┣━━━╋━━━╋━━━┫
┃ 7 ┃ 8 ┃ 9 ┃
┗━━━┻━━━┻━━━┛

Enter your move (1-9): ...
```


## Author

- [DigitalWizardry](https://github.com/digitalwizardry-lab)

Contributions are welcome! Feel free to open issues or submit pull requests.
