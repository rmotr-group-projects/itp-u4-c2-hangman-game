import random
import string

from .exceptions import *


# Complete with your own, just for fun :)
LIST_OF_WORDS = []
VALID_CHARS = string.ascii_letters


def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    raise InvalidListOfWordsException


def _mask_word(word):
    if word:
        return "*" * len(word)
    raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if character.lower() not in answer_word.lower():
        return masked_word

    masked_word_list = list(masked_word)

    for index, char in enumerate(answer_word):
        if char.lower() == character.lower():
            masked_word_list[index] = character.lower()

    return "".join(masked_word_list)


def guess_letter(game, letter):
    # if game already over
    if game["masked_word"] == game["answer_word"] or game["remaining_misses"] == 0:
        raise GameFinishedException

    # check guess
    new_masked_word = _uncover_word(game["answer_word"], game["masked_word"], letter)
    game["previous_guesses"] += letter.lower()

    # incorrect guess
    if game["masked_word"] == new_masked_word:
        game["remaining_misses"] -= 1

        if game["remaining_misses"] == 0:
            raise GameLostException

    # guess is correct
    game["masked_word"] = new_masked_word

    if game["masked_word"] == game["answer_word"]:
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
