from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    return(list_of_words[random.randint(0, len(list_of_words)-1)])

def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException()
    return('*'* len(word))

def _uncover_word(answer_word, masked_word, character):
    
    character = character.lower()
    answer_word = answer_word.lower()
    
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException()
        
    if len(character) > 1:
        raise InvalidGuessedLetterException()
        
    if len(masked_word) != len(answer_word):
        raise InvalidWordException()
        
    index = [i for i,x in enumerate(list(answer_word)) if x==character]
    new_list = list(masked_word)
    for a in index:
        new_list[a] = character
    
    masked_word = ''.join(new_list)
    
    return(masked_word)

def guess_letter(game, letter):
     
    letter = letter.lower()
        
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()
    
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] <=0:
        raise GameFinishedException()
    
    prev_word = game['masked_word']
    new_word = _uncover_word(game['answer_word'], game['masked_word'],letter)
    
    game['previous_guesses'].append(letter)
        
    if new_word == prev_word:
        game['remaining_misses'] = game['remaining_misses'] - 1
    else:
        game['masked_word'] = new_word
        
    if game['masked_word'] == game['answer_word']:
        raise GameWonException()
    elif game['remaining_misses'] <= 0:
        raise GameLostException()
     
    return(game)

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
