from .exceptions import *

import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = [
]


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException
    return '*'*(len(word))


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word or len(answer_word)!=len(masked_word):
        raise InvalidWordException
    if len(character)>1 or not character or type(character) != str:
        raise InvalidGuessedLetterException
    
    
    
    list_of_indices=[]
    count=0
    answer_word=answer_word.lower()
    character=character.lower()
    for char in answer_word:
        if character==char:
            list_of_indices.append(count)
        count+=1
    
    masked_word=list(masked_word)
    for index in list_of_indices:
        masked_word[index]=character
    
    return "".join(masked_word)
    


def guess_letter(game, letter):
    if game['answer_word']==game['masked_word'] or game['remaining_misses']==0: #checks to see if game already complete
        raise GameFinishedException
        
    letter=letter.lower()
    
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException
    
    
    previously_masked=game['masked_word']
    game['masked_word']=_uncover_word(game['answer_word'],game['masked_word'],letter)
    game['previous_guesses'].append(letter)
    if previously_masked==game['masked_word']:
        game['remaining_misses'] -= 1
    
    if game['answer_word']==game['masked_word']:
        raise GameWonException
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
