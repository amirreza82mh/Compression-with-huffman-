from huffman import huffman, huffman_decoding
from draw_tree import draw_huffman_tree
from colorama import Fore, Back, Style
import pyfiglet
import os
import time

def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")


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
    print('4: draw tree')
    print('5: Exit')
    print('--------------------------------------')
    print()

    while True:
        try:
            case = int(input(Fore.YELLOW + 'Please enter a number: ' + Style.RESET_ALL))
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid integer." + Style.RESET_ALL)
            print()
            

    if case == 1:
        entered_string = input(Fore.YELLOW + 'Please enter a string: ' + Style.RESET_ALL)
        strings.append(entered_string)

    elif case == 2:
        if not strings:
            print(Fore.RED + '\nNo strings entered yet' + Style.RESET_ALL)
        else:
            print()
            for i, string in enumerate(strings):
                print(Fore.CYAN + f'{i+1}: ' + Style.RESET_ALL + f'{string}')

    elif case == 3:
        if not strings:
            print(Fore.RED + '\nNo strings entered yet' + Style.RESET_ALL)
        else:
            print(Fore.LIGHTGREEN_EX + '\nSelect a string to encode and decode:' + Style.RESET_ALL)
            for i, string in enumerate(strings):
                print(Fore.CYAN + f'{i+1}:' + Style.RESET_ALL + f'{string}')
            
            while True:
                try:
                    selected_string_index = int(input(Fore.LIGHTBLUE_EX + '\nEnter a number: ' + Style.RESET_ALL))
                    break
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a valid integer." + Style.RESET_ALL)

            selected_string = strings[selected_string_index - 1]
            encoded_string, codes, _, root = huffman(selected_string)
            decoded_string = huffman_decoding(encoded_string, root)
            clear_screen()
            print()
            print(Fore.LIGHTBLUE_EX + 'Encoded string: ' + Style.RESET_ALL + f'{encoded_string}')
            print()
            for i,j in codes.items():
                print(Fore.CYAN + f'{i}: ' + Style.RESET_ALL +  f'{j}')
            print()
            print(Fore.GREEN + 'Decoded string: ' + Style.RESET_ALL + f'{decoded_string}')
    
    elif case == 4:
        if not strings:
            print(Fore.RED + '\nNo strings entered yet' + Style.RESET_ALL)
        else:
            print(Fore.LIGHTGREEN_EX + '\nSelect a string to encode and decode:' + Style.RESET_ALL)
            for i, string in enumerate(strings):
                print(Fore.CYAN + f'{i+1}:' + Style.RESET_ALL + f'{string}')
            while True:
                try:
                    selected_string_index = int(input(Fore.LIGHTBLUE_EX + '\nEnter a number: ' + Style.RESET_ALL))
                    break
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a valid integer." + Style.RESET_ALL)
            selected_string = strings[selected_string_index - 1]
            _, _, dictionary, root = huffman(selected_string)  
            draw_huffman_tree(root, dictionary)          

    elif case == 5:
        break
    
    else:
        print(Fore.RED + '\ninput is not accrpted\n' + Style.RESET_ALL)
        time.sleep(2)
        clear_screen()
        continue
        

    input(Fore.WHITE + '\npress Enter to continue...' + Style.RESET_ALL)
    clear_screen()
