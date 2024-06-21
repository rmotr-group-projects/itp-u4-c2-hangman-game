from .exceptions import *

import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['lovely', 'bostonian', 'hare', 'lustily', 'hippopotamus']

#this function is complete, passed all tests
def _get_random_word(list_of_words):
    
    if list_of_words == []:
        raise InvalidListOfWordsException('List Invalid')
    
    for word in list_of_words:
        return random.choice(list_of_words)


#this function is complete, passed all tests
def _mask_word(word):    
    
    if word != '':
        word = '*' * len(word)
        return word 
    
    else: 
        raise InvalidWordException('must put word')
    

#function is correct, tests all pass.
def _uncover_word(answer_word, masked_word, character):
    if answer_word == '':
        raise InvalidWordException('must have word')
    
    if masked_word == '':
        raise InvalidWordException('must have word')
        
    if character == '':
        raise InvalidWordException('must put character')
    
    if len(character) > 1:
        raise InvalidGuessedLetterException('you can only guess one letter at a time')
        
    if len(masked_word) != len(answer_word):
        raise InvalidWordException('length of guessed word must be the same as the hidden word')
    
    answer = answer_word.lower()
    
    if character.lower() not in answer:
        return masked_word

    new_word = ''

    for answer_char, masked_char in zip(answer, masked_word):
        if character.lower() == answer_char:
            new_word += answer_char
        else:
            new_word += masked_char

    return new_word

def is_game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()

def is_game_lost(game):
    return game['remaining_misses'] <= 0
        
def is_game_over(game):
    return is_game_lost(game) or is_game_won(game)

#don't know how to write this function
def guess_letter(game, letter):
    if is_game_over(game): 
        raise GameFinishedException('the game is already done')
    
    letter = letter.lower()
    
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException('you already guessed that letter')
    previous_masked = game['masked_word']
    new_masked = _uncover_word(game['answer_word'], previous_masked, letter)
    if previous_masked == new_masked:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_masked

    game['previous_guesses'].append(letter)
    
      
    if is_game_won(game):
        raise GameWonException('you have won')
    if is_game_lost(game):
        raise GameLostException('you lost, hahaha')
    #game won first try
    '''
    if is_game_won(game) and game['previous_guesses'] == 0:
        raise GameWonException('you won on the first try')
    #game won several moves some misses    
    if is_game_won(game) and letter in game['previous_guesses']:
        raise GameWonException('you won, try again to get it with less misses')
    #game won several moves no misses
    if is_game_won(game) and letter not in game['previous_guesses']:
        raise GameWonException('you won, no misses')
    #game already won raises game finished
    if is_game_won(game):
        raise GameFinishedException('game already won')
    #game already lost raises game finished
    if is_game_lost(game):
        raise GameFinishedException('game already lost')
    return new_masked
    '''

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
