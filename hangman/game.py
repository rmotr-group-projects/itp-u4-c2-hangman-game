from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['rmotr', 'python', 'intro']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException('Those words invalid!')
    masked = ''
    for letter in word:
        masked += '*'
    return masked


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException('Those words invalid!')
    if len(character) > 1:
        raise InvalidGuessedLetterException('Guess letter should be an individual character!')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Word is an invalid length!')
    
    umasked = list(masked_word)
    occur = list(answer_word)
    index = 0
    for letter in occur:
        if letter == character.lower() or letter == character.upper():
            umasked[index] = character.lower()
        index += 1
    masked_word = ''.join(umasked)
    return masked_word
    
    
def guess_letter(game, letter):
    if game['remaining_misses'] == 0:
        raise GameFinishedException
    elif game['masked_word'] ==  game['answer_word']:
        raise GameFinishedException
    if letter in game['answer_word'].lower() or letter in game['answer_word'].upper():
        correct = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['masked_word'] = correct
        game['previous_guesses'].append(letter.lower())
        if '*' not in game['masked_word']:
            raise GameWonException
        return correct
    else:
        incorrect = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['masked_word'] = incorrect
        game['remaining_misses'] -= 1
        game['previous_guesses'].append(letter.lower())
        if game['remaining_misses'] == 0:
            raise GameLostException
        return game['masked_word']


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
