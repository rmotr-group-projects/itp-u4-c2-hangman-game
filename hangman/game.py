from .exceptions import *
import random 
# Complete with your own, just for fun :)
LIST_OF_WORDS = ['dog', 'cat', 'badger','fish', 'tiger', 'lion', 'hamster', 'fox']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)
    


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException()
    return len(word) * '*'
   

def _uncover_word(answer_word, masked_word, character):
    
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    if len(answer_word) < 1 or len(masked_word) < 1 or len(answer_word) != len(masked_word):
        raise InvalidWordException()
    
    answer_word = answer_word.lower()
    character = character.lower()
    
    if character in answer_word:
        masked_word = list(masked_word)
        for i in range(len(answer_word)):
            if answer_word[i] == character:
                masked_word[i] = character
        
        uncovered_word = "".join(masked_word)
        return uncovered_word
    
    return masked_word


def guess_letter(game, letter):
    
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException()
    
    letter = letter.lower()
    
    word_left = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    game['masked_word'] = word_left
    if letter not in word_left:
        game['remaining_misses'] -= 1
       
    game['previous_guesses'].append(letter)
    
    if game['remaining_misses'] == 0:
        raise GameLostException()
    if game['answer_word'] == game['masked_word']:
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
