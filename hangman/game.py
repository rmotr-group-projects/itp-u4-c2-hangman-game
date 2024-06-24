from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    try:
        return random.choice(list_of_words)
    except:
        raise InvalidListOfWordsException()


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException()
    size = len(word)
    word = '*' * size
    return word


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException()
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    new_masked_word = ''
    for idx, char in enumerate(answer_word.lower()):
        if masked_word[idx] != '*':
            new_masked_word += masked_word[idx]
        elif character.lower() == char:
            new_masked_word += char
        else:
            new_masked_word += '*'
    
    return new_masked_word


def guess_letter(game, letter):
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException()
    
    orig_masked_word = game['masked_word']
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    if orig_masked_word == game['masked_word']:
        game['remaining_misses'] -= 1
    game['previous_guesses'].append(letter.lower())
    
    if game['answer_word'] == game['masked_word']:
        raise GameWonException()
    if game['remaining_misses'] == 0:
        raise GameLostException()
    return game


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
