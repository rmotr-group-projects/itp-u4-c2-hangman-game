from .exceptions import *
from .exceptions import GameWonException, GameLostException
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    raise InvalidListOfWordsException


def _mask_word(word):
    if word:
        return (len(word) * '*')
    raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    if not (answer_word or masked_word):
        raise InvalidWordException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) != 1:
        raise InvalidGuessedLetterException

    result = ''
    for answer_letter in answer_word:
        if answer_letter.lower() == character.lower():
            result += character
            continue
        elif answer_letter.lower() in masked_word.lower():
            result += answer_letter
            continue

        result += '*'

    return result.lower()


def game_finished(game):
    return game_lost(game) or game_won(game)


def game_lost(game):
    return game['remaining_misses'] <= 0


def game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()


def guess_letter(game, letter):

    letter = letter.lower()
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()

    if game_finished(game):
        raise GameFinishedException()

    previous_masked = game['masked_word']
    new_masked = _uncover_word(game['answer_word'], previous_masked, letter)

    if previous_masked == new_masked:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_masked

    game['previous_guesses'].append(letter)

    if game_won(game):
        raise GameWonException()

    if game_lost(game):
        raise GameLostException()




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
