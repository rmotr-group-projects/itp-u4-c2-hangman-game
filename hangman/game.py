from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Chris', 'Maria', 'Chico']


def _get_random_word(list_of_words):
    
    if not list_of_words:
        raise InvalidListOfWordsException()
        
    return random.choice(list_of_words)
    

def _mask_word(word):
    
    if not word:
        raise InvalidWordException()
        
    masked = ''
    for item in word:
        masked += '*'
        
    return masked


def _uncover_word(answer_word, masked_word, character):
    
    if not answer_word or not masked_word:
        raise InvalidWordException()
        
    if len(character) > 1:
        raise InvalidGuessedLetterException()
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

        
    answer_word_low = answer_word.lower()
    character_low = character.lower()
    masked_list = list(masked_word)
    index_to_switch = []
    masked_string = masked_word
    
    if character_low in answer_word_low:
        for ind, letter in enumerate(answer_word_low):
            if character_low == letter:
                index_to_switch.append(ind)
        for item in index_to_switch:
            masked_list[item] = character_low
        masked_string = ''.join(masked_list)
        
    return masked_string
                


def guess_letter(game, letter):
    
    if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException()
        
    letter = letter.lower()
    game_return = game
    answer_word = game['answer_word']
    game_return['answer_word'] = answer_word.lower()
    
    if letter in game['answer_word']:
        game_return['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    else:
        game['remaining_misses'] -= 1
    game_return['previous_guesses'].append(letter)
    
    
    if '*' not in game_return['masked_word']:
        raise GameWonException()
        
    if game_return['remaining_misses'] == 0:
        raise GameLostException()
    
    return game_return
        


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
