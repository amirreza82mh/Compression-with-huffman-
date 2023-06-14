from huffman import huffman, huffman_decoding
from draw_tree import draw_huffman_tree
from colorama import Fore, Back, Style
import pyfiglet
import os
import time

def clear_screen():
        if os.name == "posix":     # for linux
            os.system("clear")
        elif os.name == "nt":    # windows
            os.system("cls")


strings = []

clear_screen()

while True:
    # print title
    title_text = pyfiglet.figlet_format('namir huffman', font='slant')        
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT + title_text + Style.RESET_ALL)        

    # show options
    print()
    print('--------------------------------------')
    print('1: Enter a string')
    print('2: Show all strings')
    print('3: Show encoded and decoded string')
    print('4: draw tree')
    print('5: Exit')
    print('--------------------------------------')
    print()

    #check vaild input
    while True:
        try:
            case = int(input(Fore.YELLOW + 'Please enter a number: ' + Style.RESET_ALL))
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid integer." + Style.RESET_ALL)
            print()
            
    # Enter string
    if case == 1:
        entered_string = input(Fore.YELLOW + 'Please enter a string: ' + Style.RESET_ALL)
        strings.append(entered_string)

    # show strings
    elif case == 2:
        if not strings:
            print(Fore.RED + '\nNo strings entered yet' + Style.RESET_ALL)
        else:
            print()
            for i, string in enumerate(strings):
                print(Fore.CYAN + f'{i+1}: ' + Style.RESET_ALL + f'{string}')

    # show decoded and encoded strings
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
            encoded_string, codes, _, root = huffman(selected_string)  # decode string with huffman
            decoded_string = huffman_decoding(encoded_string, root)  # decode string
            clear_screen()
            print()
            print(Fore.LIGHTBLUE_EX + 'Encoded string: ' + Style.RESET_ALL + f'{encoded_string}') # show encode string
            print()
            for i,j in codes.items():
                print(Fore.CYAN + f'{i}: ' + Style.RESET_ALL +  f'{j}') # show codes of each char
            print()
            print(Fore.GREEN + 'Decoded string: ' + Style.RESET_ALL + f'{decoded_string}') # show decode string
            print()
            bit_of_ASCII = 8 * len(selected_string) # calculate space of ASCII code
            print(Fore.YELLOW + 'len of string: ' + Style.RESET_ALL + f'{len(selected_string)}') # show len of string
            print()
            print(Fore.CYAN + 'number of string bit by ASCII: ' + Style.RESET_ALL + f'{bit_of_ASCII}')
            print(Fore.CYAN + 'number of string bit by huffman: ' + Style.RESET_ALL + f'{len(encoded_string)}')
            print()
            precent =  100 - (len(encoded_string) / bit_of_ASCII) * 100
            print(Fore.RED + 'Ratio of Ski code to Huffman coding : ' + Style.RESET_ALL + '%2f%%' %precent) # show compression of ratio

    
    
    # draw tree
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
            draw_huffman_tree(root, dictionary)  # show graphical tree


    # exit from program
    elif case == 5:
        break
    
    else:
        print(Fore.RED + '\ninput is not accepted\n' + Style.RESET_ALL)
        time.sleep(2)
        clear_screen()
        continue
        

    input(Fore.WHITE + '\npress Enter to continue...' + Style.RESET_ALL)
    clear_screen()
