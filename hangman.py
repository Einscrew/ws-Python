#!/usr/bin/env python3

import os
import random
import string


def printLine():
    print('+---------------------------------+')


def printText(msg, printTop=False, printBottom=False):

    if printTop:
        printLine()

    message = msg.upper()

    begin = True

    for i in range(len(message), 33):

        if begin is True:
            message = " " + message
        else:
            message = message + " "

        begin = not begin

    print('|' + message + '|')

    if printBottom:
        printLine()


def printHangman(num_tries):
    printText('|')
    printText('|')

    if num_tries >= 1:
        printText('O')
    else:
        printText('')

    if num_tries == 2:
        printText('/  ')
    elif num_tries == 3:
        printText('/| ')
    elif num_tries >= 4:
        printText('/|\\')
    else:
        printText('')

    if num_tries >= 5:
        printText('|')
    else:
        printText('')

    if num_tries == 6:
        printText('/  ')
    elif num_tries >= 7:
        printText('/ \\')
    else:
        printText('')

    # close box
    printText('')
    printLine()


def printAvailableLetters(av_letters):

    letters = string.ascii_uppercase

    s_1 = ''
    for l in letters[:13]:
        if l in av_letters:
            s_1 += l + " "
        else:
            s_1 += "  "

    s_2 = ''
    for l in letters[13:]:
        if l in av_letters:
            s_2 += l + " "
        else:
            s_2 += "  "

    printText(s_1)
    printText(s_2)

    printLine()


def getRandomWord():
    try:
        with open('words.txt', 'r') as f:
            words = f.readlines()
    except FileNotFoundError:
        print('File with words not found!')
        exit(-1)

    words = [x.strip() for x in words]
    return random.choice(words).upper()


def printGuesses(word, guesses):

    s = ''
    for x in word:
        if x in guesses:
            s += x + ' '
        else:
            s += '_ '

    printText(s)
    printLine()


def getLetter(av_letters):

    letter = input("Insert one letter: ")
    letter = letter.upper()

    while not len(letter) == 1 or letter not in av_letters or letter not in string.ascii_uppercase:
        print("Insert one available letter!")
        letter = input("Insert one letter: ").upper()

    return letter


def checkVictory(word, guesses):
    w = set(word)
    g = guesses

    return sorted(w) == sorted(g)


def runGame():
    # os.system('cls')  # on windows
    os.system('clear')

    available_letters = list(string.ascii_uppercase)
    wordToGuess = getRandomWord()
    guesses = list()
    print(wordToGuess)
    wrongTries = 0
    victory = False

    while wrongTries < 8 and not victory:

        os.system('clear')
        printText('hangman', True, True)
        printHangman(wrongTries)
        printText('Your guess...', False, False)
        printGuesses(wordToGuess, guesses)
        printText('Available letters', False, False)
        printAvailableLetters(available_letters)
        letter = getLetter(available_letters)
        available_letters.remove(letter)

        if letter not in wordToGuess:
            wrongTries += 1
        else:
            guesses.append(letter)

        victory = checkVictory(wordToGuess, guesses)
#        if checkVictory(wordToGuess, guesses):
#            victory = True
#            break

    os.system('clear')
    printText('hangman', True, True)
    printHangman(wrongTries)
    printText('Your guess...', False, False)
    printGuesses(wordToGuess, guesses)
    printText('Available letters', False, False)
    printAvailableLetters(available_letters)

    if victory:
        print("Congratz!")
    else:
        print("Better luck next time...")


if __name__ == "__main__":
    runGame()
