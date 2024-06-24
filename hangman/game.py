from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    raise InvalidListOfWordsException()


def _mask_word(word):
    if len(word):
        return '*' * len(word)
    raise InvalidWordException()



def _uncover_word(answer_word, masked_word, character):
    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    character = character.lower()
    result = ''
    if answer_word and masked_word and len(answer_word) == len(masked_word):
        if len(character) == 1:
            for i,v in enumerate(answer_word):
                if answer_word[i] == character:
                    result += character
                else:
                    result += masked_word[i]
            return result
        raise InvalidGuessedLetterException()
    raise InvalidWordException()



def guess_letter(game, letter):
    for ea_key in game:
        if type(game[ea_key]) == str:
            game[ea_key] = game[ea_key].lower()
    letter = letter.lower()
    if letter in game['answer_word']:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter)
        if '*' not in game['masked_word']:
            raise GameWonException()
        if '*' not in game['masked_word'] or game['remaining_misses'] < 1:
            raise GameFinishedException()
    else:
        game['remaining_misses'] -= 1
        game['previous_guesses'].append(letter)
        if game['remaining_misses'] == 0:
            raise GameLostException()
        if '*' not in game['masked_word'] or game['remaining_misses'] < 1:
            raise GameFinishedException()





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
