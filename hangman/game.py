from .exceptions import *
import random 
# Complete with your own, just for fun :)
LIST_OF_WORDS = [
    'puppy',
    'library',
    'painting',
    'obelisk',
    'evening',
    'letterbox',
    'alias',
    'hunger',
    'infinite',
                ]


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException
    idx = random.randint(1, len(list_of_words)) - 1
    return list_of_words[idx]


def _mask_word(word):
    masked_word = ""
    if not word:
        raise InvalidWordException
    for letter in word:
        masked_word += "*"
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    new_masked_word = list(masked_word)
    if not answer_word or not masked_word:
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    for idx, letter in enumerate(answer_word):
        if character.lower() == letter.lower():
            new_masked_word[idx] = letter.lower()
    return "".join(new_masked_word)
    


def guess_letter(game, letter):
    if game['remaining_misses'] == 0 or game['masked_word'].lower() == game['answer_word']:
        raise GameFinishedException
    new_mask = _uncover_word(game['answer_word'], game['masked_word'], letter)
    if new_mask == game['masked_word']:
        game['remaining_misses'] -= 1
    game['previous_guesses'].append(letter.lower())
    game['masked_word'] = new_mask
    if game['remaining_misses'] == 0:
        raise GameLostException
    if game['masked_word'].lower() == game['answer_word'].lower(): 
        raise GameWonException


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
