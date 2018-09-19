from .exceptions import *
import random
import string

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['hangman', 'turtle', 'avocado']


def _get_random_word(list_of_words):
    
    if not list_of_words:
        raise InvalidListOfWordsException
    
    rand_int = random.randint(0, len(list_of_words) - 1)
    
    return list_of_words[rand_int]


def _mask_word(word):
    
    if not word:
        raise InvalidWordException
        
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    
    if not answer_word:
        raise InvalidWordException;
    
    if len(character) > 1:
        raise InvalidGuessedLetterException
        
    if character not in string.ascii_letters:
        raise InvalidGuessedLetterException
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
        
    response_list = []      
    
    for idx, c in enumerate(answer_word):       
        
        if character == c.lower() or character == c.upper():          
            response_list.append(character.lower());           
        else:           
            response_list.append(masked_word[idx])
        
    return ''.join(response_list)
        
        


def guess_letter(game, letter):
    
    answer_word = game['answer_word']
    masked_word = game['masked_word']
    remaining_misses = game['remaining_misses']
    previous_guesses = game['previous_guesses']
    
    if answer_word == masked_word or remaining_misses == 0:
        raise GameFinishedException
    
    if letter in previous_guesses:
        raise InvalidGuessedLetterException
    else:
        game['previous_guesses'].append(letter.lower())
    
    new_masked_word = _uncover_word(answer_word, masked_word, letter)
          
    if masked_word == new_masked_word:
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            raise GameLostException
            
    elif answer_word == new_masked_word:
        game['masked_word'] = answer_word
        raise GameWonException
        
    else:
        game['masked_word'] = new_masked_word


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
