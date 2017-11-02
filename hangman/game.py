from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['python', 'exceptions', 'hangman']


def _get_random_word(list_of_words):
    
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    
    randomIdx = random.randint(0, len(list_of_words)-1)
    
    return list_of_words[randomIdx]

def _mask_word(word):
    
    if len(word) == 0:
        raise InvalidWordException()
    
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    
    if len(answer_word) == 0 or len(masked_word) == 0 or len(masked_word) != len(answer_word):
        raise InvalidWordException()
    elif len(character) > 1:
        raise InvalidGuessedLetterException()
    
    answer_word_lower = answer_word.lower()
    character_lower = character.lower()
    new_masked_word = ''
    
    for idx in range(0, len(answer_word)):
        if answer_word_lower[idx] == character_lower:
            new_masked_word += character_lower
        elif masked_word[idx] != '*':
            new_masked_word += masked_word[idx]
        else:
            new_masked_word += '*'
    
    masked_word = new_masked_word
    
    return masked_word

def guess_letter(game, letter):
    
    if game['masked_word'] == game['answer_word'].lower() or game['remaining_misses'] == 0:
        raise GameFinishedException()
    
    letter_lowercase = letter.lower()
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter_lowercase)
    game['previous_guesses'].append(letter_lowercase)
    
    # only if the letter missed
    if letter_lowercase not in game['masked_word']:
        game['remaining_misses'] -= 1
    
    if game['masked_word'] == game['answer_word']:
        raise GameWonException()
    elif game['remaining_misses'] == 0:
        raise GameLostException()

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
