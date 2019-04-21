from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    try:
        return random.choice(list_of_words)
    except:
        raise InvalidListOfWordsException


def _mask_word(word):
    mask = '*'
    if len(word) < 1:
        raise InvalidWordException
    return mask * len(word)
    

def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException('Answer word and/or masked word is missing.')
    if len(character) > 1:
        raise InvalidGuessedLetterException("Too many characters.")
    if len(answer_word) != len(masked_word):
        raise InvalidWordException("Answer and masked words must match.")
    for idx, char in enumerate(answer_word):
        if char.lower() == character.lower():
            masked_word = list(masked_word)
            masked_word[idx] = character.lower()
            masked_word = ''.join(masked_word)
    return masked_word


def guess_letter(game, letter):
    
    if game['remaining_misses'] == 0 or game['answer_word'] == game['masked_word']:
        raise GameFinishedException()
      
    #if GameLostException:
        #raise GameFinishedException()
        
    mask = '*'
    letter = letter.lower()
    a_word = game['answer_word'].lower()
    m_word = game['masked_word']
    game['previous_guesses'].append(letter)
    game['masked_word'] = _uncover_word(a_word, m_word, letter)
       
    if letter not in a_word:
        game['remaining_misses'] -= 1

        
    if game['answer_word'] == game['masked_word']:
        raise GameWonException('You won!')
   
    if game['remaining_misses'] == 0:
        raise GameLostException('You lost!') 
          
    #return game['masked_word']
    
        

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
