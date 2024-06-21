import random
from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)    


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    return '*' * len(word)    


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()
        
    if len(character) > 1:
        raise InvalidGuessedLetterException()
        
    if len(answer_word) != len(masked_word) :
        raise InvalidWordException
    
    final_answer = answer_word.lower()  
    
    if character.lower() not in final_answer:
        return masked_word
        
    new_word = ''   

    for answer_char, masked_char in zip(answer_word, masked_word):
        if character.lower() == answer_char.lower() :
            new_word += answer_char.lower()
        else:
            new_word += masked_char.lower()
        
    return new_word   
    
def game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()

def game_lost(game):
    return game['remaining_misses'] <= 0   
    
def game_finished(game):
    return game_lost(game) or game_won(game)    
    


def guess_letter(game, letter):
    letter = letter.lower()
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException
        
    previous_masked = game['masked_word']  
    
    new_masked = _uncover_word(game['answer_word'],previous_masked, letter)
    
    if game_finished(game):
        raise GameFinishedException 
    
    if previous_masked == new_masked:
        game['remaining_misses'] -=1
    else:
        game['masked_word'] = new_masked
        
    game['previous_guesses'].append(letter)
    
    if game_won(game):
        raise GameWonException()

    if game_lost(game):
        raise GameLostException()
        
        
    
    
    return new_masked    
        


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
