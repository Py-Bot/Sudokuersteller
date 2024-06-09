import random

def create_sudoku():
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(sudoku)
    
    # Lösche einige Zellen, um das Sudoku-Rätsel zu erstellen
    num_cells_to_clear = random.randint(40, 50) # Anzahl der Zellen, die gelöscht werden sollen
    cells_to_clear = random.sample(range(81), num_cells_to_clear) # Zufällige Auswahl der Zellen
    
    for cell_index in cells_to_clear:
        row = cell_index // 9
        col = cell_index % 9
        sudoku[row][col] = 0
    
    return sudoku

def solve_sudoku(sudoku):
    solve(0, 0, sudoku)

def solve(row, col, sudoku):
    if col == 9:
        col = 0
        row += 1
    
    if row == 9:
        return True
    
    if sudoku[row][col] != 0:
        return solve(row, col + 1, sudoku)
    
    for value in range(1, 10):
        if is_valid(sudoku, row, col, value):
            sudoku[row][col] = value
            if solve(row, col + 1, sudoku):
                return True
            sudoku[row][col] = 0
    
    return False

def is_valid(sudoku, row, col, value):
    if value in sudoku[row]:
        return False
    
    for r in range(9):
        if sudoku[r][col] == value:
            return False
    
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if sudoku[r][c] == value:
                return False
    
    return True

def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j, value in enumerate(row):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if value == 0:
                print('_ ', end='')
            else:
                print(value, end=' ')
        print()

sudoku = create_sudoku()
print_sudoku(sudoku)