
from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['aquaria', 'cracker', 'monet', 'eureka', 'vanjie', 'asia', 'kalorie', 'monique', 'dusty', 'yuhua', 'kameron', 'blair', 'mayhem', 'vixen']


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException()
    else:
        return random.choice(list_of_words)

def _mask_word(word):
    if word == '':
        raise InvalidWordException()
    else:
        return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    masked_word_list = list(masked_word)
    if answer_word == '' or masked_word == '':
        raise InvalidWordException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    if len(character) != 1:
        raise InvalidGuessedLetterException()
    for index, letter in enumerate(answer_word):
        if character.lower() == letter.lower():
            masked_word_list[index] = character.lower()
    new_string = ''
    for letter in masked_word_list:
        new_string += str(letter)
    return new_string

def guess_letter(game, letter):
    if letter.lower() in game['answer_word'].lower() and game['remaining_misses'] == 0:
        raise GameFinishedException()
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException()
    if letter.lower() in game['answer_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
        if game['answer_word'] == game['masked_word']:
            raise GameWonException()
        return game
    else:
        game['previous_guesses'].append(letter)
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
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
