from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    raise InvalidListOfWordsException

def _mask_word(word):
    if word:
        len_of_word = len(word)
        return '*' * len_of_word
    raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    if answer_word and masked_word and len(answer_word) == len(masked_word):
        if len(character) == 1:
            list_word = list(answer_word)
            list_masked = list(masked_word)
            for index, char in enumerate(answer_word):
                if char.lower() == character.lower() and list_masked[index] == '*':
                    list_masked[index] = character.lower()
            return ''.join(list_masked)
        else:
            raise InvalidGuessedLetterException
    else:
        raise InvalidWordException

def guess_letter(game, letter):
    if game['answer_word'].lower() == game['masked_word'].lower() or game['remaining_misses'] <= 0:
        raise GameFinishedException
    new_masked_word = _uncover_word(game['answer_word'],game['masked_word'],letter)
    if new_masked_word.lower() != game['answer_word'].lower():
        game['previous_guesses'].append(letter.lower())
        if game['masked_word'] == new_masked_word:
           game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:    
            raise GameLostException
        game['masked_word'] = new_masked_word
    else:
        game['masked_word'] = new_masked_word
        raise GameWonException

    

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
