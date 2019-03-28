from dfunct import get_choice
from dfunct import show_stats
from dfunct import new_game
from dfunct import save_game
from dfunct import load_game
from dfunct import get_roll
from dfunct import get_winner

players = []
while True:
    choice = get_choice()

    if choice == "1":
        new_game(players)
    elif choice == "2":
        load_game(players)
    elif choice == "3":
        save_game(players)
    elif choice == "4":
        rolls = get_roll()
        winner = get_winner(rolls)
        if winner < 0:
            print("ITS A TIE")
        else:
            pw = players[winner]
            name = pw.get_name()
            print(name + " WINS!!!")
            wins = pw.get_wins()
            wins += 1
            pw.set_wins(wins)
    elif choice == "5":
        show_stats(players)
    elif choice == "6":
        break

print("See ya!!")
