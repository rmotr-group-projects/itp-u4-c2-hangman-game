from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    
    masked_word = ''
    for _ in range(0, len(word)):
        masked_word += '*'
    
    return masked_word
        

def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()
        
    if len(character) != 1:
        raise InvalidGuessedLetterException()
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    
    unmasked_word = ''
    
    for char in answer_word:
        index = answer_word.index(char)
        
        if char.lower() == character.lower():
            unmasked_word += char.lower()
            continue

        if masked_word[index] != '*':
            unmasked_word += masked_word[index]
            continue
        
        unmasked_word += '*'
    
    return unmasked_word

def guess_letter(game, letter):
    
    game_finished = False
    
    if game_finished == True:
        raise GameFinishedException()
    
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter.lower())

    if game['masked_word'] == game['answer_word']:
        if letter not in game['answer_word']:
            raise GameFinishedException()
        raise GameWonException()
    
    if letter.lower() not in game['answer_word'].lower():
        game['remaining_misses'] += -1
    
    if game['remaining_misses'] == 0:
        if letter in game['answer_word']:
            raise GameFinishedException()
        raise GameLostException()
    
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
