from .exceptions import *

import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Sierra', 'Hotel', 'India', 'Echo', 'Lima', 'Delta', 'the', 'shield']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException('Words are empty')
    if len(character) > 1:
        raise InvalidGuessedLetterException('Character to guess has len() >1')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Length of words is different')
    uncovered_word = list(masked_word.lower())
    answer_list = list(answer_word.lower())
    for i in range(len(answer_list)):
        if character.lower() == answer_list[i]:
            uncovered_word[i] = character.lower()
    return "".join(uncovered_word)


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException()
    return len(word)*'*'


def guess_letter(game, letter):
    letterlower = letter.lower()
    if game['remaining_misses'] == 0 or game['answer_word'] == game['masked_word']:
        raise GameFinishedException('The game is over')
    if letterlower in game.get('previous_guesses'):
        raise InvalidGuessedLetterException('You have already guessed this letter')
    else:
        game['previous_guesses'].append(letterlower)
    if letterlower not in game['answer_word'].lower():
        game['remaining_misses'] -=1
        
    game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'],letterlower)
    
    if game['masked_word'] == game['answer_word']:
        raise GameWonException
    if game['remaining_misses'] == 0:
        raise GameLostException


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException('')

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game


