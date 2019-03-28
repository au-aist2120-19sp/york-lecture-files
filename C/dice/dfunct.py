import shelve
from random import randint
from dclass import player

def show_menu():
    print()
    print('MENU')
    print('----')
    print('1) New Game')
    print('2) Load Game')
    print('3) Save Game')
    print('4) Roll')
    print('5) Show Stats')
    print('6) Exit')


def get_choice():
    valid_choices = ('1','2','3','4','5','6')

    show_menu()
    choice = input('Enter choice: ')

    while choice not in valid_choices:
        print("You have chosen poorly!")
        show_menu()
        choice = input('Enter choice: ')
    return choice




def new_game(playas):
    playas.clear()
    p1 = player()
    name = input('Enter player 1 name: ')
    p1.set_name(name)
    playas.append(p1)
    p2 = player()
    name = input('Enter player 2 name: ')
    p2.set_name(name)
    playas.append(p2)



def show_stats(playas):
    print()
    print('STATISTICS')
    print('----------')
    for pl in playas:
        name = pl.get_name()
        wins = pl.get_wins()
        print(f'{name:30s}{wins:5.0f}')


def save_game(playas):
    shelf = shelve.open('players_db')
    shelf['p1'] = playas[0]
    shelf['p2'] = playas[1]
    shelf.close()


def load_game(playas):
    playas.clear()
    shelf = shelve.open('players_db')
    playas.append(shelf['p1'])
    playas.append(shelf['p2'])
    shelf.close()


def get_rolls():
    d1 = randint(1,6)
    d2 = randint(1,6)
    d3 = randint(1,6)
    d4 = randint(1,6)
    r1 = d1 + d2
    r2 = d3 + d4
    return (r1,r2)


def get_winner(rolls):
    if rolls[0] > rolls[1]:
        return 0
    elif rolls[1] > rolls[0]:
        return 1
    else:
        return -1
        
