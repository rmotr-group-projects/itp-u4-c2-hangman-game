from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    try:
        return list_of_words[random.randint(0,len(list_of_words) - 1)]
    except:
        raise InvalidListOfWordsException

def _mask_word(word):
    if word:
        return len(word) * '*'
    else:
        raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    lower_char = character.lower()
    temp_uncovered_word = masked_word
    if not (len(answer_word) == len(masked_word) and answer_word and masked_word):
        raise InvalidWordException
    if len(lower_char) != 1:
        raise InvalidGuessedLetterException
    for i, letter_in_word in enumerate(answer_word):
        if letter_in_word.lower() == lower_char:
            temp_uncovered_word = temp_uncovered_word[:i] + lower_char + temp_uncovered_word[i + 1:]
    return temp_uncovered_word
        
        
def guess_letter(game, letter):
    if not '*' in game['masked_word'] or game['remaining_misses'] == 0:
            raise GameFinishedException
    lower_letter = letter.lower()
    temp_answer_word = game['answer_word']
    temp_masked_word = game['masked_word']
    uncovered_word = _uncover_word(temp_answer_word, temp_masked_word, lower_letter)
    if len(letter) != 1:
        raise InvalidGuessedLetterException
    letter_found = not(uncovered_word == game['masked_word'])
    game['masked_word'] = uncovered_word
    game['previous_guesses'].append(lower_letter)
    if not letter_found:
        game['remaining_misses'] -= 1
    if not '*' in game['masked_word']:
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