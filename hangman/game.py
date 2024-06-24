from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)


def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException()
    return "*" * len(word)


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0:
        raise InvalidWordException()
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
        
    if len(character) != 1:
        raise InvalidGuessedLetterException()
    
    if character.lower() in answer_word.lower():
        string_rep = ''
        for ind, letter in enumerate(answer_word):
            print(letter)
            if letter.lower() == character.lower():
                string_rep += letter.lower()
            else:
                string_rep += masked_word[ind]
        masked_word = string_rep
    return masked_word


def guess_letter(game, letter):
    letter = letter.lower()
    initial_masked_word = game['masked_word']
    
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()
    
    if game['remaining_misses'] <= 0 or game['answer_word'] == game['masked_word']:
        raise GameFinishedException()
    
        
    game['previous_guesses'].append(letter)
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        
        
    if game['masked_word'] == initial_masked_word:
        game['remaining_misses'] -= 1
        
    if game['remaining_misses'] and '*' in game['masked_word']:
        return game
    else:
        if '*' in game['masked_word']:
            raise GameLostException()
        else:
            raise GameWonException()
            


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
