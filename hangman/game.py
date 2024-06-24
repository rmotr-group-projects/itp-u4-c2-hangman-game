from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    try:
        return random.choice(list_of_words)
    except:
        pass
    raise InvalidListOfWordsException


def _mask_word(word):
    masked_word = ''
    
    if not word:
        raise InvalidWordException

    for i in range(0, len(word)):
        masked_word += '*'
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if not answer_word and not masked_word:
        raise InvalidWordException

    if len(character) > 1:
        raise InvalidGuessedLetterException

    if len(answer_word) != len(masked_word):
        raise InvalidWordException

    new_masked_word= ''
    
    for answer_index, answer_character in enumerate(answer_word):
        if answer_character.lower() == character.lower():
            new_masked_word += character.lower()
        else:
            new_masked_word += masked_word[answer_index]
            
    return new_masked_word

    
def guess_letter(game, letter):
    if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
    
    previous_word = game['masked_word']
    
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if letter not in game['previous_guesses']:
        game['previous_guesses'].append(letter.lower())
    
    if previous_word == game['masked_word']:
        game['remaining_misses'] -= 1

    if '*' not in game['masked_word']:
        game_finished = True
        raise GameWonException
        
    if game['remaining_misses'] == 0:
        game_finished = True
        raise GameLostException
        
def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [], #the letters already guessed
        'remaining_misses': number_of_guesses,
    }

    return game
    
