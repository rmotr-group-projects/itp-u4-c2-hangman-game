from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["test1", "test2", "test3"]


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException("The list is empty")
    return random.choice(list_of_words)


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException ('Word is empty.')
    hashed = ""
    for w in range(len(word)):
        hashed += "*"
    return hashed


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException("Answer_word or masked_word is empty.")
    if len(character) != 1:
        raise InvalidGuessedLetterException("Character is not 1.")
    if len(answer_word) != len(masked_word):
        raise InvalidWordException("Answer_word and masked_word have different length.")
    lst_pos = []

    for idx, w in enumerate(answer_word):
        if w.lower() != character.lower():
            continue
        lst_pos.append(idx)

    newmask = ""
    if lst_pos:
        for ix, m in enumerate(masked_word):
            if ix in lst_pos:
                newmask += character.lower()
            elif m != "*":
                newmask += m
            else:
                newmask += "*"
        return newmask
    return masked_word

def is_game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()

def is_game_lost(game):
    return game['remaining_misses'] <= 0

def game_finished(game):
    return is_game_lost(game) or is_game_won(game)

def guess_letter(game, letter):
    letter = letter.lower()
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()

    if game_finished(game):
        raise GameFinishedException()

    previous_masked = game['masked_word']
    new_masked = _uncover_word(game['answer_word'], previous_masked, letter)

    if previous_masked == new_masked:
        # This is a miss!
        game['remaining_misses'] -= 1
    else:
        # This is a correct guess!
        game['masked_word'] = new_masked

    game['previous_guesses'].append(letter)

    if is_game_won(game):
        raise GameWonException()

    if is_game_lost(game):
        raise GameLostException()

    # return new_masked


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
