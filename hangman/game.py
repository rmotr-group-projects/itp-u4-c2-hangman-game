from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    else:
        return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException
    else:
        return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    if len(character) > 1:
        raise InvalidGuessedLetterException()
        
    word = ''
    answer_case = answer_word.lower()
    character_case = character.lower()
        
    if character_case not in answer_case:
        return masked_word

    for index in range(len(answer_word)):
        if character_case == answer_case[index]:
            word += answer_case[index]
        else:
            word += masked_word[index]

    return word


def guess_letter(game, letter):
    if game['answer_word'].lower() == game['masked_word'].lower() or game['remaining_misses'] < 1:
        raise GameFinishedException()
    if letter.lower() in game['previous_guesses']:
        raise InvalidGuessedLetterException()

    masked = game['masked_word']
    word = _uncover_word(game['answer_word'], masked, letter)

    if masked == word:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = word

    game['previous_guesses'].append(letter.lower())
    
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameWonException()
    if game['remaining_misses'] < 1:
        raise GameLostException()

    return word


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
