'''
class InvalidListOfWordsException(Exception):
    pass


class InvalidWordException(Exception):
    pass


class GameWonException(Exception):
    pass


class GameLostException(Exception):
    pass


class GameFinishedException(Exception):
    pass


class InvalidGuessedLetterException(Exception):
    pass
'''
from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['apple', 'banana', 'mango', 'lemon', 'strawberry']

import random
def _get_random_word(list_of_words):
    if list_of_words==[]:
        raise InvalidListOfWordsException("Cannot pass an empty list")
    else:
        x=random.choice(list_of_words)
        return x

def _mask_word(word):
    if not word:
        raise InvalidWordException('Word cannot be missing')
    return '*'*len(word)

def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException('Word cannot be missing')
    elif len(character)>1:
        raise InvalidGuessedLetterException('Can only guess 1 character')
    elif len(answer_word)!=len(masked_word):
        raise InvalidWordException("Length of answer not equal to length of masked")
    elif character.upper() in answer_word.upper():
        test_list=[i for i,n in enumerate(answer_word.upper()) if (n==character.upper())]
        masked_list=list(masked_word)
        for index_number in test_list:
            masked_list[index_number]=character.lower()
        final_masked=''.join(masked_list)
        return final_masked
    elif character.upper() not in answer_word.upper():
        return masked_word

def guess_letter(game, letter):
    if game['masked_word'] != game['answer_word'] and game['remaining_misses'] >0:
        masked_word = game['masked_word']
        answer_word = game['answer_word']
        character = letter
        new_masked = _uncover_word(answer_word, masked_word, character)
        game['previous_guesses']+=letter.lower()     
        if new_masked == game['masked_word']:
            game['remaining_misses']-=1
        game['masked_word'] = new_masked
        if new_masked == answer_word:
            raise GameWonException("Game Won!")
        if game['remaining_misses'] == 0 and new_masked != answer_word:
            raise GameLostException("Game lost!")
        return game
    else:
        raise GameFinishedException("Game is finished.")

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


