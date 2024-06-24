import random 
from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['mallorca', 'odessa', 'beer', 'beach', 'pool', 'food']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    word = random.choice(list_of_words)
    return word 

def _mask_word(word):
    masked = ('*' * len(word))
    if len(word) == 0:
        raise InvalidWordException('invalid length')
    return masked 

def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException("Invalid word")
    if len(character) > 1: 
        raise InvalidGuessedLetterException("invalid character")
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('invalid length')
    # this will do a case insensitve for all three parameters 
    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    character = character.lower()
    if character not in answer_word: 
        return masked_word
        
    # set a new string     
    result = ''
    # iterate through the items of the list, from range(0-4 for example) and len (the total items in the word)
    for i in range(len(answer_word)):
        # if the index [i] of answer_word appears at that certain index and equals to character, then new string will show the character  
        if answer_word[i] == character:
            result += character
        # if not, then the new string will just show the masked_word at the item 
        else:
            result += masked_word[i]
    return result
 

def guess_letter(game, letter):
    if not '*' in game['masked_word']:
        raise GameFinishedException
    if letter.lower() in game['answer_word'].lower(): # lower both! 
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter) # we copy the function here 
        game['previous_guesses'].append(letter.lower()) 
        if not '*' in game['masked_word']:
            raise GameWonException
            
    else:
        game['remaining_misses'] -= 1 
        game['previous_guesses'].append(letter.lower())
        if game['remaining_misses'] == 0:
            raise GameLostException()
    if game['remaining_misses'] == 0:
        raise GameFinishedException   


# DON'T CHANGE!!!!

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
