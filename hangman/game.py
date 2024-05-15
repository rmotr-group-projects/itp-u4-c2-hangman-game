from .exceptions import *
from random import choice
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    return choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    character = character.lower()
    if not answer_word or not masked_word:
        raise InvalidWordException()
    if len(character) > 1 :
        raise InvalidGuessedLetterException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    if character in answer_word:
        index = 0
        new_masked_word = ''
        for char in answer_word:
            if char == character:
                new_masked_word += character
            else:
                new_masked_word += masked_word[index]
            index += 1
        return new_masked_word
    else:
        return masked_word
        


def guess_letter(game, letter):
    letter = letter.lower()
    print(game['remaining_misses'])
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0  :
        raise GameFinishedException()
    
    remaining_misses = game['remaining_misses']
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'] += [letter]
        
    if letter not in game['answer_word'].lower():
        game['remaining_misses'] -= 1
        
        
    if game['masked_word'] == game['answer_word']:
        raise GameWonException() 
    if not game['remaining_misses']:
        raise GameLostException()
 
    

def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,#Python
        'masked_word': masked_word,#'******'
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,#5
    }

    return game