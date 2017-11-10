from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    return (random.choice(list_of_words))

def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException('empty string')
    num_ast = len(word)
    return num_ast * "*"

def _uncover_word(answer_word, masked_word, character):
    character = character.lower()
    answer_word = answer_word.lower()
    
    if len(character) > 1:
        raise InvalidGuessedLetterException('too many characters')
    
    if masked_word == '':
        raise InvalidWordException("empty string")
    
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException("Invalid words")
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException("Answer word does not match masked")
    
    previous_guesses = []
    if character in previous_guesses:
        raise InvalidGuessedLetterException('invalid character')
    for c in answer_word:
        if c not in previous_guesses:
            previous_guesses.append(c)
            if character == c:
                list_c = [i for i, char in enumerate(answer_word) if char == c]
                for i in list_c:
                    masked_word = masked_word[:i] + c + masked_word[i + 1:]
            
    return masked_word     
      

def guess_letter(game, letter):
    if game['remaining_misses'] == 0:
        raise GameFinishedException('game already finished')
    
    if _is_game_finished(game):
        raise GameFinishedException('all done')
    
    letter = letter.lower()
    
    if game['masked_word'] == '':
        raise InvalidWordException("empty string")
    
    masked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if game['masked_word'] == masked_word:
        game['remaining_misses'] -= 1
    game['masked_word'] = masked_word
    
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException('already guessed letter')
    else:
        game['previous_guesses'].append(letter)
    
    if _is_game_won(game):
        raise GameWonException('You finally won.')
    
    if game['remaining_misses'] == 0:
        raise GameLostException('You lost again.')
    
    return game

def _is_game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()
    
def _is_game_lost(game):
    return game['remaining_misses'] <=0

def _is_game_finished(game):
    return _is_game_lost(game) or _is_game_won(game)

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
