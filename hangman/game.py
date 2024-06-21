from .exceptions import *
from random import choice
#from exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Python','javascript','microsoft']


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException()
    
    return choice(list_of_words)


def _mask_word(word):
    masked_word = ''
    for char in word:
        masked_word += '*'
    
    if masked_word == '':
        raise InvalidWordException()
    return masked_word



def _uncover_word(answer_word, masked_word, character):
    #testing with answer_word are missing
    if answer_word == '' or masked_word == '':
        raise InvalidWordException()

    #Different lengths of answered_word or masked_word
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

    #invalid character
    if len(character) > 1:
        raise InvalidGuessedLetterException()

    #if Character not in word return masked_word
    if character.lower() not in answer_word.lower():
        return masked_word

    #grab all the indexes where character may appear
    idxs = []
    for index,letter in enumerate(answer_word):
        if letter.lower() == character.lower():
            idxs.append(index)
    
    #update new_masked word
    new_masked_word = ''
    for index,char in enumerate(masked_word):
        if index in idxs:
            new_masked_word += character.lower()
        elif char != '*':
            new_masked_word += char
        else:
            new_masked_word += '*'
    
   
    return new_masked_word


def guess_letter(game, letter):
    #test if finished
    if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
       raise GameFinishedException()

    #Test for letter

    if letter.lower() in game['answer_word'].lower():
        
        game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
    else:
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses'] -= 1
    
    #End game

    

    if game['answer_word'] == game['masked_word']:
        raise GameWonException()

    if game['remaining_misses'] == 0:
        raise GameLostException()

    
    


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