from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    
    if not list_of_words:
        raise InvalidListOfWordsException
        
    random_number = random.randint(0, len(list_of_words) - 1)
    
    return list_of_words[random_number]


def _mask_word(word):
    
    if not word:
        raise InvalidWordException
        
    masked_word = ''
    
    
    for letter in word:
        masked_word += ('*')
        
    return masked_word
        
        
        


def _uncover_word(answer_word, masked_word, character):
    
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        
        raise InvalidWordException
        
    if len(character) > 1:
        
        raise InvalidGuessedLetterException
    
    low_answer_word = answer_word.lower()
    low_masked_word = masked_word.lower()
    low_char = character.lower()
    
    new_masked_word = ''
    
    
                        
    for idx, value in enumerate(low_answer_word):
        
        if low_char == value:

            new_masked_word += low_char

        else:

            new_masked_word += low_masked_word[idx]
                
    return new_masked_word
            
        
    
        
        
        
        
def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
    
        raise GameFinishedException
        
    low_letter = letter.lower()
    answer_word = game['answer_word'].lower()
    
    if low_letter in answer_word:
        
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        
    else:
        
        game['remaining_misses'] -= 1
        
         
    
    if game['answer_word'] == game['masked_word']:
        
        raise GameWonException
        
        
    
        
    game['previous_guesses'].append(low_letter)
    
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
