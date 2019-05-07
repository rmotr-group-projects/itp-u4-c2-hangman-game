from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['python','java','php','swift']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    else:
        return random.choice(list_of_words)


def _mask_word(word):
    if len(word)==0:
        raise InvalidWordException()
    return '*'*len(word)


def _uncover_word(answer_word, masked_word, character):
    ret = masked_word
    if len(answer_word)==0 or len(masked_word)==0 or len(answer_word) != len(masked_word):
        raise InvalidWordException()
    if len(character)>1:
        raise InvalidGuessedLetterException()
    for index,value in enumerate(answer_word):
        if character.lower() == value.lower():
            ret = ret[:index] + character.lower() + ret[index+1:]
    return ret
    


def guess_letter(game, letter):
    if game['remaining_misses'] == 0 or game['masked_word'] == game['answer_word']:
        raise GameFinishedException()
    res = _uncover_word(game['answer_word'],game['masked_word'],letter)
    game['previous_guesses'].append(letter.lower())
    if res == game['masked_word']:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = res
        if game['masked_word'] == game['answer_word']:
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
