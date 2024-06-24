from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['hello','jing','liu','happy']


def _get_random_word(list_of_words):
    
    
    if not list_of_words:
        raise InvalidListOfWordsException('words list can not be empty')
        
    return random.choice(list_of_words)
    


def _mask_word(word):
    
    if not word:
        raise InvalidWordException('invalid words')
    
    
    n=len(word)
    return '*'*n


def _uncover_word(answer_word, masked_word, character):
    
        
    if len(answer_word) != len(masked_word) or not answer_word or not masked_word:
        
        raise InvalidWordException('invalid words')
        
    if len(character)>1:
        raise InvalidGuessedLetterException('character should be a letter')
    
    tot_str=''
    for idx, elem in enumerate(masked_word):
        
        if elem =='*' and answer_word[idx].lower() == character.lower():
            tot_str += character.lower()
        
        elif elem =='*' and answer_word[idx].lower() != character.lower():
            tot_str += elem.lower()
        
        elif elem !='*':
            tot_str += elem.lower()
    
    return tot_str   
    
    


def guess_letter(game, letter):
    
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
        
        raise GameFinishedException('game finished')
    
    
    game['masked_word']= _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter.lower())
    
    if letter.lower() not in game['answer_word'].lower():
        game['remaining_misses'] = game['remaining_misses'] -1
        
        if game['remaining_misses'] == 0:
            raise GameLostException('aww you lost..')
    
    
    if game['masked_word'].lower() == game['answer_word'].lower():        
        raise GameWonException('YAY! you win!!!')
    
    
        
        
    
    

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
