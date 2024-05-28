# code of Game
from random import shuffle
def shuffle_list(my_list=['','','O']):
    shuffle(my_list)
    return my_list

def player_guess():
    guess=''
    while guess not in ('0','1','2'):
        guess=input('print a number 0,1 or 2')
    return int(guess)

def check_game(my_list,guess):
    if my_list[guess]=='O':
        print('Correct!!!')
    else:
        print('Wrong')
        print(my_list) 
        
# call this to Run the Game 
mixed_list=shuffle_list()
guess=player_guess()
check_game(mixed_list,guess)