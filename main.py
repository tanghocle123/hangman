""" This is based on https://repl.it/@awdimmick/Hangman"""
import random

word_file = 'google-10000-english.txt'
hangman = [
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""
]
def show_hangman(wrong_guesses):
    print(hangman[wrong_guesses])
def letter_is_correct(letter, guess_word):

    if letter.lower() in guess_word:
        print('Good guess!')
        return True
    else:
        print('Nope, try again!')
        return False
def show_guessed_letters(guesses):
    print("You have guessed the following letters:")
    output = ""
    for letter in guesses:
        output += letter + ", "
    print(output + "\n")
def load_word(a = word_file):
    with open(a, 'r') as f:
        word_list = f.readlines()
    return word_list
def get_random_word():
    word_list = load_word()
    rand_word = random.choice(word_list)
    return rand_word
def show_blanks_and_letters(guessed_letter, guess_word):
    out_put = ''
    for letter in guess_word:
        if letter in guessed_letter:
            out_put += letter
        else:
            out_put += '-'
    print('Word to guess: {}'.format(out_put))
def is_game_won(correct_letters, guess_word):
    for letter in guess_word:
        if letter not in correct_letters:
            return False

    print("\nYOU WIN!\n")
    return True
def play_again():
    print('\n Press two times on any letters to play again \n')
    input()
    input()
    
def get_player_name():
    """ Get player's name and welcome him"""
    player_name = input('What is your name?: ')
    print('Welcome {}'.format(player_name))
def introduction():
    print('This is a game of guessing a word or phrase one letter at a time')
    print('You have a maximum of 7 wrong guesses')
def game_end(wrong_guesses, guesses):
    if wrong_guesses == guesses:
        print('Unfortunately. You lose!!')
        return True
    else:
        return False
def clear_screen():
    print("\n" * 40)
def game_begin():
    wrong_guesses = 0
    guesses = 11
    guess_word = get_random_word()
    guessed_letter = []
    correct_letters = []
    clear_screen()
    introduction()
    get_player_name()
    
    while not is_game_won(correct_letters, guess_word) and not game_end(wrong_guesses,guesses):
        show_hangman(wrong_guesses)
        show_blanks_and_letters(guessed_letter, guess_word)
        show_guessed_letters(guessed_letter)
        guess = input("Enter a letter to guess: ").lower()
        
        if guess in guessed_letter:
            print('You\'ve alreay guessed that letter')
        else:
            guessed_letter.append(guess)
            if letter_is_correct(guess, guess_word):
                correct_letters.append(guess)
            else:
                wrong_guesses += 1
                
    print("Game finished! The guess word was:", guess_word)
    
game_begin()
        
    
    
    




