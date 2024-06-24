import random
from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['rmotr', 'python', 'program']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException('Those words are invalid.')
        
    try:    
        random_word = random.choice(list_of_words)
    except IndexError as err:
        print(err)
        
    return random_word


def _mask_word(word):
    random_word = ''
    if not word:
        raise InvalidWordException('That word is invalid.')
    
    for char in word:
        random_word += '*'

    return random_word


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException('That word is invalid.')
    if len(character) > 1:
        raise InvalidGuessedLetterException('That letter is invalid.')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Those words are invalid.')
    
    character = character.lower()
    answer_word = answer_word.lower()
    unmasked_word = masked_word
    
    for idx, char in enumerate(answer_word):
        if character == char:
            unmasked_word = masked_word[:idx] + char + masked_word[idx+1:]
            masked_word = unmasked_word.lower()
            
    return masked_word


def guess_letter(game, letter):
    
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException('Game over.') 
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()
        
    game['answer_word'] = game['answer_word'].lower()
    game['masked_word'] = game['masked_word'].lower()
    letter = letter.lower()
    
    unmasked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if letter in game['answer_word']:
        game['masked_word'] = unmasked_word
        game['previous_guesses'].append(letter)
        if unmasked_word == game['answer_word']:
            raise GameWonException('You won!')
    else:
        game['remaining_misses'] -= 1
        game['previous_guesses'].append(letter)
        if game['remaining_misses'] == 0 and game['answer_word'] != unmasked_word:
            raise GameLostException('You lose!')

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
