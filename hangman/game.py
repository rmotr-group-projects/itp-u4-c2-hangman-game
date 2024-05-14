from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['this', 'is', 'a', 'sample', 'set', 'of', 'words', 'aaaaa', 'TESTING']


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)

def _mask_word(word):
    if (len(word) < 1):
        raise InvalidWordException('The word provided is invalid.')
    return ('*' * len(word))


def _uncover_word(answer_word, masked_word, character):
    guessed = []
    if (len(answer_word) < 1):
        raise InvalidWordException
    if len(character) != 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    for posistion, letter in enumerate(answer_word):
        if letter.lower() == character.lower():
            guessed.append(posistion)
            masked_word = masked_word[:posistion] + character.lower() + masked_word[posistion + 1:]
    return masked_word


def guess_letter(game, letter):
    if ( game['answer_word'] == game['masked_word'] ) or ( game['remaining_misses'] == 0 ):
        raise GameFinishedException
    try:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter.lower())
        game['previous_guesses'].append(letter.lower())
        if letter.lower() not in game['answer_word'].lower():
            game['remaining_misses'] -= 1
    except Exception as e:
        raise e
    if game['answer_word'] == game['masked_word']:
        raise GameWonException
    if game['remaining_misses']  == 0:
        raise GameLostException


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
