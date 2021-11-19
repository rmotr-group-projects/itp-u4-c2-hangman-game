from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    import random
    try:
        return random.choice(list_of_words)
    except:
        raise InvalidListOfWordsException


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException
    else:
        return '*'*len(word)


def _uncover_word(answer_word, masked_word, character):
    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    character = character.lower()
    if answer_word == '':
        raise InvalidWordException
    elif len(character)>1:
        raise InvalidGuessedLetterException
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException
    else:
        anslist = list(answer_word)
        masklist = list(masked_word)
        
        for count,elem in enumerate(anslist):
            if character == elem:
                masklist[count]=character
        
        masked_word = ''.join(masklist)
        
        return masked_word


def guess_letter(game, letter):
    if game['answer_word'].lower() ==game['masked_word'].lower() or game['remaining_misses']==0:
        raise GameFinishedException()
    game['previous_guesses'].append(letter.lower())
    
    new_masked = _uncover_word(game['answer_word'], game['masked_word'], letter)    
    if new_masked != game['masked_word']:
        game['masked_word'] = new_masked
    else:
        game['remaining_misses'] -= 1 
    
    if game['answer_word'] == game['masked_word']:
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
