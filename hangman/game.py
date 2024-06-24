from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException("Invalid List of Words")
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException("Invalid Words")
    return '*'*len(word)


def _uncover_word(answer_word, masked_word, character):   
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException("Invalid Words")
    if len(character) > 1:
        raise InvalidGuessedLetterException("Only one letter to guess")
    
    result_str=''
    for idx, letter in enumerate(answer_word):
        if character.lower() ==letter.lower():
            result_str+=answer_word[idx].lower()
        else:
            result_str+=masked_word[idx].lower()        
    return result_str


def guess_letter(game, letter):
    if game['masked_word']==game['answer_word']:
        raise GameFinishedException("You Win")

    if game['remaining_misses']==0:
        raise GameFinishedException()    
    
    new_masked =_uncover_word(game['answer_word'], game['masked_word'],letter)
    
    if new_masked ==game['answer_word']:
        game['masked_word']=new_masked
        raise GameWonException("You Win")
        
    if game['masked_word']==new_masked:
        game['remaining_misses'] -= 1
    else:
        game['masked_word']=new_masked
        
    game['previous_guesses'] += letter.lower()
    
    if game['remaining_misses']==0:
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
