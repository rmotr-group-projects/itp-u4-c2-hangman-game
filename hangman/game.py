from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['rmotr', 'sonia', 'des', 'pizza', 'wine', 'french']

# you are going to have to import the random module
def _get_random_word(list_of_words):
    # Use try and except to raise an exception if 
    # the list of words is invalid
    try:
        return random.choice(list_of_words)
    except:
        raise InvalidListOfWordsException

# has astrixes to that you need to replace word with.
def _mask_word(word):
    
    # Add exception if the length of the word is 0
    if len(word) == 0:
        raise InvalidWordException()
    
    # Otherwise create a masked word
    empty_string = ''
    for letter in range(len(word)):
        empty_string += '*'
    return(empty_string)

# this will be if a user guesses the correct letter you will need 
# to uncover the letter.
# REMEMBER that if a letter appears twice, you need to uncover both
# InvalidWordException can fail for different things, eg empty, diferent
# lengths
def _uncover_word(answer_word, masked_word, character):
    new_masked_word = ''
    if len(answer_word) != len(masked_word) or answer_word == '' or  masked_word == '':
        raise InvalidWordException()
    if len(character) == 0 or len(character) > 1:
        raise InvalidGuessedLetterException()
    
    # Create a variable that turns all letters into lowercase
    lower_char = character.lower()
    results = masked_word 

    for i, letter in enumerate(answer_word.lower()):
        if letter == lower_char:
            # This splits the word so that we can replace with a character surorunded by *'s'
            results = results[:i] + lower_char + results[i + 1:]

    return results
    
def guess_letter(game, letter):
    
    # Add a clause in case word already guessed
    if not '*' in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException

    temp_answer_word = game['answer_word']
    temp_masked_word = game['masked_word']
    uncovered_word = _uncover_word(temp_answer_word, temp_masked_word, letter)

    # This stops a guess being subtracted if correct guess
    if uncovered_word == game['masked_word']:
        game['remaining_misses'] -= 1

    game['masked_word'] = uncovered_word
    game['previous_guesses'].append(letter.lower())

    # If no more *'s then game won
    if not '*' in game['masked_word']:
        raise GameWonException
        
    # If used all guesses then game lost
    if game['remaining_misses'] == 0:
        raise GameLostException
           
# Do not need to do anything with this.  This is the game.
def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    # See this is the function above (at the top)
    word_to_guess = _get_random_word(list_of_words)
    # this is a function I will create which will return astrixes 
    # so the user cannot see it.
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        # we are adding the previous guesses in here
        'previous_guesses': [],
        # this will decrease as the user make more guesses
        'remaining_misses': number_of_guesses,
    }

    return game
