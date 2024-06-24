from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):

    if not list_of_words:
        raise InvalidListOfWordsException()
        
    return random.choice(list_of_words)


def _mask_word(word):
    
    if word:
        return len(word) * '*'
        
    raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
   
    if len(character) > 1 or not character or type(character) != str:
        raise InvalidGuessedLetterException()
    
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException()
        
    answer_word = answer_word.lower()
    character = character.lower()
    index_list = []
    count = 0
    
    for char in answer_word:
        
        if char == character:
            index_list.append(count)
            
        count += 1
        
    masked_word = list(masked_word)  
    for i in index_list:
        masked_word[i] = character

    return "".join(masked_word)

def guess_letter(game, letter):
    
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0: #check to make sure game isnt finised 
        raise GameFinishedException()
    
    letter = letter.lower()
    
    if game['previous_guesses'] == letter:
        raise InvalidGuessedLetterException()

    prev_mask_word = game['masked_word']
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter)
    
    if prev_mask_word == game['masked_word']:
        game['remaining_misses'] -= 1
    
    if game['answer_word'] == game['masked_word']:
        raise GameWonException()
        
    if game['remaining_misses'] == 0:
        raise GameLostException()
    
    return game
    
    

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
