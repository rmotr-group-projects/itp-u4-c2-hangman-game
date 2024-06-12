from .exceptions import *

import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    try:
        return random.choice(list_of_words)
    except:
        raise InvalidListOfWordsException
        
def _mask_word(word):
    if len(word) <1:
        raise InvalidWordException
    return len(word) * '*'


def _uncover_word(answer_word, masked_word, character):
    
    if answer_word == '' or masked_word =='' :
        raise InvalidWordException
    if len(character) != 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    result = ''
    character = character.lower()
    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    if character in answer_word:
        for idx, char in enumerate(answer_word):
            if char == character:
                result +=  character
            else:
                result += masked_word[idx]
    else:
        result = masked_word
    return result

def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess, #Python
        'masked_word': masked_word, #******
        'previous_guesses': [], #?
        'remaining_misses': number_of_guesses,  #5
    }

    return game

def guess_letter(game, letter):
    
    letter = letter.lower()
    game['masked_word'] = _uncover_word (game['answer_word'], game['masked_word'],letter)
    
    if game['remaining_misses'] == 0:
        raise GameFinishedException
   
    if letter not in game['masked_word'] :
        if game['masked_word'] == game['answer_word'].lower(): 
            raise GameFinishedException
        game['remaining_misses']-=1
   
    game ['previous_guesses'].append(letter)
    if game['remaining_misses'] == 0:
        raise GameLostException
    if game['masked_word'] == game['answer_word'].lower():        
        raise GameWonException

