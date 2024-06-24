from .exceptions import *
#from exceptions import * 
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['croatia', 'denmark', 'spain', 'russia']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    else:
        return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    else:
        masked_st_arr = ['*' for x in list(word)]
        return ''.join(masked_st_arr).lower()
        

def _uncover_word(answer_word, masked_word, character):
    if answer_word == '' or masked_word == '':
        raise InvalidWordException('You must enter both words')
    if len(character) > 1:
        raise InvalidGuessedLetterException('One only please')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Same length for first two please')
    
    rt_arr = []
    for i in range(len(masked_word)):
        if character.lower() == answer_word[i].lower():
            rt_arr.append(character.lower())
        else:
            rt_arr.append(masked_word[i].lower())
    return ''.join(rt_arr)


def guess_letter(game, letter):
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] < 1:
        raise GameFinishedException("It\'s over amigo")
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    if letter.lower() not in game['previous_guesses']:
        game['previous_guesses'].append(letter.lower())
    if letter.lower() not in game['masked_word']:
        game['remaining_misses'] -= 1
    if game['masked_word'] == game['answer_word']:
        raise GameWonException('Well Done')
    if game['remaining_misses'] == 0:
        raise GameLostException('Out of Guesses / Lo Siento')

    
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

