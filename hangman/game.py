from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = [
    'apple',
    'banana',
    'orange',
    'tangerine',
    'grape',
    'pear',
    'kiwi',
    'strawberry',
    'blueberry',
    'watermelon'
]

# _get_random_word recieves a list or words to pick one randomly. If the list is empty, raises an exception.
def _get_random_word(list_of_words):
    if len(list_of_words) > 0:
        return random.choice(list_of_words)
    else:
        raise InvalidListOfWordsException

# _mask_word recieves a string and returns the word masked or raises an exception if the string is empty.
def _mask_word(word):
    n = len(word)
    if n > 0:
        mask = '*' * n
        return mask
    else:
        raise InvalidWordException

# _uncover_word recieves the word to answer, the mask and a character picked by the user.
def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0 or len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    if len(character) > 1:
        raise InvalidGuessedLetterException  
    
    if character.lower() in answer_word.lower():
        list_from_word = list(answer_word)
        pos = 0
        while list_from_word[pos] != character and pos < len(list_from_word):
            pos += 1
        list_from_mask = list(masked_word)
        list_from_mask[pos] = character
        masked_word = ''.join(list_from_mask)
        return masked_word
    else:
        return masked_word
                    
                    
def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
