from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["rmotr","python","code"]


def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    
    raise InvalidListOfWordsException ()

def _mask_word(word):
    if word:
        return '*'*len(word)
    raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
    
    if not answer_word or not masked_word or not character:
        raise InvalidWordException()
        
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    
    if len(masked_word)!=len(answer_word):
        raise InvalidWordException()
    
    num_match=0
    character=character.lower()
    
    for index,char in enumerate(answer_word.lower()):
        if char==character:
            num_match+=1
            masked_word=masked_word[:index]+char+masked_word[index+1:]
    
    return masked_word
    
        


def guess_letter(game, letter):
    
    
    if game['remaining_misses']==0 or game['masked_word'] == game['answer_word'].lower():
        raise GameFinishedException()
    
    new_masked_word=_uncover_word(game['answer_word'],game['masked_word'],letter)
    
    if new_masked_word == game['masked_word']:
        game['remaining_misses']-=1
        
    game['masked_word']=new_masked_word
    game['previous_guesses'].append(letter.lower())
    
    if game['masked_word'] == game['answer_word'].lower():
        raise GameWonException()
    
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
