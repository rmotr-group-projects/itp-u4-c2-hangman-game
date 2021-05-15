from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Python','Hello','Me','GameOver','JustInCase']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException
    i = random.randint(0,len(list_of_words)-1)
    return list_of_words[i]


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException
    return '*'*len(word)


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0 or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    answer = answer_word.lower()
    result = ''
    char = character.lower()
    for i in range(len(answer)):
        if char != answer[i] or masked_word[i] != '*':
            result += masked_word[i]
            continue
        result += char
    changed = False
    if result == masked_word:
        changed = True
    return result


def guess_letter(game, letter):
    if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
    result = _uncover_word(game['answer_word'],game['masked_word'],letter)
    game['previous_guesses'].append(letter.lower())
    if result == game['masked_word']:
        game['remaining_misses'] -= 1
    game['masked_word'] = result
    if '*' not in game['masked_word']:
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
