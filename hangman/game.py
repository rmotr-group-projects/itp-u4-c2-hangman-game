from .exceptions import *
from random import choice
from string import ascii_letters

# Complete with your own, just for fun :)
with open('./hangman/sowpods.txt', 'r') as f:
    raw_list = f.readlines()

LIST_OF_WORDS = [word.strip() for word in raw_list]    # Remove '\n' from end of each word


def _get_random_word(list_of_words):
    if list_of_words:
        return choice(list_of_words)
    else:
        raise InvalidListOfWordsException


def _mask_word(word):
    if len(word) > 0:
        return '*' * len(word)
    else:
        raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) < 1 or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1 or character not in ascii_letters:
        raise InvalidGuessedLetterException
    masked_output = ''
    for letter in answer_word:
        if letter.lower() == character.lower() and masked_word[answer_word.index(letter)] == '*':
            masked_output += character.lower()
        elif masked_word[answer_word.index(letter)].lower() != '*':
            masked_output += masked_word[answer_word.index(letter)].lower()
        else:
            masked_output += '*'
    return masked_output


def guess_letter(game, letter):
    if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
    if len(letter) > 1 or letter not in ascii_letters or letter.lower() in game['previous_guesses']:
        raise InvalidGuessedLetterException
    if game['masked_word'] == _uncover_word(game['answer_word'], game['masked_word'], letter):
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            raise GameLostException
    else:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter.lower())
    if '*' not in game['masked_word']:
        raise GameWonException

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
        'remaining_misses': number_of_guesses
    }

    return game
