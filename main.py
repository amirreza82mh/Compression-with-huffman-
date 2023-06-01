from huffman import huffman, huffman_decoding
from colorama import Fore, Back, Style
import pyfiglet
import os

def clear_screen():
        if os.name == "posix":
            # For UNIX-based systems (Linux, macOS)
            os.system("clear")


strings = []

clear_screen()

while True:
    title_text = pyfiglet.figlet_format('namir huffman', font='slant')
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT + title_text + Style.RESET_ALL)
    print()
    print('--------------------------------------')
    print('1: Enter a string')
    print('2: Show all strings')
    print('3: Show encoded and decoded string')
    print('4: Exit')
    print('--------------------------------------')
    print()

    case = int(input('Please enter a number: '))

    if case == 1:
        entered_string = input('Please enter a string: ')
        strings.append(entered_string)
    elif case == 2:
        if not strings:
            print('No strings entered yet')
        else:
            for i, string in enumerate(strings):
                print(f'{i+1}: {string}')
    elif case == 3:
        if not strings:
            print('No strings entered yet')
        else:
            print('Select a string to encode and decode:')
            for i, string in enumerate(strings):
                print(f'{i+1}: {string}')
            selected_string_index = int(input('Enter a number: '))
            selected_string = strings[selected_string_index - 1]
            encoded_string, root = huffman(selected_string)
            decoded_string = huffman_decoding(encoded_string, root)
            print(f'Encoded string: {encoded_string}')
            print(f'Decoded string: {decoded_string}')
    elif case == 4:
        break

    input('\npress Enter to continue...')
    clear_screen()
