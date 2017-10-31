from .exceptions import *
import random



# Complete with your own, just for fun :)
LIST_OF_WORDS = ['apple', 'banana', 'orange', 'grape', 'persimmon']


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException
    masked_word = '*' * len(word)
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) < 1 or len(masked_word) < 1:
        raise InvalidWordException("Words are empty")
    if len(character) != 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    if answer_word == masked_word:
        raise GameFinishedException
    counter = 0
    masked_word_as_list = list(masked_word)
    for letter in answer_word:
        if letter.lower() == character.lower():
             masked_word_as_list[counter] = letter.lower()
        counter += 1
    return ''.join(masked_word_as_list)


def guess_letter(game, letter):
    if game['remaining_misses'] == 0:
        raise GameFinishedException
    game['previous_guesses'].append(letter.lower())
    if letter.lower() not in game['answer_word'].lower():
        game['remaining_misses'] -= 1
    game['masked_word'] = _uncover_word(game['answer_word'].lower(), game['masked_word'].lower(), letter)
    if  game['masked_word'] ==  game['answer_word']:
        raise GameWonException
    if game['remaining_misses'] == 0:
        raise GameLostException




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
