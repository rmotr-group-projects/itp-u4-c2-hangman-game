from .exceptions import *
import random

LIST_OF_WORDS = ['apple', 'banana', 'chocolate', 'danish']


def _get_random_word(list_of_words):
    try:
        choice_word = random.choice(list_of_words)
        return choice_word
    except:
        raise InvalidListOfWordsException


def _mask_word(word):
    if word != '':
        output = '*' * len(word)
        return output
    else:
        raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    
    list_masked_word = list(masked_word)
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    elif len(character) > 1:
        raise InvalidGuessedLetterException
    elif answer_word == '' or masked_word == '':
        raise InvalidWordException
    
    for idx, letter in enumerate(answer_word):
        if letter.lower() == character.lower():
            list_masked_word[idx] = character.lower()
    
    return ''.join(list_masked_word)


def guess_letter(game, letter):
    letter = letter.lower()
    if game['masked_word'].lower() == game['answer_word'].lower() or game['remaining_misses'] == 0:
        raise GameFinishedException
    elif letter not in game['answer_word'].lower():
        game['previous_guesses'].append(letter)
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            raise GameLostException
    elif letter in game['answer_word'].lower():
        game['previous_guesses'].append(letter)
        game['masked_word'] = _uncover_word(game['answer_word'], 
            game['masked_word'], letter)
        if game['masked_word'] == game["answer_word"]:
            raise GameWonException
    elif game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
            raise GameFinishedException
            

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
