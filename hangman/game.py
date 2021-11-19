from .exceptions import *
from random import choice

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):    
    
    if len(list_of_words) != 0:
        return choice(list_of_words)
    else:
        raise InvalidListOfWordsException()


def _mask_word(word): 
    if len(word) != 0:
        return '*' * len(word)
    else:
        raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
    index = 0
    length_answer_word  = len(answer_word)
    length_character = len(character)
    length_masked_word = len(masked_word
                            )
    if length_answer_word == 0:
        raise InvalidWordException()
        
    if length_character > 1:
        raise InvalidGuessedLetterException()
        
    if length_answer_word != length_masked_word:
        raise InvalidWordException()
        
    masked_word = [letter for letter in masked_word]
    for letter in answer_word:
        if letter.lower() == character.lower():
            masked_word[index] = character.lower()
        index += 1
    
    return ''.join(masked_word)
            
        
def guess_letter(game, letter):
    if game['remaining_misses'] == 0:
        raise GameFinishedException()
        
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameFinishedException()       
    
              
    game['previous_guesses'].append(letter.lower())
    game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'],letter)
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameWonException()
              
    if letter.lower() not in game['answer_word'].lower():
        game['remaining_misses'] -= 1
        
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
