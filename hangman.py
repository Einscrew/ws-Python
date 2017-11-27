#!/usr/bin/env python3
from os import system
from random import choice as random_choice
import string

DRAW_SIZE = 35 # odd int


def print_separator() -> None:
    print('+' + '-' * DRAW_SIZE + '+')


def print_text(message: str) -> None:
    print('|' + message.center(DRAW_SIZE).upper() + '|')


def print_hangman(num_tries: int) -> None:
    print_text('|')
    print_text('|')
    limbs = ['O', ' | ', '/| ', '/|\\', '|', '/  ', '/ \\']
    bodyCombinations = {
        1: [0],
        2: [0, 1],
        3: [0, 2],
        4: [0, 3],
        5: [0, 3, 4],
        6: [0, 3, 4, 5],
        7: [0, 3, 4, 6]
    }

    body = bodyCombinations.get(num_tries, [])

    for i in range(5):
        if i < len(body):
            print_text(limbs[body[i]])
        else:
            print_text('')

    print_separator()


def print_available_letters(initial_letters: list, av_letters: list) -> None:
    
    print_text('Available Letters')
    firstset=''
    secondset=''
    set_size = len(initial_letters)

    for l in initial_letters[:set_size//2]:
        if l in av_letters:
            firstset += l + ' '
        else:
            firstset += ' ' * 2

    print_text(firstset)

    for l in initial_letters[set_size//2:]:
        if l in av_letters:
            secondset += l + ' '
        else:
            secondset += ' ' * 2
    print_text(secondset)

    print_separator()


def get_random_word() -> str:

    try:
        with open('words.txt', 'r') as f:
            words = f.readlines()
            if not words:                
                print('No words were found in the file specified')
                exit(-2)
    except FileNotFoundError:
        print('File with words not found!')
        exit(-1)
    
    words = [w.strip() for w in words]
    
    return random_choice(words).upper()

    

def print_guesses(word: str, guesses: list) -> None:
    
    guess_set = ''
    for c in word:
        if c in guesses:
            guess_set += c + ' '
            pass
        elif c == ' ':
            guess_set += (' '*2);
            pass
        else:
            guess_set += '_ '

    print_text(guess_set)
    print_separator()


def get_letter(available_letters: list) -> str:
    while True:
        letter = input('Insert one available letter: ').upper()
        if len(letter) == 1 and letter in available_letters:
            return letter


def main() -> None:
    initial_letters = list(string.ascii_uppercase)
    available_letters = initial_letters.copy()
    word_to_guess = get_random_word()
    guesses = list()
    failed_attempts = 0
    has_won = False

    while failed_attempts <= 7:
        system('clear') #cls in windows
        print_separator()
        print_text('Hangman')
        print_separator()
        print_hangman(failed_attempts)
        print_text('Your Guess...')
        print_guesses(word_to_guess, guesses)
        print_available_letters(initial_letters, available_letters)
        if has_won or failed_attempts == 7:
            break
        letter = get_letter(available_letters)
        available_letters.remove(letter)

        if letter in word_to_guess:
            guesses.append(letter)
        else:
            failed_attempts += 1

        cmpWord = set(word_to_guess.replace(' ', ''))
        has_won = cmpWord == set(guesses)
        
    print_text('The correct word is: {}'.format(word_to_guess))
    print_separator()
    print_text('You Won! :)' if has_won else 'You Lost! :(') #surprise
    print_separator()


if __name__ == '__main__':
    main()
