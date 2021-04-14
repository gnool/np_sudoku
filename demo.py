import numpy as np


class SudokuNP:
    def __init__(self, string=None):
        self.board = None
        if string:
            self.create(string)

    def create(self, string):
        """Create a 9x9 Sudoku board.

        Each board is a Boolean array of 9x9x9, where the dimensions correspond to row, column, and number.

        Input:
            string - a row-major string of the Sudoku puzzle where "." is used to represent unfilled cells.

        Output:
            board - 9x9x9 Boolean array
        """
        # validate input
        allowed_chars = set("123456789.")
        input_chars = set(string)
        assert len(allowed_chars.union(input_chars)) == 10
        # create blank board
        board = np.ones((9,9,9), np.bool)
        num_indices = np.array([9 if x == '.' else int(x)-1 for x in string], dtype=np.uint8)
        filled_indices = np.where(num_indices != 9)[0]
        row_indices = (np.arange(81) // 9)[filled_indices]
        col_indices = (np.arange(81) % 9)[filled_indices]
        # remove all numbers from the filled cells (except for the filled number)
        board[row_indices, col_indices] = 0
        board[row_indices, col_indices, num_indices[filled_indices]] = 1
        self.board = board

    def visualize(self):
        """Visualize sudoku board in 2D ASCII."""
        for i in range(9):
            row = self.board[i]
            string = np.chararray(9)
            string[:] = '.'
            filled_indices = np.where(np.sum(row, axis=1) == 1)
            num_indices = np.nonzero(row[filled_indices])[1]+1
            string[filled_indices] = num_indices
            print(string.tostring().decode())


if __name__ == "__main__":
    sdk = SudokuNP('.2.6.8...58...97......4....37....5..6.......4..8....13....2......98...36...3.6.9.')
    sdk.visualize()
