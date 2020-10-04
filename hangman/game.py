from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return list_of_words[random.randint(0,len(list_of_words) -1)]


def _mask_word(word):
    if word:
        return '*' * len(word)
    else:
        raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    res = ''
    for index,letter in enumerate(answer_word.lower()):
        if letter.lower() == character.lower():
            res+= character.lower()
        else:
            res += masked_word[index]
    return res


def guess_letter(game, letter):
    if (game['remaining_misses'] < 1) or (game['masked_word'] == game['answer_word']):
            raise GameFinishedException
    attempt = _uncover_word(game['answer_word'], game['masked_word'],letter)
    game['previous_guesses'].append(letter.lower())
    if attempt == game['masked_word']:
        game['remaining_misses']-=1 
        if game['remaining_misses'] < 1:
            raise GameLostException
    else:
        game['masked_word'] = attempt
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
