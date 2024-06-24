from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    try:
        return list_of_words[random.randint(0,len(list_of_words) - 1)]
    except:
        raise InvalidListOfWordsException


def _mask_word(word):
    
    if len(word) == 0:
        raise InvalidWordException()

    results = ''
    for x in word:
        results += '*'

    return results


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) != len(masked_word) or answer_word == '' or  masked_word == '':
        raise InvalidWordException
    if len(character) != 1:
        raise InvalidGuessedLetterException

    lower_char = character.lower()
    results = masked_word 
    
    for i, letter in enumerate(answer_word.lower()):
        if letter == lower_char:
            results = results[:i] + lower_char + results[i + 1:]
  
    return results


def guess_letter(game, letter):
    
    if not '*' in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
        
    if len(letter) != 1:
        raise InvalidGuessedLetterException
        
    temp_answer_word = game['answer_word']
    temp_masked_word = game['masked_word']
    uncovered_word = _uncover_word(temp_answer_word, temp_masked_word, letter)
    
    if uncovered_word == game['masked_word']:
        game['remaining_misses'] -= 1
        
    game['masked_word'] = uncovered_word
    game['previous_guesses'].append(letter.lower())
    
    if not '*' in game['masked_word']:
        raise GameWonException
    if game['remaining_misses'] == 0:
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
