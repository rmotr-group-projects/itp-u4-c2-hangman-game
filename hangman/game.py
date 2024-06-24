from random import choice
from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['anagram', 'quizzically', 'rhinoceros', 'backpacking', 'sourdough', 'cat', 'dog', 'to']


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException()
    else:
        random_word_1 = choice(list_of_words)
        return random_word_1
    pass

def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException()
    else:
        return ('*' * len(word))
    pass


def _uncover_word(answer_word, masked_word, character):
    if len(masked_word) != len(answer_word):
        raise InvalidWordException()
    if len(answer_word) < 1 or len(masked_word) < 1:
        raise InvalidWordException()
    if len(character) != 1:
        raise InvalidGuessedLetterException()
    list_answer_word = list(answer_word)
    list_masked_word = list(masked_word)
    for index, letter in enumerate(list_answer_word, 0):
        if character.lower() == letter.lower():
            list_masked_word[index] = character.lower()

    return ''.join(list_masked_word)
            
    pass


def guess_letter(game, letter):
    if game['remaining_misses'] == 0:
        raise GameFinishedException()
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException()
    if len(letter) != 1:
        raise InvalidGuessedLetterException()
    
    letter = letter.lower()
    game['masked_word'] = game['masked_word'].lower()
    game['answer_word'] = game['answer_word'].lower()
    
    if letter in (game['answer_word']):
        place_holder = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['masked_word'] = place_holder
        game['previous_guesses'].append(letter)
        if game['masked_word'] == game['answer_word']:
            raise GameWonException()
    else:
        game['remaining_misses'] -= 1
        game['previous_guesses'].append(letter)
        if game['remaining_misses'] == 0:
            raise GameLostException()
        
            
        
        
        
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
