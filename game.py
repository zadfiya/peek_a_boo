#main file
# this function provides  of playing game
def main():
    print("Peek_a_Boo")

def get_menu_choice():
    print('\nMenu:')
    print('1. Guess a pair')
    print('2. Manually uncover a cell')
    print('3. Reveal the entire grid')
    print('4. Start a new game')
    print('5. Quit')
    return input('Enter your choice: ')

if __name__ == "__main__":
    main()