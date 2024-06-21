from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException
    return "*" * len(word)


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException
    if len(character) != 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException

    updated_masked_word = ''
    for index, answer_character in enumerate(answer_word):
        if character.lower() == answer_character.lower():
            updated_masked_word += character.lower() #answer_character
            continue
        updated_masked_word += masked_word[index]
    return updated_masked_word


def guess_letter(game, letter):
    if game['remaining_misses'] <= 0:
        raise GameFinishedException
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException
    if letter in game['previous_guesses']:
        return

    updated_masked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter.lower())
    if updated_masked_word == game['masked_word']:
        game['remaining_misses'] -= 1
        if game['remaining_misses'] <= 0:
            raise GameLostException
    else:
        game['masked_word'] = updated_masked_word

    if game['masked_word'] == game['answer_word']:
            raise GameWonException


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
