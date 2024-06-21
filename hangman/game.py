from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['stephen', 'daniel', 'tim']


def _get_random_word(list_of_words):
    try:
        random_word = random.choice(list_of_words)
    except IndexError:
        raise InvalidListOfWordsException
    return random_word

def _mask_word(word):
    if word == '':
        raise InvalidWordException
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if answer_word == '' or masked_word == '':
        raise InvalidWordException
        
    if len(character) > 1:
        raise InvalidGuessedLetterException
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    new_word = ''
    for position, letter in enumerate(answer_word):
        if character.lower() == letter.lower():
            new_word += character
        elif masked_word[position] != '*':
            new_word += masked_word[position] 
        else:
            new_word += '*'
            
    return new_word.lower()
    
        

def guess_letter(game, letter):
    masked_word = game['masked_word']
    answer_word = game['answer_word'].lower()
    remaining_misses = game['remaining_misses']
    if answer_word == game['masked_word'] or remaining_misses == 0:
        raise GameFinishedException
        
    game['masked_word'] = _uncover_word(answer_word, masked_word, letter)
    
    if answer_word == game['masked_word']:
        raise GameWonException
    
    if letter.lower() not in answer_word:
        game['remaining_misses'] = remaining_misses - 1
        if game['remaining_misses'] == 0:
            raise GameLostException
    
    game['previous_guesses'].append(letter.lower())

    
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
