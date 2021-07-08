from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['python', 'hello', 'django', 'computer']


def _get_random_word(list_of_words):
    try:
        word = random.choice(list_of_words)
        return word
    except:
        if list_of_words == []:
            raise InvalidListOfWordsException()
        
def _mask_word(word):
    if not word:
        raise InvalidWordException
    return '*' * len(word)

def _uncover_word(answer_word, masked_word, character):
    if not answer_word and not masked_word:
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
        
    new_word = ''

    for answer_char, masked_char in zip(answer_word, masked_word):
        word = answer_word.lower()
        if character.lower() == answer_char.lower():
            new_word += answer_char.lower()
        else:
            new_word += masked_char

    return new_word


def guess_letter(game, letter):

    letter = letter.lower()
    game['previous_guesses'].append(letter)
    answer_word = game['answer_word'].lower()
    masked_word = game['masked_word'].lower()
    if game['masked_word'] != game['answer_word'] and game['remaining_misses'] != 0:
        if letter in answer_word:
            new_word = _uncover_word(answer_word, masked_word, letter)
            game['masked_word'] = new_word
            if '*' not in new_word:
                raise GameWonException()
        else:      
            game['remaining_misses'] -= 1
            if game['remaining_misses'] == 0:
                raise GameLostException()
    else:
        raise GameFinishedException()
  

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

