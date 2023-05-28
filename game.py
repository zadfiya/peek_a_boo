#main file
# this function provides  of playing game
import string
import time

from grid import Grid
def main():
    size = int(input("Enter the size of the grid (2, 4, or 6): "))
    assert size in [2, 4, 6], "Invalid grid size" # test case for validation of grid size

    grid = Grid(size)
    guesses = 0
    flag = True

    while flag:
        while not grid.is_all_revealed():
            title()
            print_grid(grid, size)
            action = int(get_menu_choice())
            assert action in range(1, 6), "Invalid action"  # test case for validation of menu selection

            if action == 1:
                row1, col1 = get_cell_coordinates(size)
                row2, col2 = get_cell_coordinates(size)
                grid.reveal(row1, col1)
                grid.reveal(row2, col2)
                print_grid(grid, size)
                if grid.get_value(row1, col1) != grid.get_value(row2, col2):
                    wait()
                    # os.system("clear")
                    grid.hide(row1, col1)
                    grid.hide(row2, col2)
                guesses += 1
            elif action == 2:
                row, col = get_cell_coordinates(size)
                grid.reveal(row, col)
                grid.uncover(row, col)
                guesses += 2
            elif action == 3:
                for i in range(size):
                    for j in range(size):
                        grid.reveal(i, j)
                print_grid(grid, size)
                break
            elif action == 4:  # start new game logic
                grid = Grid(size)
                guesses = 0
            elif action == 5:
                flag = False
                break

            if grid.is_all_covered() and guesses != 0:
                minimum_possible_guesses = (size * size) // 2
                score = (minimum_possible_guesses / guesses) * 100
                print(f"Oh Happy Day. You've won!! Your score is: {score}")
            elif guesses == 0:
                continue
            else:
                print("You cheated - Loser!. Your score is 0!")



def print_grid(grid,size):
    print('   ' + '  '.join(string.ascii_uppercase[:size]))
    for i in range(grid.size):
        print(i, end="  ")
        for j in range(grid.size):
            if grid.is_revealed(i, j):
                print(grid.get_value(i, j), end="  ")
            else:
                print('X', end="  ")
        print()

def get_menu_choice():
    print('\nMenu:')
    print('1. Guess a pair')
    print('2. Manually uncover a cell')
    print('3. Reveal the entire grid')
    print('4. Start a new game')
    print('5. Quit')
    return input('Enter your choice: ')

def title():
    print("--------------------")
    print("|    PEEK-A-BOO    |")
    print("--------------------\n")

def wait():
    time.sleep(2)
def get_cell_coordinates(size):
    while True:
        cell = input("Enter cell coordinates (e.g., a0): ")
        col = ord(cell[0].lower()) - ord('a')
        row = int(cell[1])
        if 0 <= row < size and 0 <= col < size:
            return row, col
        else:
            print("Invalid cell coordinates. Try again.")

if __name__ == "__main__":
    main()