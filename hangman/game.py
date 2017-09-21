from .exceptions import *
from random import randint
# Complete with your own, just for fun :)
LIST_OF_WORDS = ['sharp','evil','weeks','justice','hot','cast','letters','youth','lives','health','finished','hoped','holding','touch','spite','delight','bound','consequence','rain','third','hung','ways','weather','written','difference','kitchen','persons','quarter','promised','hopes','brown','nay','seven','simple','wood','beside','middle','ashamed','lose','dreadful','move','generally','cousin','surely','satisfied','bent','shoulder']


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException
    return list_of_words[(randint(0,(len(list_of_words)-1)))]

def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) < 1:
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    new_masked_word = ''
    for i, char in enumerate(answer_word):
        if char.lower() == character.lower():
            new_masked_word += character.lower()
        else:
            new_masked_word += masked_word[i].lower()
    return new_masked_word

        

def guess_letter(game, letter):
    if game['remaining_misses'] < 1:
        raise GameFinishedException
        
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException
    
    game['masked_word']  = _uncover_word(game['answer_word'], game['masked_word'],letter)
    game['previous_guesses'].append(letter.lower())
    if not letter.lower() in game['answer_word'].lower():
        game['remaining_misses'] -= 1
        
    if game['answer_word'] == game['masked_word']:
        raise GameWonException
    
    if game['remaining_misses'] < 1:
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
        'remaining_misses': number_of_guesses
    }

    return game
