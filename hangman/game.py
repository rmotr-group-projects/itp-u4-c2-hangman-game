from .exceptions import *
import random


# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException ("There is no word in the list")
    return random.choice(list_of_words)
    pass


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    answer = answer_word.lower()
    if len(answer_word)==0 or len(masked_word) ==0:
        raise InvalidWordException ()
    if len (character) > 1:
        raise InvalidGuessedLetterException ()
    if len(masked_word) != len(answer_word):
        raise InvalidWordException ()
    new_word = ''
    if character.lower() not in answer:
        return masked_word
    for char_word, mask_word in zip(answer, masked_word):
        if character.lower() == char_word:
            new_word += char_word
        else:
            new_word += mask_word
            
    return new_word

def _is_game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()
def _is_game_lost(game):
    return game['remaining_misses'] <=0

def _is_game_finished(game):
    return _is_game_lost(game) or _is_game_won(game)

def guess_letter(game, letter):
    letter = letter.lower()
    if letter in game ['previous_guesses']:
        raise InvalidGuessedLetterException()
    if _is_game_finished(game):  # Already Won
        raise GameFinishedException()
    
    previous_masked = game['masked_word']
    new_masked = _uncover_word (game['answer_word'], previous_masked, letter)
    
    if previous_masked == new_masked:
        game['remaining_misses'] -=1
        
    else:
        game['masked_word'] = new_masked
    
    game['previous_guesses'].append(letter)
    
    
    if _is_game_won(game):
        raise GameWonException()

    if _is_game_lost(game):
        raise GameLostException()
    


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
