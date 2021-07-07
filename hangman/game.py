from .exceptions import *
from random import choice

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['python', 'javascript', 'linux', 'computer', 'programming', 'windows' ]


def _get_random_word(list_of_words):
    if list_of_words:
        return choice(list_of_words)
    
    raise InvalidListOfWordsException

def _mask_word(word):
    if word:
        return '*' * len(word)
    
    raise InvalidWordException

def _uncover_word(answer_word, masked_word, character):
    #Exceptions
    if not answer_word or not masked_word:
        raise InvalidWordException
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
        
    if len(character) > 1:
        raise InvalidGuessedLetterException

    #Uncover Word 
    character = character.lower()
    answer_word = answer_word.lower()

    if character not in answer_word:
        return masked_word
    
    #character in answer_word    
    masked_list = [char for char in masked_word] # a list of masked and unmasked characters
    
    for index, char in enumerate(answer_word):
        if char == character:
            masked_list[index] = character
            
    masked_word = ''.join(masked_list)
    
    return masked_word

def guess_letter(game, letter):
    #Exceptions/Check if Game has already been finished
    if letter.lower() in game['previous_guesses']:
        raise InvalidGuessedLetterException
    
    if game['remaining_misses'] == 0:
        raise GameFinishedException
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException
    
    
    #Guess Letter
    game['previous_guesses'].append(letter.lower())
    
    if letter.lower() in game['answer_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    else:
        game['remaining_misses'] -= 1
    
    #Game States/Check if Game was Won or Lost
    if game['remaining_misses'] == 0:
        raise GameLostException
    if game['answer_word'] == game['masked_word']:
        raise GameWonException

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
