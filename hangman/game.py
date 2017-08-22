from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException
    import random 
    return random.choice(list_of_words)


def _mask_word(word):
    if word:
        word = '*' * len(word)
        return word
    else:
        raise InvalidWordException
   

def _uncover_word(answer_word, masked_word, character):
    answer_word = answer_word.lower()
    character = character.lower()
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
        
    if not answer_word:
        raise InvalidWordException
        
    if len(character) != 1:
        raise InvalidGuessedLetterException
        
    word_new = ''
    if character not in answer_word:
        return masked_word
    index = 0
    for char in answer_word:
        if char == character:
           word_new = word_new + character
        else:
            word_new = word_new + masked_word[index]
        index = index + 1 
        
    return word_new


    
def guess_letter(game, letter):
    if (game['masked_word'] == game['answer_word']) and (game['remaining_misses'] > 0):
        raise GameFinishedException
    if game['remaining_misses'] == 0:
        raise GameFinishedException
    
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    letter = letter.lower()
    
    if letter not in game['answer_word'].lower():
        game['remaining_misses'] = game['remaining_misses'] - 1
    game['previous_guesses'].append(letter)
    
    if (game['masked_word'] == game['answer_word']) and (game['remaining_misses'] > 0):
        raise GameWonException
        
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
