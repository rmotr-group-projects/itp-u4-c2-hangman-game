from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Betty', 'Barny', 'Wilma', 'Fred', 'Sonic', 'Alphabet', 'Fortune', 'Fortnight', 'Assume', 'Exhausted']
state = ''

def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    if len(list_of_words) == 0:
        raise IndexError()
    return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException()
    result = ''
    for letter in word:
        result += '*'
    return result

#Given a word like 'Python', it returns it "masked" (replacing real characters with asterisks): '******'


def _uncover_word(answer_word, masked_word, character):
    result = ''
    answer_word = answer_word.lower()
    character = character.lower()
    if not answer_word or not masked_word or len(answer_word) == 0 or len(masked_word) == 0 or (len(masked_word) != len(answer_word)    ) :
        raise InvalidWordException()
    if len(character) > 1 or not character:
        raise InvalidGuessedLetterException()
    if character not in answer_word:
        return masked_word
    if character in answer_word:
        for index in range(len(answer_word)):
            if character == answer_word[index]:
                result += answer_word[index]
            else:
                result += (masked_word[index])
    return result.lower()

def is_game_lost(game, letter):
    if game['masked_word'] == _uncover_word(game['answer_word'], game['masked_word'], letter) and game['remaining_misses'] <= 0:
        state = 'lost'
        return True
    return False
        
def is_game_won(game, letter):
    if game['answer_word'].lower() == game['masked_word'].lower() and game['remaining_misses'] >= 1:
        state = 'won'
        return True
    return False

def is_game_finished(game):
    if state == 'win' or state == 'lost':
        return True
    return False

def guess_letter(game, letter):
    if game['remaining_misses'] == 0 or game['masked_word'] == game['answer_word']:
        raise GameFinishedException
    if letter.lower() in game['answer_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
        if game['masked_word'] == game['answer_word']:
            raise GameWonException
    else:
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses'] -= 1
        if game['remaining_misses'] <= 0 :
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
