# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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
    # wordlist: list of stringss
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
    a = ''
    for char in secret_word:
        if char in letters_guessed:
            a += char
    if len(a) == len(secret_word):
        return True
    return False





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    a = ''
    for char in secret_word:
        if char in letters_guessed:
            a += char
        else:
            a += '_ '
    return a



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    a = string.ascii_lowercase
    for i in letters_guessed:
        if i in a:
            a = a.replace(i, '')
    return a

def check_user_input(user):
    a = string.ascii_lowercase
    if user in a:
        return True
    return False




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
    a = len(secret_word)
    guesses_remaining = 6
    c = []
    warning = 3
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    print('Welcome to Hangman!')
    print(f'I am thinking of a word that is {a} letters long')
    print('--------------------------------------------------------')
    while guesses_remaining > 0:
        if warning == 1:
            print(f'You have 1 warning left')
        else:
            print(f'You have {warning} warnings left')
        print(f'You have {guesses_remaining} guesses left')
        print('available letters:', get_available_letters(c))
        user_guess = input('Please guess a letter\n> ').lower()
        if user_guess in c:
            warning -= 1
            print(f'Oops! You have already guessed that letter. You now have {warning} warnings left')
            if warning < 1:
                guesses_remaining -= 1
                print(f'You have lost a guess! You now have {guesses_remaining} guesses left')
                warning = 3
                continue
            continue
        if not check_user_input(user_guess):
            warning -= 1
            print(f'OOps! That is not a valid letter.You have {warning} warnings left', get_guessed_word(secret_word, c))
            print('--------------------------------------------------------')
            if warning < 1:
                print('You lost a guess!')
                guesses_remaining -= 1
                print('--------------------------------------------------------')
                warning = 3
                continue
            continue
        c.append(user_guess)
        if user_guess in secret_word:
            print('Good guess!', get_guessed_word(secret_word, c))
            print('--------------------------------------------------------')
            if is_word_guessed(secret_word, c):
                print('Congratulations! You Won')
                print(f'Your score = {guesses_remaining * len(secret_word)}')
                exit()
            continue
        else:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, c))
            if user_guess in vowels:
                guesses_remaining -= 2
                continue
        guesses_remaining -= 1
        print('--------------------------------------------------------')
    print(f'You lost! try again!\nThe word was {secret_word}')

# a = choose_word(wordlist)
# hangman(a)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    ###PROBLEM WITH CODE, REPEATING LETTERS DONT WORK, SEE PRINT STATEMENT
#     my_word = my_word.replace(' ', '')
#     if not len(my_word) == len(other_word):
#         return False
#     for i in my_word:
#         print(i)
#         for char in other_word:
#             print(char)
#             if i == char:
#                 other_word = other_word.replace(char, '')
#                 break
#             elif i == '_':
#                 other_word = other_word.replace(char, '')
#                 break
#             else:
#                 return False
#     return True
#
# print(match_with_gaps('app_ _ ', 'apple'))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
#     # pass
#
#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
#
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
