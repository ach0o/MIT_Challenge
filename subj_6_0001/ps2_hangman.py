"""
6.0001 Introduction to Computer Science and Programming in Python

Assignment
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/)

Problem Set 2

Solved by achooan
"""

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "ps2_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    correct_letters = set(list(secret_word))
    for l in correct_letters:
        if l not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = list(secret_word)
    for index, letter in enumerate(result):
        if letter not in letters_guessed:
            result[index] = '_'

    return ''.join(result)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return ''.join(
        [l for l in string.ascii_lowercase if l not in letters_guessed])


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')

    warnings_left = 3
    guesses_left = 6
    letter_guess = set()

    while True:
        print('---' * 10)

        if is_word_guessed(secret_word, letter_guess):
            # Check if the user got the answer
            print('Congratulations, you won!')
            print('Your total score for this game is: '
                  f'{guesses_left * len(set(list(secret_word)))}')
            break

        if guesses_left <= 0:
            # Check if user has any guesses left
            print(f'Sorry, you ran out of guesses. The word was {secret_word}')
            break

        # Intro prints
        print(f'You have {warnings_left} warnings left.')
        print(f'You have {guesses_left} guesses left.')
        print(f'Available letters: {get_available_letters(letter_guess)}')

        user_guess = input('Please guess a letter: ')

        if not user_guess.isalpha() or len(user_guess) != 1:
            # Check if user guess is an alphabet
            if warnings_left > 0:
                warnings_left -= 1
                print('Oops! That is not a valid letter. You have '
                      f'{warnings_left} warnings left: '
                      f'{get_guessed_word(secret_word, letter_guess)}')
            else:
                guesses_left -= 1
                print('Oops! That is not a valid letter. You have '
                      'no warnings left so you lose one guess: '
                      f'{get_guessed_word(secret_word, letter_guess)}')

            continue

        user_guess = user_guess.lower()  # convert to lowercase

        if user_guess in letter_guess:
            # Check if the user guess was already given
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You "
                      f"now have {warnings_left} warnings: "
                      f"{get_guessed_word(secret_word, letter_guess)}")
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You "
                      "now have no warnings left so you lose one guess: "
                      f"{get_guessed_word(secret_word, letter_guess)}")

            continue

        letter_guess.add(user_guess)
        if user_guess in secret_word:
            print(f'Good guess: {get_guessed_word(secret_word, letter_guess)}')
        else:
            if user_guess in ('a', 'e', 'i', 'o', 'u'):
                guesses_left -= 3
            else:
                guesses_left -= 1
            print('Oops! That letter is not in my word: '
                  f'{get_guessed_word(secret_word, letter_guess)}')


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if len(my_word) != len(other_word.strip()):
        return False

    revealed_letters = set(list(my_word))
    for index, char in enumerate(my_word):
        if char == '_':
            if other_word[index] in revealed_letters:
                return False
        else:
            if char != other_word[index]:
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_words = [
        word for word in wordlist if match_with_gaps(my_word, word)]

    print(' '.join(possible_words) if possible_words else 'No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman! with HINTS')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')

    warnings_left = 3
    guesses_left = 6
    letter_guess = set()

    while True:
        print('---' * 10)

        if is_word_guessed(secret_word, letter_guess):
            print('Congratulations, you won!')
            print('Your total score for this game is: '
                  f'{guesses_left * len(set(list(secret_word)))}')
            break

        if guesses_left <= 0:
            print(f'Sorry, you ran out of guesses. The word was {secret_word}')
            break

        print(f'You have {warnings_left} warnings left.')
        print(f'You have {guesses_left} guesses left.')
        print(f'Available letters: {get_available_letters(letter_guess)}')

        user_guess = input('Please guess a letter: ')

        if user_guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letter_guess))

        if not user_guess.isalpha() or len(user_guess) != 1:
            if warnings_left > 0:
                warnings_left -= 1
                print('Oops! That is not a valid letter. You have '
                      f'{warnings_left} warnings left: '
                      f'{get_guessed_word(secret_word, letter_guess)}')
            else:
                guesses_left -= 1
                print('Oops! That is not a valid letter. You have '
                      'no warnings left so you lose one guess: '
                      f'{get_guessed_word(secret_word, letter_guess)}')

            continue

        user_guess = user_guess.lower()

        if user_guess in letter_guess:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You "
                      f"now have {warnings_left} warnings: "
                      f"{get_guessed_word(secret_word, letter_guess)}")
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You "
                      "now have no warnings left so you lose one guess: "
                      f"{get_guessed_word(secret_word, letter_guess)}")

            continue

        letter_guess.add(user_guess)
        if user_guess in secret_word:
            print(f'Good guess: {get_guessed_word(secret_word, letter_guess)}')
        else:
            if user_guess in ('a', 'e', 'i', 'o', 'u'):
                guesses_left -= 3
            else:
                guesses_left -= 1
            print('Oops! That letter is not in my word: '
                  f'{get_guessed_word(secret_word, letter_guess)}')


if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
