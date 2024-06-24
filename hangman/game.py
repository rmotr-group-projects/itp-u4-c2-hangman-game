# from .exceptions import *
from hangman.exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Hangman', 'Imagination', 'Dragon', 'Throne', 'Sword', ' Space', 'Coding', 'Python', 'Anaconda']


def _get_random_word(list_of_words):
    try:
        random_word = random.choice(list_of_words)
        return random_word
    except:
        raise InvalidListOfWordsException()
    
    
def _mask_word(word):
    if not word:
        raise InvalidWordException()

    mask_word = ''
    for char in word:
        mask_word += '*'
    return mask_word
    
    
def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()            
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

    if len(character) > 1:
        raise InvalidGuessedLetterException()
     
    char_list = list(masked_word.lower())
    for i,char in enumerate(answer_word.lower()):
        if char == character.lower():
            char_list[i] = char
    return ''.join(char_list)
            
      
def guess_letter(game, letter):
    
    if game['answer_word'].lower() == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
    
    
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    if game['answer_word'].lower() == game['masked_word']:
        raise GameWonException()

        
    game['previous_guesses'].append(letter.lower())
    
    if letter.lower() not in game['answer_word'].lower():
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            raise GameLostException()
            GAME_FINISHED = True
    
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
