# main file
# this function provides  of playing game
from os import system
from sys import argv, platform
import string
import time

from grid import Grid


def wait():
    time.sleep(2)


def main(argv):
    # size = int(input("Enter the size of the grid (2, 4, or 6): "))
    size = int(argv)
    assert size in [2, 4, 6], "Invalid grid size"  # test case for validation of grid size

    flag = True

    while flag:
        grid = Grid(size)
        guesses = 0
        while not grid.is_all_revealed():
            title()
            print_grid(grid, size)
            action = int(get_menu_choice())
            assert action in range(1, 6), "Invalid action"  # test case for validation of menu selection

            if action == 1:
                row1, col1 = get_cell_coordinates(size)
                row2, col2 = get_cell_coordinates(size)
                while row1 == row2 and col1 == col2:
                    print("Please enter different coordinates.")
                    row2, col2 = get_cell_coordinates(size)
                grid.reveal(row1, col1)
                grid.reveal(row2, col2)
                print_grid(grid, size)
                if grid.get_value(row1, col1) != grid.get_value(row2, col2):
                    wait()
                    clear()
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
            print(f"Oh Happy Day. You've won!! Your score is: ", end="")
            print("{0:.2f}".format(score))
        elif guesses == 0:
            continue
        else:
            print("You cheated - Loser!. Your score is 0!")


def get_menu_choice():
    print('\nMenu:')
    print('1. Let me select two elements')
    print('2. Uncover one element for me')
    print('3. I give up - reveal the grid')
    print('4. New game')
    print('5. Exit\n')
    a = input('Select: ')
    if a in ["1", "2", "3", "4", "5"]:
        return int(a)
    else:
        return get_menu_choice()


def print_grid(grid, size):
    horizona_line = '  '.join(['[' + chr(i + 65) + ']' for i in range(size)])
    print('    ' + horizona_line)
    for i in range(grid.size):
        print("[",end="")
        print(i, end="]   ")
        for j in range(grid.size):
            if grid.is_revealed(i, j):
                print(grid.get_value(i, j), end="   ")
            else:
                print('X', end="   ")
        print()


def title():
    print("\n--------------------")
    print("|    PEEK-A-BOO    |")
    print("--------------------\n")


def clear():
    if platform.startswith("win32"):
        system("cls")
    else:
        system("clear")
    # sys.platform.startswith()
    # check and make call for specific operating system
    # _ = call('clear' if os.name == 'posix' else 'cls')


def get_cell_coordinates(size):
    while True:
        cell = input("Enter cell coordinates (e.g., a0): ")
        if len(list(cell)) == 2 and list(cell)[1].isdigit():
            col = ord(cell[0].lower()) - ord('a')
            row = int(cell[1])
            if 0 <= row < size and 0 <= col < size:
                return row, col
            elif not (0 <= row < size) and 0 <= col < size:
                print(f"Input Error: row entry is out of range for this grid. Please try again between 0 to {size}.")
            elif not (0 <= col < size):
                print(
                    f"Input Error: column entry is out of range for this grid. Please try again between A to {chr(size + ord('a') - 1).upper()}.")
            else:
                print("Input Error: Both row and column entry out of range for this grid. Please try again.")
        else:
            print("Input Error: Invalid Input, Please try again.")


if __name__ == "__main__":
    main(argv[1])
