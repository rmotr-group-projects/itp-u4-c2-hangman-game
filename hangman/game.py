from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['apples', 'bananas', 'carrots', 'tangerines']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    '''
    Given a word like `'Python'`, it returns it "masked" (replacing real characters with asterisks): `'******'`
    '''
    masked_word = ''
    if word:
        for character in word:
            masked_word += '*'
    else:
        raise InvalidWordException
    return masked_word
    

def _uncover_word(answer_word, masked_word, character):
    '''
    _uncover_word('Python', '******', 'y')  # '*y****'  # Match
    _uncover_word('Python', '*y****', 'n')  # '*y***n'  # Match

    _uncover_word('Python', '******', 'x')  # '******'  # Miss
    _uncover_word('Python', '*y****', 'x')  # '*y****'  # Miss
    '''
    if not answer_word or not masked_word:
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    word_guess_list = list(masked_word)
    word_guess = ''
    answer_word = answer_word.lower()
    character = character.lower()
    
    for idx, char in enumerate(answer_word):
         if char == character:
            word_guess_list[idx] = char
    word_guess = word_guess.join(word_guess_list)
    
    return word_guess

def guess_letter(game, letter):
    game['answer_word'] = game['answer_word'].lower()
    if game['remaining_misses'] == 0 or game['masked_word'] == game['answer_word']:
        raise GameFinishedException
    letter = letter.lower()
    updated_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['masked_word'] = updated_word
    game['previous_guesses'].append(letter)
    if letter not in game['answer_word']:
        game['remaining_misses'] -= 1
    if game['remaining_misses'] == 0:
        raise GameLostException
    if game['masked_word'] == game['answer_word']:
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