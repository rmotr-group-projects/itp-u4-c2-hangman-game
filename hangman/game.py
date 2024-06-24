from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Santa', 'Cowboys', 'rolltide', 'Alabama', 'Amazon']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)


def _mask_word(word):
    if word == '':
        raise InvalidWordException()

    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if answer_word == '' or masked_word == '' or len(answer_word) != len(masked_word):
        raise InvalidWordException()

    if len(character) > 1:
        raise InvalidGuessedLetterException()

    character = character.lower()
    masked = masked_word.lower()
    answer = answer_word.lower()
    if character in answer:
        change = answer.find(character)

        while change != -1:
            answer = answer.replace(character, '*', 1)
            masked = masked[:change] + character + masked[change+1:] 

            change = answer.find(character)

    return masked


def guess_letter(game, letter):
    if game['remaining_misses'] <= 0 or '*' not in game['masked_word']:
        game['masked_word'] = _mask_word(game['masked_word'])
        raise GameFinishedException()

    holder = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter.lower())

    if holder == game['masked_word']:
        game['remaining_misses'] -= 1
        if game['remaining_misses'] <= 0:
            game['masked_word'] = _mask_word(game['masked_word'])
            raise GameLostException()
    else:
        game['masked_word'] = holder
        if '*' not in game['masked_word']:
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
