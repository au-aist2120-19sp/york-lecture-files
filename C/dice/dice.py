from dfunct import get_choice
from dfunct import new_game
from dfunct import show_stats
from dfunct import load_game
from dfunct import save_game
from dfunct import get_rolls
from dfunct import get_winner

players = []

while True:
    choice = get_choice()

    if choice == '1':
        new_game(players)
    elif choice == '2':
        load_game(players)
    elif choice == '3':
        save_game(players)
    elif choice == '4':
        rolls = get_rolls()
        winner = get_winner(rolls)
        if winner == -1:
            print('It was a tie!')
        else:
            pl = players[winner]
            name = pl.get_name()
            wins = pl.get_wins()
            print(name + " wins!!")
            wins += 1
            pl.set_wins(wins)
    elif choice == '5':
        show_stats(players)
    elif choice == '6':
        break

print("See ya, woudn't want to be ya.")
