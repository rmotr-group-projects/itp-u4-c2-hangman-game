from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException
        
    masked_word = ''
    for i in range(len(word)):
        masked_word += '*'
    return masked_word


def _uncover_word(answer_word, masked_word, character):

    if not answer_word or not masked_word:
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
        
    result = list(masked_word)
    
    try:
        for index, char in enumerate(list(answer_word)):
            if char.lower() == character.lower():
                result[index] = character.lower()
        result = ''.join(result)
        return result
    except:
        return result
    

def guess_letter(game, letter):   
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0 :
        raise GameFinishedException
    
    uncovered_word = _uncover_word(game['answer_word'],game['masked_word'],letter.lower())
    
    if game['masked_word'] == uncovered_word:
        game['remaining_misses'] -= 1
    game['masked_word'] = uncovered_word
    game['previous_guesses'].append(letter.lower())
    

    if game['answer_word'] == game['masked_word']:
        game_over = True
        raise GameWonException('You win!')
        
    if game['remaining_misses'] == 0:
        game_over = True
        raise GameLostException('You lost!')
    


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
