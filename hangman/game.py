from .exceptions import *

import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['testing','hola','runner','jokes']


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)

"""mask word complete"""
def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException
    return len(word) * '*'

"""if the character is in the word, replace the mask char"""
def _uncover_word(answer_word, masked_word, character):
    
    #print("answer_word", answer_word)
    #print("masked word", masked_word)
    
    #force it to make everything lowercase
    answer_word = answer_word.lower()
    character = character.lower()
    
    temp_word = "" #strings are immutable
    
    if len(character) > 1:
        raise InvalidGuessedLetterException
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    if len(answer_word) < 1 or len(masked_word) < 1:
        raise InvalidWordException
    
    if character in answer_word:
        index_list = []
        for index,char in enumerate(answer_word):
        #for char in answer_word:
            if char == character:
                temp_word += char
            else:
                # replace with a char from the masked word if not correct
                temp_word += masked_word[index]
               
        #print("DEBUG temp_word is", temp_word)
        return temp_word
    
    #print("DEBUG masked_word is", masked_word)
    return masked_word

""" In this game the 'game' variable is a dictionary that holds the state of the game.
    This function needs to update the 'masked_word' dictionary value"""
def guess_letter(game, letter):
    
    # GameFinishedException, is there a better way to do this?
    if game['masked_word'] == game['answer_word']:
        raise GameFinishedException
        
    if game['remaining_misses'] == 0:
        raise GameFinishedException
            
    #make sure guess letters are lowercase
    letter = letter.lower()
    
    #print(game)
    #print(letter)
    #####  _uncover_word(answer_word, masked_word, character)
    
    # for remaining misses you have to keep track of the differences
    # between previous masked word and new masked word
    previous_masked_word = game['masked_word']
    
    # DEBUG
    new_masked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    #update the masked word for each guess
    game['masked_word'] = new_masked_word
    #print("new_masked_word",new_masked_word)
    #print("game['answer_word'] = {} and game['masked_word'] = {}".format(game['answer_word'],game['masked_word']))
    
    # update the previous guesses list
    game['previous_guesses'].append(letter)
    # return the dictionary
    
    #update remaining misses
    if previous_masked_word == game['masked_word']:
        game['remaining_misses'] -= 1
        
        if game['remaining_misses'] == 0:
            raise GameLostException
#             try:
#                 raise GameFinishedException
#             except:
#                 raise GameLostException

    if game['masked_word'] == game['answer_word']:
        raise GameWonException
#         try:
#             print('this')
            
#             #SYNTAX IMPORTANT !!!
#         except GameWonException as e:
#             pass
# #         except GameFinishedException as e:
# #             pass

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
