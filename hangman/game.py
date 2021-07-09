import random
from .exceptions import *


# Complete with your own, just for fun :)
LIST_OF_WORDS = ['test', 'python', 'rmotr']

def _check_if_game_won(game):
    if game['masked_word'].lower() == game['answer_word'].lower():
        raise GameWonException
        
def _check_if_game_lost(game):
    game['remaining_misses'] -= 1
    if game['remaining_misses'] == 0:
        raise GameLostException

def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException('Please provide a single or comma separated list of words:')
    else:
        return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException()
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()
    elif len(character) > 1:
        raise InvalidGuessedLetterException()
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException()
    
    index = 0
    new_masked = ''
    while index < len(answer_word):
        if masked_word[index].lower() != '*':
            new_masked += masked_word[index].lower()
            index += 1
            continue
        if character.lower() == answer_word[index].lower():
            new_masked += character.lower()
        else:
            new_masked += '*'
        index += 1
    return new_masked


def guess_letter(game, letter):
    if letter in game['answer_word'] and letter not in game['previous_guesses']:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    _check_if_game_won(game)
    _check_if_game_lost(game)
        
        
        
        
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