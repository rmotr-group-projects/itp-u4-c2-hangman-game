from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['python','for','data', 'science','fun']


def _get_random_word(list_of_words):
    if len(list_of_words)==0:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)


def _mask_word(word):
    if len(word)==0:
        raise InvalidWordException
    mask=""
    for c in word:
        mask+="*"
    return mask    


def _uncover_word(answer_word, masked_word, character):
    if  len(character)!=1:
        raise InvalidGuessedLetterException()
    if len(answer_word)==0 or len(masked_word)==0 or len(answer_word)!=len(masked_word):
        raise InvalidWordException() 
    masked_list=list(masked_word)
    for index, char in enumerate(answer_word):
        if char.lower()==character.lower():    
            masked_list[index]=char.lower()
    result=''.join(masked_list)                
    return result


def guess_letter(game, letter):
    answer_word=game['answer_word']
    masked_word=game['masked_word']
    uncover_word=_uncover_word(game['answer_word'], masked_word, letter)
    remaining_misses=game['remaining_misses']
    if answer_word==masked_word or remaining_misses==0:
        raise GameFinishedException()
    
        
    game['masked_word']=uncover_word
    (game['previous_guesses']).append(letter.lower())
    
    if letter.lower() not in game['answer_word'].lower():
        (game['remaining_misses'])-=1
        
    if answer_word==uncover_word:
        raise GameWonException()
    if game['remaining_misses']==0:
        raise GameLostException     

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
