from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    raise InvalidListOfWordsException()

    
def _mask_word(word):
    if word:
        count = len(word)
        masked = count * '*'
        return masked
    raise InvalidWordException()
    

def _uncover_word(answer_word, masked_word, character):
    answer = answer_word.lower()
    character = character.lower()
    result = ""
    
    if not answer or not masked_word:
        raise InvalidWordException()
        
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    
    if len(answer) != len(masked_word):
        raise InvalidWordException()
    
    if character not in answer:
        return masked_word
    
    for i, letter in enumerate(answer):
        if letter == character:
            result += letter
        else:
            result += masked_word[i]
                
    return result

def _game_won(game):
    return game['masked_word'].lower() == game['answer_word'].lower()

def _game_lost(game):
    return game['remaining_misses'] == 0

def _is_game_finished(game):
    return _game_lost(game) or _game_won(game)

    
def guess_letter(game, letter):
    new_answer = game['answer_word'].lower()
    game['answer_word'] = new_answer
    ltr = letter.lower()
    
    if ltr in game['previous_guesses']:
        raise InvalidGuessedLetterException()
        
    if _is_game_finished(game):
        raise GameFinishedException()
    
    if ltr not in game['answer_word']:
        game['remaining_misses'] -= 1
        game['previous_guesses'].append(ltr)
        
        if game['remaining_misses'] == 0:
            raise GameLostException()
        
    else:
        game['previous_guesses'].append(ltr)
        previous_mask = game['masked_word']
        new_mask = _uncover_word(game['answer_word'], previous_mask, ltr)
        game['masked_word'] = new_mask
        
        if '*' not in game['masked_word']:
            raise GameWonException()
            

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
