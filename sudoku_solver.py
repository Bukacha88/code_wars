def sudoku(puzzle):
    n = 9

    def is_safe(puzzle, row, col, num):
        for x in range(9):
            if puzzle[row][x] == num:
                return False
        for x in range(9):
            if puzzle[x][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if puzzle[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_suduko(puzzle, row, col):
        if row == n - 1 and col == n:
            return True
        if col == n:
            row += 1
            col = 0
        if puzzle[row][col] > 0:
            return solve_suduko(puzzle, row, col + 1)
        for num in range(1, n + 1, 1):
            if is_safe(puzzle, row, col, num):
                puzzle[row][col] = num
                if solve_suduko(puzzle, row, col + 1):
                    return True
            puzzle[row][col] = 0
        return False

    if solve_suduko(puzzle, 0, 0):
        return puzzle


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku(puzzle)
