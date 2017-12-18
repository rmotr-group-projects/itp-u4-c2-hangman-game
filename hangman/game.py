from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    random_choice = random.randint(0, len(list_of_words))
    
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    else:
        return list_of_words[random_choice - 1]



def _mask_word(word):
    #EXCEPTIONS
    if word == '':
        raise InvalidWordException()
    else:
        return '*' * len(word)
    


def _uncover_word(answer_word, masked_word, character):
    #EXCEPTIONS
    if len(answer_word) == 0 or len(masked_word) == 0 or len(answer_word) != len(masked_word):
        raise InvalidWordException('Those words are invalid!')
    if len(character) != 1:
        raise InvalidGuessedLetterException()
    else:
        letter_reveal = ''
     
        for letters in answer_word.lower():
            if letters == character.lower() or letters in masked_word:
                letter_reveal += letters
            else:
                letter_reveal += '*'
        return letter_reveal
    
    

def guess_letter(game, letter):
    #EXCEPTIONS
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException()
    else:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter.lower())
        game['previous_guesses'].append(letter.lower())
        
        if letter.lower() not in game['masked_word']:
            game['remaining_misses'] -= 1
            
        #EXCEPTIONS
        if game['answer_word'] == game['masked_word'] and game['remaining_misses'] >= 0:
            raise GameWonException('You WON!')
        elif game['answer_word'] != game['masked_word'] and game['remaining_misses'] == 0:
            raise GameLostException('You LOST!')
        
    print(game)

        
     

    


   
        

#-----------------------DO NOT TOUCH-----------------------#
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
