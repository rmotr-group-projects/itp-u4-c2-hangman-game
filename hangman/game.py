import random
from .exceptions import *
import re
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Yellow', 'Blue', 'Green']


def _get_random_word(list_of_words):
    try:
        return random.choice(list_of_words)
    except:
        raise InvalidListOfWordsException


def _mask_word(word):
    masked_word = ''

    if not word:
        raise InvalidWordException
    else:
        for i in range(len(word)):
            masked_word += '*'

    return masked_word


def _uncover_word(answer_word, masked_word, character):
    guesses = 0
    answer_word = answer_word.lower()
    character = character.lower()

    unmasked_word = ''

    if not answer_word:
        raise InvalidWordException

    if len(character) > 1:
        raise InvalidGuessedLetterException

    if len(masked_word) != len(answer_word):
        raise InvalidWordException

    if character not in answer_word:
        if guesses == 0:
            guesses += 1
            return masked_word
        else:
            return unmasked_word

    elif character in answer_word:
        indices = [m.start() for m in re.finditer(character, answer_word)]

        for index, letter in enumerate(masked_word):
            if index in indices:
                unmasked_word += character
            else:
                unmasked_word += letter

    return unmasked_word


def guess_letter(game, letter):
    answer_word = game['answer_word'].lower()
    masked_word = game['masked_word']
    character = letter.lower()

    if character in answer_word:
        game['masked_word'] = _uncover_word(
            answer_word, masked_word, character)
    else:
        game['remaining_misses'] -= 1

    if game['remaining_misses'] == 0:
        raise GameLostException
    elif game['masked_word'] == answer_word:
        raise GameWonException

    game['previous_guesses'].append(character)

    return masked_word


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
