import random
from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['banana', 'Nintendo', 'guitar']

#Note: Really rough around the edges, but it works!
def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)

def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException
    mask = len(word) * '*'
    return mask

def _uncover_word(answer_word, masked_word, character):
    index_of_word = []
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    for index, letter_in_word in enumerate(answer_word):
        if letter_in_word.lower() == character.lower():
            index_of_word.append(index)
    for element in index_of_word:
        masked_word = list(masked_word)
        masked_word[element] = character.lower()
        masked_word = ''.join(masked_word)
    return masked_word
    
    
def guess_letter(game, letter):
    if game['remaining_misses'] == 0 or game['masked_word'] == game['answer_word']:
        raise GameFinishedException
    if letter.lower() in game['answer_word'].lower():
        reveal_word = _uncover_word(game['answer_word'],game['masked_word'], letter)
        game['masked_word'] = reveal_word
        game['previous_guesses'].append(letter.lower())
        if game['masked_word'] == game['answer_word']:
            raise GameWonException
    else:
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses'] -= 1
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
