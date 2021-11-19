from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

from random import choice
def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException
    masked_word = '*' * len(word)
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if character.lower() not in answer_word.lower():
        return masked_word
    listt = []
    for letter in answer_word.lower():
        if letter == character.lower():                         listt.append(character.lower())
        if letter != character.lower():
            listt.append('*')
    for item in masked_word:
        if item != '*':
            number = masked_word.index(item)
            listt[number] = item
            if masked_word.count(item) > 1:
                second_number = masked_word.rindex(item)
                listt[second_number] = item
    new_masked_word = ''.join(listt)
    return new_masked_word
        


def guess_letter(game, letter):
    letter = letter.lower()
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException
    if game['remaining_misses'] <= 0 or game['answer_word'].lower() == game['masked_word'].lower():
        raise GameFinishedException
    
    before = game['masked_word']
    after = _uncover_word(game['answer_word'], game['masked_word'], letter)

    if before == after:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = after

    game['previous_guesses'].append(letter)
    
    if game['remaining_misses'] <= 0:
        raise GameLostException
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameWonException
    return after

    


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
