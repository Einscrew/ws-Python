#!/usr/bin/env python3

from random import choice as random_choice
import string

draw_size = 35 # odd int
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


def print_separator() -> None:
    print('+' + '-' * draw_size + '+')


def print_text(message: str) -> None:
    print('|' + message.center(draw_size).upper() + '|')


def print_hangman(num_tries: int) -> None:
    print_text('|')
    print_text('|')

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
            firstset += ' '*2

    print_text(firstset)

    for l in initial_letters[set_size//2:]:
        if l in av_letters:
            secondset += l + ' '
        else:
            secondset += ' '*2
    print_text(secondset)

    print_separator()


def get_random_word() -> str:

    try:
        with open('words.txt', 'r') as f:
            words = f.readlines()
            print(words)
            if not words:                
                print('No words were found in the file specified')
                exit(-1)
    except FileNotFoundError:
        print('File with words not found!')
        exit(-1)

    w=[]
    for x in words[:]:
        w.append(x.strip())
    return random_choice(w).upper()

    

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
        print('\033[H\033[J')
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

        cmpWord = list(set(word_to_guess.replace(' ', '')))
        cmpWord.sort()
        guesses.sort()
        if cmpWord == guesses:
            has_won = True
        else:
            has_won = False

    print('You Won! :)' if has_won else 'You Lost! :(')


if __name__ == '__main__':
    main()
