from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)

def _mask_word(word):
    if word == '':
        raise InvalidWordException()
        
    masked=''
    for char in word:
        masked += '*'
    return masked
 
        
def _uncover_word(answer_word, masked_word, character):
    
    if len(answer_word) != len(masked_word) or len(answer_word)== 0 or len(masked_word) == 0:
        raise InvalidWordException()
        
    if len(character) > 1:
        raise InvalidGuessedLetterException()
        
    lcase_answer_word = answer_word.lower()
    wordlist = list(masked_word)

    for index,char in enumerate(lcase_answer_word):
        if char == character.lower():
            wordlist[index] = character.lower()
    new_ans_word = ''.join(wordlist)
    return new_ans_word


def guess_letter(game, letter):
    
    if '*' not in game['masked_word'] and game['remaining_misses'] == 0:
        raise GameFinishedException()  
    
    guessed_letter_check = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if game['answer_word'].lower() == guessed_letter_check:
        raise GameWonException()
        
    if letter.lower() not in guessed_letter_check:
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses'] -= 1
    else:
        game['previous_guesses'].append(letter.lower())
        
    game['masked_word'] = guessed_letter_check
        
    if '*' in game['masked_word'] and game['remaining_misses'] == 0:
        raise GameLostException() 
    

        
        
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
