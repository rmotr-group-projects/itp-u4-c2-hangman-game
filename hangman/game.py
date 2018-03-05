from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
        
    return list_of_words[random.randrange(len(list_of_words))]
   


def _mask_word(word):
    if not word:
        raise InvalidWordException
        
    return '*' * len(word)
    
        
        


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException
        
    if len(character) > 1:
        raise InvalidGuessedLetterException
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    answer = answer_word.lower()
    if character.lower() not in answer:
        return masked_word
    
        
    new_word = ""
    
    for i in range(len(answer)):
        if answer[i] == character.lower():
            new_word += answer[i]
        else:
            new_word += masked_word[i]
            
    return new_word
            
    


def guess_letter(game, letter):
    if letter.lower() in game['previous_guesses']:
        raise InvalidGuessedLetterException
        
    if game['answer_word'] == game['masked_word'] and len(game['previous_guesses']) == 1:
        raise GameFinishedException
        
    if game['remaining_misses'] == 0 and len(game['previous_guesses']) == 1:
        raise GameFinishedException
    
        
    masked_word = game['masked_word']
    new_masked = _uncover_word(game['answer_word'], masked_word, letter)
     
    
    if masked_word == new_masked:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_masked
    
    game['previous_guesses'].append(letter.lower())
    
    
    if game['masked_word'] == game['answer_word']:
        raise GameWonException
    
    if game['remaining_misses'] == 0:
        raise GameLostException
    
            
    return new_masked
        


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
