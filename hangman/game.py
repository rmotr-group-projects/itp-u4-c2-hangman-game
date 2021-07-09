from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    try:
        return random.choice(list_of_words)
    except IndexError as e:
        raise InvalidListOfWordsException
    pass


def _mask_word(word):
    length = len(word)
    masked = "*" * length
    if length == 0 :
        raise InvalidWordException
    return masked
    


def _uncover_word(answer_word, masked_word, character):
    if not (len(character) ==  1):
        raise InvalidGuessedLetterException
    if not len(answer_word) == len(masked_word):
        raise InvalidWordException
    if not len(answer_word) >0 :
        raise InvalidWordException    
    
        
    newmask = ""
    for index,letter in enumerate(answer_word):
        if letter.lower() == character.lower():
            newmask += letter.lower()
        else:
            newmask += masked_word[index].lower()
    return newmask
        


def guess_letter(game, letter):
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameFinishedException
        
    if game['remaining_misses'] == 0 :
        raise GameFinishedException()
        
    old_mask = game['masked_word']
    game['previous_guesses'].append(letter.lower())
    new_mask = _uncover_word(game['answer_word'],old_mask,letter)
    game['masked_word'] = new_mask
    

    
    if new_mask == old_mask:
        game['remaining_misses'] -= 1
    
    if new_mask.lower() == game['answer_word'].lower():
        raise GameWonException
        
    if game['remaining_misses'] == 0:
        raise GameLostException
    pass


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
