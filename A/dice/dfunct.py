from random import randint
from dclass import player
import shelve

def show_menu():
    print()
    print("MENU")
    print("----")
    print('1) New Game')
    print('2) Load Game')
    print('3) Save Game')
    print('4) Roll')
    print('5) Show Stats')
    print('6) Exit')


def get_choice():
    valid_choices = ('1','2','3','4','5','6')
    show_menu()
    choice = input("Enter choice: ")
    while choice not in valid_choices:
        print('BAD INPUT. TRY AGAIN!')
        show_menu()
        choice = input("Enter choice: ")
    return choice

def new_game(players):
    players.clear()
    p1 = player()
    name = input("Enter player 1 name: ")
    p1.set_name(name)
    players.append(p1)
    p2 = player()
    name = input("Enter player 2 name: ")
    p2.set_name(name)
    players.append(p2)

def show_stats(playas):
    print()
    print('STATISTICS')
    print('----------')
    for pl in playas:
        n = pl.get_name()
        w = pl.get_wins()
        print(f"{n:30s}{w:5.0f}")

def save_game(players):
    shelf = shelve.open('players_db')
    shelf['p1'] = players[0]
    shelf['p2'] = players[1]
    shelf.close()

def load_game(players):
    players.clear()
    shelf = shelve.open('players_db')
    players.append(shelf['p1'])
    players.append(shelf['p2'])
    shelf.close()


def get_roll():
    d1 = randint(1,6)
    d2 = randint(1,6)
    d3 = randint(1,6)
    d4 = randint(1,6)
    p1roll = d1 + d2
    p2roll = d3 + d4
    return (p1roll, p2roll)

def get_winner(rolls):
    if rolls[0] > rolls[1]:
        return 0
    elif rolls[1] > rolls[0]:
        return 1
    else:
        return -1 # fake index meaning equal (to me)
