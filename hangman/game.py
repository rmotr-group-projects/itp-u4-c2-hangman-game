from .exceptions import *
from random import choice

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['blakclist', 'happy', 'blindspot']


def _get_random_word(list_of_words):
    try:
        random_word = choice(list_of_words)
        return random_word
    except:
        raise InvalidListOfWordsException()


def _mask_word(word):
    if not word:
        raise InvalidWordException
    my_masked_word = len(word) * '*'
    return my_masked_word
    


def _uncover_word(answer_word, masked_word, character):
    
    masked_word_list = list(masked_word)
    new_char = character.lower()

    if not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException()
        
    if len(new_char) != 1:
        raise InvalidGuessedLetterException()
    
    for idx, char in enumerate(answer_word):
        if new_char == char.lower():
            masked_word_list[idx] = new_char
            masked_word = ''.join(masked_word_list)
            
    return masked_word
    
    

def guess_letter(game, letter):
    
    low_case_letter = letter.lower()
    masked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if game['remaining_misses'] == 0 or game['masked_word'] == game['answer_word']:
        raise GameFinishedException()
        
    game['masked_word'] = masked_word
    game['previous_guesses'].append(low_case_letter)
    
    if low_case_letter not in game['answer_word'].lower():
        game['remaining_misses'] -= 1
    
    if game['remaining_misses'] == 0:
        raise GameLostException()
    
    if game['masked_word'] == game['answer_word']:
        raise GameWonException()



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
