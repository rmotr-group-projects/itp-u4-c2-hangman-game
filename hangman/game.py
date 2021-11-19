from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = ['LOL', 'HELLO', 'FOOL']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    character = character.lower()
    new_masked_word = masked_word.lower()
    answer_word = answer_word.lower()
    for index, alpha in enumerate(answer_word): #just in case of repeated letters, iterating over each letter in answer_word
        if character == alpha:
            new_masked_word = new_masked_word[:index] + character + new_masked_word[(index + 1):]
    return new_masked_word



def guess_letter(game, letter):
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException

    if game['answer_word'].lower() == game['masked_word'].lower() or game['remaining_misses'] == 0:
        raise GameFinishedException

    letter = letter.lower()
    previous_masked = game['masked_word']
    new_masked = _uncover_word(game['answer_word'], previous_masked, letter)

    #letter not in answer, masked_word remains unchanged
    if previous_masked == new_masked:
        game['remaining_misses'] -= 1 #remaining misses go down by one

    #letter in answer, masked_word is updated
    elif previous_masked != new_masked:
        game['masked_word'] = new_masked
        
    game['previous_guesses'].append(letter)

    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameWonException

    if game['remaining_misses'] <= 0:
        game['masked_word'] = _mask_word(game['masked_word'])
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
