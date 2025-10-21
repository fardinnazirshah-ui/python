import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "=" * 35)
    print("         TIC TAC TOE ")
    print("=" * 35 + "\n")
    print(Fore.WHITE + "Cells are numbered 1 to 9 as shown below:\n")
    print_board([str(i) for i in range(1, 10)])
    print()

def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = " | ".join(
            (Fore.GREEN + b if b == "X"
             else Fore.MAGENTA + b if b == "O"
             else Fore.WHITE + b)
            for b in board[i:i + 3]
        )
        print(" " + row + Style.RESET_ALL)
        if i < 6:
            print(Fore.YELLOW + "-" * 11)
    print()

def check_win(board, mark):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == mark for i in combo) for combo in wins)

def get_move(board, current):
    while True:
        move = input(Fore.CYAN + f"{current}'s move (1-9): " + Style.RESET_ALL).strip()
        if not move.isdigit() or not 1 <= int(move) <= 9:
            print(Fore.RED + " Invalid input! Enter a number between 1 and 9.\n")
            continue
        pos = int(move) - 1
        if board[pos] != " ":
            print(Fore.RED + " That spot is already taken!\n")
            continue
        return pos

def play_game():
    board = [" "] * 9
    current = "X"
    clear_screen()
    print_banner()
    for turn in range(9):
        print_board(board)
        pos = get_move(board, current)
        board[pos] = current
        if check_win(board, current):
            clear_screen()
            print_board(board)
            print(Fore.GREEN + f" {current} wins the game!\n")
            break
        current = "O" if current == "X" else "X"
    else:
        clear_screen()
        print_board(board)
        print(Fore.YELLOW + "It's a draw!\n")
    time.sleep(1)

def main():
    while True:
        clear_screen()
        print_banner()
        play_game()
        again = input(Fore.CYAN + "Play again? (y/n): " + Style.RESET_ALL).strip().lower()
        if again != 'y':
            print(Fore.WHITE + "\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
